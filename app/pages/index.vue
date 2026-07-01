<script setup lang="ts">
// t() renders flat strings and <i18n-t> the rich paragraphs. Structured content
// (arrays of objects) is read with tm() and resolved to plain strings with rt()
// inside computeds, so templates iterate clean data. Single source: the locale
// JSON files.
const { t, tm, rt } = useI18n()

// Language-agnostic tech list (proper names stay the same in every locale).
const heroSkills = [
  'Vue.js',
  'Nuxt.js',
  'JavaScript',
  'TypeScript',
  'Solidity',
  'Tailwind CSS',
  'React',
  'Node.js',
  'Web3',
  'Git'
]

// Links / icons / tags are language-agnostic; the translatable text (title,
// description, status) comes from the locale files and is merged in by id.
const projectMeta: Record<string, { url: string, icon: string, tags: string[] }> = {
  cnc: { url: 'https://app.cncportal.io/login', icon: 'i-lucide-building-2', tags: ['Vue', 'Team', 'Pro'] },
  nova: { url: 'https://novagraphikvisu.com/', icon: 'i-lucide-palette', tags: ['Nuxt', 'Landing', 'Pro'] },
  orga: { url: 'https://www.orga-africa.com/', icon: 'i-lucide-store', tags: ['Nuxt', 'Landing', 'Pro'] },
  pulse: { url: 'https://pulse-score-two.vercel.app/', icon: 'i-lucide-activity', tags: ['Vue', 'App', 'WIP'] },
  meet: { url: 'https://meet-landing-page-kohl.vercel.app/', icon: 'i-lucide-video', tags: ['Vue', 'Responsive', 'Landing'] },
  pomodoro: { url: 'https://promodoro-app-iota.vercel.app/', icon: 'i-lucide-timer', tags: ['Vue', 'App', 'UI'] },
  audiophile: { url: 'https://audiophile-ecommerce-psi-ecru.vercel.app/', icon: 'i-lucide-headphones', tags: ['E-commerce', 'Front-end'] },
  fem: { url: 'https://www.frontendmentor.io/profile/Georginio-prod?tab=solutions', icon: 'i-lucide-code-2', tags: ['Challenges', 'HTML/CSS'] }
}

const focusAreas = computed(() =>
  (tm('focusAreas') as any[]).map(a => ({ title: rt(a.title), description: rt(a.description) }))
)

const softSkills = computed(() =>
  (tm('about.softSkills') as any[]).map(s => rt(s))
)

const projects = computed(() =>
  (tm('projects.items') as any[]).map((item) => {
    const id = rt(item.id)
    return {
      id,
      title: rt(item.title),
      description: rt(item.description),
      status: rt(item.status),
      ...projectMeta[id]
    }
  })
)

const experiences = computed(() =>
  (tm('experience.items') as any[]).map(e => ({
    period: rt(e.period),
    role: rt(e.role),
    company: rt(e.company),
    place: rt(e.place),
    points: (e.points as any[]).map(p => rt(p))
  }))
)

const education = computed(() =>
  (tm('education.items') as any[]).map(e => ({
    period: rt(e.period),
    title: rt(e.title),
    detail: rt(e.detail),
    school: rt(e.school)
  }))
)

const interests = computed(() =>
  (tm('interests.items') as any[]).map(i => rt(i))
)

const contactLinks = computed(() => [
  {
    key: 'email',
    label: t('contact.emailLabel'),
    value: 'etonameklou19@gmail.com',
    href: 'mailto:etonameklou19@gmail.com',
    icon: 'i-lucide-mail',
    wide: true
  },
  {
    key: 'phone',
    label: t('contact.phoneLabel'),
    value: '+228 98 93 85 55',
    href: 'tel:+22898938555',
    icon: 'i-lucide-phone',
    wide: false
  },
  {
    key: 'github',
    label: t('contact.githubLabel'),
    value: 'Georginio-prod',
    href: 'https://github.com/Georginio-prod',
    icon: 'i-simple-icons-github',
    wide: false
  }
])
</script>

