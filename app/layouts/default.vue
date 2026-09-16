<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <div class="min-h-screen flex flex-col portfolio-layout">
    <a class="skip-link" href="#main-content">{{ t('navigation.skip') }}</a>
    <PortfolioNav />

    <!-- Language switch + theme toggle (fixed, top-right) -->
    <div class="portfolio-tools">
      <LanguageSwitcher />
      <div class="portfolio-mode-toggle">
        <ColorModeToggle />
      </div>
    </div>

    <main id="main-content" class="flex-1">
      <slot />
    </main>

    <footer class="portfolio-footer">
      <UContainer class="portfolio-footer-content">
        <p>© {{ new Date().getFullYear() }} Komla Etonam Georges EKLOU — {{ t('footer.role') }}.</p>
        <div>
          <a
            href="https://github.com/Georginio-prod"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-highlighted transition-colors duration-300"
          >GitHub</a>
          <a
            href="https://www.linkedin.com/in/komla-etonam-georges-eklou-68518b23b/"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-highlighted transition-colors duration-300"
          >LinkedIn</a>
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
