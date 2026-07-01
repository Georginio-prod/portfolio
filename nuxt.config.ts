// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-01',
  devtools: { enabled: true },

  modules: ['@nuxt/ui', '@nuxtjs/i18n'],

  css: ['~/assets/css/main.css'],

  i18n: {
    strategy: 'no_prefix',
    defaultLocale: 'en',
    lazy: false,
    langDir: 'locales',
    // English is always the first-visit default (browser-language auto-detection
    // is off on purpose). The visitor's manual choice is restored from a cookie
    // by the `restore-locale` plugin, before render, on both server and client.
    detectBrowserLanguage: false,
    locales: [
      { code: 'en', language: 'en-US', name: 'English', file: 'en.json' },
      { code: 'fr', language: 'fr-FR', name: 'Français', file: 'fr.json' }
    ]
  },

  colorMode: {
    preference: 'dark',
    fallback: 'dark'
  },

  ui: {
    theme: {
      colors: ['primary', 'secondary', 'success', 'info', 'warning', 'error', 'neutral']
    }
  },

  app: {
    head: {
      title: 'Komla Etonam Georges EKLOU — Portfolio',
      htmlAttrs: { lang: 'en' },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'Portfolio of Komla Etonam Georges EKLOU — Full Stack & Web3 developer. Projects, skills, and experience.'
        }
      ],
      link: [{ rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }]
    }
  }
})
