<script setup lang="ts">
// Project detail page, reached from the "View project" button on a card.
// Layout follows the classic case-study shape: full-width cover, a narrow
// identity column (title / description / stack / link) beside a wide reading
// column (background + static previews), then prev/next and the closing CTA.
const route = useRoute()
const { t } = useI18n()
const { projects } = useProjects()

const index = computed(() => projects.value.findIndex(p => p.id === route.params.id))
const project = computed(() => projects.value[index.value])

// A missing id is a real 404, not an empty page.
if (index.value === -1) {
  throw createError({ statusCode: 404, statusMessage: 'Project not found', fatal: true })
}

// Wrap around, the way the landing carousel does.
const count = computed(() => projects.value.length)
const previous = computed(() => projects.value[(index.value - 1 + count.value) % count.value]!)
const next = computed(() => projects.value[(index.value + 1) % count.value]!)

// The cover is the local asset when there is one, otherwise a generated
// screenshot of the live site. When the local file 404s, coverFailed flips
// and the computed falls through to the microlink URL automatically.
const cover = computed(() => {
  const p = project.value
  if (!p) return null
  if (p.cover && !coverFailed.value) return p.cover
  return p.url && p.online ? screenshotUrl(p.url, 1440, 900) : null
})

// "Static previews": explicit gallery assets first. When gallery images 404
// (files haven't been saved yet), `galleryFailed` flips and the computed falls
// through to generated microlink screenshots — desktop + mobile, like the no-
// gallery path. This keeps the detail page useful before local assets exist.
const galleryFailed = ref(false)

const previews = computed(() => {
  const p = project.value
  if (!p) return []
  if (p.gallery?.length && !galleryFailed.value) return p.gallery
  if (p.url && p.online) return [screenshotUrl(p.url, 1280, 1600), screenshotUrl(p.url, 480, 900)]
  return p.cover ? [p.cover] : []
})

const host = computed(() => {
  const p = project.value
  if (!p?.url) return ''
  try {
    const { host, pathname } = new URL(p.url)
    return !p.online && pathname !== '/' ? host + pathname : host
  } catch {
    return p.url
  }
})

// Generated screenshots are a best-effort service call: they fail for sites
// behind a login, and rate-limit. Anything that fails is dropped rather than
// left as a broken image — the icon placeholder shows through instead.
const coverFailed = ref(false)
const failedPreviews = ref(new Set<string>())
watch(() => project.value?.id, () => {
  coverFailed.value = false
  galleryFailed.value = false
  failedPreviews.value = new Set()
})

function onCoverError() {
  if (project.value?.cover && !coverFailed.value) {
    coverFailed.value = true
  }
}

function onPreviewError(src: string) {
  // If a gallery image 404s, the whole gallery is local-only and missing.
  // Flip galleryFailed so the computed switches to microlink screenshots.
  const p = project.value
  if (p?.gallery?.includes(src) && !galleryFailed.value) {
    galleryFailed.value = true
    failedPreviews.value = new Set()
    return
  }
  // Microlink or other source failed — hide that single image.
  failedPreviews.value = new Set([...failedPreviews.value, src])
}

useHead(() => ({
  title: project.value ? `${project.value.title} — Komla Etonam Georges EKLOU` : 'Project',
  meta: [
    { name: 'description', content: project.value?.description ?? '' },
    { property: 'og:title', content: project.value ? `${project.value.title} — Komla Etonam Georges EKLOU` : 'Project' },
    { property: 'og:description', content: project.value?.description ?? '' },
    { property: 'og:type', content: 'website' }
  ],
  link: [{ rel: 'canonical', href: `https://georginio.w3frame.com/projects/${project.value?.id ?? ''}` }]
}))
</script>

