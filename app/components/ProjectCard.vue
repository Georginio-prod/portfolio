<script setup lang="ts">
import type { Project } from '~/composables/useProjects'

const props = defineProps<{
  project: Project
  index: number
  total: number
}>()

const { t } = useI18n()

// A local cover wins when the project provides one (nothing to screenshot for
// something that isn't deployed). Otherwise: live homepage thumbnail via
// microlink's image embed. Plain, natively lazy <img>, so the browser only
// fetches it when the card nears the viewport and it never blocks rendering.
// The icon tile shows as a placeholder underneath and stays if loading fails.
//
// When the local cover 404s (files haven't been saved yet), `coverFailed`
// flips and the computed falls through to the microlink URL — so the card
// always shows *something* for online projects.
const coverFailed = ref(false)

const previewSrc = computed(() => {
  if (props.project.cover && !coverFailed.value) return props.project.cover
  return props.project.url && props.project.online ? screenshotUrl(props.project.url) : null
})

// Hostname for the fake browser chrome address bar ("www.orga-africa.com").
// Offline projects link to their repository instead of a site, so those keep
// the path too — otherwise the bar would just read "github.com" above a
// screenshot of the app itself.
const host = computed(() => {
  if (!props.project.url) return ''
  try {
    const { host, pathname } = new URL(props.project.url)
    return !props.project.online && pathname !== '/' ? host + pathname : host
  } catch {
    return props.project.url
  }
})

// Two-digit counter, "03 / 09".
const pad = (n: number) => String(n).padStart(2, '0')

const loaded = ref(false)
const failed = ref(false)

// A new project means a new image: reset the fade-in state.
watch(previewSrc, () => {
  loaded.value = false
  failed.value = false
})

// When a cover 404s we also need to reset the general image state so the
// microlink fallback URL gets a fresh chance.
watch(() => props.project.id, () => {
  coverFailed.value = false
  loaded.value = false
  failed.value = false
})

function onPreviewError() {
  // Local cover failed → try microlink next (coverFailed flips previewSrc).
  // If microlink also fails → give up (failed = true → icon stays).
  if (props.project.cover && !coverFailed.value) {
    coverFailed.value = true
    loaded.value = false
  } else {
    failed.value = true
  }
}
</script>

