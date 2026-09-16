<script setup lang="ts">
const { t, tm, rt } = useI18n()
const { projects } = useProjects()

const heroSkills = [
  'Vue.js', 'Nuxt.js', 'React', 'TypeScript', 'Node.js',
  'Solidity', 'Web3', 'Tailwind CSS', 'Docker'
]

const skillGroups = computed(() =>
  (tm('skillGroups') as any[]).map(group => ({ title: rt(group.title), items: (group.items as any[]).map(item => rt(item)) }))
)
const softSkills = computed(() => (tm('about.softSkills') as any[]).map(skill => rt(skill)))
const experiences = computed(() =>
  (tm('experience.items') as any[]).map(item => ({
    period: rt(item.period), role: rt(item.role), company: rt(item.company), place: rt(item.place),
    points: (item.points as any[]).map(point => rt(point))
  }))
)
const education = computed(() =>
  (tm('education.items') as any[]).map(item => ({
    period: rt(item.period), title: rt(item.title), detail: rt(item.detail), school: rt(item.school)
  }))
)
const interests = computed(() => (tm('interests.items') as any[]).map(item => rt(item)))

type ProjectFilter = 'featured' | 'all' | 'learning'
const featuredProjectIds = ['cnc', 'nova', 'designer', 'orga']
const learningProjectIds = ['meet', 'pomodoro', 'audiophile', 'fem']
const activeFilter = ref<ProjectFilter>('featured')
const activeProject = ref(0)

const projectFilters = computed(() => [
  { id: 'featured' as const, label: t('projects.filters.featured') },
  { id: 'all' as const, label: t('projects.filters.all') },
  { id: 'learning' as const, label: t('projects.filters.learning') }
])
const visibleProjects = computed(() => {
  if (activeFilter.value === 'featured') return projects.value.filter(project => featuredProjectIds.includes(project.id))
  if (activeFilter.value === 'learning') return projects.value.filter(project => learningProjectIds.includes(project.id))
  return projects.value
})
const currentProject = computed(() => visibleProjects.value[activeProject.value])
const projectCount = computed(() => String(projects.value.length).padStart(2, '0'))

const contactLinks = computed(() => [
  { key: 'email', label: t('contact.emailLabel'), value: 'etonameklou19@gmail.com', href: 'mailto:etonameklou19@gmail.com', icon: 'i-lucide-mail' },
  { key: 'phone', label: t('contact.phoneLabel'), value: '+228 98 93 85 55', href: 'tel:+22898938555', icon: 'i-lucide-phone' },
  { key: 'github', label: t('contact.githubLabel'), value: 'Georginio-prod', href: 'https://github.com/Georginio-prod', icon: 'i-simple-icons-github' },
  { key: 'linkedin', label: t('contact.linkedinLabel'), value: 'LinkedIn', href: 'https://www.linkedin.com/in/komla-etonam-georges-eklou-68518b23b/', icon: 'i-simple-icons-linkedin' }
])

function setProjectFilter(filter: ProjectFilter) {
  activeFilter.value = filter
  activeProject.value = 0
}
function goToProject(step: number) {
  const count = visibleProjects.value.length
  activeProject.value = (activeProject.value + step + count) % count
}
</script>