<template>
  <div v-if="project" class="pt-24 md:pt-28">
    <UContainer>
      <!-- Back to the projects section of the landing page -->
      <NuxtLink
        to="/#projects"
        class="group inline-flex items-center gap-2 font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed transition-colors hover:text-highlighted"
      >
        <UIcon name="i-lucide-arrow-left" class="size-3.5 transition-transform group-hover:-translate-x-0.5" />
        {{ t('projects.backToProjects') }}
      </NuxtLink>

      <!-- Cover: collage grid when there are gallery images, single cover otherwise -->
      <div v-if="previews.length > 1 && previews.some(src => !failedPreviews.has(src))" class="mt-6">
        <!-- Collage grid in the style of hermanneho.com/portfolio: browser-
             chrome mockups laid out in a 2-column (or 3-column for 3+ images)
             masonry-like grid. -->
        <div
          class="grid gap-3"
          :class="previews.length >= 4 ? 'grid-cols-2 lg:grid-cols-3' : previews.length === 3 ? 'grid-cols-2 lg:grid-cols-3' : 'grid-cols-2'"
        >
          <div
            v-for="(src, i) in previews"
            v-show="!failedPreviews.has(src)"
            :key="src"
            class="overflow-hidden rounded-xl border border-default bg-elevated/40"
            :class="previews.length >= 5 && i === 0 ? 'col-span-2 lg:col-span-1' : ''"
          >
            <!-- Browser window chrome -->
            <div class="flex h-7 items-center gap-1.5 border-b border-default bg-accented/60 pl-3">
              <span class="size-[7px] rounded-full bg-[#ff5f57]" />
              <span class="size-[7px] rounded-full bg-[#febc2e]" />
              <span class="size-[7px] rounded-full bg-[#28c840]" />
              <span class="ml-3 mr-2 truncate font-mono text-[10px] text-dimmed">{{ host }}</span>
            </div>
            <img
              :src="src"
              :alt="`${project.title} — ${i + 1}`"
              loading="lazy"
              decoding="async"
              class="w-full max-h-[420px] object-cover object-top"
              @error="onPreviewError(src)"
            >
          </div>
        </div>
      </div>
      <!-- Fallback: single cover when there is only one preview or no gallery -->
      <div v-else class="relative mt-6 aspect-[16/7] overflow-hidden rounded-2xl border border-default bg-elevated/40">
        <div class="absolute inset-0 z-0 flex items-center justify-center">
          <div class="flex size-24 items-center justify-center rounded-2xl bg-primary/15 text-primary ring-1 ring-primary/20">
            <UIcon :name="project.icon" class="size-12" />
          </div>
        </div>
        <img
          v-if="cover && !coverFailed"
          :src="cover"
          :alt="project.title"
          decoding="async"
          class="absolute inset-0 z-10 h-full w-full object-cover object-top"
          @error="onCoverError"
        >
      </div>

      <!-- Identity column + reading column -->
      <div class="mt-12 grid gap-10 lg:grid-cols-[340px_1fr] lg:gap-16">
        <aside class="border-y border-default py-8 lg:sticky lg:top-24 lg:self-start">
          <div class="font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed">
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

          <h1 class="mt-4 text-3xl font-bold leading-[1.05] tracking-tight text-highlighted sm:text-4xl">
            {{ project.title }}
          </h1>

          <p class="mt-4 text-[15px] leading-[1.6] text-muted">
            {{ project.description }}
          </p>

          <!-- Stack, slash-separated the way a spec sheet reads -->
          <p
            v-if="project.stack.length"
            class="mt-6 font-mono text-[12px] leading-[1.9] tracking-[0.04em] text-dimmed"
          >
            <template v-for="(item, i) in project.stack" :key="item">
              <span v-if="i" class="mx-1.5 text-accented">/</span>{{ item }}
            </template>
          </p>

          <p
            v-if="project.note"
            class="mt-6 border-t border-default pt-4 font-mono text-[12px] leading-[1.5] tracking-[0.04em]"
            :class="project.online ? 'text-secondary' : 'text-warning'"
          >
            {{ project.note }}
          </p>

          <a
            v-if="project.url"
            :href="project.url"
            target="_blank"
            rel="noopener noreferrer"
            class="group mt-8 inline-flex items-center gap-2.5 rounded-full border border-accented px-[22px] py-3.5 text-[15px] font-semibold text-highlighted transition-colors duration-200 hover:bg-elevated"
          >
            {{ project.online ? t('projects.viewWebsite') : t('projects.viewCode') }}
            <UIcon
              name="i-lucide-arrow-up-right"
              class="size-4 transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
            />
          </a>
        </aside>

        <div class="min-w-0">
          <section v-if="project.background">
            <h2 class="text-2xl font-bold tracking-tight text-highlighted sm:text-3xl">
              {{ t('projects.background') }}
            </h2>
            <p class="mt-5 text-[15px] leading-[1.75] text-muted">
              {{ project.background }}
            </p>
          </section>

          <!-- Previews section now lives in the top collage grid; this spot is
               kept only for projects with a single preview (no collage). -->
          <section
            v-if="previews.length === 1 && previews.some(src => !failedPreviews.has(src))"
            :class="project.background ? 'mt-14' : ''"
          >
            <h2 class="text-2xl font-bold tracking-tight text-highlighted sm:text-3xl">
              {{ t('projects.previews') }}
            </h2>
            <div class="mt-6 flex flex-col gap-6">
              <div
                v-for="src in previews"
                v-show="!failedPreviews.has(src)"
                :key="src"
                class="overflow-hidden rounded-xl border border-default bg-elevated/40"
              >
                <div class="flex h-7 items-center gap-1.5 border-b border-default bg-accented/60 pl-3">
                  <span class="size-[7px] rounded-full bg-[#ff5f57]" />
                  <span class="size-[7px] rounded-full bg-[#febc2e]" />
                  <span class="size-[7px] rounded-full bg-[#28c840]" />
                  <span class="ml-3 mr-2 truncate font-mono text-[10px] text-dimmed">{{ host }}</span>
                </div>
                <img
                  :src="src"
                  :alt="project.title"
                  loading="lazy"
                  decoding="async"
                  class="w-full object-cover object-top"
                  @error="onPreviewError(src)"
                >
              </div>
            </div>
          </section>
        </div>
      </div>

      <!-- Previous / next -->
      <nav class="mt-20 grid grid-cols-2 divide-x divide-default border-y border-default">
        <NuxtLink
          :to="`/projects/${previous.id}`"
          class="group flex items-center gap-4 py-6 pr-4 transition-colors hover:bg-elevated/40"
        >
          <UIcon
            name="i-lucide-arrow-left"
            class="size-4 shrink-0 text-dimmed transition-transform group-hover:-translate-x-0.5"
          />
          <span class="min-w-0">
            <span class="block truncate text-lg font-semibold text-highlighted">{{ previous.title }}</span>
            <span class="block font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed">
              {{ t('projects.prev') }}
            </span>
          </span>
        </NuxtLink>
        <NuxtLink
          :to="`/projects/${next.id}`"
          class="group flex flex-row-reverse items-center gap-4 py-6 pl-4 text-right transition-colors hover:bg-elevated/40"
        >
          <UIcon
            name="i-lucide-arrow-right"
            class="size-4 shrink-0 text-dimmed transition-transform group-hover:translate-x-0.5"
          />
          <span class="min-w-0">
            <span class="block truncate text-lg font-semibold text-highlighted">{{ next.title }}</span>
            <span class="block font-mono text-[11px] tracking-[0.14em] uppercase text-dimmed">
              {{ t('projects.next') }}
            </span>
          </span>
        </NuxtLink>
      </nav>

      <!-- Closing CTA -->
      <div class="my-24 flex flex-col items-center gap-8 sm:flex-row md:my-32">
        <h2 class="max-w-[380px] text-center text-2xl font-bold tracking-tight text-highlighted sm:text-left sm:text-3xl">
          {{ t('projects.ctaHeading') }}
        </h2>
        <span class="hidden h-px flex-1 bg-[var(--ui-border)] sm:block" />
        <NuxtLink
          to="/#contact"
          class="group inline-flex shrink-0 items-center gap-2.5 rounded-full border border-accented px-8 py-4 text-[15px] font-semibold text-highlighted transition-colors duration-200 hover:bg-elevated"
        >
          {{ t('projects.ctaButton') }}
          <UIcon name="i-lucide-arrow-right" class="size-4 transition-transform group-hover:translate-x-0.5" />
        </NuxtLink>
      </div>
    </UContainer>
  </div>
</template>
