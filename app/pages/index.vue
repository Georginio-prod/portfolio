<script setup lang="ts">
interface Project {
  title: string
  description: string
  tags: string[]
  url?: string
  status?: string
  icon: string
}

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

const focusAreas = [
  {
    title: 'Web Applications',
    description: 'Full-stack products with Vue, Nuxt, and React'
  },
  {
    title: 'Web3 & Blockchain',
    description: 'DApps, smart contracts & decentralized integrations'
  },
  {
    title: 'UI Engineering',
    description: 'Pixel-perfect, responsive & accessible interfaces'
  }
]

const coreSkills = [
  { name: 'Vue.js', icon: 'i-simple-icons-vuedotjs' },
  { name: 'Nuxt.js', icon: 'i-simple-icons-nuxtdotjs' },
  { name: 'JavaScript', icon: 'i-simple-icons-javascript' },
  { name: 'TypeScript', icon: 'i-simple-icons-typescript' },
  { name: 'HTML & CSS', icon: 'i-simple-icons-html5' },
  { name: 'Tailwind CSS', icon: 'i-simple-icons-tailwindcss' },
  { name: 'DaisyUI', icon: 'i-simple-icons-daisyui' },
  { name: 'Solidity', icon: 'i-simple-icons-solidity' }
]

const secondarySkills = [
  'React.js / Next.js',
  'Node.js',
  'Python',
  'Java',
  'WordPress',
  'Figma · UI/UX',
  'Docker',
  'Linux',
  'Git / Git Flow',
  'MongoDB',
  'Firebase',
  'MySQL',
  'Scrum'
]

const projects: Project[] = [
  {
    title: 'CNC Portal',
    description:
      'Web portal for CNC. As a development team member, I work on integration and platform features.',
    tags: ['Vue', 'Team', 'Pro'],
    url: 'https://app.cncportal.io/login',
    status: 'Pro',
    icon: 'i-lucide-building-2'
  },
  {
    title: 'Nova Graphik Visu',
    description:
      'Showcase website for the Nova Graphik creative agency: services, portfolio, and team presentation.',
    tags: ['Nuxt', 'Landing', 'Pro'],
    url: 'https://novagraphikvisu.com/',
    status: 'Pro',
    icon: 'i-lucide-palette'
  },
  {
    title: 'OrgaAfrica',
    description:
      'Showcase platform for restaurants and local businesses: orders, payments, and queue management.',
    tags: ['Nuxt', 'Landing', 'Pro'],
    url: 'https://www.orga-africa.com/',
    status: 'Pro',
    icon: 'i-lucide-store'
  },
  {
    title: 'Pulse Score',
    description:
      'Score and performance tracking application, currently in active development.',
    tags: ['Vue', 'App', 'WIP'],
    url: 'https://pulse-score-two.vercel.app/',
    status: 'In progress',
    icon: 'i-lucide-activity'
  },
  {
    title: 'Meet — Landing Page',
    description:
      'Responsive product landing page, pixel-perfect integration with Vue.',
    tags: ['Vue', 'Responsive', 'Landing'],
    url: 'https://meet-landing-page-kohl.vercel.app/',
    icon: 'i-lucide-video'
  },
  {
    title: 'Pomodoro App',
    description:
      'Pomodoro timer for productivity, with customizable settings and themes.',
    tags: ['Vue', 'App', 'UI'],
    url: 'https://promodoro-app-iota.vercel.app/',
    icon: 'i-lucide-timer'
  },
  {
    title: 'Audiophile E-commerce',
    description:
      'Multi-page audio e-commerce store: catalog, cart, and checkout.',
    tags: ['E-commerce', 'Front-end'],
    url: 'https://audiophile-ecommerce-psi-ecru.vercel.app/',
    icon: 'i-lucide-headphones'
  },
  {
    title: 'Frontend Mentor',
    description:
      'My Frontend Mentor challenge solutions: pixel-perfect, responsive, and accessible builds.',
    tags: ['Challenges', 'HTML/CSS'],
    url: 'https://www.frontendmentor.io/profile/Georginio-prod?tab=solutions',
    icon: 'i-lucide-code-2'
  }
]

