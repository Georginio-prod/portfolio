# Portfolio — Georginio

Portfolio personnel construit avec [Nuxt](https://nuxt.com), [Nuxt UI](https://ui.nuxt.com) et [Tailwind CSS](https://tailwindcss.com).

## Stack

- **Nuxt 4** — framework Vue full-stack
- **Nuxt UI 4** — bibliothèque de composants (basée sur Tailwind CSS v4 + Reka UI)
- **Tailwind CSS v4** — styles utilitaires
- **TypeScript**

## Prérequis

- Node.js >= 20
- npm

## Installation

```bash
npm install
```

## Développement

Lance le serveur de développement sur `http://localhost:3000` :

```bash
npm run dev
```

## Production

Génère la version de production :

```bash
npm run build
```

Prévisualise le build localement :

```bash
npm run preview
```

## Génération statique

Pour un déploiement statique (ex. GitHub Pages, Netlify, Vercel) :

```bash
npm run generate
```

## Structure

```
.
├── nuxt.config.ts           # Configuration Nuxt
├── public/                  # Fichiers statiques (favicon...)
└── app/
    ├── app.vue              # Point d'entrée
    ├── app.config.ts        # Thème Nuxt UI (couleurs)
    ├── assets/css/main.css  # Import Tailwind + Nuxt UI
    ├── layouts/default.vue  # Header / footer
    └── pages/index.vue      # Sections du portfolio
```

## Personnalisation

- Contenu (projets, compétences, liens) : `app/pages/index.vue`
- Couleur principale : `app/app.config.ts`
- Métadonnées SEO : `nuxt.config.ts`
