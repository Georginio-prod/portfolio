<script setup lang="ts">
const links = [
  { label: 'Home', to: '#home' },
  { label: 'About', to: '#about' },
  { label: 'Skills', to: '#skills' },
  { label: 'Projects', to: '#projects' },
  { label: 'Experience', to: '#experience' }
]

const open = ref(false)
const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 24
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <div class="min-h-screen flex flex-col bg-neutral-950 text-white">
    <header class="fixed inset-x-0 top-0 z-50 px-4 pt-4 transition-all duration-500">
      <UContainer>
        <div
          class="flex items-center justify-between gap-4 rounded-2xl px-4 sm:px-6 h-14 transition-all duration-500"
          :class="
            scrolled
              ? 'bg-neutral-950/80 backdrop-blur-xl shadow-lg shadow-black/40 ring-1 ring-white/10'
              : 'bg-white/95 backdrop-blur shadow-lg shadow-black/20 ring-1 ring-black/5'
          "
        >
          <NuxtLink
            to="#home"
            class="font-bold text-sm sm:text-base tracking-tight transition-colors duration-300"
            :class="scrolled ? 'text-white' : 'text-neutral-900'"
          >
            K. EKLOU
          </NuxtLink>

          <nav class="hidden md:flex items-center gap-1">
            <NuxtLink
              v-for="link in links"
              :key="link.to"
              :to="link.to"
              class="nav-link px-3 py-1.5 rounded-lg text-sm font-medium transition-colors duration-300"
              :class="
                scrolled
                  ? 'text-neutral-400 hover:text-white'
                  : 'text-neutral-600 hover:text-neutral-900'
              "
            >
              {{ link.label }}
            </NuxtLink>
          </nav>

          <UButton
            class="md:hidden rounded-xl"
            :color="scrolled ? 'neutral' : 'neutral'"
            variant="ghost"
            :icon="open ? 'i-lucide-x' : 'i-lucide-menu'"
            aria-label="Menu"
            @click="open = !open"
          />
        </div>

        <Transition
          enter-active-class="transition duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="open"
            class="md:hidden mt-2 rounded-2xl bg-neutral-950/95 backdrop-blur-xl p-2 shadow-xl ring-1 ring-white/10"
          >
            <NuxtLink
              v-for="link in links"
              :key="link.to"
              :to="link.to"
              class="block px-4 py-2.5 rounded-xl text-sm font-medium text-neutral-300 hover:bg-white/5 hover:text-white transition"
              @click="open = false"
            >
              {{ link.label }}
            </NuxtLink>
          </div>
        </Transition>
      </UContainer>
    </header>

    <main class="flex-1">
      <slot />
    </main>

    <footer class="border-t border-white/10 py-10">
      <UContainer
        class="flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-neutral-400"
      >
        <p>© {{ new Date().getFullYear() }} Komla Etonam Georges EKLOU — Full Stack Developer.</p>
        <div class="flex items-center gap-4">
          <a
            href="https://github.com/Georginio-prod"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-white transition-colors duration-300"
          >GitHub</a>
          <a
            href="https://www.frontendmentor.io/profile/Georginio-prod?tab=solutions"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:text-white transition-colors duration-300"
          >Frontend Mentor</a>
        </div>
      </UContainer>
    </footer>
  </div>
</template>
