<template>
  <div class="min-h-screen flex flex-col bg-neutral-950 text-white">
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
