<script setup lang="ts">
interface Project {
  title: string
  description: string
  tags: string[]
  url?: string
  status?: string
  icon: string
}

const props = defineProps<{
  project: Project
}>()

const { t } = useI18n()

// Live homepage thumbnail via microlink's image embed. Unlike the old version
// this is a plain, natively lazy-loaded <img>: the browser only fetches it when
// the card nears the viewport and it never blocks rendering. The icon tile shows
// as a placeholder underneath and stays if the screenshot fails to load.
const previewSrc = computed(() =>
  props.project.url
    ? `https://api.microlink.io/?url=${encodeURIComponent(props.project.url)}&screenshot=true&embed=screenshot.url&meta=false&viewport.width=1280&viewport.height=800`
    : null
)

const loaded = ref(false)
const failed = ref(false)
</script>

<template>
  <div
    class="project-card group relative w-[90vw] h-[50vh] md:w-[75vw] md:h-[60vh] lg:w-[800px] lg:h-[520px] rounded-xl overflow-hidden border border-primary/30 hover:border-primary/60 transition-all duration-300 flex-shrink-0"
  >
    <div class="relative w-full h-full bg-gradient-to-br from-primary/10 via-[var(--ui-bg-elevated)] to-secondary/10">
      <!-- Icon placeholder: shown instantly while the screenshot loads (or if it fails) -->
      <div class="absolute inset-0 flex items-center justify-center">
        <div
          class="flex size-24 md:size-28 items-center justify-center rounded-3xl bg-primary/15 text-primary ring-1 ring-primary/20 transition-transform duration-500 group-hover:scale-110"
        >
          <UIcon :name="project.icon" class="size-12 md:size-14" />
        </div>
      </div>

      <!-- Real homepage preview: lazy + async so it streams in without blocking -->
      <img
        v-if="previewSrc && !failed"
        :src="previewSrc"
        :alt="`Preview of ${project.title}`"
        loading="lazy"
        decoding="async"
        class="absolute inset-0 h-full w-full object-cover object-top transition-[opacity,transform] duration-700 group-hover:scale-105"
        :class="loaded ? 'opacity-100' : 'opacity-0'"
        @load="loaded = true"
        @error="failed = true"
      >

      <!-- Full-card link: lets touch users open the project with a single tap
           (the rich details overlay below is hover-only and unreachable on mobile). -->
      <a
        v-if="project.url"
        :href="project.url"
        target="_blank"
        rel="noopener noreferrer"
        class="absolute inset-0 z-[15] lg:hidden"
        :aria-label="`${t('projects.visit')}: ${project.title}`"
      />

      <!-- Title badge (top-right) -->
      <div class="absolute top-0 right-0 bg-gradient-to-bl from-black/80 to-transparent p-6 md:p-8 text-right pointer-events-none z-10">
        <h3 class="text-2xl md:text-3xl lg:text-4xl font-bold text-white">
          {{ project.title }}
        </h3>
        <span
          v-if="project.status"
          class="inline-block mt-2 px-3 py-1.5 bg-primary/90 text-white text-xs md:text-sm font-semibold rounded"
        >
          {{ project.status }}
        </span>
      </div>

      <!-- Hover overlay -->
      <div
        class="absolute inset-0 z-20 bg-black/95 backdrop-blur-sm flex flex-col justify-end items-end p-6 md:p-10 lg:p-12 transition-opacity duration-300 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto"
      >
        <div class="max-w-md lg:max-w-lg text-right">
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-3">
            {{ project.title }}
          </h3>
          <span
            v-if="project.status"
            class="inline-block mb-4 px-4 py-2 bg-primary text-white text-sm md:text-base font-semibold rounded"
          >
            {{ project.status }}
          </span>
          <p class="text-neutral-300 text-sm md:text-base lg:text-lg leading-relaxed mb-6">
            {{ project.description }}
          </p>
          <div class="flex flex-wrap justify-end gap-2 mb-6">
            <span
              v-for="tag in project.tags"
              :key="tag"
              class="text-xs rounded-full bg-white/10 ring-1 ring-white/15 text-neutral-300 px-3 py-1"
            >
              {{ tag }}
            </span>
          </div>
          <a
            v-if="project.url"
            :href="project.url"
            target="_blank"
            rel="noopener noreferrer"
            class="inline-flex items-center gap-2 text-primary hover:text-primary-300 font-medium text-base md:text-lg transition-colors"
          >
            {{ t('projects.visit') }}
            <UIcon name="i-lucide-external-link" class="size-5 md:size-6" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
