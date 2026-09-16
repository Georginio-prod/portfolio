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
  <main v-if="project" class="case-study">
    <UContainer>
      <header class="case-study-intro">
        <NuxtLink to="/#projects" class="case-study-back">
          <UIcon name="i-lucide-arrow-left" class="size-3.5" />
          {{ t('projects.backToProjects') }}
        </NuxtLink>

        <div class="case-study-heading">
          <div>
            <p class="case-study-kicker">
              <span class="case-study-status" :class="{ 'is-wip': project.wip }"><i />{{ project.status || project.tags[0] }}</span>
              <span v-if="host">{{ host }}</span>
            </p>
            <h1>{{ project.title }}</h1>
          </div>
          <p class="case-study-index">{{ t('projects.projectIndex', { current: index + 1, total: count }) }}</p>
        </div>

        <div class="case-study-summary">
          <p>{{ project.description }}</p>
          <a
            v-if="project.url"
            :href="project.url"
            target="_blank"
            rel="noopener noreferrer"
            class="signal-button signal-button-primary"
          >
            {{ project.online ? t('projects.viewWebsite') : t('projects.viewCode') }}
            <UIcon name="i-lucide-arrow-up-right" class="size-4" />
          </a>
        </div>
      </header>

      <section class="case-study-visual" :aria-label="`${project.title} — ${t('projects.previews')}`">
        <div class="case-study-visual-grid" />
        <div class="case-study-browser case-study-browser-main">
          <div class="case-study-browser-bar">
            <span /><span /><span />
            <p>{{ host }}</p>
            <UIcon name="i-lucide-arrow-up-right" class="size-3.5" />
          </div>
          <div class="case-study-screen">
            <div class="case-study-image-fallback"><UIcon :name="project.icon" class="size-12" /></div>
            <img
              v-if="cover && !coverFailed"
              :src="cover"
              :alt="project.title"
              decoding="async"
              @error="onCoverError"
            >
          </div>
        </div>
        <div class="case-study-visual-note">
          <span>{{ t('projects.caseStudy') }}</span>
          <strong>{{ project.tags.join(' · ') }}</strong>
        </div>
      </section>

      <div class="case-study-content">
        <aside class="case-study-facts">
          <div>
            <span>{{ t('projects.statusLabel') }}</span>
            <strong>{{ project.status || project.tags[0] }}</strong>
          </div>
          <div v-if="project.stack.length">
            <span>{{ t('projects.stackLabel') }}</span>
            <p>
              <template v-for="(item, i) in project.stack" :key="item">
                <b v-if="i">/</b>{{ item }}
              </template>
            </p>
          </div>
          <p v-if="project.note" class="case-study-note">{{ project.note }}</p>
        </aside>

        <div class="case-study-story">
          <section v-if="project.background" class="case-study-context">
            <p class="section-kicker"><span>02</span>{{ t('projects.background') }}</p>
            <p>{{ project.background }}</p>
          </section>

          <section v-if="previews.some(src => !failedPreviews.has(src))" class="case-study-previews">
            <p class="section-kicker"><span>03</span>{{ t('projects.previews') }}</p>
            <div class="case-study-preview-grid">
              <article
                v-for="(src, i) in previews"
                v-show="!failedPreviews.has(src)"
                :key="src"
                class="case-study-browser case-study-preview"
                :class="{ 'is-mobile': i % 2 === 1 }"
              >
                <div class="case-study-browser-bar">
                  <span /><span /><span />
                  <p>{{ host }}</p>
                </div>
                <img
                  :src="src"
                  :alt="`${project.title} — ${i + 1}`"
                  loading="lazy"
                  decoding="async"
                  @error="onPreviewError(src)"
                >
              </article>
            </div>
          </section>
        </div>
      </div>

      <nav class="case-study-pagination" :aria-label="t('projects.projectNavigation')">
        <NuxtLink :to="`/projects/${previous.id}`" class="case-study-page-link is-previous">
          <span>{{ t('projects.prev') }}</span>
          <strong><UIcon name="i-lucide-arrow-left" class="size-4" />{{ previous.title }}</strong>
        </NuxtLink>
        <NuxtLink :to="`/projects/${next.id}`" class="case-study-page-link is-next">
          <span>{{ t('projects.next') }}</span>
          <strong>{{ next.title }}<UIcon name="i-lucide-arrow-right" class="size-4" /></strong>
        </NuxtLink>
      </nav>

      <div class="case-study-cta">
        <p>{{ t('projects.ctaHeading') }}</p>
        <NuxtLink to="/#contact" class="signal-button">
          {{ t('projects.ctaButton') }}
          <UIcon name="i-lucide-arrow-right" class="size-4" />
        </NuxtLink>
      </div>
    </UContainer>
  </main>
</template>
