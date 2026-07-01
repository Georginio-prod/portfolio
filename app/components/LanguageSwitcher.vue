<script setup lang="ts">
const { locale, setLocale, t } = useI18n()

// The choice is stored in this cookie and restored before render by the
// `restore-locale` plugin (SSR + client), avoiding any hydration mismatch.
const localeCookie = useCookie<string>('locale', {
  maxAge: 60 * 60 * 24 * 365,
  sameSite: 'lax',
  path: '/'
})

const options = [
  { code: 'en', label: 'EN' },
  { code: 'fr', label: 'FR' }
] as const

const activeIndex = computed(() =>
  Math.max(0, options.findIndex(o => o.code === locale.value))
)

function choose(code: string) {
  if (locale.value === code) return
  setLocale(code as 'en' | 'fr')
  localeCookie.value = code
}
</script>

<template>
  <div
    class="relative flex items-center rounded-full border border-default bg-elevated/90 p-1 shadow-lg backdrop-blur-md"
    role="group"
    :aria-label="t('switcher.label')"
  >
    <!-- Sliding highlight -->
    <span
      class="pointer-events-none absolute bottom-1 top-1 w-9 rounded-full bg-primary transition-transform duration-300 ease-out"
      :style="{ transform: `translateX(${activeIndex * 100}%)` }"
      aria-hidden="true"
    />
    <button
      v-for="option in options"
      :key="option.code"
      type="button"
      class="relative z-10 w-9 rounded-full py-1.5 text-xs font-semibold transition-colors duration-200"
      :class="locale === option.code ? 'text-white' : 'text-muted hover:text-highlighted'"
      :aria-pressed="locale === option.code"
      :aria-label="`${t('switcher.label')}: ${option.label}`"
      @click="choose(option.code)"
    >
      {{ option.label }}
    </button>
  </div>
</template>
