<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    delay?: number
  }>(),
  { delay: 0 }
)

const target = ref<HTMLElement | null>(null)
const visible = ref(false)

onMounted(() => {
  const el = target.value
  if (!el) return

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry?.isIntersecting) {
        visible.value = true
        observer.disconnect()
      }
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  )

  observer.observe(el)
})
</script>

<template>
  <div
    ref="target"
    class="reveal-on-scroll"
    :class="{ 'is-visible': visible }"
    :style="{ transitionDelay: `${delay}ms` }"
  >
    <slot />
  </div>
</template>
