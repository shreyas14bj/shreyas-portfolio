# Shreyas B J — Cinematic Portfolio & Observational Sketch Studio 🎬⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg)](LICENSE)
[![Deployment: Netlify](https://img.shields.io/badge/Deploy-Netlify%20Ready-00C7B7?logo=netlify&logoColor=white)](https://app.netlify.com)
[![Storage: IndexedDB](https://img.shields.io/badge/Storage-IndexedDB%20%2B%20Canvas-6366F1)](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
[![Security: Owner Protected](https://img.shields.io/badge/Security-Admin%20Authorized-emerald)](https://github.com)
[![Responsive: Mobile & Desktop](https://img.shields.io/badge/Design-Cinematic%20Responsive-orange)](https://tailwindcss.com)

A luxury, editorial-grade cinematic portfolio and observational drawing studio crafted for **Shreyas B J** — AI/ML Engineer at **Tata Consultancy Services (TCS)**, creative technologist, and fine-art sketch artist.

---

## 🌟 Key Architecture & Features

### 1. 🎨 Observational Sketch Studio (100+ Artworks Support)
- **5-Row Balanced Cinematic Slider**: Artworks dynamically distribute across up to 5 synchronized horizontal rows using round-robin column balancing.
- **Client-Side Canvas Image Compression**: Uploaded high-resolution photos (often 5MB–12MB from smartphone cameras) are automatically downsampled to 1600px max dimension and compressed to high-grade 85% JPEG on an offscreen `<canvas>`. Reduces memory consumption by 98% while maintaining razor-sharp graphite and ink details.
- **High-Capacity IndexedDB Engine (`ShreyasArtStudioDB`)**: Bypasses traditional 5MB browser `localStorage` restrictions to provide hundreds of megabytes of persistent storage for single or batch uploads.
- **Drag & Drop Multi-Image Dropzone**: Select multiple drawings simultaneously with live progress feedback, thumbnail management, and one-click removal before publishing.
- **Full View Lightbox Inspector**: High-resolution modal with blurred ambient backdrops, aspect-ratio preservation, metadata breakdown, and double-tap heart animations.

### 2. 🔐 Owner Administrative Security Gate
- **Centralized Authorization**: All content modification capabilities (posting drawings, managing projects, editing bio, adding career entries, updating certifications, and deleting content) are protected behind a master administrative passcode.
- **No Unauthorized Tampering**: Public visitors can browse, view, like, and explore all media, but only the verified owner can initiate edits.
- **Locked on Refresh**: Every page refresh automatically begins at the very start of the prologue in locked mode to prevent session lingering.

### 3. 📂 Dynamic Technical Projects Hub
- **Automated Visual Generation**: Automatically renders aesthetic system architecture diagrams and procedural tech visuals based on project domain tags.
- **Rich Metric Badges**: Live repository links, tech-stack pills, and full project descriptions.
- **Full In-Browser CRUD**: Add, edit, or remove technical projects with instant state updates.

### 4. 📜 Verified Accreditations & Career Chronicles
- **Interactive Certifications**: Verified credentials covering Databricks, Generative AI, Computer Vision, and Cloud Engineering with direct PDF/Image inspector modal.
- **Experience Timeline**: Career milestones spanning TCS (AI/ML) and Foxconn Industrial Internet (Hardware Failure Analysis).

### 5. 🌓 Dual Cinematic Theme Engine
- **Cinematic Noir (Default)**: Deep obsidian void (`#060709`), rich carbon cards (`#0B0D12`), warm champagne gold (`#E5A93C`), and platinum typography.
- **Editorial Light Mode**: High-contrast, clean gallery aesthetic with smooth CSS variable transitions.

---

## 📁 Repository Structure

```text
shreyas-cinematic-portfolio/
├── assets/
│   ├── drawings/
│   │   ├── ganesha.png               # Hand-drawn Ganesha master sketch
│   │   ├── drawing-portrait.svg      # Forensic anatomical study
│   │   ├── drawing-architecture.svg  # Monolithic structural grid
│   │   ├── drawing-cybernetic.svg    # Machine optical sensor
│   │   └── drawing-landscape.svg     # Western Ghats terrain study
│   └── profile-avatar.svg            # Default profile avatar
├── dist/                             # Clean production folder for 1-click deployment
│   ├── assets/
│   └── index.html
├── build_ultimate_portfolio.py       # Python automated build generator
├── index.html                        # Production cinematic single-page application
├── package.json                      # Project metadata & local dev scripts
└── README.md                         # Documentation
```

---

## 🚀 Getting Started

### Option A: Direct Browser Preview (Zero Installation)
Simply open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, or Safari):
```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

### Option B: Local Development Server
To test under a local HTTP origin:

**Using Python:**
```bash
python -m http.server 3000
```
Then navigate to: `http://localhost:3000`

**Using Node / Vite:**
```bash
npm install
npm run dev
```

---

## 🌐 Free Production Deployment (Netlify)

This project is 100% static (HTML5, Tailwind CDN, Vanilla JS, IndexedDB) with zero server dependencies, making it optimal for free global edge deployment.

### Deploy via Netlify Drop (Under 1 Minute)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `dist/` folder directly onto the page.
3. Your portfolio goes live instantly with free automated SSL (`https://your-site-name.netlify.app`).

### Deploy via GitHub (Continuous Deployment)
1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "feat: cinematic portfolio release"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
2. Log into [Netlify](https://www.netlify.com/) or [Vercel](https://vercel.com/).
3. Select **"Import from Git"** &rarr; Choose your repository.
4. Set publish directory to `.` or `dist` and deploy.

---

## 🛡️ Security & Privacy Notice
All admin actions (editing biographical details, uploading new drawings, modifying projects, and deleting content) require owner authorization via the administrative prompt. Unauthorized users can view and appreciate the work, but cannot alter the published portfolio.

---

## 📄 License
Released under the [MIT License](LICENSE). Built with cinematic precision for **Shreyas B J**.
