<script setup lang="ts">
const { locale } = useI18n()

// Keep the <html lang> attribute in sync with the active locale.
useHead({
  htmlAttrs: { lang: locale }
})
</script>

<template>
  <UApp>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UApp>
</template>
