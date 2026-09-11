// Single source of truth for the project list.
//
// The landing carousel and the /projects/:id detail pages both read from here,
// so a project only ever has to be declared once. Links / icons / tags / stack
// are language-agnostic (proper names don't translate); the prose (title,
// description, status, note, background) comes from the locale files and is
// merged in by id.

export interface ProjectMeta {
  url: string
  icon: string
  tags: string[]
  online: boolean
  wip?: boolean
  /** Overrides the generated screenshot when there is no live site to shoot. */
  cover?: string
  /** Full tech stack, shown on the detail page under the description. */
  stack: string[]
  /** Explicit "Static previews" images; falls back to generated screenshots. */
  gallery?: string[]
}

export interface Project extends ProjectMeta {
  id: string
  title: string
  description: string
  status: string
  note: string
  background: string
}

const projectMeta: Record<string, ProjectMeta> = {
  cnc: {
    url: 'https://app.cncportal.io/login',
    icon: 'i-lucide-building-2',
    tags: ['Vue', 'Team', 'Pro'],
    online: true,
    wip: true,
    cover: '/projects/cnc/cover.png',
    stack: ['Vue.js', 'TypeScript', 'Solidity', 'Web3', 'Tailwind CSS', 'Node.js', 'Git'],
    gallery: [
      '/projects/cnc/preview-desktop.png',
      '/projects/cnc/preview-mobile.png'
    ]
  },
  nova: {
    url: 'https://novagraphikvisu.com/',
    icon: 'i-lucide-palette',
    tags: ['Nuxt', 'Landing', 'Pro'],
    online: true,
    cover: '/projects/nova/cover.png',
    stack: ['Nuxt.js', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'SEO'],
    gallery: [
      '/projects/nova/preview-desktop.png',
      '/projects/nova/preview-mobile.png'
    ]
  },
  designer: {
    url: 'https://my-portfolio-production-e928.up.railway.app/',
    icon: 'i-lucide-pen-tool',
    tags: ['Portfolio', 'Design', 'Pro'],
    online: true,
    cover: '/projects/designer/cover.png',
    stack: ['Nuxt.js', 'Vue.js', 'Tailwind CSS', 'Railway'],
    gallery: [
      '/projects/designer/preview-desktop.png',
      '/projects/designer/preview-mobile.png'
    ]
  },
  orga: {
    url: 'https://www.orga-africa.com/',
    icon: 'i-lucide-store',
    tags: ['Nuxt', 'Landing', 'Pro'],
    online: true,
    cover: '/projects/orga/cover.png',
    stack: ['Nuxt.js', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'Node.js'],
    gallery: [
      '/projects/orga/preview-desktop.png',
      '/projects/orga/preview-mobile.png'
    ]
  },
  pulse: {
    url: 'https://pulse-score-two.vercel.app/',
    icon: 'i-lucide-activity',
    tags: ['Vue', 'App', 'WIP'],
    online: true,
    wip: true,
    cover: '/projects/pulse-cover.png',
    stack: ['Vue.js', 'TypeScript', 'Tailwind CSS', 'Vercel'],
    gallery: [
      '/projects/pulse-desktop.png',
      '/projects/pulse-mobile.png'
    ]
  },
  // Deployed on Railway. The local cover stays as the card image; the detail
  // page gallery falls through to generated screenshots of the live site.
  worktogo: {
    url: 'https://alodowoto-production.up.railway.app/',
    icon: 'i-lucide-handshake',
    tags: ['Nuxt', 'TypeScript', 'Marketplace'],
    online: true,
    wip: true,
    cover: '/projects/worktogo.png',
    stack: ['Nuxt.js', 'TypeScript', 'Tailwind CSS', 'Node.js', 'Mobile Money', 'Escrow']
  },
  microread: {
    url: 'https://micro-read-app.vercel.app/',
    icon: 'i-lucide-book-open',
    tags: ['React', 'Vite', 'App'],
    online: true,
    wip: true,
    cover: '/projects/microread/cover.png',
    stack: ['React', 'Vite', 'TypeScript', 'Tailwind CSS', 'WhatsApp API', 'Project Gutenberg'],
    gallery: [
      '/projects/microread/preview-desktop.png',
      '/projects/microread/preview-mobile.png'
    ]
  },
  meet: {
    url: 'https://meet-landing-page-kohl.vercel.app/',
    icon: 'i-lucide-video',
    tags: ['Vue', 'Responsive', 'Landing'],
    online: true,
    cover: '/projects/meet-cover.png',
    stack: ['Vue.js', 'HTML', 'CSS', 'Responsive design'],
    gallery: [
      '/projects/meet-desktop.png',
      '/projects/meet-mobile.png'
    ]
  },
  pomodoro: {
    url: 'https://promodoro-app-iota.vercel.app/',
    icon: 'i-lucide-timer',
    tags: ['Vue', 'App', 'UI'],
    online: true,
    cover: '/projects/pomodoro/cover.png',
    stack: ['Vue.js', 'JavaScript', 'CSS', 'LocalStorage'],
    gallery: [
      '/projects/pomodoro/preview-mobile.png'
    ]
  },
  audiophile: {
    url: 'https://audiophile-ecommerce-psi-ecru.vercel.app/',
    icon: 'i-lucide-headphones',
    tags: ['E-commerce', 'Front-end'],
    online: true,
    cover: '/projects/audiophile/cover.png',
    stack: ['Vue.js', 'JavaScript', 'CSS', 'E-commerce'],
    gallery: [
      '/projects/audiophile/preview-desktop.png'
    ]
  },
  fem: {
    url: 'https://www.frontendmentor.io/profile/Georginio-prod?tab=solutions',
    icon: 'i-lucide-code-2',
    tags: ['Challenges', 'HTML/CSS'],
    online: true,
    cover: '/projects/fem-cover.png',
    stack: ['HTML', 'CSS', 'JavaScript', 'Vue.js', 'React'],
    gallery: [
      '/projects/fem-desktop.png',
      '/projects/fem-mobile.png'
    ]
  }
}

const fallbackMeta: ProjectMeta = { url: '', icon: 'i-lucide-folder', tags: [], online: false, stack: [] }

/**
 * Live homepage thumbnail through microlink's image embed. Used wherever a
 * project has no local asset — a plain <img> URL, so the browser lazy-loads it
 * and nothing blocks rendering.
 */
export function screenshotUrl(url: string, width = 1280, height = 800) {
  return `https://api.microlink.io/?url=${encodeURIComponent(url)}&screenshot=true&embed=screenshot.url&meta=false&viewport.width=${width}&viewport.height=${height}`
}

export function useProjects() {
  const { tm, rt } = useI18n()

  const projects = computed<Project[]>(() =>
    (tm('projects.items') as any[]).map((item) => {
      const id = rt(item.id)
      return {
        id,
        title: rt(item.title),
        description: rt(item.description),
        status: rt(item.status),
        note: item.note ? rt(item.note) : '',
        background: item.background ? rt(item.background) : '',
        ...(projectMeta[id] ?? fallbackMeta)
      }
    })
  )

  return { projects }
}