<template>
  <div class="portfolio-shell overflow-hidden">
    <section id="home" class="signal-hero relative isolate">
      <div class="signal-grain" aria-hidden="true" />
      <div class="signal-orbit signal-orbit-one" aria-hidden="true" />
      <div class="signal-orbit signal-orbit-two" aria-hidden="true" />

      <UContainer class="relative z-10">
        <div class="hero-topline hero-enter">
          <p class="signal-eyebrow"><span class="status-light" aria-hidden="true" />{{ t('portfolio.availability') }}</p>
          <p class="signal-eyebrow hidden sm:block">Lomé, Togo · 06.13 N / 01.22 E</p>
        </div>

        <div class="hero-composition">
          <div class="hero-copy">
            <p class="hero-role hero-enter hero-enter-delay-1">{{ t('hero.role') }}</p>
            <h1 class="hero-name hero-enter hero-enter-delay-2" :aria-label="t('hero.name')">
              <span class="hero-name-prefix">{{ t('hero.namePrefix') }}</span>
              <span>Komla</span>
              <span class="hero-name-last">Eklou</span>
            </h1>
            <p class="hero-intro hero-enter hero-enter-delay-3">{{ t('portfolio.heroStatement') }}</p>
            <div class="hero-actions hero-enter hero-enter-delay-4">
              <a href="#projects" class="signal-button signal-button-primary">
                {{ t('hero.ctaProjects') }} <UIcon name="i-lucide-arrow-down-right" class="size-4" />
              </a>
              <CvDownloadMenu />
            </div>
          </div>

          <div class="hero-portrait hero-enter hero-enter-delay-3">
            <div class="portrait-sun" aria-hidden="true" />
            <div class="portrait-frame">
              <img src="/profile.jpg" :alt="t('hero.name')" class="portrait-image">
            </div>
            <div class="portrait-caption"><span class="portrait-caption-index">01</span><span>{{ t('hero.openToWork') }}</span></div>
            <div class="portrait-stamp" aria-hidden="true"><span>WEB · WEB3 · PRODUCT</span></div>
          </div>
        </div>

        <div class="hero-footer hero-enter hero-enter-delay-4">
          <p class="hero-location"><span>{{ t('hero.basedIn') }}</span><strong>{{ t('hero.location') }}</strong></p>
          <a href="#about" class="hero-scroll-link"><span>{{ t('portfolio.scroll') }}</span><span class="hero-scroll-line" aria-hidden="true" /></a>
          <p class="hero-count"><span>{{ projectCount }}</span> {{ t('portfolio.projectsCount') }}</p>
        </div>
      </UContainer>

      <div class="skill-ticker" aria-label="Technical skills">
        <div class="skill-ticker-track">
          <template v-for="loop in 2" :key="loop">
            <span v-for="skill in heroSkills" :key="`${loop}-${skill}`" class="skill-ticker-item">{{ skill }} <i aria-hidden="true">✦</i></span>
          </template>
        </div>
      </div>
    </section>

    <section id="about" class="portfolio-section about-section">
      <UContainer>
        <RevealOnScroll>
          <div class="section-kicker"><span>01</span><p>{{ t('about.label') }}</p></div>
          <div class="about-lead">
            <h2>{{ t('about.heading') }}</h2>
            <div class="about-prose">
              <i18n-t keypath="about.p1" tag="p" scope="global"><template #degree><strong>{{ t('about.p1Degree') }}</strong></template></i18n-t>
              <i18n-t keypath="about.p2" tag="p" scope="global"><template #devops><strong>{{ t('about.p2Devops') }}</strong></template></i18n-t>
            </div>
          </div>
        </RevealOnScroll>

        <div class="capability-grid">
          <RevealOnScroll v-for="(group, index) in skillGroups" :key="group.title" :delay="index * 90">
            <article class="capability-card">
              <p class="capability-number">0{{ index + 1 }}</p><h3>{{ group.title }}</h3>
              <ul><li v-for="item in group.items" :key="item">{{ item }}</li></ul>
            </article>
          </RevealOnScroll>
        </div>

        <RevealOnScroll :delay="120">
          <div class="about-meta-row">
            <div class="about-meta"><UIcon name="i-lucide-map-pin" class="size-4" /><span>{{ t('about.location') }}</span></div>
            <div class="about-meta"><UIcon name="i-lucide-languages" class="size-4" /><span>{{ t('about.languages') }}</span></div>
            <div class="soft-skills"><span v-for="skill in softSkills" :key="skill">{{ skill }}</span></div>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>

    <section id="projects" class="portfolio-section projects-section">
      <UContainer>
        <RevealOnScroll>
          <div class="projects-heading">
            <div><div class="section-kicker"><span>02</span><p>{{ t('projects.label') }}</p></div><h2>{{ t('portfolio.projectsHeading') }}</h2></div>
            <p>{{ t('projects.subtitle') }}</p>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="80">
          <div class="project-controls">
            <div class="project-filters" :aria-label="t('projects.filterLabel')">
              <button v-for="filter in projectFilters" :key="filter.id" type="button" :class="{ 'is-active': activeFilter === filter.id }" :aria-pressed="activeFilter === filter.id" @click="setProjectFilter(filter.id)">{{ filter.label }}</button>
            </div>
            <div class="project-arrows">
              <button type="button" :aria-label="t('projects.prev')" @click="goToProject(-1)"><UIcon name="i-lucide-arrow-left" class="size-4" /></button>
              <button type="button" :aria-label="t('projects.next')" @click="goToProject(1)"><UIcon name="i-lucide-arrow-right" class="size-4" /></button>
            </div>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="130">
          <ProjectCard v-if="currentProject" :key="`${activeFilter}-${currentProject.id}`" :project="currentProject" :index="activeProject" :total="visibleProjects.length" />
          <div class="project-selector" role="tablist" :aria-label="t('portfolio.projectSelector')">
            <button v-for="(project, index) in visibleProjects" :key="project.id" type="button" role="tab" :aria-selected="index === activeProject" :class="{ 'is-active': index === activeProject }" @click="activeProject = index">
              <span>{{ String(index + 1).padStart(2, '0') }}</span>{{ project.title }}
            </button>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>

    <section id="experience" class="portfolio-section trajectory-section">
      <UContainer>
        <RevealOnScroll><div class="trajectory-heading"><div class="section-kicker"><span>03</span><p>{{ t('experience.label') }}</p></div><h2>{{ t('portfolio.trajectoryHeading') }}</h2></div></RevealOnScroll>
        <div class="trajectory-layout">
          <div class="trajectory-list">
            <RevealOnScroll v-for="(experience, index) in experiences" :key="experience.role + experience.period" :delay="index * 65">
              <article class="trajectory-card">
                <p class="trajectory-period">{{ experience.period }}</p>
                <div><h3>{{ experience.role }}</h3><p class="trajectory-company">{{ experience.company }} <span>—</span> {{ experience.place }}</p><ul><li v-for="point in experience.points" :key="point">{{ point }}</li></ul></div>
              </article>
            </RevealOnScroll>
          </div>

          <RevealOnScroll :delay="130">
            <aside class="trajectory-aside">
              <div class="trajectory-orbit" aria-hidden="true"><span>build</span><span>learn</span><span>share</span></div>
              <div v-for="item in education" :key="item.title" class="education-card">
                <p class="section-kicker"><span>+</span>{{ t('education.label') }}</p><p class="education-period">{{ item.period }}</p><h3>{{ item.title }}</h3><p>{{ item.detail }}</p><p class="education-school">{{ item.school }}</p>
              </div>
              <div class="interest-list"><p>{{ t('interests.title') }}</p><span v-for="interest in interests" :key="interest">{{ interest }}</span></div>
            </aside>
          </RevealOnScroll>
        </div>
      </UContainer>
    </section>

    <section id="contact" class="contact-section">
      <UContainer>
        <RevealOnScroll>
          <div class="contact-intro"><div class="section-kicker"><span>04</span><p>{{ t('contact.label') }}</p></div><p>{{ t('contact.subtitle') }}</p></div>
          <a class="contact-email" href="mailto:etonameklou19@gmail.com"><span>{{ t('portfolio.contactLead') }}</span><strong>etonameklou19@gmail.com</strong><UIcon name="i-lucide-arrow-up-right" class="contact-arrow" /></a>
        </RevealOnScroll>
        <div class="contact-grid">
          <a v-for="link in contactLinks" :key="link.key" :href="link.href" :target="link.href.startsWith('http') ? '_blank' : undefined" :rel="link.href.startsWith('http') ? 'noopener noreferrer' : undefined" class="contact-card">
            <UIcon :name="link.icon" class="size-5" /><div><p>{{ link.label }}</p><strong>{{ link.value }}</strong></div><UIcon name="i-lucide-arrow-up-right" class="contact-card-arrow" />
          </a>
        </div>
      </UContainer>
    </section>
  </div>
</template>
