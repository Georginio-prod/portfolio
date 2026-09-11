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
  <nav :aria-label="t('navigation.label')" class="fixed left-1/2 top-3 z-50 -translate-x-1/2 sm:top-4">
    <details class="relative sm:hidden">
      <summary class="inline-flex cursor-pointer list-none items-center gap-2 rounded-full border border-default bg-elevated/90 px-4 py-2 text-sm font-medium text-highlighted shadow-lg backdrop-blur-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary">
        <UIcon name="i-lucide-menu" class="size-4" />
        {{ t('navigation.menu') }}
      </summary>
      <div class="absolute left-0 mt-2 grid min-w-44 gap-1 rounded-2xl border border-default bg-elevated p-2 shadow-xl">
        <a
          v-for="link in links"
          :key="link.anchor"
          :href="href(link.anchor)"
          class="rounded-xl px-3 py-2 text-sm text-muted transition-colors hover:bg-accented hover:text-highlighted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          {{ link.label }}
        </a>
      </div>
    </details>

    <div class="hidden items-center gap-1 rounded-full border border-default bg-elevated/90 p-1 shadow-lg backdrop-blur-md sm:flex">
      <a
        v-for="link in links"
        :key="link.anchor"
        :href="href(link.anchor)"
        class="rounded-full px-3 py-1.5 text-sm text-muted transition-colors hover:bg-accented hover:text-highlighted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
      >
        {{ link.label }}
      </a>
    </div>
  </nav>
</template>
