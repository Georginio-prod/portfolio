<script setup lang="ts">
import type { Project } from '~/composables/useProjects'

const props = defineProps<{
  project: Project
  index: number
  total: number
}>()

const { t } = useI18n()
const coverFailed = ref(false)
const loaded = ref(false)
const failed = ref(false)

const previewSrc = computed(() => {
  if (props.project.cover && !coverFailed.value) return props.project.cover
  return props.project.url && props.project.online ? screenshotUrl(props.project.url) : null
})

const host = computed(() => {
  if (!props.project.url) return ''
  try {
    const { host, pathname } = new URL(props.project.url)
    return !props.project.online && pathname !== '/' ? `${host}${pathname}` : host
  } catch {
    return props.project.url
  }
})

const pad = (number: number) => String(number).padStart(2, '0')

watch(previewSrc, () => {
  loaded.value = false
  failed.value = false
})

watch(() => props.project.id, () => {
  coverFailed.value = false
  loaded.value = false
  failed.value = false
})

function onPreviewError() {
  if (props.project.cover && !coverFailed.value) {
    coverFailed.value = true
    loaded.value = false
  } else {
    failed.value = true
  }
}
</script>

<template>
  <article class="project-stage">
    <div class="project-stage-visual">
      <div class="project-stage-grid" aria-hidden="true" />
      <component
        :is="project.url ? 'a' : 'div'"
        v-bind="project.url ? { href: project.url, target: '_blank', rel: 'noopener noreferrer' } : {}"
        class="project-browser"
      >
        <div class="project-browser-bar">
          <span class="browser-dot" /><span class="browser-dot" /><span class="browser-dot" />
          <span class="project-browser-host">{{ host }}</span>
          <UIcon name="i-lucide-arrow-up-right" class="size-3.5" />
        </div>
        <div class="project-browser-screen">
          <div v-if="!previewSrc || failed" class="project-image-fallback">
            <UIcon :name="project.icon" class="size-12" />
          </div>
          <img
            v-if="previewSrc && !failed"
            :key="previewSrc"
            :src="previewSrc"
            :alt="`Preview of ${project.title}`"
            loading="lazy"
            decoding="async"
            :class="{ 'is-loaded': loaded }"
            @load="loaded = true"
            @error="onPreviewError"
          >
        </div>
      </component>
      <p class="project-visual-counter" aria-hidden="true">{{ pad(index + 1) }} / {{ pad(total) }}</p>
    </div>

    <div class="project-stage-copy">
      <div class="project-stage-meta">
        <span :class="['project-status', { 'is-wip': project.wip }]">
          <i aria-hidden="true" />{{ project.status || project.tags[0] }}
        </span>
        <span>{{ host }}</span>
      </div>
      <h3>{{ project.title }}</h3>
      <p class="project-description">{{ project.description }}</p>
      <div class="project-tags">
        <span v-for="tag in project.tags" :key="tag">{{ tag }}</span>
      </div>
      <p v-if="project.note" class="project-note">{{ project.note }}</p>
      <div class="project-stage-actions">
        <NuxtLink :to="`/projects/${project.id}`" class="signal-button signal-button-primary">
          {{ t('projects.viewProject') }} <UIcon name="i-lucide-arrow-up-right" class="size-4" />
        </NuxtLink>
        <a v-if="project.url" :href="project.url" target="_blank" rel="noopener noreferrer" class="text-action">
          {{ t('projects.visit') }} <UIcon name="i-lucide-arrow-up-right" class="size-4" />
        </a>
      </div>
    </div>
  </article>
</template>
