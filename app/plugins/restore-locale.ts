/**
 * Restores the visitor's previously chosen language from a cookie.
 *
 * Runs universally (server + client) BEFORE the app renders, so the SSR markup
 * and the client's first render use the same locale — no flash, no hydration
 * mismatch. On a first visit (no cookie) the locale stays at the configured
 * default (English); browser-language auto-detection is intentionally off.
 */
export default defineNuxtPlugin(async (nuxtApp) => {
  const i18n = nuxtApp.$i18n as {
    locale: { value: string }
    setLocale: (code: string) => Promise<void>
  } | undefined

  if (!i18n) return

  const cookie = useCookie<string>('locale', {
    maxAge: 60 * 60 * 24 * 365,
    sameSite: 'lax',
    path: '/'
  })

  const wanted = cookie.value
  if (wanted && ['en', 'fr'].includes(wanted) && i18n.locale.value !== wanted) {
    await i18n.setLocale(wanted)
  }
})
