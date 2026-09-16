<script setup lang="ts">
const { t } = useI18n()
const route = useRoute()

const links = computed(() => [
  { label: t('navigation.home'), anchor: 'home' },
  { label: t('navigation.work'), anchor: 'projects' },
  { label: t('navigation.experience'), anchor: 'experience' },
  { label: t('navigation.contact'), anchor: 'contact' }
])

function href(anchor: string) {
  return route.path === '/' ? `#${anchor}` : `/#${anchor}`
}
</script>

<template>
  <nav :aria-label="t('navigation.label')" class="portfolio-nav">
    <a :href="href('home')" class="portfolio-mark" aria-label="Go to homepage">K<span>.</span>E</a>

    <div class="portfolio-nav-links">
      <a v-for="link in links" :key="link.anchor" :href="href(link.anchor)">{{ link.label }}</a>
    </div>

    <details class="portfolio-nav-mobile">
      <summary :aria-label="t('navigation.menu')"><UIcon name="i-lucide-menu" class="size-4" /></summary>
      <div>
        <a v-for="link in links" :key="link.anchor" :href="href(link.anchor)">{{ link.label }}</a>
      </div>
    </details>
  </nav>
</template>
