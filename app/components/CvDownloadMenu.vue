<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <details class="cv-download-menu group relative">
    <summary class="inline-flex cursor-pointer list-none items-center gap-2 rounded-full border border-accented px-6 py-3 text-sm font-semibold text-highlighted transition-colors hover:bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary">
      <UIcon name="i-lucide-download" class="size-4" />
      {{ t('hero.ctaCv') }}
      <UIcon name="i-lucide-chevron-down" class="size-4 transition-transform duration-200 group-open:rotate-180" />
    </summary>
    <div class="absolute right-0 top-full z-30 mt-2 w-48 overflow-hidden rounded-xl border border-default bg-elevated p-1 shadow-xl">
      <a
        href="/cv/CV_Komla_Etonam_Georges_EKLOU_FR.pdf"
        download="CV_Komla_Etonam_Georges_EKLOU_FR.pdf"
        class="flex min-h-11 items-center justify-between rounded-lg px-3 text-sm font-medium text-highlighted transition-colors hover:bg-accented focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
      >
        <span class="flex items-center gap-2">
          <UIcon name="i-lucide-file-text" class="size-4 text-primary" />
          {{ t('hero.cvFrench') }}
        </span>
        <UIcon name="i-lucide-download" class="size-4 text-dimmed" />
      </a>
      <a
        href="/cv/CV_Komla_Etonam_Georges_EKLOU_EN.pdf"
        download="CV_Komla_Etonam_Georges_EKLOU_EN.pdf"
        class="flex min-h-11 items-center justify-between rounded-lg px-3 text-sm font-medium text-highlighted transition-colors hover:bg-accented focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
      >
        <span class="flex items-center gap-2">
          <UIcon name="i-lucide-file-text" class="size-4 text-primary" />
          {{ t('hero.cvEnglish') }}
        </span>
        <UIcon name="i-lucide-download" class="size-4 text-dimmed" />
      </a>
    </div>
  </details>
</template>
