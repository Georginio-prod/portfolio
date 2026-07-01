<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <div class="min-h-screen flex flex-col bg-default text-default">
    <!-- Language switch + theme toggle (fixed, top-right) -->
    <div class="fixed top-3 right-3 sm:top-4 sm:right-4 z-50 flex items-center gap-2">
      <LanguageSwitcher />
      <div class="rounded-full border border-default bg-elevated/90 p-1 shadow-lg backdrop-blur-md">
        <ColorModeToggle />
      </div>
    </div>

    <main class="flex-1">
      <slot />
    </main>

    <footer class="border-t border-default py-10">
      <UContainer
        class="flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-muted"
      >
        <p>© {{ new Date().getFullYear() }} Komla Etonam Georges EKLOU — {{ t('footer.role') }}.</p>
        <div class="flex items-center gap-4">
          <a
            href="https://github.com/Georginio-prod"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-highlighted transition-colors duration-300"
          >GitHub</a>
          <a
            href="https://www.frontendmentor.io/profile/Georginio-prod?tab=solutions"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-highlighted transition-colors duration-300"
          >Frontend Mentor</a>
        </div>
      </UContainer>
    </footer>
  </div>
</template>