<template>
  <div>
    <!-- Hero -->
    <section id="home" class="hero-section relative min-h-[92vh] overflow-hidden pt-28 pb-16 md:pt-32 md:pb-24">
      <!-- Geometric background -->
      <svg
        class="hero-grid pointer-events-none absolute inset-0 h-full w-full"
        preserveAspectRatio="xMidYMid slice"
        viewBox="0 0 1200 800"
        xmlns="http://www.w3.org/2000/svg"
        aria-hidden="true"
      >
        <defs>
          <pattern id="hero-grid" width="80" height="80" patternUnits="userSpaceOnUse">
            <path d="M 80 0 L 0 0 0 80" fill="none" stroke="rgba(120,120,140,0.06)" stroke-width="1" />
          </pattern>
        </defs>
        <rect width="1200" height="800" fill="url(#hero-grid)" />
        <line x1="0" y1="0" x2="1200" y2="800" stroke="rgba(120,120,140,0.04)" stroke-width="2" />
        <line x1="1200" y1="0" x2="0" y2="800" stroke="rgba(120,120,140,0.04)" stroke-width="2" />
        <g class="animate-float-slow">
          <polygon points="150,100 300,50 350,200 200,250" fill="none" stroke="rgba(161,161,170,0.12)" stroke-width="1" />
        </g>
        <g class="animate-float-slow-reverse">
          <polygon points="900,600 1050,550 1100,700 950,750" fill="none" stroke="rgba(161,161,170,0.10)" stroke-width="1" />
        </g>
        <g class="hero-spin-slow" style="transform-origin: 1100px 150px">
          <circle cx="1100" cy="150" r="100" fill="none" stroke="rgba(120,120,140,0.08)" stroke-width="1" />
        </g>
      </svg>

      <div
        class="pointer-events-none absolute -left-40 top-10 size-96 rounded-full bg-primary/10 blur-3xl"
      />
      <div
        class="pointer-events-none absolute -right-32 bottom-20 size-80 rounded-full bg-secondary/10 blur-3xl"
      />

      <UContainer class="relative z-10">
        <header class="hero-animate mb-12 border-b border-default pb-8 md:mb-16">
          <div class="mb-3 flex items-center gap-3">
            <span class="hero-gradient-text text-5xl font-bold md:text-6xl">{{ t('hero.greeting') }}</span>
            <span class="hero-animate hero-animate-delay-1 text-5xl md:text-6xl">👋</span>
          </div>
          <h1 class="hero-animate hero-animate-delay-1 text-3xl font-bold tracking-tight text-highlighted break-words sm:text-5xl lg:text-6xl">
            {{ t('hero.namePrefix') }} {{ t('hero.name') }}
          </h1>
          <p class="hero-animate hero-animate-delay-2 mt-3 text-xl font-light text-primary md:text-2xl">
            {{ t('hero.role') }}
          </p>
        </header>

        <div class="grid items-start gap-12 lg:grid-cols-[1fr_auto] lg:gap-16">
          <div class="space-y-10">
            <i18n-t
              keypath="hero.bio"
              tag="p"
              scope="global"
              class="hero-animate hero-animate-delay-2 max-w-2xl text-lg leading-relaxed text-muted"
            >
              <template #university>
                <span class="font-semibold text-highlighted">{{ t('hero.bioUniversity') }}</span>
              </template>
              <template #focus>
                <span class="italic text-primary">{{ t('hero.bioFocus') }}</span>
              </template>
              <template #company>
                <span class="font-semibold text-highlighted">{{ t('hero.bioCompany') }}</span>
              </template>
            </i18n-t>

            <div class="hero-animate hero-animate-delay-3">
              <h3 class="mb-3 text-sm font-semibold uppercase tracking-widest text-dimmed">
                {{ t('hero.skillsTitle') }}
              </h3>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="skill in heroSkills"
                  :key="skill"
                  class="hero-skill-tag rounded-full border border-primary/40 bg-primary/10 px-3 py-1 text-sm text-primary transition-colors hover:bg-primary/20"
                >
                  {{ skill }}
                </span>
              </div>
            </div>

            <div class="hero-animate hero-animate-delay-4">
              <h3 class="mb-4 text-sm font-semibold uppercase tracking-widest text-dimmed">
                {{ t('hero.focusTitle') }}
              </h3>
              <div class="grid gap-4 sm:grid-cols-3">
                <div
                  v-for="area in focusAreas"
                  :key="area.title"
                  class="hero-focus-card rounded-xl border border-default bg-elevated p-4 transition-colors hover:border-primary/40 hover:bg-accented"
                >
                  <h4 class="font-medium text-highlighted">{{ area.title }}</h4>
                  <p class="mt-1 text-sm text-muted">{{ area.description }}</p>
                </div>
              </div>
            </div>

            <p class="hero-animate hero-animate-delay-4 text-muted italic">
              {{ t('hero.tagline') }}
            </p>

            <div class="hero-animate hero-animate-delay-4 flex flex-wrap gap-3 pt-2">
              <UButton
                to="#projects"
                size="lg"
                class="rounded-full px-6 font-semibold"
                trailing-icon="i-lucide-arrow-right"
              >
                {{ t('hero.ctaProjects') }}
              </UButton>
              <UButton
                to="#contact"
                size="lg"
                color="neutral"
                variant="outline"
                class="rounded-full px-6 font-semibold"
                icon="i-lucide-mail"
              >
                {{ t('hero.ctaContact') }}
              </UButton>
            </div>
          </div>

          <!-- Profile visual -->
          <div class="hero-animate hero-animate-delay-3 hidden lg:flex lg:flex-col lg:items-center lg:gap-6">
            <div class="relative">
              <div class="hero-avatar-ring absolute -inset-3 rounded-full border border-primary/20" />
              <div class="hero-avatar-ring absolute -inset-6 rounded-full border border-default" />
              <div
                class="relative flex size-56 items-center justify-center rounded-full bg-gradient-to-br from-primary/20 via-[var(--ui-bg-elevated)] to-secondary/10 ring-1 ring-primary/30"
              >
                <span class="bg-gradient-to-br from-primary via-primary-400 to-secondary bg-clip-text text-5xl font-bold text-transparent">
                  KE
                </span>
              </div>
            </div>
            <div class="w-52 space-y-2 rounded-2xl border border-default bg-elevated p-4 text-center backdrop-blur-sm">
              <p class="text-xs uppercase tracking-widest text-dimmed">{{ t('hero.basedIn') }}</p>
              <p class="font-medium text-highlighted">{{ t('hero.location') }}</p>
              <div class="flex items-center justify-center gap-1.5 pt-1">
                <span class="relative flex size-2">
                  <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75" />
                  <span class="relative inline-flex size-2 rounded-full bg-emerald-400" />
                </span>
                <span class="text-xs text-emerald-500 dark:text-emerald-400">{{ t('hero.openToWork') }}</span>
              </div>
            </div>
          </div>
        </div>
      </UContainer>
    </section>

    <!-- About -->
    <section id="about" class="py-20 md:py-28 border-t border-default">
      <UContainer>
        <RevealOnScroll>
          <div class="grid md:grid-cols-2 gap-12 items-start">
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                {{ t('about.label') }}
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight text-highlighted">
                {{ t('about.heading') }}
              </h2>
              <i18n-t keypath="about.p1" tag="p" scope="global" class="mt-5 text-muted leading-relaxed">
                <template #degree>
                  <span class="text-highlighted font-medium">{{ t('about.p1Degree') }}</span>
                </template>
                <template #company>
                  <span class="text-highlighted font-medium">{{ t('about.p1Company') }}</span>
                </template>
              </i18n-t>
              <i18n-t keypath="about.p2" tag="p" scope="global" class="mt-4 text-muted leading-relaxed">
                <template #devops>
                  <span class="text-highlighted font-medium">{{ t('about.p2Devops') }}</span>
                </template>
              </i18n-t>
            </div>

            <div class="space-y-4">
              <div class="rounded-2xl bg-elevated ring-1 ring-default p-6 space-y-3 text-sm text-muted transition-all duration-500 hover:ring-primary/40">
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-map-pin" class="size-5 text-primary shrink-0" /> {{ t('about.location') }}
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-languages" class="size-5 text-primary shrink-0" /> {{ t('about.languages') }}
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-mail" class="size-5 text-primary shrink-0" /> etonameklou19@gmail.com
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-phone" class="size-5 text-primary shrink-0" /> {{ t('about.phone') }}
                </p>
              </div>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="skill in softSkills"
                  :key="skill"
                  class="rounded-full bg-elevated ring-1 ring-default px-3 py-1 text-xs text-muted transition-all duration-300 hover:ring-primary/40 hover:text-highlighted"
                >
                  {{ skill }}
                </span>
              </div>
            </div>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>

    <!-- Projects -->
    <section id="projects" class="py-20 md:py-28 border-t border-default">
      <UContainer>
        <RevealOnScroll>
          <div class="max-w-2xl mb-12">
            <p class="text-sm font-semibold uppercase tracking-widest text-secondary mb-3">{{ t('projects.label') }}</p>
            <h2 class="text-3xl md:text-4xl font-bold tracking-tight text-highlighted">
              {{ t('projects.heading') }}
            </h2>
            <p class="mt-3 text-muted">
              <span class="hidden lg:inline">{{ t('projects.subtitle') }}</span>
              <span class="lg:hidden">{{ t('projects.subtitleTouch') }}</span>
            </p>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="80">
          <div class="relative overflow-x-auto scrollbar-hide pb-4 -mx-4 px-4 md:-mx-6 md:px-6">
            <div class="flex gap-8 w-max">
              <ProjectCard
                v-for="project in projects"
                :key="project.id"
                :project="project"
              />
            </div>
          </div>
          <p class="mt-6 text-center text-sm text-dimmed">
            {{ t('projects.scrollHint') }}
          </p>
        </RevealOnScroll>
      </UContainer>
    </section>

    <!-- Experience -->
    <section id="experience" class="py-20 md:py-28 border-t border-default">
      <UContainer>
        <div class="grid lg:grid-cols-2 gap-12">
          <RevealOnScroll>
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                {{ t('experience.label') }}
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight mb-8 text-highlighted">{{ t('experience.heading') }}</h2>
              <ol class="relative border-l border-default space-y-8 pl-6">
                <li v-for="exp in experiences" :key="exp.role + exp.period" class="relative group">
                  <span class="timeline-dot absolute -left-[31px] top-1.5 size-3 rounded-full bg-primary ring-4 ring-[var(--ui-bg)] transition-transform duration-300 group-hover:scale-125" />
                  <p class="text-xs uppercase tracking-widest text-dimmed">{{ exp.period }}</p>
                  <h3 class="mt-1 font-semibold text-lg text-highlighted">{{ exp.role }}</h3>
                  <p class="text-sm text-primary">{{ exp.company }} · {{ exp.place }}</p>
                  <ul class="mt-2 space-y-1 text-sm text-muted list-disc list-inside">
                    <li v-for="p in exp.points" :key="p">{{ p }}</li>
                  </ul>
                </li>
              </ol>
            </div>
          </RevealOnScroll>

          <RevealOnScroll :delay="120">
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-secondary mb-3">
                {{ t('education.label') }}
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight mb-8 text-highlighted">{{ t('education.heading') }}</h2>
              <div class="space-y-4">
                <div
                  v-for="edu in education"
                  :key="edu.title"
                  class="rounded-2xl bg-elevated ring-1 ring-default p-6 transition-all duration-500 hover:ring-primary/40 hover:-translate-y-0.5"
                >
                  <p class="text-xs uppercase tracking-widest text-dimmed">{{ edu.period }}</p>
                  <h3 class="mt-1 font-semibold text-lg text-highlighted">{{ edu.title }}</h3>
                  <p class="mt-1 text-sm text-muted">{{ edu.detail }}</p>
                  <p class="mt-2 text-sm text-primary">{{ edu.school }}</p>
                </div>
              </div>

              <div class="mt-6 rounded-2xl bg-elevated ring-1 ring-default p-6">
                <h3 class="text-xs font-semibold uppercase tracking-widest text-dimmed mb-3">
                  {{ t('interests.title') }}
                </h3>
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="i in interests"
                    :key="i"
                    class="rounded-full bg-accented ring-1 ring-default px-3 py-1 text-xs text-muted"
                  >
                    {{ i }}
                  </span>
                </div>
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </UContainer>
    </section>

    <!-- Contact -->
    <section id="contact" class="py-20 md:py-28 border-t border-default">
      <UContainer>
        <RevealOnScroll>
          <div class="grid md:grid-cols-5 gap-10 md:gap-16 items-start">
            <div class="md:col-span-2">
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                {{ t('contact.label') }}
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight text-highlighted">
                {{ t('contact.heading') }}
              </h2>
              <p class="mt-4 text-muted leading-relaxed">
                {{ t('contact.subtitle') }}
              </p>
            </div>

            <div class="md:col-span-3 grid gap-3 sm:grid-cols-2">
              <a
                v-for="link in contactLinks"
                :key="link.key"
                :href="link.href"
                :target="link.href.startsWith('http') ? '_blank' : undefined"
                :rel="link.href.startsWith('http') ? 'noopener noreferrer' : undefined"
                class="group flex items-start gap-4 rounded-2xl bg-elevated ring-1 ring-default p-5 transition-all duration-500 hover:-translate-y-1 hover:ring-primary/40 hover:bg-accented"
                :class="link.wide ? 'sm:col-span-2' : ''"
              >
                <div
                  class="flex size-11 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary ring-1 ring-primary/20 transition-transform duration-300 group-hover:scale-110"
                >
                  <UIcon :name="link.icon" class="size-5" />
                </div>
                <div class="min-w-0">
                  <p class="text-xs font-semibold uppercase tracking-widest text-dimmed">
                    {{ link.label }}
                  </p>
                  <p class="mt-1 text-sm font-medium text-highlighted truncate group-hover:text-primary transition-colors duration-300">
                    {{ link.value }}
                  </p>
                </div>
                <UIcon
                  name="i-lucide-arrow-up-right"
                  class="ml-auto size-4 shrink-0 text-dimmed transition-all duration-300 group-hover:text-primary group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                />
              </a>
            </div>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>
  </div>
</template>