const experiences = [
  {
    period: 'Since June 2025',
    role: 'Junior Web3 Developer',
    company: 'W3 Frame',
    place: 'Lomé, Avédji — Togo',
    points: ['Building decentralized applications and Web3 integrations.']
  },
  {
    period: 'Dec 2024 – Mar 2025',
    role: 'Customer Service & Sales Analyst Intern',
    company: 'Prodicom Inter Togo',
    place: 'Tsévié — Togo',
    points: [
      'Analyzed customer data to identify purchasing trends.',
      'Created detailed reports on product and sales performance.'
    ]
  },
  {
    period: 'Aug 2024 – Oct 2024',
    role: 'UI Integration',
    company: 'W3 Frame',
    place: 'Lomé — Togo',
    points: [
      'Created and integrated pixel-perfect mockups for web projects.',
      'Developed web applications.'
    ]
  },
  {
    period: 'May 2024 – Aug 2024',
    role: 'Web Developer Intern',
    company: 'New Brain Factory',
    place: 'Klikamé, Lomé — Togo',
    points: [
      'Designed an e-commerce application with React / Next.js (final-year project).'
    ]
  }
]

const education = [
  {
    period: 'Nov 2021 – Jul 2024',
    title: "Bachelor's in Engineering Sciences — Computer Science",
    detail: 'Application Development specialization · Good standing (Bachelor +3)',
    school: 'UCAO / UUT — Lomé, Togo'
  },
  {
    period: 'Nov 2019 – Nov 2020',
    title: 'Scientific Baccalaureate (Series D)',
    detail: 'Second part',
    school: "Lycée Moderne d'Adidogomé — Lomé, Togo"
  }
]

