<script setup lang="ts">
interface Project {
  title: string
  description: string
  tags: string[]
  url?: string
  status?: string
  note?: string
  icon: string
}

const props = defineProps<{
  project: Project
  index: number
  total: number
}>()

const { t } = useI18n()

// Live homepage thumbnail via microlink's image embed. Plain, natively lazy
// <img>: the browser only fetches it when the card nears the viewport and it
// never blocks rendering. The icon tile shows as a placeholder underneath and
// stays if the screenshot fails to load.
const previewSrc = computed(() =>
  props.project.url
    ? `https://api.microlink.io/?url=${encodeURIComponent(props.project.url)}&screenshot=true&embed=screenshot.url&meta=false&viewport.width=1280&viewport.height=800`
    : null
)

// Bare hostname for the fake browser chrome address bar ("www.orga-africa.com").
const host = computed(() => {
  if (!props.project.url) return ''
  try {
    return new URL(props.project.url).host
  } catch {
    return props.project.url
  }
})

// Two-digit counter, "03 / 09".
const pad = (n: number) => String(n).padStart(2, '0')

const loaded = ref(false)
const failed = ref(false)

// A new project means a new screenshot: reset the fade-in state.
watch(() => props.project.url, () => {
  loaded.value = false
  failed.value = false
})
</script>

<template>
  <article
    class="grid grid-cols-1 lg:grid-cols-[1.4fr_1fr] rounded-2xl border border-default bg-elevated/40 overflow-hidden"
  >
    <!-- Left: browser mockup -->
    <div
      class="relative min-h-[280px] sm:min-h-[380px] lg:min-h-[460px] p-6 sm:p-8 lg:p-12 border-b lg:border-b-0 lg:border-r border-default bg-gradient-to-br from-elevated to-default"
    >
      <component
        :is="project.url ? 'a' : 'div'"
        v-bind="project.url ? { href: project.url, target: '_blank', rel: 'noopener noreferrer' } : {}"
        class="group absolute inset-6 sm:inset-8 lg:inset-12 block rounded-xl border border-accented overflow-hidden bg-default"
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
            @error="failed = true"
          >
        </div>
      </component>
    </div>

    <!-- Right: meta panel -->
    <div class="p-6 sm:p-8 lg:p-11 flex flex-col">
      <div class="font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed">
        <span class="text-primary">● {{ project.status || project.tags[0] }}</span>
        <template v-if="host">&nbsp;·&nbsp;{{ host }}</template>
      </div>

      <h3 class="mt-4 text-2xl sm:text-3xl lg:text-4xl font-bold leading-[1.05] tracking-tight text-highlighted">
        {{ project.title }}
      </h3>

      <p class="mt-3.5 text-sm sm:text-base text-muted leading-relaxed">
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

      <p
        v-if="project.note"
        class="mt-5 pt-4 border-t border-default font-mono text-xs text-secondary tracking-[0.04em] leading-relaxed"
      >
        {{ project.note }}
      </p>

      <div class="flex items-center justify-between gap-4 mt-auto pt-7">
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