<template>
  <article
    class="grid grid-cols-1 lg:grid-cols-[1.4fr_1fr] rounded-2xl border border-default bg-elevated/40 overflow-hidden"
  >
    <!-- Left: browser mockup. The fixed aspect ratio is what keeps every cover
         the same size — otherwise the panel stretches to match however long the
         description on the right happens to be. -->
    <div
      class="flex items-center p-4 sm:p-5 lg:p-6 border-b lg:border-b-0 lg:border-r border-default bg-gradient-to-br from-elevated to-default"
    >
      <component
        :is="project.url ? 'a' : 'div'"
        v-bind="project.url ? { href: project.url, target: '_blank', rel: 'noopener noreferrer' } : {}"
        class="group block w-full aspect-[16/10] rounded-xl border border-accented overflow-hidden bg-default"
      >
        <!-- Window chrome -->
        <div class="h-8 flex items-center gap-1.5 pl-3.5 bg-accented/60 border-b border-default">
          <span class="size-2 rounded-full bg-[#ff5f57]" />
          <span class="size-2 rounded-full bg-[#febc2e]" />
          <span class="size-2 rounded-full bg-[#28c840]" />
          <span class="ml-4 mr-3 font-mono text-[11px] text-dimmed truncate">{{ host }}</span>
        </div>

        <!-- Viewport -->
        <div class="relative h-[calc(100%-2rem)] bg-muted">
          <!-- Icon placeholder: instant, and stays if the screenshot fails -->
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="flex size-20 items-center justify-center rounded-2xl bg-primary/15 text-primary ring-1 ring-primary/20">
              <UIcon :name="project.icon" class="size-10" />
            </div>
          </div>

          <img
            v-if="previewSrc && !failed"
            :key="previewSrc"
            :src="previewSrc"
            :alt="`Preview of ${project.title}`"
            loading="lazy"
            decoding="async"
            class="absolute inset-0 h-full w-full object-cover object-top transition-[opacity,transform] duration-500 ease-out group-hover:scale-[1.02]"
            :class="loaded ? 'opacity-100' : 'opacity-0'"
            @load="loaded = true"
            @error="onPreviewError"
          >
        </div>
      </component>
    </div>

    <!-- Right: meta panel -->
    <div class="p-6 sm:p-8 lg:p-11 flex flex-col">
      <div class="font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed">
        <!-- Unfinished work gets a pulsing amber dot — the signal that the
             project is still moving, whether or not it is already online. -->
        <span
          class="inline-flex items-center gap-2 align-[1px]"
          :class="project.wip ? 'text-warning' : 'text-primary'"
        >
          <span class="relative flex size-1.5">
            <span
              v-if="project.wip"
              class="absolute inline-flex h-full w-full rounded-full bg-current opacity-75 animate-ping motion-reduce:hidden"
            />
            <span class="relative inline-flex size-1.5 rounded-full bg-current" />
          </span>
          {{ project.status || project.tags[0] }}
        </span>
        <template v-if="host">&nbsp;·&nbsp;{{ host }}</template>
      </div>

      <h3 class="mt-4 text-2xl sm:text-3xl lg:text-4xl font-bold leading-[1.05] tracking-tight text-highlighted">
        {{ project.title }}
      </h3>

      <p class="mt-3.5 text-[14px] sm:text-[15px] text-muted leading-[1.55]">
        {{ project.description }}
      </p>

      <div class="flex flex-wrap gap-1.5 mt-6">
        <span
          v-for="tag in project.tags"
          :key="tag"
          class="inline-flex items-center px-2.5 py-1 border border-accented rounded-full font-mono text-[10px] tracking-[0.08em] uppercase text-muted"
        >
          {{ tag }}
        </span>
      </div>

      <!-- Special mention: blue once the project is reachable online, amber
           while it is still unpublished. -->
      <p
        v-if="project.note"
        class="mt-5 pt-4 border-t border-default font-mono text-[12px] tracking-[0.04em] leading-[1.5]"
        :class="project.online ? 'text-secondary' : 'text-warning'"
      >
        {{ project.note }}
      </p>

      <div class="flex flex-wrap items-center gap-3 mt-auto pt-7">
        <!-- Primary path: the full case study. The live site stays reachable
             next to it, one step down in weight. -->
        <NuxtLink
          :to="`/projects/${project.id}`"
          class="group inline-flex items-center gap-2.5 rounded-full bg-inverted px-[22px] py-3.5 font-semibold text-[15px] text-inverted whitespace-nowrap transition-opacity duration-200 hover:opacity-90"
        >
          {{ t('projects.viewProject') }}
          <UIcon
            name="i-lucide-arrow-right"
            class="size-4 transition-transform duration-200 group-hover:translate-x-0.5"
          />
        </NuxtLink>

        <a
          v-if="project.url"
          :href="project.url"
          target="_blank"
          rel="noopener noreferrer"
          class="group inline-flex items-center gap-2.5 rounded-full border border-accented px-[22px] py-3.5 font-semibold text-[15px] text-highlighted whitespace-nowrap transition-colors duration-200 hover:bg-elevated"
        >
          {{ t('projects.visit') }}
          <UIcon
            name="i-lucide-arrow-up-right"
            class="size-4 transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
          />
        </a>
        <span class="ml-auto shrink-0 font-mono text-[11px] tracking-[0.08em] text-dimmed">
          {{ pad(index + 1) }} / {{ pad(total) }}
        </span>
      </div>
    </div>
  </article>
</template>
