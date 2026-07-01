<script setup lang="ts">
const colorMode = useColorMode()

const isDark = computed({
  get: () => colorMode.value === 'dark',
  set: (value: boolean) => {
    colorMode.preference = value ? 'dark' : 'light'
  }
})
</script>

<template>
  <ClientOnly>
    <UButton
      :icon="isDark ? 'i-lucide-moon' : 'i-lucide-sun'"
      color="neutral"
      variant="ghost"
      size="lg"
      :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
      :title="isDark ? 'Light mode' : 'Dark mode'"
      @click="isDark = !isDark"
    />
    <template #fallback>
      <div class="size-9" />
    </template>
  </ClientOnly>
</template>
