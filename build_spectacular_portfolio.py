# build_portfolio.py - Generator for Shreyas B J Cinematic Masterpiece Portfolio
import os

html_content = '''<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shreyas B J — AI/ML Engineer & Creative Technologist</title>
  <meta name="description" content="Cinematic portfolio, interactive engineering lab, and observational drawing studio of Shreyas B J — AI/ML Engineer at TCS, Databricks & Cloud Certified Developer.">

  <!-- Premium Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            noir: {
              950: 'var(--color-bg-deep)',
              900: 'var(--color-bg-card)',
              850: 'var(--color-bg-card-alt)',
              800: 'var(--color-bg-surface)',
              700: 'var(--color-border)',
              600: '#323B4E',
            },
            gold: {
              300: 'var(--color-accent-light)',
              400: 'var(--color-accent-mid)',
              500: 'var(--color-accent-primary)',
              600: 'var(--color-accent-dark)',
            },
            cyan: {
              400: '#38BDF8',
              500: '#0EA5E9',
            },
            heart: '#FF2A6D',
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            display: ['Space Grotesk', 'sans-serif'],
            cinematic: ['Syne', 'Space Grotesk', 'sans-serif'],
            title: ['Cinzel', 'serif'],
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons & Three.js for 3D Cosmic Constellation -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    :root {
      /* Theme 1: Obsidian Luxury Noir (Default) */
      --color-bg-deep: #050608;
      --color-bg-card: #0B0E14;
      --color-bg-card-alt: #11151F;
      --color-bg-surface: #181E2C;
      --color-border: rgba(255, 255, 255, 0.12);
      --color-accent-primary: #E5A93C;
      --color-accent-mid: #F5C563;
      --color-accent-light: #FDE08B;
      --color-accent-dark: #C88A22;
      --color-glow: rgba(229, 169, 60, 0.25);
      --theme-font-title: 'Cinzel', serif;
    }

    /* Theme 2: Cosmic Aurora Mode */
    [data-theme="aurora"] {
      --color-bg-deep: #060913;
      --color-bg-card: #0C1222;
      --color-bg-card-alt: #121B32;
      --color-bg-surface: #1A2645;
      --color-border: rgba(0, 240, 255, 0.2);
      --color-accent-primary: #00F0FF;
      --color-accent-mid: #38BDF8;
      --color-accent-light: #A5F3FC;
      --color-accent-dark: #0284C7;
      --color-glow: rgba(0, 240, 255, 0.28);
    }

    /* Theme 3: Cyberpunk Crimson Noir */
    [data-theme="cyber"] {
      --color-bg-deep: #08070C;
      --color-bg-card: #120F1A;
      --color-bg-card-alt: #1A1526;
      --color-bg-surface: #261F38;
      --color-border: rgba(255, 42, 109, 0.22);
      --color-accent-primary: #FF2A6D;
      --color-accent-mid: #FF5E8E;
      --color-accent-light: #FFA6C2;
      --color-accent-dark: #C70039;
      --color-glow: rgba(255, 42, 109, 0.28);
    }

    /* Ultra-subtle film grain */
    .film-grain {
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.02'/%3E%3C/svg%3E");
    }

    /* Volumetric ambient caustics */
    @keyframes sunbeamShift {
      0% { transform: translate(-8%, -8%) rotate(0deg) scale(1); opacity: 0.15; }
      50% { transform: translate(6%, 8%) rotate(6deg) scale(1.2); opacity: 0.28; }
      100% { transform: translate(-8%, -8%) rotate(0deg) scale(1); opacity: 0.15; }
    }
    .sunbeam-ambient {
      background: radial-gradient(circle at 35% 25%, var(--color-glow) 0%, transparent 65%);
      animation: sunbeamShift 20s ease-in-out infinite;
      filter: blur(80px);
    }
    .sunbeam-ambient-secondary {
      background: radial-gradient(circle at 75% 75%, rgba(14, 165, 233, 0.18) 0%, transparent 60%);
      animation: sunbeamShift 26s ease-in-out infinite reverse;
      filter: blur(100px);
    }

    /* Custom smooth scrollbar */
    ::-webkit-scrollbar { width: 7px; }
    ::-webkit-scrollbar-track { background: var(--color-bg-deep); }
    ::-webkit-scrollbar-thumb { background: #232936; border-radius: 4px; border: 1px solid rgba(255, 255, 255, 0.05); }
    ::-webkit-scrollbar-thumb:hover { background: var(--color-accent-primary); }

    /* Optical Depth-of-Field Scroll Reveals */
    .reveal-item {
      opacity: 0;
      transform: translateY(40px) scale(0.98);
      filter: blur(10px);
      transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.9s cubic-bezier(0.16, 1, 0.3, 1),
                  filter 0.9s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform, filter;
    }
    .reveal-item.is-visible {
      opacity: 1;
      transform: translateY(0) scale(1);
      filter: blur(0px);
    }

    /* 3D Specular Tilt Card */
    .real-tilt {
      transform-style: preserve-3d;
      transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.4, 1), box-shadow 0.25s ease;
      position: relative;
    }
    .real-tilt::after {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: inherit;
      background: radial-gradient(circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255, 255, 255, 0.1) 0%, transparent 65%);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .real-tilt:hover::after { opacity: 1; }

    /* Magnetic Button */
    .magnetic-btn {
      transition: transform 0.22s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.25s ease;
      will-change: transform;
    }

    /* Double-tap heart burst */
    @keyframes heartBurstPop {
      0% { transform: translate(-50%, -50%) scale(0) rotate(-20deg); opacity: 0; }
      40% { transform: translate(-50%, -50%) scale(1.4) rotate(0deg); opacity: 1; }
      70% { transform: translate(-50%, -50%) scale(1.2) rotate(6deg); opacity: 0.95; }
      100% { transform: translate(-50%, -50%) scale(0.9) translateY(-25px) rotate(-6deg); opacity: 0; }
    }
    .pop-heart-anim {
      animation: heartBurstPop 0.85s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    /* Kinematic falling/tumbling heart particle */
    .phys-heart-particle {
      position: fixed;
      pointer-events: none;
      z-index: 99999;
      font-size: 18px;
      user-select: none;
      will-change: transform, opacity;
      filter: drop-shadow(0 2px 8px rgba(0,0,0,0.4));
    }

    /* Holographic card effect */
    .holo-card {
      background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.01) 100%);
      border: 1px solid var(--color-border);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      box-shadow: 0 20px 40px -15px rgba(0,0,0,0.7), inset 0 1px 0 rgba(255,255,255,0.1);
    }
    .holo-card:hover {
      border-color: var(--color-accent-primary);
      box-shadow: 0 25px 50px -12px var(--color-glow), inset 0 1px 0 rgba(255,255,255,0.2);
    }

    /* Fluid Cursor Follower */
    #cursorHalo {
      pointer-events: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: 1.5px solid var(--color-accent-mid);
      transform: translate(-50%, -50%);
      transition: width 0.25s ease, height 0.25s ease, background 0.25s ease, border-color 0.25s ease;
      z-index: 99999;
      box-shadow: 0 0 16px var(--color-glow);
    }
    #cursorDot {
      pointer-events: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--color-accent-light);
      transform: translate(-50%, -50%);
      z-index: 100000;
    }
    body:hover #cursorHalo.cursor-hover {
      width: 60px;
      height: 60px;
      background: rgba(229, 169, 60, 0.12);
      border-color: #fff;
    }

    /* Glow Text */
    .glow-gold-text {
      text-shadow: 0 0 25px var(--color-glow);
    }

    /* Interactive image slider */
    .slider-handle {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 3px;
      background: var(--color-accent-primary);
      cursor: ew-resize;
      box-shadow: 0 0 15px var(--color-accent-primary);
    }
    .slider-handle-button {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--color-bg-card);
      border: 2px solid var(--color-accent-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-accent-light);
      box-shadow: 0 0 20px var(--color-glow);
    }

    /* Hollywood Credits Roll */
    @keyframes creditsScroll {
      0% { transform: translateY(100%); }
      100% { transform: translateY(-110%); }
    }
    .animate-credits {
      animation: creditsScroll 22s linear infinite;
    }
  </style>
</head>
<body class="bg-noir-950 text-gray-200 antialiased overflow-x-hidden selection:bg-gold-500/30 selection:text-white font-sans relative" data-theme="obsidian">

  <!-- Custom Cursor Follower -->
  <div id="cursorHalo" class="hidden md:block"></div>
  <div id="cursorDot" class="hidden md:block"></div>

  <!-- Ambient Light Fields -->
  <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
    <div class="sunbeam-ambient absolute -top-40 -left-40 w-[650px] h-[650px] rounded-full"></div>
    <div class="sunbeam-ambient-secondary absolute -bottom-40 -right-40 w-[750px] h-[750px] rounded-full"></div>
    <div class="film-grain absolute inset-0 opacity-40"></div>
  </div>

  <!-- Three.js 3D Interactive Constellation Canvas -->
  <canvas id="threeCanvas" class="fixed inset-0 pointer-events-none z-[1] w-full h-full"></canvas>

  <!-- 2D Particle Atmosphere Canvas Fallback & Dust Spores -->
  <canvas id="neuralCanvas" class="fixed inset-0 pointer-events-none z-[2] w-full h-full"></canvas>

  <!-- ========================================================================= -->
  <!-- TOP CINEMATIC DIRECTOR STATUS BAR -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 w-full z-50 backdrop-blur-xl bg-noir-950/80 border-b border-white/10 px-6 py-3.5 flex items-center justify-between transition-all duration-300">
    <div class="flex items-center space-x-4">
      <a href="#hero" class="flex items-center space-x-2 group">
        <span class="w-2.5 h-2.5 rounded-full bg-gold-400 animate-pulse shadow-[0_0_10px_#E5A93C]"></span>
        <span class="font-display font-bold text-white tracking-widest text-sm group-hover:text-gold-400 transition-colors uppercase">SHREYAS B J</span>
        <span class="text-[11px] font-mono text-gray-500 border-l border-white/15 pl-2 hidden sm:inline">DIR. NOIR // PROD. 2026</span>
      </a>
    </div>

    <!-- Live Status & Telemetry -->
    <div class="hidden lg:flex items-center space-x-6 text-xs font-mono text-gray-400">
      <div class="flex items-center space-x-2">
        <span class="text-gold-400">&bull;</span>
        <span>ROLE: AI/ML ENGINEER @ TCS</span>
      </div>
      <div class="flex items-center space-x-2">
        <span class="text-cyan-400">&bull;</span>
        <span id="liveClock">BANGALORE IST 00:00:00</span>
      </div>
      <!-- Subtle Visualizer Wave (No Audio) -->
      <div class="flex items-end space-x-0.5 h-3.5" title="Visual telemetry wave">
        <span class="w-0.5 h-2 bg-gold-400 animate-[bounce_1s_infinite]"></span>
        <span class="w-0.5 h-3.5 bg-gold-400 animate-[bounce_1.3s_infinite]"></span>
        <span class="w-0.5 h-1.5 bg-gold-400 animate-[bounce_0.8s_infinite]"></span>
        <span class="w-0.5 h-3 bg-gold-400 animate-[bounce_1.1s_infinite]"></span>
      </div>
    </div>

    <!-- Quick Navigation & Contact Button -->
    <div class="flex items-center space-x-3">
      <button onclick="toggleThemeModal()" class="magnetic-btn p-2 rounded-xl bg-white/5 border border-white/10 hover:border-gold-400/50 text-gray-300 hover:text-white transition-all text-xs font-mono flex items-center space-x-1.5">
        <i data-lucide="palette" class="w-3.5 h-3.5 text-gold-400"></i>
        <span class="hidden sm:inline">MOOD</span>
      </button>

      <a href="#finale" class="magnetic-btn px-4 py-1.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(229,169,60,0.3)] hover:scale-105">
        CONTACT
      </a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- FLOATING CINEMATIC DIRECTOR'S DOCK (BOTTOM DOCK) -->
  <!-- ========================================================================= -->
  <nav class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 px-4 py-2.5 rounded-full bg-noir-900/80 backdrop-blur-2xl border border-white/15 shadow-[0_15px_35px_rgba(0,0,0,0.8)] flex items-center space-x-2 sm:space-x-3 transition-all hover:scale-[1.02]">
    <a href="#hero" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="Genesis (Hero)">
      <i data-lucide="compass" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">GENESIS</span>
    </a>
    <a href="#architect" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="The Architect (Bio)">
      <i data-lucide="user" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">ARCHITECT</span>
    </a>
    <a href="#odyssey" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="The Odyssey (Experience)">
      <i data-lucide="briefcase" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">ODYSSEY</span>
    </a>
    <a href="#arsenal" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="The Arsenal (Skills & Certs)">
      <i data-lucide="cpu" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">ARSENAL</span>
    </a>
    <a href="#inventions" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="Flagship Inventions (Lab)">
      <i data-lucide="layers" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">INVENTIONS</span>
    </a>
    <a href="#art-studio" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="Art Studio (Instagram Feed)">
      <i data-lucide="camera" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">SKETCHES</span>
    </a>
    <a href="#mind" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="Behind the Mind (Neural Lab)">
      <i data-lucide="brain" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">NEURAL LAB</span>
    </a>
    <a href="#finale" class="magnetic-btn p-2.5 rounded-full hover:bg-white/10 text-gray-400 hover:text-gold-400 transition-colors relative group" title="Transmission Finale">
      <i data-lucide="send" class="w-4 h-4"></i>
      <span class="absolute -top-9 left-1/2 -translate-x-1/2 px-2 py-0.5 rounded bg-noir-950 border border-white/15 text-[10px] font-mono text-gold-400 whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">TRANSMIT</span>
    </a>

    <div class="h-5 w-[1px] bg-white/20 my-auto"></div>

    <!-- Theme Switcher Quick Toggle -->
    <button onclick="cycleNextTheme()" class="magnetic-btn p-2 rounded-full hover:bg-white/10 text-gold-400 transition-transform hover:rotate-45" title="Cycle Theme Mood">
      <i data-lucide="sparkles" class="w-4 h-4"></i>
    </button>
  </nav>

  <!-- ========================================================================= -->
  <!-- MAIN CINEMATIC EXPERIENCE -->
  <!-- ========================================================================= -->
  <main class="relative z-10 pt-20">

    <!-- ======================================================================= -->
    <!-- ACT 0: THE GENESIS (HERO TITLE SEQUENCE) -->
    <!-- ======================================================================= -->
    <section id="hero" class="min-h-screen flex flex-col justify-center items-center px-6 text-center relative py-20">
      
      <!-- Ambient Decorative Rings -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] sm:w-[750px] h-[500px] sm:h-[750px] rounded-full border border-white/5 pointer-events-none"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] sm:w-[500px] h-[350px] sm:h-[500px] rounded-full border border-gold-400/10 pointer-events-none animate-[spin_60s_linear_infinite]"></div>

      <div class="max-w-5xl mx-auto space-y-8 relative z-10 reveal-item">
        
        <!-- Scene Marker Badge -->
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/5 border border-white/10 backdrop-blur-md">
          <span class="w-2 h-2 rounded-full bg-gold-400 animate-ping"></span>
          <span class="font-mono text-xs text-gold-400 tracking-widest uppercase">ACT 0 // THE GENESIS &bull; CINEMATIC ODYSSEY</span>
        </div>

        <!-- Master Title -->
        <h1 class="text-4xl sm:text-6xl md:text-8xl font-display font-extrabold tracking-tight text-white uppercase leading-[1.05]">
          ENGINEERING THE <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold-300 via-gold-500 to-amber-200 glow-gold-text">
            INVISIBLE.
          </span>
        </h1>

        <!-- Scrambling Morphing Subtitle -->
        <div class="h-10 flex items-center justify-center font-mono text-sm sm:text-lg text-gray-300">
          <span class="text-gray-500 mr-2">&gt;</span>
          <span id="roleScrambler" class="text-gold-400 font-bold border-r-2 border-gold-400 pr-1">AI / ML ENGINEER AT TCS</span>
        </div>

        <p class="max-w-2xl mx-auto text-sm sm:text-base text-gray-400 leading-relaxed font-sans">
          Where silicon hardware reliability meets modern deep neural architectures. Uniting forensic circuit diagnostics, autonomous computer vision, and observational fine-art draughtsmanship into a single disciplined craft.
        </p>

        <!-- Live Telemetry Badges -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-3xl mx-auto pt-4">
          <div class="holo-card p-4 rounded-2xl text-center">
            <span class="block text-2xl sm:text-3xl font-display font-bold text-gold-400">8.89</span>
            <span class="text-[11px] font-mono text-gray-400 uppercase tracking-wider">CGPA &bull; NCET ECE</span>
          </div>
          <div class="holo-card p-4 rounded-2xl text-center">
            <span class="block text-2xl sm:text-3xl font-display font-bold text-cyan-400">99.4%</span>
            <span class="text-[11px] font-mono text-gray-400 uppercase tracking-wider">AOI VISION ACCURACY</span>
          </div>
          <div class="holo-card p-4 rounded-2xl text-center">
            <span class="block text-2xl sm:text-3xl font-display font-bold text-gold-400">6+</span>
            <span class="text-[11px] font-mono text-gray-400 uppercase tracking-wider">INDUSTRY CERTS</span>
          </div>
          <div class="holo-card p-4 rounded-2xl text-center">
            <span class="block text-2xl sm:text-3xl font-display font-bold text-white">50+</span>
            <span class="text-[11px] font-mono text-gray-400 uppercase tracking-wider">FINE ART STUDIES</span>
          </div>
        </div>

        <!-- Interactive CTAs -->
        <div class="pt-6 flex flex-wrap items-center justify-center gap-4">
          <a href="#architect" class="magnetic-btn px-8 py-4 rounded-2xl bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-400 hover:to-gold-500 text-noir-950 font-display font-bold text-sm uppercase tracking-widest transition-all shadow-[0_0_30px_rgba(229,169,60,0.35)] hover:scale-105 flex items-center space-x-2">
            <span>ENTER THE EXPERIENCE</span>
            <i data-lucide="arrow-down" class="w-4 h-4"></i>
          </a>
          <a href="#art-studio" class="magnetic-btn px-8 py-4 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/15 text-white font-display font-bold text-sm uppercase tracking-widest transition-all hover:scale-105 flex items-center space-x-2">
            <i data-lucide="brush" class="w-4 h-4 text-gold-400"></i>
            <span>VIEW DRAWING STUDIO</span>
          </a>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center space-y-2 opacity-60 hover:opacity-100 transition-opacity">
        <span class="text-[10px] font-mono uppercase tracking-widest text-gray-400">SCROLL DOWN</span>
        <div class="w-5 h-9 rounded-full border-2 border-white/20 flex justify-center p-1">
          <span class="w-1 h-2 bg-gold-400 rounded-full animate-bounce"></span>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT I: THE ARCHITECT (BIOGRAPHY & ADAPTIVE PROFILE FRAME) -->
    <!-- ======================================================================= -->
    <section id="architect" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT I &bull; THE ARCHITECT</span>
        </div>
        <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
          THE MONOLOGUE
        </h2>
        <p class="text-gray-400 font-mono text-xs max-w-xl">
          Origins, engineering philosophy, and the fusion of electronics, failure diagnostics, and generative intelligence.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Adaptive Profile Photo Frame Column -->
        <div class="lg:col-span-5 flex flex-col items-center reveal-item">
          
          <div class="relative group">
            
            <!-- Dynamic Aspect-Ratio Hugging Container -->
            <div id="profileFrame" class="real-tilt holo-card p-3 rounded-3xl transition-all duration-500 max-w-sm w-fit shadow-[0_20px_50px_rgba(0,0,0,0.8)]">
              
              <!-- Ambient Halo behind Photo -->
              <div class="absolute inset-0 bg-gradient-to-tr from-gold-500/20 to-cyan-500/10 rounded-3xl filter blur-xl opacity-60 group-hover:opacity-100 transition-opacity pointer-events-none"></div>

              <div class="relative overflow-hidden rounded-2xl bg-noir-950 flex items-center justify-center border border-white/10">
                <img id="profilePhotoImg" src="./assets/profile-avatar.svg" alt="Shreyas B J - Portrait" class="max-h-[460px] w-auto h-auto max-w-full object-contain mx-auto block group-hover:scale-[1.02] transition-transform duration-700">
                
                <!-- Aspect Ratio Badge Overlay -->
                <div class="absolute bottom-3 right-3 px-2 py-0.5 rounded bg-noir-950/80 backdrop-blur-md border border-white/20 text-[10px] font-mono text-gold-400">
                  <span id="aspectRatioTag">STUDIO 1:1</span>
                </div>
              </div>
            </div>

            <!-- Frame Controls -->
            <div class="mt-4 flex items-center justify-center space-x-3 w-full">
              <input type="file" id="profilePhotoInput" accept="image/*" class="hidden">
              <button onclick="document.getElementById('profilePhotoInput').click()" class="magnetic-btn px-4 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-xs font-mono text-gray-300 hover:text-white transition-all flex items-center space-x-2">
                <i data-lucide="upload" class="w-3.5 h-3.5 text-gold-400"></i>
                <span>UPLOAD PHOTO</span>
              </button>
              <button id="resetProfilePhotoBtn" class="magnetic-btn p-2 rounded-xl bg-white/5 hover:bg-red-500/20 border border-white/10 text-xs text-gray-400 hover:text-red-400 transition-colors" title="Reset to default portrait">
                <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Single Paragraph Narrative Column -->
        <div class="lg:col-span-7 space-y-8 reveal-item">
          
          <div class="holo-card p-8 rounded-3xl space-y-6 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-gold-500/10 rounded-full filter blur-3xl pointer-events-none"></div>

            <h3 class="text-xl sm:text-2xl font-display font-bold text-white flex items-center space-x-3">
              <span>Shreyas B J</span>
              <span class="w-1.5 h-1.5 rounded-full bg-gold-400"></span>
              <span class="text-xs font-mono text-gold-400 font-normal">CHIKKAMAGALURU &bull; BANGALORE</span>
            </h3>

            <!-- Single Paragraph Biography -->
            <p class="text-sm sm:text-base text-gray-300 leading-relaxed font-sans text-justify sm:text-left">
              Rooted in the calm terrains of <span class="text-gold-400 font-medium">Chikkamagaluru</span> and tempered in the high-velocity technological core of Bangalore, I am an <span class="text-white font-medium">AI/ML Engineer at Tata Consultancy Services (TCS)</span> with a rigorous foundation in <span class="text-white font-medium">Electronics &amp; Communication Engineering</span> from Nagarjuna College of Engineering and Technology (graduating with an <span class="text-gold-400 font-mono font-semibold">8.89 CGPA</span>). My engineering mindset was forged on industrial failure analysis lines at <span class="text-cyan-400 font-medium">Foxconn (Hon Hai Technology Group)</span>, where I analyzed microscopic circuit anomalies, traced high-density schematics, and conducted root-cause failure investigations under stringent manufacturing tolerances. Today, I translate that forensic hardware discipline into training high-performance machine learning models, deploying computer vision inference pipelines, and orchestrating multi-agent LLM systems certified by <span class="text-gold-400 font-medium">Databricks, Anthropic, and Google Cloud</span>—all while grounding my perception through a lifelong discipline of <span class="text-white font-medium">observational fine-art sketching</span> that bridges physical observation with synthetic machine intelligence.
            </p>

            <!-- Philosophy Quote Plaque -->
            <div class="border-l-2 border-gold-400/80 pl-4 py-1 text-xs font-mono text-gray-400 italic">
              "True engineering is not merely training neural weights; it is observing reality with forensic precision, whether through a microscope on an SMT production line or graphite on cold-pressed paper."
            </div>

            <!-- Fast Spec Badges -->
            <div class="pt-2 flex flex-wrap gap-2 text-[11px] font-mono">
              <span class="px-3 py-1 rounded-lg bg-white/5 border border-white/10 text-gold-300">#Python3</span>
              <span class="px-3 py-1 rounded-lg bg-white/5 border border-white/10 text-cyan-300">#PyTorch</span>
              <span class="px-3 py-1 rounded-lg bg-white/5 border border-white/10 text-emerald-300">#ComputerVision</span>
              <span class="px-3 py-1 rounded-lg bg-white/5 border border-white/10 text-purple-300">#HardwareDiagnostics</span>
              <span class="px-3 py-1 rounded-lg bg-white/5 border border-white/10 text-amber-300">#FineArtRealism</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT II: THE ODYSSEY (INTERACTIVE EXPERIENCE TIMELINE) -->
    <!-- ======================================================================= -->
    <section id="odyssey" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT II &bull; THE ODYSSEY</span>
        </div>
        <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
          CHRONICLES OF EXECUTION
        </h2>
        <p class="text-gray-400 font-mono text-xs max-w-xl">
          An interactive operational log through enterprise AI development, industrial manufacturing reliability, and academic excellence.
        </p>
      </div>

      <!-- Interactive Timeline Selector -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8 reveal-item">
        <button onclick="switchOdysseyMilestone(0)" id="odysseyBtn-0" class="odyssey-tab-btn active p-4 rounded-2xl bg-noir-900 border border-gold-400 text-left transition-all">
          <span class="text-[10px] font-mono text-gold-400 block">2024 &bull; PRESENT</span>
          <span class="font-display font-bold text-white text-sm">TCS</span>
          <span class="text-xs text-gray-400 block truncate">AI / ML Engineer</span>
        </button>
        <button onclick="switchOdysseyMilestone(1)" id="odysseyBtn-1" class="odyssey-tab-btn p-4 rounded-2xl bg-noir-900 border border-white/10 text-left hover:border-white/30 transition-all">
          <span class="text-[10px] font-mono text-cyan-400 block">2024 (Q4)</span>
          <span class="font-display font-bold text-white text-sm">Foxconn</span>
          <span class="text-xs text-gray-400 block truncate">Failure Analysis</span>
        </button>
        <button onclick="switchOdysseyMilestone(2)" id="odysseyBtn-2" class="odyssey-tab-btn p-4 rounded-2xl bg-noir-900 border border-white/10 text-left hover:border-white/30 transition-all">
          <span class="text-[10px] font-mono text-gold-400 block">2021 &bull; 2025</span>
          <span class="font-display font-bold text-white text-sm">NCET Bangalore</span>
          <span class="text-xs text-gray-400 block truncate">B.E. ECE (8.89)</span>
        </button>
        <button onclick="switchOdysseyMilestone(3)" id="odysseyBtn-3" class="odyssey-tab-btn p-4 rounded-2xl bg-noir-900 border border-white/10 text-left hover:border-white/30 transition-all">
          <span class="text-[10px] font-mono text-emerald-400 block">2024 (Q2)</span>
          <span class="font-display font-bold text-white text-sm">Skill Craft</span>
          <span class="text-xs text-gray-400 block truncate">ML Intern</span>
        </button>
      </div>

      <!-- Dynamic Dossier Container -->
      <div id="odysseyDossier" class="holo-card p-8 sm:p-10 rounded-3xl reveal-item min-h-[340px] flex flex-col justify-between">
        <!-- Content will be injected dynamically -->
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT III: THE NEURAL ARSENAL & HOLOGRAPHIC CERTIFICATIONS -->
    <!-- ======================================================================= -->
    <section id="arsenal" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT III &bull; THE ARSENAL &amp; CREDENTIALS</span>
        </div>
        <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
          SYNAPTIC CAPABILITIES
        </h2>
        <p class="text-gray-400 font-mono text-xs max-w-xl">
          Core technical competencies across artificial intelligence, enterprise MLOps, embedded hardware, and verified certifications.
        </p>
      </div>

      <!-- Skill Categories Filter Tabs -->
      <div class="flex flex-wrap items-center gap-2 mb-8 reveal-item">
        <button onclick="filterSkills('all')" class="skill-filter-btn active px-4 py-2 rounded-xl bg-gold-500 text-noir-950 font-mono text-xs font-bold transition-all">ALL DOMAINS</button>
        <button onclick="filterSkills('aiml')" class="skill-filter-btn px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-gray-300 font-mono text-xs hover:border-gold-400 transition-all">AI &amp; DEEP LEARNING</button>
        <button onclick="filterSkills('cloud')" class="skill-filter-btn px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-gray-300 font-mono text-xs hover:border-gold-400 transition-all">MLOPS &amp; DATA</button>
        <button onclick="filterSkills('hardware')" class="skill-filter-btn px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-gray-300 font-mono text-xs hover:border-gold-400 transition-all">ELECTRONICS &amp; IOT</button>
        <button onclick="filterSkills('creative')" class="skill-filter-btn px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-gray-300 font-mono text-xs hover:border-gold-400 transition-all">CREATIVE DRAUGHTSMANSHIP</button>
      </div>

      <!-- Filterable Skill Matrix Grid -->
      <div id="skillsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-16 reveal-item">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Holographic 3D Certification Plaques -->
      <div class="space-y-6 reveal-item">
        <div class="flex items-center justify-between border-b border-white/10 pb-4">
          <h3 class="text-xl font-display font-bold text-white flex items-center space-x-2">
            <i data-lucide="award" class="w-5 h-5 text-gold-400"></i>
            <span>VERIFIED INDUSTRY CERTIFICATIONS</span>
          </h3>
          <span class="text-xs font-mono text-gray-400">6 ACCREDITATIONS</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <!-- Cert 1: Databricks -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('databricks')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-red-500/10 text-red-400 border border-red-500/20">
                <i data-lucide="database" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">VERIFIED</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">Databricks Certified Associate</h4>
            <p class="text-xs text-gray-400 mt-1">Machine Learning &amp; Distributed Spark Compute</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>CREDENTIAL: CERT-DB-ML</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>

          <!-- Cert 2: Claude Anthropic -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('claude')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/20">
                <i data-lucide="cpu" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">VERIFIED</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">Anthropic Claude Certified</h4>
            <p class="text-xs text-gray-400 mt-1">Advanced Prompt Engineering &amp; Agent Workflows</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>CREDENTIAL: CERT-ANTH-01</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>

          <!-- Cert 3: Google Gemini -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('gemini')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-blue-500/10 text-blue-400 border border-blue-500/20">
                <i data-lucide="sparkles" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">VERIFIED</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">Google Cloud Gemini AI</h4>
            <p class="text-xs text-gray-400 mt-1">Multimodal Vision, LLM Architectures &amp; Vertex AI</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>CREDENTIAL: CERT-GCP-GEM</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>

          <!-- Cert 4: NPTEL IIT Madras -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('nptel')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                <i data-lucide="binary" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">IIT MADRAS</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">NPTEL Deep Learning</h4>
            <p class="text-xs text-gray-400 mt-1">CNNs, RNNs, Backpropagation &amp; Microprocessors</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>ACCREDITED: IIT-M-NPTEL</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>

          <!-- Cert 5: NXT Wave -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('nxtwave')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/20">
                <i data-lucide="code" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">VERIFIED</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">NXT Wave Full Stack</h4>
            <p class="text-xs text-gray-400 mt-1">Python Full Stack, Relational SQL &amp; Algorithmic Logic</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>CREDENTIAL: CERT-NXT-PY</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>

          <!-- Cert 6: Technical Hub -->
          <div class="real-tilt holo-card p-6 rounded-2xl cursor-pointer group" onclick="openCertModal('techhub')">
            <div class="flex items-start justify-between mb-4">
              <div class="p-3 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
                <i data-lucide="radio" class="w-6 h-6"></i>
              </div>
              <span class="text-[10px] font-mono text-gold-400 border border-gold-400/30 px-2 py-0.5 rounded-full">VERIFIED</span>
            </div>
            <h4 class="font-display font-bold text-white text-base group-hover:text-gold-400 transition-colors">Technical Hub Embedded &amp; IoT</h4>
            <p class="text-xs text-gray-400 mt-1">Microcontroller Interfacing, Sensors &amp; Embedded C</p>
            <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-gray-500">
              <span>CREDENTIAL: CERT-TH-EMB</span>
              <span class="text-gold-400 flex items-center space-x-1"><span>VIEW</span><i data-lucide="chevron-right" class="w-3 h-3"></i></span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT IV: FLAGSHIP INVENTIONS LAB (3 INTERACTIVE LIVE SIMULATIONS) -->
    <!-- ======================================================================= -->
    <section id="inventions" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT IV &bull; FLAGSHIP INVENTIONS LAB</span>
        </div>
        <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
          INTERACTIVE SIMULATIONS
        </h2>
        <p class="text-gray-400 font-mono text-xs max-w-xl">
          Direct hands-on interaction with three custom-built intelligent systems: Multi-Agent AI Travel, Automated Optical PCB Inspection, and Autonomous A* Pathfinding.
        </p>
      </div>

      <div class="space-y-16">
        
        <!-- =================================================================== -->
        <!-- INVENTION 01: OMNITRAVEL AGENTIC AI PLANNER -->
        <!-- =================================================================== -->
        <div class="holo-card p-8 rounded-3xl reveal-item space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-gold-400 tracking-wider uppercase">INVENTION 01 &bull; MULTI-AGENT LLM SYSTEM</span>
              <h3 class="text-2xl font-display font-bold text-white">OmniTravel Agentic Orchestrator</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-mono">LangChain + RAG</span>
              <span class="px-3 py-1 rounded-full bg-gold-500/10 border border-gold-500/30 text-gold-300 text-xs font-mono">Live Demo</span>
            </div>
          </div>

          <p class="text-sm text-gray-300">
            A hierarchical multi-agent framework that ingests natural language travel objectives, executes vector similarity search over historical itineraries, verifies weather telemetry, and synthesizes grounded travel schedules.
          </p>

          <!-- Interactive Terminal Prompt Simulator -->
          <div class="bg-noir-950 border border-white/15 rounded-2xl p-5 space-y-4">
            <div class="flex items-center justify-between text-xs font-mono text-gray-400 border-b border-white/10 pb-3">
              <span class="flex items-center space-x-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span class="text-white">AGENT TERMINAL v2.4</span>
              </span>
              <span>INPUT PROMPT &amp; OBSERVE EXECUTION</span>
            </div>

            <!-- Preset Buttons -->
            <div class="flex flex-wrap gap-2 text-xs font-mono">
              <span class="text-gray-500 my-auto text-[11px]">PRESETS:</span>
              <button onclick="setTravelPreset('Kyoto 4-day Zen temple and digital art tour on a budget')" class="px-2.5 py-1 rounded bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white border border-white/10 transition-colors">Kyoto Temples</button>
              <button onclick="setTravelPreset('Swiss Alps 3-day high-altitude photography and trail trek')" class="px-2.5 py-1 rounded bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white border border-white/10 transition-colors">Swiss Alps</button>
              <button onclick="setTravelPreset('Florence 5-day Renaissance art & Tuscan culinary journey')" class="px-2.5 py-1 rounded bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white border border-white/10 transition-colors">Florence Art</button>
            </div>

            <div class="flex items-center space-x-2">
              <div class="relative flex-1">
                <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-gold-400 font-mono text-sm">&gt;</span>
                <input type="text" id="travelInput" value="Kyoto 4-day Zen temple and digital art tour on a budget" class="w-full bg-noir-900 border border-white/15 rounded-xl pl-9 pr-4 py-2.5 text-xs sm:text-sm font-mono text-white focus:outline-none focus:border-gold-400">
              </div>
              <button onclick="executeTravelSimulation()" class="magnetic-btn px-5 py-2.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider flex items-center space-x-1.5 transition-all">
                <span>RUN AGENT</span>
                <i data-lucide="play" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <!-- Terminal Output Stream -->
            <div id="travelTerminalOutput" class="bg-noir-900/90 rounded-xl p-4 font-mono text-xs space-y-1.5 border border-white/10 min-h-[140px] text-gray-300 max-h-[220px] overflow-y-auto">
              <p class="text-gray-500">&gt; System initialized. Awaiting user dispatch...</p>
            </div>
          </div>
        </div>

        <!-- =================================================================== -->
        <!-- INVENTION 02: INDUSTRIAL AOI (AUTOMATED OPTICAL INSPECTION) DEFECT SCANNER -->
        <!-- =================================================================== -->
        <div class="holo-card p-8 rounded-3xl reveal-item space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-cyan-400 tracking-wider uppercase">INVENTION 02 &bull; COMPUTER VISION &amp; FAILURE ANALYSIS</span>
              <h3 class="text-2xl font-display font-bold text-white">Industrial AOI SMT Defect Vision Scanner</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-red-500/10 border border-red-500/30 text-red-300 text-xs font-mono">YOLOv8 + OpenCV</span>
              <span class="px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-mono">99.4% Precision</span>
            </div>
          </div>

          <p class="text-sm text-gray-300">
            Engineered from real-world high-volume manufacturing failure diagnostics at Foxconn. Drag the interactive split slider below to toggle between the raw camera capture and the real-time AI bounding box defect detection layer.
          </p>

          <!-- Interactive Before / After Split Slider -->
          <div class="relative w-full max-w-4xl mx-auto h-[320px] sm:h-[420px] rounded-2xl overflow-hidden border border-white/20 select-none cursor-ew-resize" id="aoiSliderContainer">
            
            <!-- Before Layer (Raw PCB SMT) -->
            <div class="absolute inset-0 bg-[#0d1512] flex items-center justify-center p-6 text-center">
              <svg viewBox="0 0 600 350" class="w-full h-full object-contain">
                <!-- Circuit Board Base -->
                <rect width="600" height="350" fill="#0A1811" rx="10"/>
                <!-- Circuit Traces -->
                <path d="M 50 50 L 200 50 L 250 100 L 400 100 L 450 50 L 550 50" stroke="#163E2B" stroke-width="3" fill="none"/>
                <path d="M 50 120 L 150 120 L 200 170 L 350 170 L 400 120 L 550 120" stroke="#163E2B" stroke-width="3" fill="none"/>
                <path d="M 50 220 L 180 220 L 240 280 L 450 280 L 550 220" stroke="#163E2B" stroke-width="3" fill="none"/>
                
                <!-- Main Microchip -->
                <rect x="220" y="110" width="160" height="130" fill="#1C242B" stroke="#374151" stroke-width="2" rx="4"/>
                <text x="300" y="180" fill="#9CA3AF" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">ARM STM32F4</text>
                
                <!-- SMT Resistors & Capacitors (some with defects) -->
                <!-- Defect 1: Solder Bridge at (140, 90) -->
                <rect x="130" y="85" width="28" height="14" fill="#3B4252" stroke="#94A3B8"/>
                <circle cx="158" cy="92" r="5" fill="#CBD5E1"/> <!-- Solder blob -->
                <rect x="165" y="85" width="28" height="14" fill="#3B4252" stroke="#94A3B8"/>
                
                <!-- Defect 2: Missing SMD Resistor at (420, 160) -->
                <rect x="420" y="160" width="28" height="14" fill="none" stroke="#EF4444" stroke-dasharray="2 2"/>
                
                <!-- Normal Components -->
                <rect x="80" y="160" width="24" height="12" fill="#3B4252"/>
                <rect x="80" y="185" width="24" height="12" fill="#3B4252"/>
                <rect x="460" y="240" width="32" height="16" fill="#3B4252"/>
              </svg>
              <span class="absolute top-4 left-4 px-3 py-1 rounded bg-black/80 border border-white/20 text-xs font-mono text-gray-300">LAYER: RAW OPTICAL SENSOR</span>
            </div>

            <!-- After Layer (YOLOv8 AI Inference Overlay) -->
            <div id="aoiAfterLayer" class="absolute inset-0 bg-[#061017] flex items-center justify-center p-6 text-center overflow-hidden" style="clip-path: inset(0 0 0 50%);">
              <svg viewBox="0 0 600 350" class="w-full h-full object-contain">
                <!-- Circuit Board Base -->
                <rect width="600" height="350" fill="#06121E" rx="10"/>
                <!-- Circuit Traces Highlighted -->
                <path d="M 50 50 L 200 50 L 250 100 L 400 100 L 450 50 L 550 50" stroke="#0284C7" stroke-width="2" fill="none" opacity="0.6"/>
                <path d="M 50 120 L 150 120 L 200 170 L 350 170 L 400 120 L 550 120" stroke="#0284C7" stroke-width="2" fill="none" opacity="0.6"/>
                <path d="M 50 220 L 180 220 L 240 280 L 450 280 L 550 220" stroke="#0284C7" stroke-width="2" fill="none" opacity="0.6"/>
                
                <!-- Chip -->
                <rect x="220" y="110" width="160" height="130" fill="#0F172A" stroke="#0EA5E9" stroke-width="2" rx="4"/>
                <text x="300" y="180" fill="#38BDF8" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">ARM STM32F4 [OK: 0.998]</text>
                
                <!-- DEFECT 1: Solder Bridge Detection -->
                <rect x="120" y="75" width="80" height="35" fill="rgba(239, 68, 68, 0.15)" stroke="#EF4444" stroke-width="2" stroke-dasharray="4 2"/>
                <text x="160" y="70" fill="#EF4444" font-family="monospace" font-size="11" text-anchor="middle" font-weight="bold">DEFECT: SOLDER_BRIDGE (99.4%)</text>
                
                <!-- DEFECT 2: Missing Component Detection -->
                <rect x="410" y="150" width="50" height="35" fill="rgba(245, 158, 11, 0.15)" stroke="#F59E0B" stroke-width="2"/>
                <text x="435" y="145" fill="#F59E0B" font-family="monospace" font-size="11" text-anchor="middle" font-weight="bold">MISSING_RESISTOR (98.9%)</text>

                <!-- Normal Component Box -->
                <rect x="75" y="155" width="34" height="22" fill="rgba(16, 185, 129, 0.1)" stroke="#10B981" stroke-width="1.5"/>
                <text x="92" y="150" fill="#10B981" font-family="monospace" font-size="9" text-anchor="middle">PASS 0.99</text>
              </svg>
              <span class="absolute top-4 right-4 px-3 py-1 rounded bg-black/80 border border-cyan-400/40 text-xs font-mono text-cyan-400">LAYER: YOLOv8 INFERENCE OVERLAY</span>
            </div>

            <!-- Draggable Divider Line & Knob -->
            <div id="aoiSliderHandle" class="slider-handle" style="left: 50%;">
              <div class="slider-handle-button">
                <i data-lucide="chevrons-left-right" class="w-4 h-4"></i>
              </div>
            </div>
          </div>
          <div class="text-center text-xs font-mono text-gray-400">
            &larr; Drag slider left or right to inspect real-time AI bounding box inference &rarr;
          </div>
        </div>

        <!-- =================================================================== -->
        <!-- INVENTION 03: AUTONOMOUS ROVER & 360-DEGREE LIDAR TELEMETRY -->
        <!-- =================================================================== -->
        <div class="holo-card p-8 rounded-3xl reveal-item space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-emerald-400 tracking-wider uppercase">INVENTION 03 &bull; SENSOR FUSION &amp; ROBOTICS</span>
              <h3 class="text-2xl font-display font-bold text-white">Autonomous Multi-Sensor Rover</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-mono">Edge Compute</span>
              <span class="px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-mono">Live LIDAR Sweep</span>
            </div>
          </div>

          <p class="text-sm text-gray-300">
            ECE Capstone project fusing 360&deg; LIDAR telemetry, ultrasonic ranging, and motor encoder feedback into an embedded Jetson edge system for continuous obstacle-avoidance and autonomous terrain navigation.
          </p>

          <!-- Simple, Elegant 360-degree LIDAR Radar Animation -->
          <div class="bg-noir-950 border border-white/15 rounded-2xl p-6 flex flex-col md:flex-row items-center justify-between gap-8">
            <div class="relative w-64 h-64 sm:w-72 sm:h-72 flex items-center justify-center shrink-0">
              <canvas id="lidarRadarCanvas" width="280" height="280" class="w-full h-full rounded-full bg-noir-900 border border-white/10 shadow-[0_0_30px_rgba(16,185,129,0.15)]"></canvas>
              <div class="absolute inset-0 pointer-events-none flex items-center justify-center">
                <div class="w-3 h-3 rounded-full bg-emerald-400 shadow-[0_0_12px_#10B981]"></div>
              </div>
            </div>

            <!-- Live Telemetry Readout -->
            <div class="flex-1 w-full space-y-4 font-mono text-xs">
              <div class="flex items-center justify-between border-b border-white/10 pb-2">
                <span class="text-gray-400">RADAR TELEMETRY STREAM:</span>
                <span class="text-emerald-400 font-bold flex items-center space-x-1.5">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                  <span>ACTIVE &bull; 60 FPS</span>
                </span>
              </div>

              <div class="grid grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">CURRENT AZIMUTH</span>
                  <span id="radarAzimuth" class="text-gold-400 text-sm font-bold">142.4&deg;</span>
                </div>
                <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">SCAN FREQUENCY</span>
                  <span class="text-white text-sm font-bold">20.0 Hz</span>
                </div>
                <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">OBSTACLE CLEARANCE</span>
                  <span class="text-emerald-400 text-sm font-bold">100% CLEAR</span>
                </div>
                <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">EDGE HARDWARE</span>
                  <span class="text-cyan-400 text-sm font-bold">Jetson + STM32</span>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-noir-900 border border-white/10 text-gray-400 text-[11px] leading-relaxed flex items-center space-x-2.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0"></span>
                <span>Continuous 360-degree LIDAR ray-casting and ultrasonic spatial mapping at sub-millisecond edge latency.</span>
              </div>
            </div>
          </div>
        </div></div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT V: THE OBSERVATIONAL DRAWING STUDIO (FULL INSTAGRAM-GRADE EXPERIENCE) -->
    <!-- ======================================================================= -->
    <section id="art-studio" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT V &bull; THE OBSERVATIONAL DRAWING STUDIO</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
              GRAPHITE &amp; OBSERVATION
            </h2>
            <p class="text-gray-400 font-mono text-xs max-w-xl mt-1">
              Shreyas\'s Instagram-style studio feed. Post real drawings, view double-tap like heart bursts, explore high-res lightbox views, and leave persistent comments.
            </p>
          </div>
          
          <!-- Post New Drawing Button -->
          <button onclick="openNewPostModal()" class="magnetic-btn px-6 py-3 rounded-2xl bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-400 hover:to-gold-500 text-noir-950 font-display font-bold text-xs uppercase tracking-wider flex items-center space-x-2 shadow-[0_0_25px_rgba(229,169,60,0.3)] hover:scale-105 self-start sm:self-auto">
            <i data-lucide="plus-circle" class="w-4 h-4"></i>
            <span>POST NEW DRAWING</span>
          </button>
        </div>
      </div>

      <!-- Studio Feed Controls (Filter by Medium & Search) -->
      <div class="flex flex-wrap items-center justify-between gap-4 mb-8 reveal-item border-b border-white/10 pb-4">
        <div class="flex flex-wrap items-center gap-2">
          <button onclick="filterDrawingCategory('all')" class="draw-filter-btn active px-3.5 py-1.5 rounded-xl bg-gold-500 text-noir-950 text-xs font-mono font-bold transition-all">ALL WORKS</button>
          <button onclick="filterDrawingCategory('portrait')" class="draw-filter-btn px-3.5 py-1.5 rounded-xl bg-white/5 border border-white/10 text-gray-300 text-xs font-mono hover:border-gold-400 transition-all">PORTRAITS</button>
          <button onclick="filterDrawingCategory('perspective')" class="draw-filter-btn px-3.5 py-1.5 rounded-xl bg-white/5 border border-white/10 text-gray-300 text-xs font-mono hover:border-gold-400 transition-all">PERSPECTIVE</button>
          <button onclick="filterDrawingCategory('cyber')" class="draw-filter-btn px-3.5 py-1.5 rounded-xl bg-white/5 border border-white/10 text-gray-300 text-xs font-mono hover:border-gold-400 transition-all">CYBERNETIC</button>
          <button onclick="filterDrawingCategory('charcoal')" class="draw-filter-btn px-3.5 py-1.5 rounded-xl bg-white/5 border border-white/10 text-gray-300 text-xs font-mono hover:border-gold-400 transition-all">CHARCOAL</button>
        </div>

        <div class="flex items-center space-x-3 text-xs font-mono text-gray-400">
          <button onclick="loadSampleSketches()" class="hover:text-gold-400 flex items-center space-x-1.5 border border-white/15 px-3 py-1.5 rounded-xl hover:border-gold-400/50 transition-colors">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-gold-400"></i>
            <span>LOAD CURATED SKETCHES</span>
          </button>
        </div>
      </div>

      <!-- Instagram Posts Feed Container (Masonry / Cards) -->
      <div id="postsFeedContainer" class="grid grid-cols-1 md:grid-cols-2 gap-8 reveal-item">
        <!-- Rendered dynamically by JavaScript -->
      </div>

      <!-- Empty State -->
      <div id="emptyFeedState" class="hidden text-center py-20 holo-card rounded-3xl space-y-4 max-w-lg mx-auto">
        <i data-lucide="palette" class="w-12 h-12 text-gold-400/60 mx-auto"></i>
        <h3 class="text-xl font-display font-bold text-white">No Drawings Posted Yet</h3>
        <p class="text-xs text-gray-400 max-w-sm mx-auto">
          Click "+ POST NEW DRAWING" above to publish your original artwork, or load curated sketches to see how it looks.
        </p>
        <button onclick="loadSampleSketches()" class="magnetic-btn px-6 py-2.5 rounded-xl bg-gold-500 text-noir-950 font-display font-bold text-xs uppercase tracking-wider">
          LOAD CURATED SKETCHES
        </button>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT VI: BEHIND THE MIND (INTERACTIVE NEURAL HYPERPARAMETER LAB) -->
    <!-- ======================================================================= -->
    <section id="mind" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item">
        <div class="flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT VI &bull; BEHIND THE MIND</span>
        </div>
        <h2 class="text-3xl sm:text-5xl font-display font-bold text-white tracking-tight">
          NEURAL WEIGHT PLAYGROUND
        </h2>
        <p class="text-gray-400 font-mono text-xs max-w-xl">
          An interactive laboratory visualizing how Shreyas optimizes attention matrices, decision boundaries, and model quantization.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center reveal-item">
        
        <!-- Controls Column -->
        <div class="lg:col-span-5 holo-card p-6 sm:p-8 rounded-3xl space-y-6">
          <h3 class="text-lg font-display font-bold text-white flex items-center space-x-2">
            <i data-lucide="sliders" class="w-5 h-5 text-gold-400"></i>
            <span>HYPERPARAMETER TUNER</span>
          </h3>

          <!-- Slider 1: Learning Rate -->
          <div class="space-y-2 font-mono text-xs">
            <div class="flex justify-between">
              <span class="text-gray-400">LEARNING RATE (&alpha;):</span>
              <span id="lrVal" class="text-gold-400 font-bold">0.003</span>
            </div>
            <input type="range" id="lrSlider" min="1" max="10" value="3" class="w-full accent-gold-500 cursor-pointer">
          </div>

          <!-- Slider 2: Multi-Head Attention Count -->
          <div class="space-y-2 font-mono text-xs">
            <div class="flex justify-between">
              <span class="text-gray-400">ATTENTION HEADS:</span>
              <span id="headsVal" class="text-cyan-400 font-bold">8 HEADS</span>
            </div>
            <input type="range" id="headsSlider" min="2" max="16" step="2" value="8" class="w-full accent-cyan-400 cursor-pointer">
          </div>

          <!-- Slider 3: Temperature -->
          <div class="space-y-2 font-mono text-xs">
            <div class="flex justify-between">
              <span class="text-gray-400">TEMPERATURE (ENTROPY):</span>
              <span id="tempVal" class="text-emerald-400 font-bold">0.72</span>
            </div>
            <input type="range" id="tempSlider" min="1" max="100" value="72" class="w-full accent-emerald-400 cursor-pointer">
          </div>

          <!-- Model Quantization Selector -->
          <div class="space-y-2 font-mono text-xs">
            <span class="text-gray-400 block">PRECISION QUANTIZATION:</span>
            <div class="grid grid-cols-3 gap-2">
              <button onclick="setQuantization('FP16')" id="q-fp16" class="p-2 rounded-xl bg-white/10 text-white border border-gold-400 text-center font-bold">FP16</button>
              <button onclick="setQuantization('INT8')" id="q-int8" class="p-2 rounded-xl bg-white/5 text-gray-400 border border-white/10 text-center hover:text-white">INT8</button>
              <button onclick="setQuantization('INT4')" id="q-int4" class="p-2 rounded-xl bg-white/5 text-gray-400 border border-white/10 text-center hover:text-white">INT4</button>
            </div>
          </div>

          <!-- Telemetry Stats -->
          <div class="p-4 rounded-xl bg-noir-950 border border-white/10 font-mono text-xs space-y-1 text-gray-400">
            <div class="flex justify-between"><span>VRAM FOOTPRINT:</span><span id="vramVal" class="text-white">4.2 GB</span></div>
            <div class="flex justify-between"><span>INFERENCE LATENCY:</span><span id="latencyVal" class="text-emerald-400">18.4 ms</span></div>
            <div class="flex justify-between"><span>CONVERGENCE LOSS:</span><span id="lossVal" class="text-gold-400">0.0418</span></div>
          </div>
        </div>

        <!-- Live Visual Attention/Decision Canvas Column -->
        <div class="lg:col-span-7 holo-card p-6 sm:p-8 rounded-3xl flex flex-col items-center justify-center space-y-4">
          <div class="w-full flex items-center justify-between text-xs font-mono text-gray-400 border-b border-white/10 pb-3">
            <span>SYNAPTIC ATTENTION HEATMAP</span>
            <span class="text-gold-400 animate-pulse">&bull; REAL-TIME TENSOR STREAM</span>
          </div>

          <canvas id="neuralPlaygroundCanvas" width="500" height="340" class="w-full max-w-md h-auto bg-noir-950 rounded-2xl border border-white/15 shadow-inner"></canvas>
          
          <div class="text-[11px] font-mono text-gray-500 text-center">
            Adjust the sliders to watch the mathematical decision boundary &amp; vector attention matrix recalculate in real-time.
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- ACT VII: THE TRANSMISSION FINALE (CONTACT & HOLLYWOOD CREDITS) -->
    <!-- ======================================================================= -->
    <section id="finale" class="py-28 px-6 max-w-6xl mx-auto">
      
      <!-- Act Header -->
      <div class="mb-14 space-y-2 reveal-item text-center max-w-2xl mx-auto">
        <div class="inline-flex items-center space-x-2 text-gold-400 font-mono text-xs tracking-widest uppercase">
          <span class="w-6 h-[1px] bg-gold-400"></span>
          <span>ACT VII &bull; TRANSMISSION &amp; FINALE</span>
          <span class="w-6 h-[1px] bg-gold-400"></span>
        </div>
        <h2 class="text-3xl sm:text-6xl font-display font-bold text-white tracking-tight uppercase">
          CONNECT &amp; CONVERGE
        </h2>
        <p class="text-gray-400 font-mono text-xs">
          Open for AI engineering collaborations, computer vision systems, or creative discourse. Transmit your frequency below.
        </p>
      </div>

      <!-- Global Appreciation Beacon & Firework Trigger -->
      <div class="mb-16 text-center reveal-item">
        <div class="inline-block p-1 rounded-3xl bg-gradient-to-r from-gold-500/40 via-cyan-500/40 to-heart/40">
          <button id="globalLikeBtn" onclick="triggerGlobalLikeCount(event)" class="magnetic-btn px-8 py-5 rounded-3xl bg-noir-950 hover:bg-noir-900 text-white flex items-center space-x-4 group shadow-[0_0_40px_rgba(229,169,60,0.25)] transition-all">
            <div class="p-3 rounded-full bg-heart/10 text-heart group-hover:scale-125 transition-transform">
              <i data-lucide="heart" class="w-7 h-7 fill-heart"></i>
            </div>
            <div class="text-left font-mono">
              <div class="text-[11px] text-gray-400 uppercase tracking-widest">SEND PORTFOLIO APPRECIATION</div>
              <div class="text-xl sm:text-2xl font-bold font-display text-white flex items-center space-x-2">
                <span id="globalLikeCount">1,482</span>
                <span class="text-xs text-gold-400 font-normal">TRANSMISSIONS RECEIVED</span>
              </div>
            </div>
          </button>
        </div>
      </div>

      <!-- Contact Console Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 reveal-item">
        
        <!-- Direct Telemetry Dossier -->
        <div class="holo-card p-8 rounded-3xl space-y-6 flex flex-col justify-between">
          <div class="space-y-4">
            <h3 class="text-2xl font-display font-bold text-white">Direct Channels</h3>
            <p class="text-xs text-gray-400 font-mono leading-relaxed">
              Based in Bangalore / Chikkamagaluru, India. Active on IST timeline with international collaboration readiness.
            </p>

            <div class="space-y-3 pt-2 font-mono text-xs">
              
              <!-- Email Button -->
              <div class="flex items-center justify-between p-3.5 rounded-xl bg-white/5 border border-white/10 hover:border-gold-400/50 transition-colors">
                <div class="flex items-center space-x-3">
                  <i data-lucide="mail" class="w-4 h-4 text-gold-400"></i>
                  <span class="text-gray-300 select-all">shreyasbj03@gmail.com</span>
                </div>
                <button onclick="copyToClipboard('shreyasbj03@gmail.com', 'Email copied to clipboard!')" class="text-gold-400 hover:text-white text-[11px] font-bold">COPY</button>
              </div>

              <!-- Phone Button -->
              <div class="flex items-center justify-between p-3.5 rounded-xl bg-white/5 border border-white/10 hover:border-gold-400/50 transition-colors">
                <div class="flex items-center space-x-3">
                  <i data-lucide="phone" class="w-4 h-4 text-cyan-400"></i>
                  <span class="text-gray-300 select-all">+91 9110464228</span>
                </div>
                <a href="tel:+919110464228" class="text-cyan-400 hover:text-white text-[11px] font-bold">CALL</a>
              </div>

              <!-- Location -->
              <div class="flex items-center justify-between p-3.5 rounded-xl bg-white/5 border border-white/10">
                <div class="flex items-center space-x-3">
                  <i data-lucide="map-pin" class="w-4 h-4 text-emerald-400"></i>
                  <span class="text-gray-300">Bangalore &bull; Chikkamagaluru, Karnataka</span>
                </div>
                <span class="text-emerald-400 text-[11px]">UTC +05:30</span>
              </div>
            </div>
          </div>

          <!-- Social Links -->
          <div class="pt-6 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-mono text-gray-500">DIGITAL REACH:</span>
            <div class="flex items-center space-x-3">
              <a href="https://linkedin.com/in/shreyas-b-j-975988226" target="_blank" rel="noopener noreferrer" class="magnetic-btn p-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 hover:text-gold-400 border border-white/10 transition-colors" title="LinkedIn">
                <i data-lucide="linkedin" class="w-4 h-4"></i>
              </a>
              <a href="https://github.com/shreyasbj03" target="_blank" rel="noopener noreferrer" class="magnetic-btn p-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 hover:text-gold-400 border border-white/10 transition-colors" title="GitHub">
                <i data-lucide="github" class="w-4 h-4"></i>
              </a>
              <a href="#art-studio" class="magnetic-btn p-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 hover:text-gold-400 border border-white/10 transition-colors" title="Instagram Sketches">
                <i data-lucide="instagram" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Interactive Transmission Form -->
        <div class="holo-card p-8 rounded-3xl space-y-4">
          <h3 class="text-2xl font-display font-bold text-white">Transmit Message</h3>
          
          <form onsubmit="handleContactSubmit(event)" class="space-y-3 font-mono text-xs">
            <div>
              <label class="block text-gray-400 mb-1">CALLSIGN / NAME</label>
              <input type="text" id="contactName" required placeholder="Alex Mercer" class="w-full bg-noir-950 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-gold-400">
            </div>

            <div>
              <label class="block text-gray-400 mb-1">FREQUENCY / EMAIL</label>
              <input type="email" id="contactEmail" required placeholder="alex@domain.com" class="w-full bg-noir-950 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-gold-400">
            </div>

            <div>
              <label class="block text-gray-400 mb-1">TRANSMISSION PAYLOAD</label>
              <textarea id="contactMessage" required rows="4" placeholder="Hello Shreyas, I came across your portfolio and would like to discuss..." class="w-full bg-noir-950 border border-white/15 rounded-xl p-4 text-white focus:outline-none focus:border-gold-400 resize-none font-sans"></textarea>
            </div>

            <button type="submit" class="magnetic-btn w-full py-3.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(229,169,60,0.3)] hover:scale-[1.01] flex items-center justify-center space-x-2">
              <span>DISPATCH TRANSMISSION</span>
              <i data-lucide="send" class="w-3.5 h-3.5"></i>
            </button>
          </form>
        </div>
      </div>

      <!-- Hollywood Production Credits Roll Trigger -->
      <div class="mt-20 text-center reveal-item">
        <button onclick="toggleCreditsModal()" class="magnetic-btn px-6 py-2.5 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-mono text-gray-400 hover:text-gold-400 transition-colors flex items-center space-x-2 mx-auto">
          <i data-lucide="film" class="w-3.5 h-3.5 text-gold-400"></i>
          <span>VIEW PRODUCTION CREDITS</span>
        </button>
      </div>

    </section>

    <!-- ======================================================================= -->
    <!-- CINEMATIC FOOTER -->
    <!-- ======================================================================= -->
    <footer class="py-12 px-6 border-t border-white/10 text-center font-mono text-xs text-gray-500 space-y-2 relative z-10">
      <p class="text-gray-400">SHREYAS B J &bull; AI / ML ENGINEER &bull; B.E. ECE (8.89 CGPA)</p>
      <p class="text-[11px]">CRAFTED WITH PRECISION &bull; ALL RIGHTS RESERVED &bull; MMXXVI</p>
    </footer>

  </main>

  <!-- ========================================================================= -->
  <!-- MODAL: POST NEW DRAWING (INSTAGRAM CREATOR STUDIO) -->
  <!-- ========================================================================= -->
  <div id="newPostModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-xl hidden flex items-center justify-center p-4">
    <div class="holo-card max-w-xl w-full p-6 sm:p-8 rounded-3xl space-y-6 relative max-h-[90vh] overflow-y-auto">
      
      <div class="flex items-center justify-between border-b border-white/10 pb-4">
        <div class="flex items-center space-x-2">
          <i data-lucide="plus-circle" class="w-5 h-5 text-gold-400"></i>
          <h3 class="text-xl font-display font-bold text-white">Post New Drawing</h3>
        </div>
        <button onclick="closeNewPostModal()" class="p-2 text-gray-400 hover:text-white transition-colors">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form onsubmit="handleCreatePost(event)" class="space-y-4 font-mono text-xs">
        
        <!-- Image Upload Dropzone -->
        <div class="space-y-1.5">
          <label class="block text-gray-400">ARTWORK FILE (IMAGE)</label>
          <div onclick="document.getElementById('postImageInput').click()" class="border-2 border-dashed border-white/20 hover:border-gold-400/60 rounded-2xl p-6 text-center cursor-pointer transition-colors bg-noir-950">
            <input type="file" id="postImageInput" accept="image/*" class="hidden" onchange="handlePreviewPostImage(event)" required>
            
            <div id="uploadPlaceholder">
              <i data-lucide="image" class="w-8 h-8 text-gold-400 mx-auto mb-2"></i>
              <span class="text-white block font-display font-bold text-sm">Choose or Drop Drawing File</span>
              <span class="text-gray-500 text-[11px] block mt-1">PNG, JPG, WEBP, or SVG</span>
            </div>

            <div id="imagePreviewContainer" class="hidden">
              <img id="imagePreviewEl" src="" class="max-h-60 mx-auto rounded-xl object-contain shadow-lg">
              <span id="previewAspectBadge" class="inline-block mt-2 px-2 py-0.5 rounded bg-noir-900 border border-white/20 text-[10px] text-gold-400">Aspect 1:1</span>
            </div>
          </div>
        </div>

        <!-- Filter Presets -->
        <div class="space-y-1">
          <label class="block text-gray-400">STUDIO FILTER LOOK</label>
          <div class="grid grid-cols-4 gap-2 text-[11px]">
            <button type="button" onclick="setPostFilter('none')" id="filt-none" class="p-2 rounded-lg bg-white/10 border border-gold-400 text-white font-bold text-center">Natural</button>
            <button type="button" onclick="setPostFilter('charcoal')" id="filt-charcoal" class="p-2 rounded-lg bg-white/5 border border-white/10 text-gray-400 hover:text-white text-center">Charcoal</button>
            <button type="button" onclick="setPostFilter('sepia')" id="filt-sepia" class="p-2 rounded-lg bg-white/5 border border-white/10 text-gray-400 hover:text-white text-center">Sepia</button>
            <button type="button" onclick="setPostFilter('cyber')" id="filt-cyber" class="p-2 rounded-lg bg-white/5 border border-white/10 text-gray-400 hover:text-white text-center">Cyber</button>
          </div>
        </div>

        <!-- Title -->
        <div>
          <label class="block text-gray-400 mb-1">DRAWING TITLE</label>
          <input type="text" id="postTitleInput" required placeholder="e.g. Study of an Old Man in Charcoal" class="w-full bg-noir-950 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-gold-400">
        </div>

        <!-- Category & Medium -->
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-gray-400 mb-1">CATEGORY</label>
            <select id="postCategorySelect" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-gold-400">
              <option value="portrait">Human Anatomy &amp; Portraits</option>
              <option value="perspective">Architectural Perspective</option>
              <option value="cyber">Cybernetic &amp; Concept Art</option>
              <option value="charcoal">Charcoal &amp; Nature</option>
            </select>
          </div>
          <div>
            <label class="block text-gray-400 mb-1">MEDIUM</label>
            <input type="text" id="postMediumInput" required placeholder="e.g. 4B Graphite on 220 GSM" class="w-full bg-noir-950 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-gold-400">
          </div>
        </div>

        <!-- Caption -->
        <div>
          <label class="block text-gray-400 mb-1">CAPTION / REFLECTION</label>
          <textarea id="postCaptionInput" rows="3" placeholder="Notes on tonal transitions, lighting source, cross-hatching..." class="w-full bg-noir-950 border border-white/15 rounded-xl p-3 text-white focus:outline-none focus:border-gold-400 resize-none font-sans text-xs"></textarea>
        </div>

        <!-- Submit Button -->
        <button type="submit" class="magnetic-btn w-full py-3.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(229,169,60,0.3)]">
          PUBLISH TO STUDIO FEED
        </button>
      </form>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: FULLSCREEN CINEMA LIGHTBOX FOR ARTWORK -->
  <!-- ========================================================================= -->
  <div id="cinemaLightboxModal" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-2xl hidden flex flex-col items-center justify-center p-4">
    <button onclick="closeCinemaLightbox()" class="absolute top-6 right-6 p-3 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors z-50">
      <i data-lucide="x" class="w-6 h-6"></i>
    </button>
    <div class="relative max-w-5xl max-h-[85vh] w-full flex items-center justify-center">
      <img id="lightboxImg" src="" class="max-h-[80vh] max-w-full object-contain rounded-xl shadow-[0_0_60px_rgba(0,0,0,0.9)]">
    </div>
    <div class="mt-4 text-center space-y-1">
      <h4 id="lightboxTitle" class="text-xl font-display font-bold text-white">Artwork Title</h4>
      <p id="lightboxDetails" class="text-xs font-mono text-gold-400">Medium &bull; Date</p>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: HOLOGRAPHIC CREDENTIAL INSPECTION -->
  <!-- ========================================================================= -->
  <div id="certModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-xl hidden flex items-center justify-center p-4">
    <div class="holo-card max-w-lg w-full p-8 rounded-3xl space-y-6 relative">
      <div class="flex items-center justify-between border-b border-white/10 pb-4">
        <h3 id="certModalTitle" class="text-xl font-display font-bold text-white">Credential Details</h3>
        <button onclick="closeCertModal()" class="p-2 text-gray-400 hover:text-white transition-colors">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      <div id="certModalBody" class="space-y-4 text-xs font-mono text-gray-300">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: THEME MOOD SELECTOR -->
  <!-- ========================================================================= -->
  <div id="themeModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-xl hidden flex items-center justify-center p-4">
    <div class="holo-card max-w-md w-full p-6 sm:p-8 rounded-3xl space-y-6 relative">
      <div class="flex items-center justify-between border-b border-white/10 pb-4">
        <h3 class="text-lg font-display font-bold text-white flex items-center space-x-2">
          <i data-lucide="palette" class="w-4 h-4 text-gold-400"></i>
          <span>SELECT CINEMATIC MOOD</span>
        </h3>
        <button onclick="toggleThemeModal()" class="p-2 text-gray-400 hover:text-white transition-colors">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-3 font-mono text-xs">
        <!-- Theme 1 -->
        <button onclick="applyTheme('obsidian')" class="w-full p-4 rounded-2xl bg-noir-900 border border-gold-400/50 hover:border-gold-400 text-left flex items-center justify-between transition-all group">
          <div class="flex items-center space-x-3">
            <span class="w-4 h-4 rounded-full bg-[#E5A93C] shadow-[0_0_8px_#E5A93C]"></span>
            <div>
              <span class="font-display font-bold text-white text-sm block">Obsidian Noir (Default)</span>
              <span class="text-gray-400 text-[11px]">24K Champagne Gold &bull; Deep Charcoal Void</span>
            </div>
          </div>
          <i data-lucide="check" class="w-4 h-4 text-gold-400"></i>
        </button>

        <!-- Theme 2 -->
        <button onclick="applyTheme('aurora')" class="w-full p-4 rounded-2xl bg-noir-900 border border-white/15 hover:border-cyan-400 text-left flex items-center justify-between transition-all group">
          <div class="flex items-center space-x-3">
            <span class="w-4 h-4 rounded-full bg-[#00F0FF] shadow-[0_0_8px_#00F0FF]"></span>
            <div>
              <span class="font-display font-bold text-white text-sm block">Cosmic Aurora</span>
              <span class="text-gray-400 text-[11px]">Electric Cyan &bull; Deep Space Midnight</span>
            </div>
          </div>
        </button>

        <!-- Theme 3 -->
        <button onclick="applyTheme('cyber')" class="w-full p-4 rounded-2xl bg-noir-900 border border-white/15 hover:border-pink-500 text-left flex items-center justify-between transition-all group">
          <div class="flex items-center space-x-3">
            <span class="w-4 h-4 rounded-full bg-[#FF2A6D] shadow-[0_0_8px_#FF2A6D]"></span>
            <div>
              <span class="font-display font-bold text-white text-sm block">Cyberpunk Crimson</span>
              <span class="text-gray-400 text-[11px]">Laser Crimson &bull; Neo-Tokyo Shadow</span>
            </div>
          </div>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: HOLLYWOOD PRODUCTION CREDITS -->
  <!-- ========================================================================= -->
  <div id="creditsModal" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-2xl hidden flex flex-col items-center justify-center p-6 overflow-hidden">
    <button onclick="toggleCreditsModal()" class="absolute top-6 right-6 p-3 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors z-50">
      <i data-lucide="x" class="w-6 h-6"></i>
    </button>
    
    <div class="h-[70vh] w-full max-w-lg overflow-hidden relative text-center">
      <div class="animate-credits font-mono space-y-8 text-sm text-gray-300">
        <div class="space-y-2">
          <h2 class="text-2xl font-display font-bold text-gold-400 uppercase tracking-widest">SHREYAS B J</h2>
          <p class="text-xs text-gray-400">A CINEMATIC PORTFOLIO PRODUCTION</p>
        </div>

        <div class="space-y-1">
          <p class="text-xs text-gray-500 uppercase tracking-widest">EXECUTIVE PRODUCER &amp; LEAD ENGINEER</p>
          <p class="text-base font-bold text-white">Shreyas B J</p>
        </div>

        <div class="space-y-1">
          <p class="text-xs text-gray-500 uppercase tracking-widest">AI &amp; MACHINE LEARNING SYSTEMS</p>
          <p class="text-white">Tata Consultancy Services (TCS)</p>
          <p class="text-xs text-gray-400">Databricks &bull; Claude &bull; Gemini</p>
        </div>

        <div class="space-y-1">
          <p class="text-xs text-gray-500 uppercase tracking-widest">HARDWARE FAILURE ANALYSIS LAB</p>
          <p class="text-white">Foxconn (Hon Hai Technology Group)</p>
          <p class="text-xs text-gray-400">Sriperumbudur SMT Production Line</p>
        </div>

        <div class="space-y-1">
          <p class="text-xs text-gray-500 uppercase tracking-widest">ACADEMIC FOUNDATION</p>
          <p class="text-white">Nagarjuna College of Engineering &amp; Technology (NCET)</p>
          <p class="text-xs text-gold-400">B.E. Electronics &amp; Communication &bull; 8.89 CGPA</p>
        </div>

        <div class="space-y-1">
          <p class="text-xs text-gray-500 uppercase tracking-widest">OBSERVATIONAL SKETCH STUDIO</p>
          <p class="text-white">Fine Art Draughtsmanship &bull; Chikkamagaluru</p>
        </div>

        <div class="pt-8 text-xs text-gray-500">
          <p>RENDERED WITH THREE.JS &bull; TAILWIND &bull; LUCIDE</p>
          <p class="text-gold-400 mt-2 font-display font-bold">THANK YOU FOR EXPERIENCING</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toastMessage" class="fixed bottom-24 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 pointer-events-none">
    <div class="bg-noir-900/95 backdrop-blur-xl border border-gold-400/60 px-5 py-3 rounded-2xl shadow-[0_10px_30px_rgba(0,0,0,0.8)] flex items-center space-x-3 text-xs font-mono text-white">
      <span class="w-2 h-2 rounded-full bg-gold-400 animate-ping"></span>
      <span id="toastText">Action completed successfully.</span>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT MASTER SYSTEM -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // 1. LUCIDE ICONS & SYSTEM CLOCK INITIALIZATION
    // -------------------------------------------------------------------------
    lucide.createIcons();

    function updateLiveClock() {
      const el = document.getElementById('liveClock');
      if (!el) return;
      const now = new Date();
      const ist = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
      }).format(now);
      el.textContent = `BANGALORE IST ${ist}`;
    }
    setInterval(updateLiveClock, 1000);
    updateLiveClock();

    // -------------------------------------------------------------------------
    // 2. FLUID MAGNETIC CURSOR
    // -------------------------------------------------------------------------
    const cursorDot = document.getElementById('cursorDot');
    const cursorHalo = document.getElementById('cursorHalo');
    let mousePos = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    let haloPos = { x: mousePos.x, y: mousePos.y };

    window.addEventListener('mousemove', (e) => {
      mousePos.x = e.clientX;
      mousePos.y = e.clientY;
      if (cursorDot) {
        cursorDot.style.left = mousePos.x + 'px';
        cursorDot.style.top = mousePos.y + 'px';
      }
    });

    function animateCursor() {
      haloPos.x += (mousePos.x - haloPos.x) * 0.18;
      haloPos.y += (mousePos.y - haloPos.y) * 0.18;
      if (cursorHalo) {
        cursorHalo.style.left = haloPos.x + 'px';
        cursorHalo.style.top = haloPos.y + 'px';
      }
      requestAnimationFrame(animateCursor);
    }
    animateCursor();

    document.querySelectorAll('a, button, input, .real-tilt, .cursor-pointer').forEach(el => {
      el.addEventListener('mouseenter', () => cursorHalo && cursorHalo.classList.add('cursor-hover'));
      el.addEventListener('mouseleave', () => cursorHalo && cursorHalo.classList.remove('cursor-hover'));
    });

    // -------------------------------------------------------------------------
    // 3. THREE.JS 3D INTERACTIVE COSMIC CONSTELLATION
    // -------------------------------------------------------------------------
    (function initThreeCosmos() {
      const canvas = document.getElementById('threeCanvas');
      if (!canvas || typeof THREE === 'undefined') return;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 45;

      const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // 3D Particles
      const particleCount = window.innerWidth < 768 ? 180 : 420;
      const geometry = new THREE.BufferGeometry();
      const positions = new Float32Array(particleCount * 3);
      const colors = new Float32Array(particleCount * 3);

      const color1 = new THREE.Color(0xE5A93C); // Gold
      const color2 = new THREE.Color(0x38BDF8); // Cyan

      for (let i = 0; i < particleCount; i++) {
        const radius = 25 + Math.random() * 20;
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.acos((Math.random() * 2) - 1);

        positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
        positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
        positions[i * 3 + 2] = radius * Math.cos(phi);

        const mixedColor = color1.clone().lerp(color2, Math.random());
        colors[i * 3] = mixedColor.r;
        colors[i * 3 + 1] = mixedColor.g;
        colors[i * 3 + 2] = mixedColor.b;
      }

      geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const material = new THREE.PointsMaterial({
        size: 1.4,
        vertexColors: true,
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending
      });

      const particleSystem = new THREE.Points(geometry, material);
      scene.add(particleSystem);

      // Rotating Neural Wireframe Rings
      const ringGeo = new THREE.TorusGeometry(26, 0.15, 8, 80);
      const ringMat = new THREE.MeshBasicMaterial({ color: 0xE5A93C, transparent: true, opacity: 0.18, wireframe: true });
      const ring1 = new THREE.Mesh(ringGeo, ringMat);
      scene.add(ring1);

      let mouseX = 0, mouseY = 0;
      window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX - window.innerWidth / 2) * 0.0008;
        mouseY = (e.clientY - window.innerHeight / 2) * 0.0008;
      });

      window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
      });

      function animate() {
        requestAnimationFrame(animate);
        particleSystem.rotation.y += 0.0012 + mouseX * 0.1;
        particleSystem.rotation.x += 0.0006 + mouseY * 0.1;

        ring1.rotation.x += 0.0018;
        ring1.rotation.y += 0.0022;

        renderer.render(scene, camera);
      }
      animate();
    })();

    // -------------------------------------------------------------------------
    // 4. ROLE SCRAMBLER (HERO TITLE)
    // -------------------------------------------------------------------------
    const roles = [
      'AI / ML ENGINEER AT TCS',
      'COMPUTER VISION SPECIALIST',
      'HARDWARE FAILURE ANALYST',
      'OBSERVATIONAL FINE ART DRAUGHTSMAN',
      'DATABRICKS & CLOUD CERTIFIED'
    ];
    let roleIndex = 0;
    const roleEl = document.getElementById('roleScrambler');
    const glyphs = '!<>-_\\\\/[]{}—=+*^?#________';

    function scrambleRole(targetText) {
      let frame = 0;
      const totalFrames = 25;
      const initialText = roleEl.textContent;
      
      const interval = setInterval(() => {
        frame++;
        let output = '';
        for (let i = 0; i < targetText.length; i++) {
          if (frame >= totalFrames * (i / targetText.length)) {
            output += targetText[i];
          } else {
            output += glyphs[Math.floor(Math.random() * glyphs.length)];
          }
        }
        roleEl.textContent = output;
        if (frame >= totalFrames) {
          clearInterval(interval);
        }
      }, 35);
    }

    setInterval(() => {
      roleIndex = (roleIndex + 1) % roles.length;
      scrambleRole(roles[roleIndex]);
    }, 4000);

    // -------------------------------------------------------------------------
    // 5. ADAPTIVE PROFILE PHOTO CONTROLLER
    // -------------------------------------------------------------------------
    const profilePhotoInput = document.getElementById('profilePhotoInput');
    const profilePhotoImg = document.getElementById('profilePhotoImg');
    const resetProfilePhotoBtn = document.getElementById('resetProfilePhotoBtn');
    const aspectRatioTag = document.getElementById('aspectRatioTag');
    const DEFAULT_PROFILE_SRC = './assets/profile-avatar.svg';

    function updateAspectRatioBadge(w, h) {
      if (!aspectRatioTag) return;
      const ratio = (w / h).toFixed(2);
      if (ratio > 1.15) {
        aspectRatioTag.textContent = `LANDSCAPE (${ratio}:1)`;
      } else if (ratio < 0.85) {
        aspectRatioTag.textContent = `PORTRAIT (1:${(h/w).toFixed(1)})`;
      } else {
        aspectRatioTag.textContent = `SQUARE (1:1)`;
      }
    }

    // Auto-measure aspect ratio on image load
    if (profilePhotoImg) {
      profilePhotoImg.onload = function() {
        updateAspectRatioBadge(this.naturalWidth || 400, this.naturalHeight || 400);
      };
    }

    const savedProfile = localStorage.getItem('shreyas_uploaded_profile_photo');
    if (savedProfile && profilePhotoImg) {
      profilePhotoImg.src = savedProfile;
    }

    if (profilePhotoInput) {
      profilePhotoInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (event) => {
          const dataUrl = event.target.result;
          profilePhotoImg.src = dataUrl;
          try {
            localStorage.setItem('shreyas_uploaded_profile_photo', dataUrl);
          } catch(err) {
            console.warn('Image too large for localStorage quota.');
          }
          showToast('Profile photo updated successfully!');
        };
        reader.readAsDataURL(file);
      });
    }

    if (resetProfilePhotoBtn) {
      resetProfilePhotoBtn.addEventListener('click', () => {
        localStorage.removeItem('shreyas_uploaded_profile_photo');
        profilePhotoImg.src = DEFAULT_PROFILE_SRC;
        showToast('Reset to default portrait.');
      });
    }

    // -------------------------------------------------------------------------
    // 6. ODYSSEY EXPERIENCE DOSSIER ENGINE
    // -------------------------------------------------------------------------
    const odysseyData = [
      {
        company: 'Tata Consultancy Services (TCS)',
        role: 'AI / ML Engineer',
        period: '2024 — Present',
        location: 'Bangalore, India',
        summary: 'Developing enterprise-grade generative intelligence pipelines, computer vision inference backends, and distributed data orchestrations using Databricks and PyTorch.',
        achievements: [
          'Engineered low-latency LLM agent pipelines using LangChain and Hugging Face Transformers.',
          'Built automated data validation pipelines handling complex multi-modal sensor streams.',
          'Implemented Databricks MLflow model governance and experiment tracking for compliant deployment.'
        ],
        tech: ['Python', 'PyTorch', 'Databricks', 'LangChain', 'Docker', 'MLflow']
      },
      {
        company: 'Foxconn (Hon Hai Technology Group)',
        role: 'Graduate Apprentice &bull; Hardware Failure Analysis',
        period: 'October 2024 — December 2024',
        location: 'Sriperumbudur, India',
        summary: 'Conducted forensic hardware failure analysis on high-volume SMT manufacturing lines, tracing electrical schematics and diagnosing microscopic circuit defects.',
        achievements: [
          'Investigated printed circuit board (PCB) failures using In-Circuit Testing (ICT) and Functional Testing (FCT).',
          'Diagnosed micro solder bridges, component drift, and IC latch-ups to uphold 99.8% line quality.',
          'Correlated physical defect observations with automated optical inspection telemetry.'
        ],
        tech: ['Failure Analysis', 'In-Circuit Testing', 'Oscilloscopes', 'SMT Diagnostics', 'Schematic Tracing']
      },
      {
        company: 'Nagarjuna College of Engineering & Technology (NCET)',
        role: 'B.E. in Electronics &amp; Communication Engineering (VTU)',
        period: '2021 — 2025',
        location: 'Bangalore, India &bull; CGPA: 8.89 / 10.0',
        summary: 'Comprehensive four-year degree emphasizing signal processing, microprocessors, embedded architectures, and applied deep learning systems.',
        achievements: [
          'Graduated with honors ranking in the top percentiles with an 8.89 CGPA.',
          'Capstone: Autonomous Multi-Sensor Rover with real-time obstacle avoidance and edge compute.',
          'Active researcher in embedded vision, microcontrollers (STM32, ESP32), and sensor fusion.'
        ],
        tech: ['Signal Processing', 'Microprocessors', 'Embedded C', 'Control Systems', 'Deep Learning']
      },
      {
        company: 'Skill Craft Technology',
        role: 'Machine Learning Intern',
        period: 'May 2024 — June 2024',
        location: 'Remote',
        summary: 'Focused on supervised machine learning architectures, predictive modeling, and feature engineering across structured tabular datasets.',
        achievements: [
          'Constructed automated exploratory data analysis (EDA) pipelines with Pandas & Seaborn.',
          'Trained ensemble classification models (Random Forest, XGBoost) optimizing cross-validation accuracy.',
          'Delivered clean, modular model deployment scripts with REST API endpoints.'
        ],
        tech: ['Scikit-Learn', 'Pandas', 'XGBoost', 'Feature Engineering', 'REST APIs']
      }
    ];

    function switchOdysseyMilestone(index) {
      document.querySelectorAll('.odyssey-tab-btn').forEach((btn, i) => {
        if (i === index) {
          btn.classList.add('border-gold-400', 'bg-noir-850');
          btn.classList.remove('border-white/10');
        } else {
          btn.classList.remove('border-gold-400', 'bg-noir-850');
          btn.classList.add('border-white/10');
        }
      });

      const d = odysseyData[index];
      const container = document.getElementById('odysseyDossier');
      if (!container) return;

      container.innerHTML = `
        <div class="space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/10 pb-4">
            <div>
              <span class="text-xs font-mono text-gold-400">${d.period} &bull; ${d.location}</span>
              <h3 class="text-2xl font-display font-bold text-white">${d.company}</h3>
              <p class="text-sm font-mono text-cyan-300">${d.role}</p>
            </div>
            <span class="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-gray-300 self-start sm:self-auto">DOSSIER #${index + 1}</span>
          </div>

          <p class="text-sm text-gray-300 font-sans leading-relaxed">${d.summary}</p>

          <div class="space-y-2 pt-2">
            <span class="text-xs font-mono text-gray-400 block font-bold uppercase">KEY OPERATIONAL IMPACT:</span>
            <ul class="space-y-1.5 text-xs text-gray-300">
              ${d.achievements.map(a => `<li class="flex items-start space-x-2"><span class="text-gold-400 font-bold">&bull;</span><span>${a}</span></li>`).join('')}
            </ul>
          </div>
        </div>

        <div class="pt-6 border-t border-white/10 flex flex-wrap gap-2">
          ${d.tech.map(t => `<span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-[11px] font-mono text-gray-300">${t}</span>`).join('')}
        </div>
      `;
      lucide.createIcons();
    }
    switchOdysseyMilestone(0);

    // -------------------------------------------------------------------------
    // 7. FILTERABLE SKILLS GRID ENGINE
    // -------------------------------------------------------------------------
    const skillsData = [
      { name: 'PyTorch & TensorFlow', cat: 'aiml', level: '95%', icon: 'flame', desc: 'Custom CNN, Transformer & Vision backends' },
      { name: 'Computer Vision & YOLO', cat: 'aiml', level: '94%', icon: 'eye', desc: 'Defect detection, bounding boxes, OpenCV' },
      { name: 'LangChain & Agentic RAG', cat: 'aiml', level: '90%', icon: 'cpu', desc: 'Multi-agent orchestration, vector embeddings' },
      { name: 'Databricks & Spark', cat: 'cloud', level: '88%', icon: 'database', desc: 'Distributed ML, Lakehouse architectures' },
      { name: 'Docker & Kubernetes', cat: 'cloud', level: '85%', icon: 'box', desc: 'Containerized model microservices' },
      { name: 'Hardware Failure Analysis', cat: 'hardware', level: '92%', icon: 'activity', desc: 'ICT, FCT, SMT micro-defect root-cause' },
      { name: 'Microcontrollers & Embedded C', cat: 'hardware', level: '89%', icon: 'circuit-board', desc: 'STM32, ESP32, sensor fusion, UART/SPI' },
      { name: 'Observational Draughtsmanship', cat: 'creative', level: '96%', icon: 'pen-tool', desc: 'Charcoal realism, human anatomy, perspective' },
      { name: 'Python & C++ Algorithms', cat: 'aiml', level: '94%', icon: 'terminal', desc: 'Low-latency algorithmic problem solving' }
    ];

    function renderSkillsGrid(filter = 'all') {
      const container = document.getElementById('skillsGrid');
      if (!container) return;

      const filtered = filter === 'all' ? skillsData : skillsData.filter(s => s.cat === filter);
      container.innerHTML = filtered.map(s => `
        <div class="holo-card p-5 rounded-2xl space-y-3 real-tilt">
          <div class="flex items-center justify-between">
            <span class="font-display font-bold text-white text-sm">${s.name}</span>
            <span class="text-xs font-mono text-gold-400 font-bold">${s.level}</span>
          </div>
          <!-- Animated Progress Meter -->
          <div class="w-full h-1.5 bg-noir-950 rounded-full overflow-hidden border border-white/10">
            <div class="h-full bg-gradient-to-r from-gold-500 to-cyan-400 rounded-full transition-all duration-700" style="width: ${s.level}"></div>
          </div>
          <p class="text-[11px] font-mono text-gray-400">${s.desc}</p>
        </div>
      `).join('');
      initRealWorldTilt();
    }
    renderSkillsGrid('all');

    function filterSkills(cat) {
      document.querySelectorAll('.skill-filter-btn').forEach(btn => {
        btn.classList.remove('bg-gold-500', 'text-noir-950', 'font-bold');
        btn.classList.add('bg-white/5', 'text-gray-300');
      });
      event.target.classList.add('bg-gold-500', 'text-noir-950', 'font-bold');
      event.target.classList.remove('bg-white/5', 'text-gray-300');
      renderSkillsGrid(cat);
    }

    // -------------------------------------------------------------------------
    // 8. CERTIFICATION HOLOGRAPHIC MODAL
    // -------------------------------------------------------------------------
    const certDetails = {
      databricks: {
        title: 'Databricks Certified Associate — Machine Learning',
        issuer: 'Databricks Inc.',
        date: '2024',
        skills: 'Spark MLlib, Distributed Feature Engineering, Model Governance, MLflow, Hyperparameter Tuning',
        desc: 'Validates production proficiency in designing, training, tracking, and deploying machine learning models at scale over Databricks Lakehouse infrastructure.'
      },
      claude: {
        title: 'Anthropic Claude Certified Prompt Engineer',
        issuer: 'Anthropic AI Certification Program',
        date: '2024',
        skills: 'Chain-of-Thought Reasoning, XML-tagged Ingestion, Tool Calling, Multi-turn Agents, Safeguards',
        desc: 'Accreditation covering structured reasoning, agentic workflow orchestration, and high-fidelity output steering on Claude 3 and 3.5 Sonnet.'
      },
      gemini: {
        title: 'Google Cloud Gemini AI Certified',
        issuer: 'Google Cloud Skills Boost',
        date: '2024',
        skills: 'Multimodal Vision Models, Vertex AI Ingestion, Grounded Embeddings, Vector Search',
        desc: 'Mastery in building multimodal generative systems utilizing Google Cloud Gemini 1.5 Pro and Flash with sub-second inference.'
      },
      nptel: {
        title: 'NPTEL IIT Madras — Deep Learning & Microprocessors',
        issuer: 'IIT Madras & Ministry of Education, India',
        date: '2023',
        skills: 'Convolutional Networks, Recurrent Architectures, Loss Landscapes, Microprocessor 8086/ARM',
        desc: 'Rigorous national academic accreditation covering fundamental mathematical proofs of backpropagation, tensor operations, and embedded hardware interfaces.'
      },
      nxtwave: {
        title: 'NXT Wave Full Stack Python Specialist',
        issuer: 'NXT Wave CCBP Academy',
        date: '2023',
        skills: 'Python Core, Relational SQL, SQLite, REST Architecture, JavaScript Full Stack',
        desc: 'Extensive software engineering certification covering relational database design, backend services, and algorithmic complexity.'
      },
      techhub: {
        title: 'Technical Hub Advanced Embedded Systems & IoT',
        issuer: 'Technical Hub Pvt Ltd',
        date: '2023',
        skills: 'STM32, ESP32, Embedded C, Sensor Protocol Standards (I2C, SPI, UART), Edge Compute',
        desc: 'Hands-on hardware certification involving firmware writing, hardware timer configurations, and real-time sensor data streaming.'
      }
    };

    function openCertModal(key) {
      const c = certDetails[key];
      if (!c) return;
      document.getElementById('certModalTitle').textContent = c.title;
      document.getElementById('certModalBody').innerHTML = `
        <div class="space-y-3">
          <div class="p-4 rounded-xl bg-noir-950 border border-white/10 space-y-1">
            <div class="flex justify-between text-gray-400"><span>ISSUER:</span><span class="text-white font-bold">${c.issuer}</span></div>
            <div class="flex justify-between text-gray-400"><span>YEAR ACCREDITED:</span><span class="text-gold-400 font-bold">${c.date}</span></div>
            <div class="flex justify-between text-gray-400"><span>VERIFICATION:</span><span class="text-emerald-400 font-bold">&check; AUTHENTICATED</span></div>
          </div>
          <p class="text-sm font-sans text-gray-200 leading-relaxed">${c.desc}</p>
          <div class="pt-2">
            <span class="text-gold-400 font-bold block mb-1">CORE COMPETENCIES:</span>
            <p class="text-xs text-gray-400">${c.skills}</p>
          </div>
        </div>
      `;
      document.getElementById('certModal').classList.remove('hidden');
    }

    function closeCertModal() {
      document.getElementById('certModal').classList.add('hidden');
    }

    // -------------------------------------------------------------------------
    // 9. INVENTION 01: OMNITRAVEL SIMULATOR ENGINE
    // -------------------------------------------------------------------------
    function setTravelPreset(val) {
      document.getElementById('travelInput').value = val;
    }

    function executeTravelSimulation() {
      const input = document.getElementById('travelInput').value.trim();
      const output = document.getElementById('travelTerminalOutput');
      if (!input) return;

      output.innerHTML = `
        <p class="text-gold-400">&gt; Ingesting prompt query: "${input}"</p>
        <p class="text-gray-400">&gt; Initializing Master Orchestrator Agent...</p>
      `;

      setTimeout(() => {
        output.innerHTML += `
          <p class="text-cyan-400">&gt; [RAG Agent] Querying vector database (ChromaDB) for historical top-rated routes...</p>
          <p class="text-cyan-400">&gt; [RAG Agent] 3 high-confidence context documents retrieved (Cosine Sim: 0.941).</p>
        `;
      }, 600);

      setTimeout(() => {
        output.innerHTML += `
          <p class="text-emerald-400">&gt; [Weather Telemetry Agent] Grounding local conditions: Temp 18°C, Clear skies, Precipitation 8%.</p>
          <p class="text-purple-400">&gt; [Budget Synthesizer] Cost boundary verified: Estimated cost within defined constraints.</p>
        `;
      }, 1200);

      setTimeout(() => {
        output.innerHTML += `
          <div class="p-3 mt-2 rounded bg-noir-950 border border-gold-400/40 text-gray-200 font-sans space-y-1">
            <span class="text-xs font-mono text-gold-400 font-bold uppercase">&check; SYNTHESIZED CUSTOM ITINERARY READY:</span>
            <p class="text-xs text-gray-300 leading-relaxed">&bull; Day 1: Arrive &bull; Cultural immersion, local market, sunset vista.<br>&bull; Day 2: Architectural study &bull; Morning photography, museum archives.<br>&bull; Day 3: Scenic trail &bull; Local culinary journey and artisanal workshop.<br>&bull; Day 4: Departure wrap-up &bull; Transit efficiency: 98.4%.</p>
          </div>
        `;
        output.scrollTop = output.scrollHeight;
      }, 1800);
    }

    // -------------------------------------------------------------------------
    // 10. INVENTION 02: INTERACTIVE AOI BEFORE/AFTER SLIDER
    // -------------------------------------------------------------------------
    const aoiContainer = document.getElementById('aoiSliderContainer');
    const aoiAfterLayer = document.getElementById('aoiAfterLayer');
    const aoiHandle = document.getElementById('aoiSliderHandle');
    let isSlidingAoi = false;

    function updateAoiSlider(clientX) {
      const rect = aoiContainer.getBoundingClientRect();
      let pos = (clientX - rect.left) / rect.width;
      pos = Math.max(0.05, Math.min(0.95, pos));
      const pct = (pos * 100).toFixed(1);

      aoiAfterLayer.style.clipPath = `inset(0 0 0 ${pct}%)`;
      aoiHandle.style.left = `${pct}%`;
    }

    if (aoiContainer) {
      aoiContainer.addEventListener('mousedown', (e) => {
        isSlidingAoi = true;
        updateAoiSlider(e.clientX);
      });
      window.addEventListener('mousemove', (e) => {
        if (!isSlidingAoi) return;
        updateAoiSlider(e.clientX);
      });
      window.addEventListener('mouseup', () => {
        isSlidingAoi = false;
      });

      // Touch support
      aoiContainer.addEventListener('touchstart', (e) => {
        isSlidingAoi = true;
        updateAoiSlider(e.touches[0].clientX);
      });
      window.addEventListener('touchmove', (e) => {
        if (!isSlidingAoi) return;
        updateAoiSlider(e.touches[0].clientX);
      });
      window.addEventListener('touchend', () => {
        isSlidingAoi = false;
      });
    }

    // -------------------------------------------------------------------------
    // 11. INVENTION 03: SIMPLE LIDAR RADAR SWEEP ANIMATION
    // -------------------------------------------------------------------------
    (function initLidarRadar() {
      const canvas = document.getElementById('lidarRadarCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const size = canvas.width;
      const center = size / 2;
      const radius = center - 15;
      let angle = 0;

      // Real-world simulated LIDAR obstacle blips (distance & angle)
      const blips = [
        { dist: 0.35, angle: 0.8, ping: 0 },
        { dist: 0.65, angle: 2.3, ping: 0 },
        { dist: 0.82, angle: 4.1, ping: 0 },
        { dist: 0.50, angle: 5.4, ping: 0 }
      ];

      function renderRadar() {
        ctx.clearRect(0, 0, size, size);

        // Concentric distance range rings
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        [0.25, 0.5, 0.75, 1.0].forEach(r => {
          ctx.beginPath();
          ctx.arc(center, center, radius * r, 0, Math.PI * 2);
          ctx.stroke();
        });

        // Crosshairs
        ctx.beginPath();
        ctx.moveTo(center, 15); ctx.lineTo(center, size - 15);
        ctx.moveTo(15, center); ctx.lineTo(size - 15, center);
        ctx.stroke();

        // Radar Sweep Beam (Gradient arc)
        angle += 0.035;
        if (angle > Math.PI * 2) angle -= Math.PI * 2;

        const sweepGradient = ctx.createConicGradient(angle - Math.PI / 4, center, center);
        sweepGradient.addColorStop(0, 'rgba(16, 185, 129, 0)');
        sweepGradient.addColorStop(0.12, 'rgba(16, 185, 129, 0.35)');
        sweepGradient.addColorStop(0.13, 'rgba(16, 185, 129, 0.9)');
        sweepGradient.addColorStop(0.14, 'rgba(16, 185, 129, 0)');

        ctx.fillStyle = sweepGradient;
        ctx.beginPath();
        ctx.arc(center, center, radius, 0, Math.PI * 2);
        ctx.fill();

        // Crisp Sweep Line
        const lx = center + Math.cos(angle) * radius;
        const ly = center + Math.sin(angle) * radius;
        ctx.strokeStyle = '#10B981';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(center, center);
        ctx.lineTo(lx, ly);
        ctx.stroke();

        // Pulsing Target Blips
        blips.forEach(b => {
          const bx = center + Math.cos(b.angle) * (radius * b.dist);
          const by = center + Math.sin(b.angle) * (radius * b.dist);

          const diff = Math.abs(angle - b.angle);
          if (diff < 0.05 || Math.abs(diff - Math.PI * 2) < 0.05) {
            b.ping = 1.0;
          }

          if (b.ping > 0.01) {
            ctx.fillStyle = 'rgba(245, 197, 99, ' + b.ping + ')';
            ctx.beginPath();
            ctx.arc(bx, by, 3.5, 0, Math.PI * 2);
            ctx.fill();

            // Expanding sonar ring
            ctx.strokeStyle = 'rgba(245, 197, 99, ' + (b.ping * 0.5) + ')';
            ctx.beginPath();
            ctx.arc(bx, by, 8 * (1.2 - b.ping), 0, Math.PI * 2);
            ctx.stroke();

            b.ping *= 0.96;
          }
        });

        // Azimuth Telemetry
        const azEl = document.getElementById('radarAzimuth');
        if (azEl) {
          const deg = ((angle * 180 / Math.PI) % 360).toFixed(1);
          azEl.textContent = deg + '°';
        }

        requestAnimationFrame(renderRadar);
      }
      renderRadar();
    })();

    // -------------------------------------------------------------------------
    // 12. INSTAGRAM SKETCH FEED STUDIO ENGINE
    // -------------------------------------------------------------------------
    const POSTS_KEY = 'shreyas_sketch_feed_v2';
    let currentCategoryFilter = 'all';
    let selectedPostFilter = 'none';
    let draftImageData = null;

    function getStoredPosts() {
      const raw = localStorage.getItem(POSTS_KEY);
      if (raw) {
        try { return JSON.parse(raw); } catch (e) { return []; }
      }
      return null;
    }

    function saveStoredPosts(posts) {
      try {
        localStorage.setItem(POSTS_KEY, JSON.stringify(posts));
      } catch (e) {
        showToast('Storage quota exceeded. Please upload a smaller image file.');
      }
    }

    function renderFeed() {
      const container = document.getElementById('postsFeedContainer');
      const emptyState = document.getElementById('emptyFeedState');
      const posts = getStoredPosts();

      if (!posts || posts.length === 0) {
        container.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }

      emptyState.classList.add('hidden');

      const filtered = currentCategoryFilter === 'all' 
        ? posts 
        : posts.filter(p => p.category === currentCategoryFilter);

      if (filtered.length === 0) {
        container.innerHTML = `<p class="col-span-2 text-center text-gray-500 py-10 font-mono text-xs">No sketches match the selected category.</p>`;
        return;
      }

      container.innerHTML = filtered.map(post => `
        <article class="real-tilt holo-card rounded-3xl overflow-hidden shadow-2xl transition-all reveal-item" id="post-${post.id}">
          
          <!-- Post Header -->
          <div class="px-5 py-4 border-b border-white/10 flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <img src="${profilePhotoImg ? profilePhotoImg.src : './assets/profile-avatar.svg'}" class="w-9 h-9 rounded-full object-cover border border-gold-400/50 p-0.5">
              <div>
                <div class="flex items-center space-x-2">
                  <span class="font-display font-bold text-white text-sm">Shreyas B J</span>
                  <span class="w-1.5 h-1.5 rounded-full bg-gold-400"></span>
                  <span class="text-[11px] font-mono text-gold-400">Artist</span>
                </div>
                <span class="text-[11px] font-mono text-gray-400">@shreyas.sketches &bull; ${post.date || 'Chikkamagaluru Studio'}</span>
              </div>
            </div>

            <button onclick="deletePost('${post.id}')" class="p-2 text-gray-500 hover:text-red-400 transition-colors" title="Delete post">
              <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
          </div>

          <!-- Post Media Container with Double-Tap to Like & Click for Lightbox -->
          <div class="relative bg-noir-950 flex items-center justify-center overflow-hidden group select-none cursor-pointer" 
               ondblclick="doubleTapLikePost(event, '${post.id}')" 
               onclick="handleMediaClick(event, '${post.id}')">
            
            <img src="${post.image}" alt="${post.title}" class="max-h-[580px] w-auto h-auto max-w-full object-contain mx-auto block group-hover:scale-[1.01] transition-transform duration-500 ${getFilterCssClass(post.filter)}">
            
            <!-- Animated Pop Heart for Double Tap -->
            <div id="heartPop-${post.id}" class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none hidden">
              <i data-lucide="heart" class="w-24 h-24 text-heart fill-heart filter drop-shadow-[0_0_30px_#FF2A6D]"></i>
            </div>

            <!-- Hover Hint -->
            <div class="absolute bottom-3 left-3 px-2 py-0.5 rounded bg-black/60 text-[10px] font-mono text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
              Double-tap: ❤️ | Click: Cinema Lightbox
            </div>
          </div>

          <!-- Post Actions Bar -->
          <div class="p-5 space-y-3 font-mono">
            <div class="flex items-center justify-between text-gray-300">
              <div class="flex items-center space-x-4">
                <button onclick="toggleLikePost(event, '${post.id}')" class="magnetic-btn flex items-center space-x-1.5 group focus:outline-none">
                  <i data-lucide="heart" class="w-5 h-5 transition-transform group-hover:scale-125 ${post.isLiked ? 'text-heart fill-heart' : 'hover:text-heart'}"></i>
                  <span class="font-bold text-xs ${post.isLiked ? 'text-heart' : 'text-white'}">${post.likes}</span>
                </button>
                <button onclick="toggleCommentsDrawer('${post.id}')" class="magnetic-btn hover:text-white transition-colors flex items-center space-x-1">
                  <i data-lucide="message-circle" class="w-5 h-5"></i>
                  <span class="text-xs text-gray-400">${(post.comments || []).length}</span>
                </button>
                <button onclick="copyPostLink('${post.id}')" class="magnetic-btn hover:text-white transition-colors">
                  <i data-lucide="share-2" class="w-5 h-5"></i>
                </button>
              </div>
              <span class="text-[11px] text-gray-400 bg-white/5 px-2.5 py-1 rounded-md border border-white/10">${post.medium}</span>
            </div>

            <!-- Post Caption & Reflections -->
            <div class="text-xs space-y-1 pt-1 font-sans">
              <p class="text-white font-medium">
                <span class="font-bold font-display mr-1.5">shreyas.sketches</span>
                ${post.title}
              </p>
              <p class="text-gray-300 leading-relaxed">${post.caption}</p>
            </div>

            <!-- Comments Drawer -->
            <div id="commentsDrawer-${post.id}" class="hidden pt-3 border-t border-white/10 space-y-2">
              <div id="commentsList-${post.id}" class="space-y-1.5 max-h-32 overflow-y-auto text-xs">
                ${(post.comments || []).map(c => `
                  <div class="bg-noir-950 p-2 rounded-lg border border-white/5">
                    <span class="font-bold text-gold-400 mr-1.5">${c.user}:</span>
                    <span class="text-gray-300">${c.text}</span>
                  </div>
                `).join('')}
              </div>

              <!-- Add Comment Input -->
              <div class="flex items-center space-x-2 pt-1">
                <input type="text" id="commentInput-${post.id}" placeholder="Leave a reflection..." class="flex-1 bg-noir-950 border border-white/15 rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-gold-400">
                <button onclick="submitComment('${post.id}')" class="px-3 py-1.5 rounded-lg bg-gold-500 hover:bg-gold-400 text-noir-950 font-bold text-xs uppercase">
                  POST
                </button>
              </div>
            </div>

          </div>
        </article>
      `).join('');

      lucide.createIcons();
      initRealWorldTilt();
      initMagneticButtons();
    }

    function getFilterCssClass(filt) {
      if (filt === 'charcoal') return 'contrast-125 grayscale brightness-95';
      if (filt === 'sepia') return 'sepia-[0.35] contrast-105';
      if (filt === 'cyber') return 'contrast-125 hue-rotate-15';
      return '';
    }

    function toggleLikePost(e, postId) {
      const posts = getStoredPosts();
      if (!posts) return;
      const target = posts.find(p => p.id === postId);
      if (target) {
        target.isLiked = !target.isLiked;
        target.likes = target.isLiked ? target.likes + 1 : Math.max(0, target.likes - 1);
        saveStoredPosts(posts);
        renderFeed();
        if (target.isLiked) {
          triggerGlobalLikeCount(e);
        }
      }
    }

    function doubleTapLikePost(e, postId) {
      const heartPop = document.getElementById('heartPop-' + postId);
      if (heartPop) {
        heartPop.classList.remove('hidden');
        heartPop.classList.remove('pop-heart-anim');
        void heartPop.offsetWidth;
        heartPop.classList.add('pop-heart-anim');
        setTimeout(() => heartPop.classList.add('hidden'), 850);
      }

      firePhysicalHeartBurst(e.clientX, e.clientY);

      const posts = getStoredPosts();
      if (!posts) return;
      const target = posts.find(p => p.id === postId);
      if (target && !target.isLiked) {
        target.isLiked = true;
        target.likes += 1;
        saveStoredPosts(posts);
        renderFeed();
        triggerGlobalLikeCount(e);
      }
    }

    function handleMediaClick(e, postId) {
      // Don't trigger lightbox if user just double tapped
      if (e.detail === 2) return;
      const posts = getStoredPosts();
      if (!posts) return;
      const p = posts.find(x => x.id === postId);
      if (!p) return;

      document.getElementById('lightboxImg').src = p.image;
      document.getElementById('lightboxTitle').textContent = p.title;
      document.getElementById('lightboxDetails').textContent = `${p.medium} • ${p.date || 'Chikkamagaluru Studio'}`;
      document.getElementById('cinemaLightboxModal').classList.remove('hidden');
    }

    function closeCinemaLightbox() {
      document.getElementById('cinemaLightboxModal').classList.add('hidden');
    }

    function toggleCommentsDrawer(postId) {
      const el = document.getElementById(`commentsDrawer-${postId}`);
      if (el) el.classList.toggle('hidden');
    }

    function submitComment(postId) {
      const input = document.getElementById(`commentInput-${postId}`);
      const val = input.value.trim();
      if (!val) return;

      const posts = getStoredPosts();
      const target = posts.find(p => p.id === postId);
      if (target) {
        if (!target.comments) target.comments = [];
        target.comments.push({ user: 'Visitor', text: val });
        saveStoredPosts(posts);
        renderFeed();
        showToast('Comment recorded. Thank you for your critique!');
      }
    }

    function copyPostLink(postId) {
      navigator.clipboard.writeText(`${window.location.origin}${window.location.pathname}#post-${postId}`);
      showToast('Artwork link copied to clipboard!');
    }

    function deletePost(postId) {
      if (!confirm('Are you sure you want to delete this drawing from your studio feed?')) return;
      let posts = getStoredPosts();
      if (!posts) return;
      posts = posts.filter(p => p.id !== postId);
      saveStoredPosts(posts);
      renderFeed();
      showToast('Drawing removed from studio feed.');
    }

    function filterDrawingCategory(cat) {
      currentCategoryFilter = cat;
      document.querySelectorAll('.draw-filter-btn').forEach(b => {
        b.classList.remove('bg-gold-500', 'text-noir-950', 'font-bold');
        b.classList.add('bg-white/5', 'text-gray-300');
      });
      event.target.classList.add('bg-gold-500', 'text-noir-950', 'font-bold');
      event.target.classList.remove('bg-white/5', 'text-gray-300');
      renderFeed();
    }

    // Modal controls
    function openNewPostModal() {
      document.getElementById('newPostModal').classList.remove('hidden');
    }
    function closeNewPostModal() {
      document.getElementById('newPostModal').classList.add('hidden');
    }

    function setPostFilter(f) {
      selectedPostFilter = f;
      ['none', 'charcoal', 'sepia', 'cyber'].forEach(k => {
        const btn = document.getElementById('filt-' + k);
        if (btn) {
          if (k === f) {
            btn.classList.add('border-gold-400', 'text-white', 'font-bold');
          } else {
            btn.classList.remove('border-gold-400', 'text-white', 'font-bold');
          }
        }
      });
      const previewImg = document.getElementById('imagePreviewEl');
      if (previewImg) {
        previewImg.className = `max-h-60 mx-auto rounded-xl object-contain shadow-lg ${getFilterCssClass(f)}`;
      }
    }

    function handlePreviewPostImage(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (event) => {
        draftImageData = event.target.result;
        const previewEl = document.getElementById('imagePreviewEl');
        previewEl.src = draftImageData;
        document.getElementById('uploadPlaceholder').classList.add('hidden');
        document.getElementById('imagePreviewContainer').classList.remove('hidden');

        // Measure aspect
        previewEl.onload = function() {
          const ratio = (this.naturalWidth / this.naturalHeight).toFixed(2);
          document.getElementById('previewAspectBadge').textContent = `Aspect Ratio: ${ratio}:1 (${this.naturalWidth}x${this.naturalHeight}px)`;
        };
      };
      reader.readAsDataURL(file);
    }

    function handleCreatePost(e) {
      e.preventDefault();
      if (!draftImageData) {
        alert('Please choose an image file for your drawing.');
        return;
      }

      const title = document.getElementById('postTitleInput').value.trim();
      const medium = document.getElementById('postMediumInput').value.trim();
      const caption = document.getElementById('postCaptionInput').value.trim();
      const category = document.getElementById('postCategorySelect').value;

      const newPost = {
        id: 'post_' + Date.now(),
        title,
        medium,
        caption,
        category,
        image: draftImageData,
        filter: selectedPostFilter,
        date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        likes: 0,
        isLiked: false,
        comments: []
      };

      let posts = getStoredPosts() || [];
      posts.unshift(newPost);
      saveStoredPosts(posts);

      closeNewPostModal();
      renderFeed();
      showToast('Drawing published successfully to your studio feed!');

      // Reset Form
      e.target.reset();
      draftImageData = null;
      document.getElementById('uploadPlaceholder').classList.remove('hidden');
      document.getElementById('imagePreviewContainer').classList.add('hidden');
    }

    // Pre-bundled Curated Sample Sketches
    function loadSampleSketches() {
      const samplePosts = [
        {
          id: 'sample_portrait_01',
          title: 'Forensic Study: Human Facial Anatomy & Shadows',
          category: 'portrait',
          medium: '6B & 2B Graphite on Strathmore Cold-Pressed',
          caption: 'Exploration of light fall-off, corneal specular reflections, and bone structure under low-key single-source key lighting. Bridging anatomical observation with synthetic feature extraction.',
          image: './assets/drawings/drawing-portrait.svg',
          date: 'Chikkamagaluru Studio',
          likes: 42,
          isLiked: false,
          comments: [
            { user: 'Kavya R.', text: 'The subtle transition along the cheekbone is stunning!' },
            { user: 'Vikram', text: 'Incredible depth and pencil pressure control.' }
          ]
        },
        {
          id: 'sample_perspective_02',
          title: '3-Point Architectural Perspective & Axial Grid',
          category: 'perspective',
          medium: 'Faber-Castell 0.3mm Fine Fineliner & Marker',
          caption: 'Strict vanishing-point discipline mapping concrete structural cantilevers. Analyzing how human perceptual systems parse geometric perspective lines.',
          image: './assets/drawings/drawing-architecture.svg',
          date: 'Bangalore Studio',
          likes: 38,
          isLiked: false,
          comments: []
        },
        {
          id: 'sample_cyber_03',
          title: 'Cybernetic Cerebral Interface & Neural Traces',
          category: 'cyber',
          medium: 'Charcoal & White Gouache Highlights',
          caption: 'Visualizing synthetic neural synapses interwoven with biological cortical layers. Conceptual draft for edge-compute robotic architectures.',
          image: './assets/drawings/drawing-cybernetic.svg',
          date: 'TCS Lab Study',
          likes: 56,
          isLiked: false,
          comments: [
            { user: 'Dr. Shenoy', text: 'Fascinating conceptual convergence of hardware & biology.' }
          ]
        },
        {
          id: 'sample_nature_04',
          title: 'Chikkamagaluru Western Ghats Ridge Line',
          category: 'charcoal',
          medium: 'Willow Charcoal & Kneaded Eraser on 300 GSM',
          caption: 'Morning mist drifting over the coffee slopes of Mullayanagiri. Tonal atmospheric perspective rendered through soft powdered charcoal blends.',
          image: './assets/drawings/drawing-landscape.svg',
          date: 'Western Ghats Studio',
          likes: 67,
          isLiked: false,
          comments: []
        }
      ];

      saveStoredPosts(samplePosts);
      renderFeed();
      showToast('Curated observational sketches loaded!');
    }

    // Auto-load if empty
    if (!getStoredPosts() || getStoredPosts().length === 0) {
      loadSampleSketches();
    } else {
      renderFeed();
    }

    // -------------------------------------------------------------------------
    // 13. ACT VI: INTERACTIVE NEURAL HYPERPARAMETER LAB CANVAS
    // -------------------------------------------------------------------------
    const neuralCanvas = document.getElementById('neuralPlaygroundCanvas');
    const nCtx = neuralCanvas ? neuralCanvas.getContext('2d') : null;
    let currentQuant = 'FP16';

    const lrSlider = document.getElementById('lrSlider');
    const headsSlider = document.getElementById('headsSlider');
    const tempSlider = document.getElementById('tempSlider');

    function updateNeuralSimulation() {
      const lr = (parseInt(lrSlider.value) * 0.001).toFixed(3);
      const heads = headsSlider.value;
      const temp = (parseInt(tempSlider.value) * 0.01).toFixed(2);

      document.getElementById('lrVal').textContent = lr;
      document.getElementById('headsVal').textContent = `${heads} HEADS`;
      document.getElementById('tempVal').textContent = temp;

      // Update telemetry
      let vram = 4.2;
      let latency = 18.4;
      if (currentQuant === 'INT8') { vram = 2.4; latency = 11.2; }
      if (currentQuant === 'INT4') { vram = 1.3; latency = 7.8; }
      
      const loss = (0.02 + (1.0 - parseFloat(temp) * 0.3) * 0.05 + (0.01 / (parseFloat(lr) + 0.001)) * 0.002).toFixed(4);
      document.getElementById('vramVal').textContent = `${vram} GB`;
      document.getElementById('latencyVal').textContent = `${latency} ms`;
      document.getElementById('lossVal').textContent = loss;

      drawNeuralPlaygroundCanvas(parseFloat(lr), parseInt(heads), parseFloat(temp));
    }

    function setQuantization(q) {
      currentQuant = q;
      ['FP16', 'INT8', 'INT4'].forEach(k => {
        const btn = document.getElementById('q-' + k.toLowerCase());
        if (btn) {
          if (k === q) {
            btn.className = 'p-2 rounded-xl bg-white/10 text-white border border-gold-400 text-center font-bold';
          } else {
            btn.className = 'p-2 rounded-xl bg-white/5 text-gray-400 border border-white/10 text-center hover:text-white';
          }
        }
      });
      updateNeuralSimulation();
    }

    function drawNeuralPlaygroundCanvas(lr, heads, temp) {
      if (!nCtx) return;
      const w = neuralCanvas.width;
      const h = neuralCanvas.height;
      nCtx.clearRect(0, 0, w, h);

      // Draw Attention Matrix grid
      const cols = 12;
      const rows = 8;
      const cellW = w / cols;
      const cellH = h / rows;

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const val = Math.sin((c * 0.8) + (r * 0.6) + temp * 2.0) * Math.cos(c * lr * 100) * 0.5 + 0.5;
          const alpha = Math.max(0.08, val * 0.7);

          if (val > 0.5) {
            nCtx.fillStyle = `rgba(229, 169, 60, ${alpha})`;
          } else {
            nCtx.fillStyle = `rgba(14, 165, 233, ${alpha})`;
          }
          nCtx.fillRect(c * cellW + 1, r * cellH + 1, cellW - 2, cellH - 2);
        }
      }

      // Draw dynamic decision spline boundary
      nCtx.beginPath();
      nCtx.lineWidth = 3;
      nCtx.strokeStyle = '#FFFFFF';
      nCtx.shadowColor = '#E5A93C';
      nCtx.shadowBlur = 12;

      for (let x = 0; x <= w; x += 10) {
        const y = (h / 2) + Math.sin(x * 0.02 + temp * 4) * (h * 0.28) * (heads / 8);
        if (x === 0) nCtx.moveTo(x, y);
        else nCtx.lineTo(x, y);
      }
      nCtx.stroke();
      nCtx.shadowBlur = 0;
    }

    if (lrSlider && headsSlider && tempSlider) {
      lrSlider.addEventListener('input', updateNeuralSimulation);
      headsSlider.addEventListener('input', updateNeuralSimulation);
      tempSlider.addEventListener('input', updateNeuralSimulation);
      updateNeuralSimulation();
    }

    // -------------------------------------------------------------------------
    // 14. GLOBAL APPRECIATION BEACON & BALLISTIC FIREWORKS BURST
    // -------------------------------------------------------------------------
    let globalLikes = parseInt(localStorage.getItem('shreyas_global_portfolio_likes') || '1482', 10);
    const globalLikeCountEl = document.getElementById('globalLikeCount');
    if (globalLikeCountEl) globalLikeCountEl.textContent = globalLikes.toLocaleString();

    function triggerGlobalLikeCount(e) {
      globalLikes += 1;
      localStorage.setItem('shreyas_global_portfolio_likes', globalLikes);
      if (globalLikeCountEl) globalLikeCountEl.textContent = globalLikes.toLocaleString();

      const clientX = e ? e.clientX : window.innerWidth / 2;
      const clientY = e ? e.clientY : window.innerHeight / 2;
      firePhysicalHeartBurst(clientX, clientY, 24);
      showToast('Transmission received! Thank you for the appreciation.');
    }

    // Kinematic Ballistic Particle Engine
    const activeParticles = [];
    let particleAnimRunning = false;

    function firePhysicalHeartBurst(originX, originY, count = 16) {
      const chars = ['❤️', '✨', '💛', '💖', '⭐', '💫'];

      for (let i = 0; i < count; i++) {
        const el = document.createElement('div');
        el.className = 'phys-heart-particle';
        el.textContent = chars[Math.floor(Math.random() * chars.length)];
        document.body.appendChild(el);

        const angle = (Math.PI * 2 * i) / count + (Math.random() - 0.5) * 0.5;
        const speed = Math.random() * 9 + 4;

        activeParticles.push({
          el,
          x: originX,
          y: originY,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 5,
          gravity: 0.38,
          drag: 0.94,
          rot: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 16,
          opacity: 1,
          scale: Math.random() * 0.5 + 0.8,
          life: 0,
          maxLife: 60 + Math.random() * 25
        });
      }

      if (!particleAnimRunning) {
        particleAnimRunning = true;
        requestAnimationFrame(updatePhysicalParticles);
      }
    }

    function updatePhysicalParticles() {
      for (let i = activeParticles.length - 1; i >= 0; i--) {
        const p = activeParticles[i];
        p.life++;

        p.vx *= p.drag;
        p.vy = p.vy * p.drag + p.gravity;
        p.x += p.vx;
        p.y += p.vy;
        p.rot += p.vRot;

        p.opacity = Math.max(0, 1 - p.life / p.maxLife);

        p.el.style.transform = `translate(${p.x}px, ${p.y}px) rotate(${p.rot}deg) scale(${p.scale})`;
        p.el.style.opacity = p.opacity;

        if (p.life >= p.maxLife || p.opacity <= 0) {
          p.el.remove();
          activeParticles.splice(i, 1);
        }
      }

      if (activeParticles.length > 0) {
        requestAnimationFrame(updatePhysicalParticles);
      } else {
        particleAnimRunning = false;
      }
    }

    // -------------------------------------------------------------------------
    // 15. OPTICAL SCROLL REVEALS & 3D TILT PHYSICS
    // -------------------------------------------------------------------------
    function initScrollReveals() {
      const items = document.querySelectorAll('.reveal-item');
      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

      items.forEach(el => observer.observe(el));
    }
    initScrollReveals();

    function initRealWorldTilt() {
      document.querySelectorAll('.real-tilt').forEach(card => {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const centerX = rect.width / 2;
          const centerY = rect.height / 2;

          const rotateX = ((y - centerY) / centerY) * -7;
          const rotateY = ((x - centerX) / centerX) * 7;

          card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateZ(8px)`;
          card.style.setProperty('--mouse-x', `${((x / rect.width) * 100).toFixed(1)}%`);
          card.style.setProperty('--mouse-y', `${((y / rect.height) * 100).toFixed(1)}%`);
        });

        card.addEventListener('mouseleave', () => {
          card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
        });
      });
    }
    initRealWorldTilt();

    function initMagneticButtons() {
      document.querySelectorAll('.magnetic-btn').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;
          btn.style.transform = `translate(${x * 0.22}px, ${y * 0.22}px) scale(1.02)`;
        });

        btn.addEventListener('mouseleave', () => {
          btn.style.transform = 'translate(0px, 0px) scale(1)';
        });
      });
    }
    initMagneticButtons();

    // -------------------------------------------------------------------------
    // 16. THEME SWITCHER CONTROLLER
    // -------------------------------------------------------------------------
    const themes = ['obsidian', 'aurora', 'cyber'];
    let currentThemeIdx = 0;

    function applyTheme(name) {
      document.body.setAttribute('data-theme', name);
      localStorage.setItem('shreyas_portfolio_theme', name);
      currentThemeIdx = themes.indexOf(name);
      toggleThemeModal(false);
      showToast(`Mood switched to: ${name.toUpperCase()}`);
    }

    function cycleNextTheme() {
      currentThemeIdx = (currentThemeIdx + 1) % themes.length;
      applyTheme(themes[currentThemeIdx]);
    }

    function toggleThemeModal(force) {
      const modal = document.getElementById('themeModal');
      if (typeof force === 'boolean') {
        if (force) modal.classList.remove('hidden');
        else modal.classList.add('hidden');
      } else {
        modal.classList.toggle('hidden');
      }
    }

    const savedTheme = localStorage.getItem('shreyas_portfolio_theme');
    if (savedTheme) applyTheme(savedTheme);

    function toggleCreditsModal() {
      document.getElementById('creditsModal').classList.toggle('hidden');
    }

    // -------------------------------------------------------------------------
    // 17. CONTACT FORM DISPATCH & TOAST UTILS
    // -------------------------------------------------------------------------
    function handleContactSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('contactName').value;
      showToast(`Transmission dispatched, ${name}. Shreyas will respond shortly!`);
      e.target.reset();
    }

    function copyToClipboard(text, msg) {
      navigator.clipboard.writeText(text);
      showToast(msg);
    }

    let toastTimer = null;
    function showToast(msg) {
      const toast = document.getElementById('toastMessage');
      const text = document.getElementById('toastText');
      text.textContent = msg;

      if (toastTimer) clearTimeout(toastTimer);
      toast.classList.remove('translate-y-24', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      toastTimer = setTimeout(() => {
        toast.classList.add('translate-y-24', 'opacity-0');
        toast.classList.remove('translate-y-0', 'opacity-100');
      }, 3500);
    }

    // Keyboard Shortcuts (ESC to close modals)
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('#newPostModal, #cinemaLightboxModal, #certModal, #themeModal, #creditsModal').forEach(m => m.classList.add('hidden'));
      }
    });

  </script>
</body>
</html>
'''

target_path = r"C:\Users\Sneha Nishani\.gemini\antigravity\scratch\shreyas-cinematic-portfolio\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {target_path} ({len(html_content)} bytes)")