const contactLinks = [
  {
    label: 'Email',
    value: 'etonameklou19@gmail.com',
    href: 'mailto:etonameklou19@gmail.com',
    icon: 'i-lucide-mail'
  },
  {
    label: 'Phone',
    value: '+228 98 93 85 55',
    href: 'tel:+22898938555',
    icon: 'i-lucide-phone'
  },
  {
    label: 'GitHub',
    value: 'Georginio-prod',
    href: 'https://github.com/Georginio-prod',
    icon: 'i-simple-icons-github'
  }
]
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
            <path d="M 80 0 L 0 0 0 80" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
          </pattern>
        </defs>
        <rect width="1200" height="800" fill="url(#hero-grid)" />
        <line x1="0" y1="0" x2="1200" y2="800" stroke="rgba(255,255,255,0.02)" stroke-width="2" />
        <line x1="1200" y1="0" x2="0" y2="800" stroke="rgba(255,255,255,0.02)" stroke-width="2" />
        <g class="animate-float-slow">
          <polygon points="150,100 300,50 350,200 200,250" fill="none" stroke="rgba(59,130,246,0.12)" stroke-width="1" />
        </g>
        <g class="animate-float-slow-reverse">
          <polygon points="900,600 1050,550 1100,700 950,750" fill="none" stroke="rgba(59,130,246,0.1)" stroke-width="1" />
        </g>
        <g class="hero-spin-slow" style="transform-origin: 1100px 150px">
          <circle cx="1100" cy="150" r="100" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
        </g>
      </svg>

      <div
        class="pointer-events-none absolute -left-40 top-10 size-96 rounded-full bg-primary/15 blur-3xl"
      />
      <div
        class="pointer-events-none absolute -right-32 bottom-20 size-80 rounded-full bg-cyan-500/10 blur-3xl"
      />

      <UContainer class="relative z-10">
        <header class="hero-animate mb-12 border-b border-white/10 pb-8 md:mb-16">
          <div class="mb-3 flex items-center gap-3">
            <span class="hero-gradient-text text-5xl font-bold md:text-6xl">Hi</span>
            <span class="hero-animate hero-animate-delay-1 text-5xl md:text-6xl">👋</span>
          </div>
          <h1 class="hero-animate hero-animate-delay-1 text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl">
            I'm Komla Etonam Georges EKLOU
          </h1>
          <p class="hero-animate hero-animate-delay-2 mt-3 text-xl font-light text-primary md:text-2xl">
            Full Stack &amp; Web3 Developer
          </p>
        </header>

        <div class="grid items-start gap-12 lg:grid-cols-[1fr_auto] lg:gap-16">
          <div class="space-y-10">
            <p class="hero-animate hero-animate-delay-2 max-w-2xl text-lg leading-relaxed text-neutral-400">
              Computer Science graduate from
              <span class="font-semibold text-white">UCAO / UUT</span>
              specializing in
              <span class="italic text-primary-300">web development and Web3</span>.
              I build full-stack applications, decentralized integrations, and polished interfaces
              — currently contributing to the
              <span class="font-semibold text-white">CNC</span>
              development team in Lomé, Togo.
            </p>

            <div class="hero-animate hero-animate-delay-3">
              <h3 class="mb-3 text-sm font-semibold uppercase tracking-widest text-neutral-500">
                Technical Skills
              </h3>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="skill in heroSkills"
                  :key="skill"
                  class="hero-skill-tag rounded-full border border-primary/40 bg-primary/10 px-3 py-1 text-sm text-primary-300 transition-colors hover:bg-primary/20"
                >
                  {{ skill }}
                </span>
              </div>
            </div>

            <div class="hero-animate hero-animate-delay-4">
              <h3 class="mb-4 text-sm font-semibold uppercase tracking-widest text-neutral-500">
                Focus Areas
              </h3>
              <div class="grid gap-4 sm:grid-cols-3">
                <div
                  v-for="area in focusAreas"
                  :key="area.title"
                  class="hero-focus-card rounded-xl border border-white/5 bg-white/[0.02] p-4 transition-colors hover:border-primary/25 hover:bg-white/[0.04]"
                >
                  <h4 class="font-medium text-white">{{ area.title }}</h4>
                  <p class="mt-1 text-sm text-neutral-500">{{ area.description }}</p>
                </div>
              </div>
            </div>

            <p class="hero-animate hero-animate-delay-4 text-neutral-500 italic">
              I enjoy turning complex ideas into clean, reliable products at the intersection of
              web, blockchain, and user experience.
            </p>

            <div class="hero-animate hero-animate-delay-4 flex flex-wrap gap-3 pt-2">
              <UButton
                to="#projects"
                size="lg"
                class="rounded-full px-6 font-semibold"
                trailing-icon="i-lucide-arrow-right"
              >
                View my projects
              </UButton>
              <UButton
                to="#contact"
                size="lg"
                color="neutral"
                variant="outline"
                class="rounded-full px-6 font-semibold"
                icon="i-lucide-mail"
              >
                Get in touch
              </UButton>
            </div>
          </div>

          <!-- Profile visual -->
          <div class="hero-animate hero-animate-delay-3 hidden lg:flex lg:flex-col lg:items-center lg:gap-6">
            <div class="relative">
              <div class="hero-avatar-ring absolute -inset-3 rounded-full border border-primary/20" />
              <div class="hero-avatar-ring absolute -inset-6 rounded-full border border-white/5" />
              <div
                class="relative flex size-56 items-center justify-center rounded-full bg-gradient-to-br from-primary/20 via-neutral-900 to-cyan-500/10 ring-1 ring-primary/30"
              >
                <span class="bg-gradient-to-br from-white to-neutral-400 bg-clip-text text-5xl font-bold text-transparent">
                  KE
                </span>
              </div>
            </div>
            <div class="w-52 space-y-2 rounded-2xl border border-white/10 bg-white/[0.03] p-4 text-center backdrop-blur-sm">
              <p class="text-xs uppercase tracking-widest text-neutral-500">Based in</p>
              <p class="font-medium text-white">Lomé, Togo</p>
              <div class="flex items-center justify-center gap-1.5 pt-1">
                <span class="relative flex size-2">
                  <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75" />
                  <span class="relative inline-flex size-2 rounded-full bg-emerald-400" />
                </span>
                <span class="text-xs text-emerald-400">Open to work</span>
              </div>
            </div>
          </div>
        </div>
      </UContainer>
    </section>

    <!-- About -->
    <section id="about" class="py-20 md:py-28 border-t border-white/10">
      <UContainer>
        <RevealOnScroll>
          <div class="grid md:grid-cols-2 gap-12 items-start">
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                About
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight">
                Rigor, curiosity, and attention to detail.
              </h2>
              <p class="mt-5 text-neutral-400 leading-relaxed">
                With a <span class="text-white font-medium">Bachelor's in Computer Science</span>
                (application development specialization), I build web and Web3 applications
                with Vue, Nuxt, and React. I currently contribute to the
                <span class="text-white font-medium">CNC</span> development team.
              </p>
              <p class="mt-4 text-neutral-400 leading-relaxed">
                I'm now looking to expand into
                <span class="text-white font-medium">DevOps</span>, cloud, and cybersecurity
                (SysOps / SecOps).
              </p>
            </div>

            <div class="space-y-4">
              <div class="rounded-2xl bg-white/5 ring-1 ring-white/10 p-6 space-y-3 text-sm text-neutral-300 transition-all duration-500 hover:ring-primary/25">
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-map-pin" class="size-5 text-primary shrink-0" /> Zanguéra, Lomé — Togo
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-languages" class="size-5 text-primary shrink-0" /> French · English (B1)
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-mail" class="size-5 text-primary shrink-0" /> etonameklou19@gmail.com
                </p>
                <p class="flex items-center gap-3">
                  <UIcon name="i-lucide-phone" class="size-5 text-primary shrink-0" /> +228 98 93 85 55
                </p>
              </div>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="t in ['Rigor', 'Curiosity', 'Team spirit', 'Active listening', 'Reliability']"
                  :key="t"
                  class="rounded-full bg-white/5 ring-1 ring-white/10 px-3 py-1 text-xs text-neutral-300 transition-all duration-300 hover:ring-primary/30 hover:text-white"
                >
                  {{ t }}
                </span>
              </div>
            </div>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>

    <!-- Skills -->
    <section id="skills" class="py-20 md:py-28 border-t border-white/10">
      <UContainer>
        <RevealOnScroll>
          <div class="max-w-2xl mb-12">
            <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
              Skills
            </p>
            <h2 class="text-3xl md:text-4xl font-bold tracking-tight">My tech stack.</h2>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="80">
          <h3 class="text-xs font-semibold uppercase tracking-widest text-neutral-500 mb-4">
            Core skills
          </h3>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
            <div
              v-for="skill in coreSkills"
              :key="skill.name"
              class="skill-pill flex items-center gap-3 rounded-xl bg-white/5 ring-1 ring-white/10 px-4 py-3 hover:ring-primary/50 hover:bg-white/[0.07]"
            >
              <UIcon :name="skill.icon" class="size-5 text-primary shrink-0" />
              <span class="text-sm font-medium">{{ skill.name }}</span>
            </div>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="160">
          <h3 class="text-xs font-semibold uppercase tracking-widest text-neutral-500 mt-10 mb-4">
            Additional skills
          </h3>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="skill in secondarySkills"
              :key="skill"
              class="skill-pill rounded-full bg-white/5 ring-1 ring-white/10 px-3.5 py-1.5 text-sm text-neutral-300 hover:ring-primary/30 hover:text-white"
            >
              {{ skill }}
            </span>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>

    <!-- Projects -->
    <section id="projects" class="py-20 md:py-28 border-t border-white/10">
      <UContainer>
        <RevealOnScroll>
          <div class="max-w-2xl mb-12">
            <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">Projects</p>
            <h2 class="text-3xl md:text-4xl font-bold tracking-tight">
              What I'm working on.
            </h2>
            <p class="mt-3 text-neutral-400">
              Hover a card to read more details and visit the project.
            </p>
          </div>
        </RevealOnScroll>

        <RevealOnScroll :delay="80">
          <div class="relative overflow-x-auto scrollbar-hide pb-4 -mx-4 px-4 md:-mx-6 md:px-6">
            <div class="flex gap-8 w-max">
              <ProjectCard
                v-for="project in projects"
                :key="project.title"
                :project="project"
              />
            </div>
          </div>
          <p class="mt-6 text-center text-sm text-neutral-500">
            ← Scroll horizontally to view more projects →
          </p>
        </RevealOnScroll>
      </UContainer>
    </section>

    <!-- Experience -->
    <section id="experience" class="py-20 md:py-28 border-t border-white/10">
      <UContainer>
        <div class="grid lg:grid-cols-2 gap-12">
          <RevealOnScroll>
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                Experience
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight mb-8">My professional journey.</h2>
              <ol class="relative border-l border-white/10 space-y-8 pl-6">
                <li v-for="exp in experiences" :key="exp.role + exp.period" class="relative group">
                  <span class="timeline-dot absolute -left-[31px] top-1.5 size-3 rounded-full bg-primary ring-4 ring-neutral-950 transition-transform duration-300 group-hover:scale-125" />
                  <p class="text-xs uppercase tracking-widest text-neutral-500">{{ exp.period }}</p>
                  <h3 class="mt-1 font-semibold text-lg">{{ exp.role }}</h3>
                  <p class="text-sm text-primary">{{ exp.company }} · {{ exp.place }}</p>
                  <ul class="mt-2 space-y-1 text-sm text-neutral-400 list-disc list-inside">
                    <li v-for="p in exp.points" :key="p">{{ p }}</li>
                  </ul>
                </li>
              </ol>
            </div>
          </RevealOnScroll>

          <RevealOnScroll :delay="120">
            <div>
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                Education
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight mb-8">Degrees &amp; studies.</h2>
              <div class="space-y-4">
                <div
                  v-for="edu in education"
                  :key="edu.title"
                  class="rounded-2xl bg-white/5 ring-1 ring-white/10 p-6 transition-all duration-500 hover:ring-primary/25 hover:-translate-y-0.5"
                >
                  <p class="text-xs uppercase tracking-widest text-neutral-500">{{ edu.period }}</p>
                  <h3 class="mt-1 font-semibold text-lg">{{ edu.title }}</h3>
                  <p class="mt-1 text-sm text-neutral-400">{{ edu.detail }}</p>
                  <p class="mt-2 text-sm text-primary">{{ edu.school }}</p>
                </div>
              </div>

              <div class="mt-6 rounded-2xl bg-white/5 ring-1 ring-white/10 p-6">
                <h3 class="text-xs font-semibold uppercase tracking-widest text-neutral-500 mb-3">
                  Interests
                </h3>
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="i in ['Sports & leisure', 'Travel & tourism', 'Reading', 'Music']"
                    :key="i"
                    class="rounded-full bg-white/5 ring-1 ring-white/10 px-3 py-1 text-xs text-neutral-300"
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
    <section id="contact" class="py-20 md:py-28 border-t border-white/10">
      <UContainer>
        <RevealOnScroll>
          <div class="grid md:grid-cols-5 gap-10 md:gap-16 items-start">
            <div class="md:col-span-2">
              <p class="text-sm font-semibold uppercase tracking-widest text-primary mb-3">
                Connect
              </p>
              <h2 class="text-3xl md:text-4xl font-bold tracking-tight">
                Let's stay in touch.
              </h2>
              <p class="mt-4 text-neutral-400 leading-relaxed">
                Open to opportunities, collaborations, and conversations around web and Web3 development.
              </p>
            </div>

            <div class="md:col-span-3 grid gap-3 sm:grid-cols-2">
              <a
                v-for="link in contactLinks"
                :key="link.label"
                :href="link.href"
                :target="link.href.startsWith('http') ? '_blank' : undefined"
                :rel="link.href.startsWith('http') ? 'noopener noreferrer' : undefined"
                class="group flex items-start gap-4 rounded-2xl bg-white/[0.03] ring-1 ring-white/10 p-5 transition-all duration-500 hover:-translate-y-1 hover:ring-primary/35 hover:bg-white/[0.06]"
                :class="link.label === 'Email' ? 'sm:col-span-2' : ''"
              >
                <div
                  class="flex size-11 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary ring-1 ring-primary/20 transition-transform duration-300 group-hover:scale-110"
                >
                  <UIcon :name="link.icon" class="size-5" />
                </div>
                <div class="min-w-0">
                  <p class="text-xs font-semibold uppercase tracking-widest text-neutral-500">
                    {{ link.label }}
                  </p>
                  <p class="mt-1 text-sm font-medium text-white truncate group-hover:text-primary transition-colors duration-300">
                    {{ link.value }}
                  </p>
                </div>
                <UIcon
                  name="i-lucide-arrow-up-right"
                  class="ml-auto size-4 shrink-0 text-neutral-600 transition-all duration-300 group-hover:text-primary group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                />
              </a>
            </div>
          </div>
        </RevealOnScroll>
      </UContainer>
    </section>
  </div>
</template>
