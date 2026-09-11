# Portfolio — Komla Etonam Georges EKLOU

![Nuxt](https://img.shields.io/badge/Nuxt-4-00DC82?logo=nuxt.js&logoColor=white)
![Nuxt UI](https://img.shields.io/badge/Nuxt_UI-4-00DC82?logo=nuxt.js&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?logo=tailwindcss&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-FR%20%2F%20EN-blue)

🔗 **Site en ligne** : <https://georginio.w3frame.com/> (miroir Vercel : <https://portfolio-georginios-projects.vercel.app>)
📦 **Code source** : <https://github.com/Georginio-prod/portfolio>

---

## 📌 Présentation

Mon portfolio personnel de développeur Full Stack Web & Web3. Il présente mon parcours,
mes compétences, mes projets phares (professionnels et d'apprentissage), et permet de
télécharger mon CV en français ou en anglais.

Le site est **bilingue (anglais par défaut, français)**, en **mode sombre par défaut**,
et entièrement **rendu côté serveur (SSR)** pour un bon référencement.

## ✨ Fonctionnalités

- **Page d'accueil** en sections : héros + compétences, domaines d'expertise, carrousel de projets filtrable (*Featured / All / Learning*), à propos, groupes de compétences, contact.
- **Pages de détail par projet** (`/projects/:id`) : description longue, contexte, stack complète, galerie de captures (desktop + mobile), lien vers la démo.
- **Bilinguisme** avec `@nuxtjs/i18n` : sélecteur de langue, choix mémorisé dans un cookie et **restauré avant le rendu** (aucun « flash » ni erreur d'hydratation).
- **Thème clair / sombre** (Nuxt UI + `colorMode`).
- **Téléchargement du CV** (PDF FR / EN) via un menu déroulant.
- **Animations d'apparition au scroll** (`RevealOnScroll`).
- **SEO** : balises meta / Open Graph, canonical, `lang` dynamique.

## 🛠️ Stack technique

| Couche | Technologie | Rôle |
|---|---|---|
| Framework | **Nuxt 4** (Vue 3, SSR) | Structure, routing basé sur les fichiers, rendu serveur |
| UI | **Nuxt UI 4** (Tailwind CSS v4 + Reka UI) | Composants, thème, mode sombre |
| i18n | **@nuxtjs/i18n 10** | Traductions FR / EN, stratégie `no_prefix` |
| Langage | **TypeScript** | Typage des composables et des données |
| Scripts | **Python + ReportLab** | Génération des PDF de CV bilingues |
| Hébergement | **Vercel** (+ domaine `georginio.w3frame.com`) | Déploiement continu |

## 📁 Structure du projet

```
portfolio/
├── nuxt.config.ts               # Modules, i18n, colorMode, meta SEO
├── app/
│   ├── app.vue                  # Point d'entrée
│   ├── app.config.ts            # Thème Nuxt UI (couleurs)
│   ├── assets/css/main.css      # Import Tailwind + Nuxt UI
│   ├── layouts/default.vue      # Header + footer communs
│   ├── pages/
│   │   ├── index.vue            # Page d'accueil (toutes les sections)
│   │   └── projects/[id].vue    # Page de détail d'un projet
│   ├── components/
│   │   ├── PortfolioNav.vue     # Navigation
│   │   ├── ProjectCard.vue      # Carte projet du carrousel
│   │   ├── LanguageSwitcher.vue # Bascule FR / EN
│   │   ├── ColorModeToggle.vue  # Bascule clair / sombre
│   │   ├── CvDownloadMenu.vue   # Menu de téléchargement du CV
│   │   └── RevealOnScroll.vue   # Animation d'apparition
│   ├── composables/useProjects.ts  # ⭐ Source unique de la liste des projets
│   └── plugins/restore-locale.ts   # Restaure la langue depuis le cookie (SSR + client)
├── i18n/locales/{en,fr}.json    # Tous les textes traduits
├── public/
│   ├── cv/                      # CV PDF (FR / EN)
│   ├── projects/                # Captures d'écran des projets
│   └── profile.jpg
└── scripts/generate_cv_assets.py  # Génère les CV PDF
```

### Comment fonctionne la liste des projets ?

`app/composables/useProjects.ts` est la **source unique de vérité** :
- les données « neutres » (URL, icône, tags, stack, galerie) sont déclarées une seule fois dans `projectMeta` ;
- les textes (titre, description, statut, contexte) viennent des fichiers de traduction `i18n/locales/*.json` et sont fusionnés par `id`.

Le carrousel de l'accueil et les pages `/projects/:id` lisent tous les deux ce composable :
**ajouter un projet = 1 entrée dans `projectMeta` + les textes dans `en.json` et `fr.json`.**

## 🚀 Installation & lancement

Prérequis : **Node.js ≥ 20** et **pnpm** (ou npm).

```bash
git clone https://github.com/Georginio-prod/portfolio.git
cd portfolio
pnpm install          # ou npm install
pnpm dev              # http://localhost:3000
```

| Commande | Description |
|---|---|
| `pnpm dev` | Serveur de développement avec rechargement à chaud |
| `pnpm build` | Build de production (SSR) |
| `pnpm preview` | Prévisualise le build |
| `pnpm generate` | Génération statique (SSG) |
| `pnpm typecheck` | Vérification TypeScript |

### Régénérer les CV (optionnel)

```bash
pip install reportlab
python scripts/generate_cv_assets.py
```

## 🎨 Personnalisation

| Quoi | Où |
|---|---|
| Projets (liens, stack, captures) | `app/composables/useProjects.ts` |
| Textes (FR / EN) | `i18n/locales/fr.json`, `i18n/locales/en.json` |
| Couleur principale / thème | `app/app.config.ts` |
| Méta SEO, titre, Open Graph | `nuxt.config.ts` |
| Photo de profil | `public/profile.jpg` |

## 🌐 Déploiement

Le site est déployé sur **Vercel** : chaque `push` sur `main` déclenche un build Nuxt.
Aucune variable d'environnement n'est nécessaire.

---

## 👤 Auteur

**Komla Etonam Georges EKLOU** (Georginio) — Développeur Full Stack Web & Web3

[![GitHub](https://img.shields.io/badge/GitHub-Georginio--prod-181717?logo=github)](https://github.com/Georginio-prod)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profil-0A66C2?logo=linkedin)](https://www.linkedin.com/in/komla-etonam-georges-eklou-68518b23b)
[![Portfolio](https://img.shields.io/badge/Portfolio-georginio.w3frame.com-6C63FF)](https://georginio.w3frame.com/)

> 📚 Tous mes projets sont listés et documentés sur mon [profil GitHub](https://github.com/Georginio-prod).
