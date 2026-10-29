# build_full_portfolio.py
# Full production build for Shreyas B J Portfolio with exact user requirements:
# 1. 4 New Projects with tailored visuals
# 2. Text justified beautifully
# 3. Removed reset avatar button
# 4. Light and Dark mode toggle with localStorage persistence
# 5. Full-width screen-fit layout (max-w-7xl)
# 6. Certificate placeholders with upload capability & verified logos
# 7. Device responsiveness across mobile, tablet, desktop, 4K

html_content = '''<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shreyas B J — AI/ML Engineer & Creative Technologist</title>
  <meta name="description" content="Portfolio of Shreyas B J — AI/ML Engineer at TCS, Electronics & Hardware Failure Analysis Background, Databricks Certified, Observational Sketch Artist.">

  <!-- Clean Modern Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            noir: {
              950: '#060911',
              900: '#0B101D',
              850: '#11182B',
              800: '#18223B',
              700: '#233050',
            },
            cyan: {
              400: '#38BDF8',
              500: '#0EA5E9',
              600: '#0284C7',
            },
            gold: {
              400: '#E5A93C',
              500: '#C28D38',
              600: '#A3782C',
            },
            heart: '#FF2A6D',
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            display: ['Space Grotesk', 'sans-serif'],
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Smooth custom scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #233050; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #38BDF8; }

    /* Beautiful Justified Text */
    .text-justify-pretty {
      text-align: justify;
      text-justify: inter-word;
      hyphens: auto;
    }

    /* Clean Card Styling with Light & Dark Compatibility */
    .theme-card {
      background: rgba(11, 16, 29, 0.78);
      border: 1px solid rgba(255, 255, 255, 0.09);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      transition: all 0.25s ease;
    }
    html:not(.dark) .theme-card {
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(15, 23, 42, 0.1);
      box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
    }
    .theme-card:hover {
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.5);
    }
    html:not(.dark) .theme-card:hover {
      box-shadow: 0 12px 30px -10px rgba(15, 23, 42, 0.12);
    }

    /* Double-tap heart pop animation */
    @keyframes heartPop {
      0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
      40% { transform: translate(-50%, -50%) scale(1.3); opacity: 1; }
      70% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.9; }
      100% { transform: translate(-50%, -50%) scale(0.85) translateY(-20px); opacity: 0; }
    }
    .pop-heart-anim {
      animation: heartPop 0.75s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    /* Ballistic Heart Particle */
    .phys-heart-particle {
      position: fixed;
      pointer-events: none;
      z-index: 99999;
      font-size: 18px;
      user-select: none;
      will-change: transform, opacity;
      filter: drop-shadow(0 2px 6px rgba(0,0,0,0.4));
    }
  </style>
</head>
<body class="bg-noir-950 dark:bg-noir-950 text-gray-200 dark:text-gray-200 font-sans antialiased selection:bg-cyan-500/25 selection:text-white relative min-h-screen transition-colors duration-300">

  <!-- ========================================================================= -->
  <!-- TWINKLING STARRY NIGHT CANVAS (SMALL SHINING STAR DOTS) -->
  <!-- ========================================================================= -->
  <canvas id="starfieldCanvas" class="fixed inset-0 pointer-events-none z-0 w-full h-full"></canvas>

  <!-- ========================================================================= -->
  <!-- TOP NAVIGATION WITH LIGHT/DARK TOGGLE -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 w-full z-50 backdrop-blur-md bg-noir-950/85 dark:bg-noir-950/85 border-b border-white/10 dark:border-white/10 px-4 sm:px-8 py-4 flex items-center justify-between transition-colors duration-300">
    <a href="#hero" class="flex items-center space-x-2.5 group">
      <div class="flex items-center space-x-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse shadow-[0_0_8px_#38BDF8]"></span>
      </div>
      <span class="font-display font-bold text-white dark:text-white text-base tracking-tight group-hover:text-cyan-400 transition-colors">SHREYAS B J</span>
      <span class="text-xs font-mono text-gray-400 hidden sm:inline">&bull; AI / ML Engineer @ TCS</span>
    </a>

    <!-- Nav Links -->
    <nav class="hidden md:flex items-center space-x-7 text-xs font-mono text-gray-300 dark:text-gray-300">
      <a href="#about" class="hover:text-cyan-400 transition-colors">ABOUT</a>
      <a href="#experience" class="hover:text-cyan-400 transition-colors">EXPERIENCE</a>
      <a href="#arsenal" class="hover:text-cyan-400 transition-colors">SKILLS &amp; CERTS</a>
      <a href="#projects" class="hover:text-cyan-400 transition-colors">PROJECTS</a>
      <a href="#sketches" class="hover:text-gold-400 transition-colors">SKETCHES</a>
      <a href="#contact" class="hover:text-cyan-400 transition-colors">CONTACT</a>
    </nav>

    <!-- Header Actions (Light/Dark Mode Toggle & Contact) -->
    <div class="flex items-center space-x-3">
      <!-- Dark / Light Mode Toggle Button -->
      <button id="themeToggleBtn" onclick="toggleThemeMode()" class="p-2 rounded-xl bg-white/5 dark:bg-white/5 border border-white/10 dark:border-white/10 text-gray-300 hover:text-white transition-all flex items-center justify-center" title="Toggle Light/Dark Mode">
        <i id="themeIcon" data-lucide="sun" class="w-4 h-4 text-amber-300"></i>
      </button>

      <a href="#contact" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(14,165,233,0.3)]">
        GET IN TOUCH
      </a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- MAIN FULL-SCREEN FIT CONTAINER (MAX-W-7XL) -->
  <!-- ========================================================================= -->
  <main class="relative z-10 pt-24 space-y-24 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

    <!-- ======================================================================= -->
    <!-- SECTION 1: HERO (FULL SCREEN FIT) -->
    <!-- ======================================================================= -->
    <section id="hero" class="min-h-[82vh] flex flex-col justify-center items-center text-center max-w-5xl mx-auto space-y-6 py-12">
      
      <!-- Current Status Tag -->
      <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-noir-900/90 dark:bg-noir-900/90 border border-white/10 text-xs font-mono text-cyan-400 shadow-md">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
        <span>AI / ML ENGINEER &bull; TATA CONSULTANCY SERVICES (TCS)</span>
      </div>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-display font-bold text-white dark:text-white tracking-tight leading-tight">
        Building Intelligent Systems. <br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-gold-400">
          Observing the World.
        </span>
      </h1>

      <!-- Subtitle -->
      <p class="text-base sm:text-lg text-gray-300 dark:text-gray-300 max-w-3xl mx-auto leading-relaxed font-sans text-justify-pretty">
        I am <strong class="text-white dark:text-white font-semibold">Shreyas B J</strong>, an AI/ML Engineer merging deep learning workflows with forensic hardware reliability and fine-art draughtsmanship. Graduating with an 8.89 CGPA in Electronics &amp; Communication from NCET Bangalore, with industrial failure analysis experience at Foxconn.
      </p>

      <!-- Key Telemetry Badges -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3.5 w-full max-w-3xl pt-2 font-mono text-xs">
        <div class="p-4 rounded-2xl theme-card text-center">
          <span class="block text-2xl font-bold text-cyan-400 font-display">8.89</span>
          <span class="text-gray-400 text-[11px]">CGPA &bull; NCET ECE</span>
        </div>
        <div class="p-4 rounded-2xl theme-card text-center">
          <span class="block text-2xl font-bold text-gold-400 font-display">Foxconn</span>
          <span class="text-gray-400 text-[11px]">Failure Analysis</span>
        </div>
        <div class="p-4 rounded-2xl theme-card text-center">
          <span class="block text-2xl font-bold text-white dark:text-white font-display">6+ Certs</span>
          <span class="text-gray-400 text-[11px]">Databricks &bull; Cloud</span>
        </div>
        <div class="p-4 rounded-2xl theme-card text-center">
          <span class="block text-2xl font-bold text-emerald-400 font-display">Studio Art</span>
          <span class="text-gray-400 text-[11px]">Fine Art Realism</span>
        </div>
      </div>

      <!-- Hero Actions -->
      <div class="pt-4 flex flex-wrap items-center justify-center gap-4">
        <a href="#about" class="px-7 py-3.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all flex items-center space-x-2 shadow-lg">
          <span>EXPLORE MY WORK</span>
          <i data-lucide="arrow-down" class="w-4 h-4"></i>
        </a>
        <a href="#sketches" class="px-7 py-3.5 rounded-xl bg-white/5 dark:bg-white/5 hover:bg-white/10 border border-white/15 text-white dark:text-white font-display font-bold text-xs uppercase tracking-wider transition-all flex items-center space-x-2">
          <i data-lucide="brush" class="w-4 h-4 text-gold-400"></i>
          <span>VIEW SKETCH STUDIO</span>
        </a>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 2: ABOUT & ADAPTIVE PROFILE FRAME -->
    <!-- ======================================================================= -->
    <section id="about" class="py-12">
      
      <!-- Section Header -->
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">ABOUT &bull; BIOGRAPHY</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">The Architect</h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Adaptive Profile Frame Column (No Reset Button) -->
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="relative group w-full max-w-sm">
            
            <!-- Dynamic Aspect-Ratio Hugging Container -->
            <div id="profileFrame" class="theme-card p-3 rounded-2xl transition-all duration-300 w-fit mx-auto shadow-xl">
              <div class="relative overflow-hidden rounded-xl bg-noir-950 dark:bg-noir-950 border border-white/10 flex items-center justify-center">
                <img id="profilePhotoImg" src="./assets/profile-avatar.svg" alt="Shreyas B J - Portrait" class="max-h-[420px] w-auto h-auto max-w-full object-contain mx-auto block group-hover:scale-[1.01] transition-transform duration-500">
                
                <!-- Aspect Ratio Tag -->
                <div class="absolute bottom-2.5 right-2.5 px-2.5 py-0.5 rounded bg-noir-950/80 backdrop-blur-md border border-white/20 text-[10px] font-mono text-cyan-400">
                  <span id="aspectRatioTag">PORTRAIT</span>
                </div>
              </div>
            </div>

            <!-- Single Upload Button (Reset Button Completely Removed) -->
            <div class="mt-4 flex items-center justify-center w-full">
              <input type="file" id="profilePhotoInput" accept="image/*" class="hidden">
              <button onclick="document.getElementById('profilePhotoInput').click()" class="px-5 py-2.5 rounded-xl bg-white/5 dark:bg-white/5 hover:bg-white/10 border border-white/15 text-xs font-mono text-gray-200 dark:text-gray-200 hover:text-white transition-all flex items-center space-x-2">
                <i data-lucide="upload" class="w-4 h-4 text-cyan-400"></i>
                <span>UPLOAD PROFILE PHOTO</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Single Paragraph Biography Column (Beautifully Justified) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="theme-card p-8 rounded-2xl space-y-5">
            <h3 class="text-xl font-display font-bold text-white dark:text-white flex items-center space-x-2.5">
              <span>Shreyas B J</span>
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
              <span class="text-xs font-mono text-cyan-400 font-normal">CHIKKAMAGALURU &bull; BANGALORE</span>
            </h3>

            <!-- Single Paragraph Biography (text-justify-pretty) -->
            <p class="text-sm sm:text-base text-gray-300 dark:text-gray-300 leading-relaxed font-sans text-justify-pretty">
              Rooted in the calm terrains of <span class="text-gold-400 font-medium">Chikkamagaluru</span> and tempered in the high-velocity technological core of Bangalore, I am an <span class="text-white dark:text-white font-medium">AI/ML Engineer at Tata Consultancy Services (TCS)</span> with a rigorous foundation in <span class="text-white dark:text-white font-medium">Electronics &amp; Communication Engineering</span> from Nagarjuna College of Engineering and Technology (graduating with an <span class="text-cyan-400 font-mono font-semibold">8.89 CGPA</span>). My engineering intuition was forged on industrial failure analysis lines at <span class="text-cyan-400 font-medium">Foxconn (Hon Hai Technology Group)</span>, where I conducted root-cause failure investigations, traced electrical schematics, and diagnosed microscopic circuit anomalies under stringent manufacturing tolerances. Today, I translate that forensic hardware discipline into building high-performance machine learning models, deploying computer vision inference pipelines, and orchestrating multi-agent LLM systems certified by <span class="text-gold-400 font-medium">Databricks, Anthropic Claude, and Google Cloud Gemini</span>—all while continuously grounding my perception through a lifelong discipline of <span class="text-white dark:text-white font-medium">observational fine-art sketching</span> that bridges physical observation with synthetic machine intelligence.
            </p>

            <div class="border-l-2 border-cyan-400 pl-4 py-1 text-xs font-mono text-gray-400 dark:text-gray-400 italic">
              "Observing reality with forensic precision—whether through a microscope on an SMT production line or graphite on cold-pressed paper."
            </div>

            <!-- Fast Specs -->
            <div class="flex flex-wrap gap-2 pt-1 text-[11px] font-mono">
              <span class="px-3 py-1 rounded-lg bg-noir-900 dark:bg-noir-900 border border-white/10 text-cyan-300">#AI/ML</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 dark:bg-noir-900 border border-white/10 text-gold-300">#ComputerVision</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 dark:bg-noir-900 border border-white/10 text-emerald-300">#HardwareReliability</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 dark:bg-noir-900 border border-white/10 text-purple-300">#Databricks</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 dark:bg-noir-900 border border-white/10 text-white">#Draughtsmanship</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 3: EXPERIENCE (TIMELINE) -->
    <!-- ======================================================================= -->
    <section id="experience" class="py-12">
      
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">EXPERIENCE &bull; TIMELINE</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">Operational Journey</h2>
      </div>

      <div class="space-y-5">
        
        <!-- Role 1: TCS -->
        <div class="theme-card p-7 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg sm:text-xl font-display font-bold text-white dark:text-white">Tata Consultancy Services (TCS)</h3>
              <p class="text-xs font-mono text-cyan-400">AI / ML Engineer &bull; Full-Time</p>
            </div>
            <span class="text-xs font-mono text-gray-400">2024 &bull; PRESENT | BANGALORE</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 dark:text-gray-300 leading-relaxed font-sans text-justify-pretty">
            Developing enterprise machine learning workflows, multi-agent LLM systems with LangChain, and automated computer vision inference pipelines. Managing model governance and distributed feature stores using Databricks MLflow.
          </p>
          <div class="flex flex-wrap gap-2 pt-1 text-[11px] font-mono text-gray-400">
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">Python</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">PyTorch</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">Databricks</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">LangChain</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">Docker</span>
          </div>
        </div>

        <!-- Role 2: Foxconn -->
        <div class="theme-card p-7 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg sm:text-xl font-display font-bold text-white dark:text-white">Foxconn (Hon Hai Technology Group)</h3>
              <p class="text-xs font-mono text-gold-400">Graduate Apprentice &bull; Hardware Failure Analysis</p>
            </div>
            <span class="text-xs font-mono text-gray-400">OCT 2024 &bull; DEC 2024 | SRIPERUMBUDUR</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 dark:text-gray-300 leading-relaxed font-sans text-justify-pretty">
            Conducted forensic hardware failure diagnostics on high-speed SMT manufacturing lines. Traced high-density PCB schematics, performed In-Circuit Testing (ICT) and Functional Testing (FCT), and diagnosed micro solder bridges and component drift to preserve 99.8% production quality.
          </p>
          <div class="flex flex-wrap gap-2 pt-1 text-[11px] font-mono text-gray-400">
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">Failure Analysis</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">ICT / FCT</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">SMT Diagnostics</span>
            <span class="px-2.5 py-1 rounded bg-noir-900 dark:bg-noir-900 border border-white/10">Schematics</span>
          </div>
        </div>

        <!-- Role 3: NCET Education -->
        <div class="theme-card p-7 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg sm:text-xl font-display font-bold text-white dark:text-white">Nagarjuna College of Engineering &amp; Technology (NCET)</h3>
              <p class="text-xs font-mono text-cyan-400">B.E. in Electronics &amp; Communication Engineering (VTU)</p>
            </div>
            <span class="text-xs font-mono text-cyan-400 font-bold">8.89 CGPA | 2021 &bull; 2025</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 dark:text-gray-300 leading-relaxed font-sans text-justify-pretty">
            Graduated with honors ranking in the top tier with an 8.89 CGPA. Capstone: Autonomous Multi-Sensor Rover with real-time obstacle avoidance, LIDAR sensor fusion, and edge compute on NVIDIA Jetson.
          </p>
        </div>

        <!-- Role 4: Skill Craft -->
        <div class="theme-card p-7 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg sm:text-xl font-display font-bold text-white dark:text-white">Skill Craft Technology</h3>
              <p class="text-xs font-mono text-emerald-400">Machine Learning Intern</p>
            </div>
            <span class="text-xs font-mono text-gray-400">MAY 2024 &bull; JUN 2024</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 dark:text-gray-300 leading-relaxed font-sans text-justify-pretty">
            Constructed predictive classification pipelines, exploratory data analysis workflows, and feature engineering benchmarks with Scikit-Learn and Pandas.
          </p>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 4: ARSENAL & VERIFIED CERTIFICATIONS (WITH PLACEHOLDERS) -->
    <!-- ======================================================================= -->
    <section id="arsenal" class="py-12">
      
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">SKILLS &bull; ACCREDITATIONS</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">Verified Certifications &amp; Arsenal</h2>
        <p class="text-xs text-gray-400 font-mono">Upload or preview official credential certificates with verified authentication seals.</p>
      </div>

      <!-- 6 Industry Certifications with Image Placeholders & Verified Logos -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Cert 1: Databricks -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <!-- Verified Header Badge -->
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-cyan-400 font-bold uppercase tracking-wider">DATABRICKS</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Certified Associate — Machine Learning</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">Distributed Apache Spark compute, feature store management, MLflow model governance, and scalable deployment.</p>

            <!-- Certificate Image Placeholder Frame with Upload Control -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_1" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_1" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-cyan-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">Databricks Certificate Plaque</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_1" accept="image/*" class="hidden" onchange="handleCertUpload(event, 1)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-DB-ML</span>
            <button onclick="document.getElementById('certFile_1').click()" class="text-cyan-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

        <!-- Cert 2: Claude Anthropic -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-gold-400 font-bold uppercase tracking-wider">ANTHROPIC</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-gold-500/10 border border-gold-500/30 text-gold-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-gold-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Claude Certified Prompt Engineer</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">Multi-turn agentic workflows, chain-of-thought steering, structured XML parsing, and tool-augmented pipelines.</p>

            <!-- Certificate Image Placeholder Frame -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_2" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_2" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-gold-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">Anthropic Certificate Plaque</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_2" accept="image/*" class="hidden" onchange="handleCertUpload(event, 2)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-ANTH-01</span>
            <button onclick="document.getElementById('certFile_2').click()" class="text-gold-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

        <!-- Cert 3: Google Gemini -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-cyan-400 font-bold uppercase tracking-wider">GOOGLE CLOUD</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Gemini AI Certified Developer</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">Multimodal vision models, Vertex AI embeddings, vector search index construction, and low-latency inference.</p>

            <!-- Certificate Image Placeholder Frame -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_3" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_3" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-cyan-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">Google Cloud Certificate Plaque</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_3" accept="image/*" class="hidden" onchange="handleCertUpload(event, 3)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-GCP-GEM</span>
            <button onclick="document.getElementById('certFile_3').click()" class="text-cyan-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

        <!-- Cert 4: NPTEL IIT Madras -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-emerald-400 font-bold uppercase tracking-wider">IIT MADRAS / NPTEL</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-emerald-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Deep Learning &amp; Microprocessors</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">Convolutional architectures, backpropagation loss landscapes, and embedded microprocessor signal processing.</p>

            <!-- Certificate Image Placeholder Frame -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_4" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_4" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-emerald-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">NPTEL IIT Madras Certificate</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_4" accept="image/*" class="hidden" onchange="handleCertUpload(event, 4)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-IITM-NPT</span>
            <button onclick="document.getElementById('certFile_4').click()" class="text-emerald-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

        <!-- Cert 5: NXT Wave -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-purple-400 font-bold uppercase tracking-wider">NXT WAVE</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-purple-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Python Full Stack Specialist</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">Python full stack architecture, relational database SQL schemas, REST microservices, and algorithmic design.</p>

            <!-- Certificate Image Placeholder Frame -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_5" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_5" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-purple-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">NXT Wave Certificate Plaque</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_5" accept="image/*" class="hidden" onchange="handleCertUpload(event, 5)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-NXT-PY</span>
            <button onclick="document.getElementById('certFile_5').click()" class="text-purple-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

        <!-- Cert 6: Technical Hub -->
        <div class="theme-card p-6 rounded-2xl flex flex-col justify-between space-y-4">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-mono text-cyan-400 font-bold uppercase tracking-wider">TECHNICAL HUB</span>
              <div class="flex items-center space-x-1 px-2 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-[10px] font-mono font-bold">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>VERIFIED</span>
              </div>
            </div>

            <h4 class="font-display font-bold text-white dark:text-white text-base">Embedded Systems &amp; IoT</h4>
            <p class="text-xs text-gray-300 dark:text-gray-300 text-justify-pretty">STM32 &amp; ESP32 microcontroller firmware, hardware timer configurations, and hardware protocols (I2C, SPI, UART).</p>

            <!-- Certificate Image Placeholder Frame -->
            <div class="relative rounded-xl overflow-hidden bg-noir-950 dark:bg-noir-950 border border-white/15 h-36 flex items-center justify-center group">
              <img id="certImg_6" src="" class="hidden w-full h-full object-cover">
              <div id="certPlaceholder_6" class="text-center p-3">
                <i data-lucide="award" class="w-8 h-8 text-cyan-400 mx-auto mb-1 opacity-80"></i>
                <span class="text-[11px] text-gray-300 font-mono block font-bold">Technical Hub Certificate</span>
                <span class="text-[10px] text-gray-500 font-mono block">Click below to upload certificate image</span>
              </div>
              <input type="file" id="certFile_6" accept="image/*" class="hidden" onchange="handleCertUpload(event, 6)">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between text-xs font-mono">
            <span class="text-gray-400">ID: CERT-TH-EMB</span>
            <button onclick="document.getElementById('certFile_6').click()" class="text-cyan-400 hover:text-white text-[11px] font-bold flex items-center space-x-1">
              <i data-lucide="upload" class="w-3 h-3"></i>
              <span>UPLOAD IMAGE</span>
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 5: 4 FEATURED PROJECTS WITH CUSTOM VISUALS -->
    <!-- ======================================================================= -->
    <section id="projects" class="py-12">
      
      <div class="mb-12 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">PROJECTS &bull; IMPLEMENTATIONS</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">Technical Portfolio Projects</h2>
        <p class="text-xs text-gray-400 font-mono">Interactive simulations, live dashboards, and software architectures built by Shreyas.</p>
      </div>

      <div class="space-y-12">
        
        <!-- =================================================================== -->
        <!-- PROJECT 1: TRAVEL AI AGENT -->
        <!-- =================================================================== -->
        <div class="theme-card p-7 sm:p-9 rounded-3xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-cyan-400 font-bold uppercase tracking-wider">PROJECT 01 &bull; BUILDING AI AGENTS</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold text-white dark:text-white">Travel AI Agent</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-mono">LangChain + RAG</span>
              <span class="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-xs font-mono">Streamlit</span>
            </div>
          </div>

          <!-- Bullet Points (Beautifully Justified) -->
          <ul class="space-y-2.5 text-xs sm:text-sm text-gray-300 dark:text-gray-300 font-sans text-justify-pretty leading-relaxed">
            <li class="flex items-start space-x-2.5">
              <span class="text-cyan-400 font-bold">&bull;</span>
              <span>Developed an AI-powered travel recommendation agent that suggests destinations, attractions, and activities based on user interests and travel preferences.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-cyan-400 font-bold">&bull;</span>
              <span>Implemented a RAG-based knowledge system with vector search to provide grounded information on hotel policies, attractions, and travel advisories.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-cyan-400 font-bold">&bull;</span>
              <span>Integrated LLM-based conversational capabilities for natural-language travel queries and personalized trip planning.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-cyan-400 font-bold">&bull;</span>
              <span>Built the solution using Python, Scikit-learn, LangChain, ChromaDB, and Streamlit.</span>
            </li>
          </ul>

          <!-- Custom Visual: Interactive Agent Console & Vector Search Simulator -->
          <div class="bg-noir-950 dark:bg-noir-950 p-5 rounded-2xl border border-white/10 space-y-4 font-mono text-xs">
            <div class="flex items-center justify-between text-gray-400 border-b border-white/10 pb-2.5">
              <span class="flex items-center space-x-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span class="text-white font-bold">TRAVEL AGENT CONVERSATION RUNTIME</span>
              </span>
              <span class="text-cyan-400 text-[11px]">CHROMADB VECTOR INDEX READY</span>
            </div>

            <div class="flex flex-col sm:flex-row items-center gap-2">
              <input type="text" id="travelInput" value="3-day cultural & photography journey in Kyoto on a budget" class="w-full bg-noir-900 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-cyan-400 text-xs">
              <button onclick="runTravelSim()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-bold text-xs uppercase flex items-center justify-center space-x-1.5 transition-all">
                <span>QUERY AGENT</span>
                <i data-lucide="send" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <div id="travelOutput" class="bg-noir-900/80 p-3.5 rounded-xl border border-white/5 text-gray-300 text-[11px] space-y-1 min-h-[90px]">
              <p class="text-gray-400">&gt; Waiting for query dispatch. Click "QUERY AGENT" to test conversational vector synthesis.</p>
            </div>
          </div>
        </div>

        <!-- =================================================================== -->
        <!-- PROJECT 2: PERSONAL PORTFOLIO -->
        <!-- =================================================================== -->
        <div class="theme-card p-7 sm:p-9 rounded-3xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-gold-400 font-bold uppercase tracking-wider">PROJECT 02 &bull; NETLIFY - WEBSITE BUILDING AND DESIGN</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold text-white dark:text-white">Personal Portfolio</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-gold-500/10 border border-gold-500/30 text-gold-300 text-xs font-mono">HTML &bull; CSS &bull; JavaScript</span>
              <span class="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-xs font-mono">Netlify CI/CD</span>
            </div>
          </div>

          <!-- Bullet Points (Beautifully Justified) -->
          <ul class="space-y-2.5 text-xs sm:text-sm text-gray-300 dark:text-gray-300 font-sans text-justify-pretty leading-relaxed">
            <li class="flex items-start space-x-2.5">
              <span class="text-gold-400 font-bold">&bull;</span>
              <span>A personal portfolio website built using HTML, CSS, and JavaScript. Showcases my skills, projects, education, and certifications in a clean and interactive layout.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-gold-400 font-bold">&bull;</span>
              <span>Implemented dark mode toggle and dynamic typewriter animations using AI-driven interaction principles, with responsive design across mobile, tablet, and desktop viewports.</span>
            </li>
          </ul>

          <!-- Custom Visual: Live Interactive Browser Mockup with Real-Time Typewriter -->
          <div class="bg-noir-950 dark:bg-noir-950 rounded-2xl border border-white/10 overflow-hidden shadow-xl">
            <!-- Browser Header Bar -->
            <div class="px-4 py-2.5 bg-noir-900 border-b border-white/10 flex items-center justify-between">
              <div class="flex items-center space-x-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
              </div>
              <span class="text-[11px] font-mono text-gray-400">https://shreyas-portfolio.netlify.app</span>
              <span class="text-[10px] font-mono text-emerald-400 flex items-center space-x-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                <span>ONLINE</span>
              </span>
            </div>

            <!-- Browser Viewport Preview -->
            <div class="p-6 bg-gradient-to-b from-noir-950 to-noir-900 flex flex-col sm:flex-row items-center justify-between gap-6 font-mono text-xs">
              <div class="space-y-2 text-left">
                <span class="text-gold-400 text-xs font-bold block">// LIVE TYPEWRITER PREVIEW:</span>
                <div class="text-lg sm:text-xl font-display font-bold text-white">
                  <span>Hello, I am Shreyas B J — </span>
                  <span id="portfolioTypewriterText" class="text-cyan-400 border-r-2 border-cyan-400 pr-1">AI/ML Engineer</span>
                </div>
                <p class="text-xs text-gray-400 font-sans">Dark mode toggle, real-world animations, and responsive screen-fit architecture.</p>
              </div>

              <!-- Live Mini Theme Switcher Preview -->
              <div class="p-3 rounded-xl bg-noir-900 border border-white/10 text-center space-y-2 shrink-0">
                <span class="text-[10px] text-gray-400 block">THEME STATUS</span>
                <button onclick="toggleThemeMode()" class="px-3.5 py-1.5 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs hover:bg-cyan-500/20 transition-all flex items-center space-x-1.5 mx-auto">
                  <i data-lucide="sun-moon" class="w-3.5 h-3.5"></i>
                  <span>SWITCH THEME</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- =================================================================== -->
        <!-- PROJECT 3: BUSINESS INTELLIGENCE PLATFORM -->
        <!-- =================================================================== -->
        <div class="theme-card p-7 sm:p-9 rounded-3xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-emerald-400 font-bold uppercase tracking-wider">PROJECT 03 &bull; STREAMLIT APPLICATION (DATA ANALYSIS &amp; VISUALIZATION)</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold text-white dark:text-white">Business Intelligence Platform</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-mono">Python &bull; Pandas &bull; NumPy</span>
              <span class="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-xs font-mono">Streamlit App</span>
            </div>
          </div>

          <!-- Bullet Points (Beautifully Justified) -->
          <ul class="space-y-2.5 text-xs sm:text-sm text-gray-300 dark:text-gray-300 font-sans text-justify-pretty leading-relaxed">
            <li class="flex items-start space-x-2.5">
              <span class="text-emerald-400 font-bold">&bull;</span>
              <span>Developed a responsive Business Intelligence Platform using Python, NumPy, Pandas, and file handling to analyze and visualize data uploaded through Excel files.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-emerald-400 font-bold">&bull;</span>
              <span>Automated the generation of data visualizations and analytical insights, enabling users to quickly interpret uploaded datasets.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-emerald-400 font-bold">&bull;</span>
              <span>Integrated AI-powered natural language querying, allowing users to interact with datasets and obtain relevant insights by entering queries through a single prompt.</span>
            </li>
          </ul>

          <!-- Custom Visual: Interactive BI Analytics Dashboard & AI Query Simulator -->
          <div class="bg-noir-950 dark:bg-noir-950 p-6 rounded-2xl border border-white/10 space-y-5 font-mono text-xs">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 pb-3">
              <span class="text-white font-bold flex items-center space-x-2">
                <i data-lucide="bar-chart-3" class="w-4 h-4 text-emerald-400"></i>
                <span>STREAMLIT BI DASHBOARD &bull; EXCEL DATASET ENGINE</span>
              </span>
              <span class="text-emerald-400 text-[11px]">SALES_Q4_REPORT.XLSX INGESTED</span>
            </div>

            <!-- KPI Metric Chips -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                <span class="text-gray-500 text-[10px] block">TOTAL REVENUE</span>
                <span class="text-white text-sm font-bold">$1,248,500</span>
                <span class="text-emerald-400 text-[10px] block">+14.2% YoY</span>
              </div>
              <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                <span class="text-gray-500 text-[10px] block">ACTIVE TRANSACTIONS</span>
                <span class="text-white text-sm font-bold">48,219</span>
                <span class="text-cyan-400 text-[10px] block">Cleaned with NumPy</span>
              </div>
              <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                <span class="text-gray-500 text-[10px] block">PROFIT MARGIN</span>
                <span class="text-white text-sm font-bold">28.4%</span>
                <span class="text-emerald-400 text-[10px] block">Optimal Tier</span>
              </div>
              <div class="p-3 rounded-xl bg-noir-900 border border-white/10">
                <span class="text-gray-500 text-[10px] block">ANOMALY DEFECTS</span>
                <span class="text-white text-sm font-bold">0.02%</span>
                <span class="text-emerald-400 text-[10px] block">Auto-Flagged</span>
              </div>
            </div>

            <!-- AI Natural Language Prompt Query Simulator -->
            <div class="p-3.5 rounded-xl bg-noir-900 border border-white/10 space-y-2">
              <div class="flex items-center space-x-2">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-emerald-400"></i>
                <span class="text-gray-300 font-bold text-[11px]">AI Dataset Query Bar (Natural Language):</span>
              </div>
              <div class="flex items-center space-x-2">
                <input type="text" id="biQueryInput" value="Show top 3 performing product categories and forecast next quarter" class="flex-1 bg-noir-950 border border-white/15 rounded-lg px-3 py-2 text-white focus:outline-none focus:border-emerald-400 text-xs">
                <button onclick="runBiSim()" class="px-4 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-noir-950 font-bold uppercase text-xs">
                  ANALYZE
                </button>
              </div>
              <div id="biOutput" class="text-gray-400 text-[11px] pt-1">
                &gt; Click "ANALYZE" to trigger automated Pandas aggregation and chart generation.
              </div>
            </div>
          </div>
        </div>

        <!-- =================================================================== -->
        <!-- PROJECT 4: TASK MANAGEMENT SYSTEM -->
        <!-- =================================================================== -->
        <div class="theme-card p-7 sm:p-9 rounded-3xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-purple-400 font-bold uppercase tracking-wider">PROJECT 04 &bull; STREAMLIT APPLICATION</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold text-white dark:text-white">Task Management System</h3>
            </div>
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-300 text-xs font-mono">Object-Oriented Python</span>
              <span class="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-xs font-mono">Keyword Categorization</span>
            </div>
          </div>

          <!-- Bullet Points (Beautifully Justified) -->
          <ul class="space-y-2.5 text-xs sm:text-sm text-gray-300 dark:text-gray-300 font-sans text-justify-pretty leading-relaxed">
            <li class="flex items-start space-x-2.5">
              <span class="text-purple-400 font-bold">&bull;</span>
              <span>A console-based Task Management System developed using Object-Oriented Programming in Python, designed to help users efficiently manage their tasks.</span>
            </li>
            <li class="flex items-start space-x-2.5">
              <span class="text-purple-400 font-bold">&bull;</span>
              <span>The application automatically categorizes tasks into Work, Study, Personal, or General using keyword-based detection and allows users to add, search, view, and delete tasks.</span>
            </li>
          </ul>

          <!-- Custom Visual: Interactive Automated Keyword Categorizer Simulation -->
          <div class="bg-noir-950 dark:bg-noir-950 p-6 rounded-2xl border border-white/10 space-y-5 font-mono text-xs">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 pb-3">
              <span class="text-white font-bold flex items-center space-x-2">
                <i data-lucide="check-square" class="w-4 h-4 text-purple-400"></i>
                <span>AUTOMATIC CATEGORIZATION ENGINE</span>
              </span>
              <span class="text-purple-400 text-[11px]">OOP ARCHITECTURE: TASKMANAGER CLASS</span>
            </div>

            <!-- Interactive Task Input -->
            <div class="flex flex-col sm:flex-row items-center gap-2">
              <input type="text" id="taskInput" placeholder="Type a task: e.g. Finish Python OOP assignment for University..." class="flex-1 bg-noir-900 border border-white/15 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-purple-400 text-xs w-full">
              <button onclick="addTaskInteractive()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-purple-500 hover:bg-purple-400 text-noir-950 font-bold text-xs uppercase flex items-center justify-center space-x-1.5 transition-all">
                <span>ADD TASK</span>
                <i data-lucide="plus" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <!-- 4 Categorized Columns -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-2">
              
              <!-- Work Column -->
              <div class="p-3 rounded-xl bg-noir-900 border border-cyan-500/20 space-y-2">
                <div class="flex items-center justify-between text-cyan-400 font-bold text-[11px]">
                  <span>💼 WORK</span>
                  <span id="badgeWork" class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/10 border border-cyan-500/30">1</span>
                </div>
                <div id="colWork" class="space-y-1.5 min-h-[50px]">
                  <div class="p-2 rounded bg-noir-950 text-[11px] text-gray-300 border border-white/5 flex justify-between items-center">
                    <span>Deploy TCS MLflow pipeline</span>
                    <button onclick="this.parentElement.remove()" class="text-gray-500 hover:text-red-400">&times;</button>
                  </div>
                </div>
              </div>

              <!-- Study Column -->
              <div class="p-3 rounded-xl bg-noir-900 border border-purple-500/20 space-y-2">
                <div class="flex items-center justify-between text-purple-400 font-bold text-[11px]">
                  <span>📚 STUDY</span>
                  <span id="badgeStudy" class="text-[10px] px-1.5 py-0.5 rounded bg-purple-500/10 border border-purple-500/30">1</span>
                </div>
                <div id="colStudy" class="space-y-1.5 min-h-[50px]">
                  <div class="p-2 rounded bg-noir-950 text-[11px] text-gray-300 border border-white/5 flex justify-between items-center">
                    <span>Review IIT Madras CNN proof</span>
                    <button onclick="this.parentElement.remove()" class="text-gray-500 hover:text-red-400">&times;</button>
                  </div>
                </div>
              </div>

              <!-- Personal Column -->
              <div class="p-3 rounded-xl bg-noir-900 border border-gold-500/20 space-y-2">
                <div class="flex items-center justify-between text-gold-400 font-bold text-[11px]">
                  <span>🎨 PERSONAL</span>
                  <span id="badgePersonal" class="text-[10px] px-1.5 py-0.5 rounded bg-gold-500/10 border border-gold-500/30">1</span>
                </div>
                <div id="colPersonal" class="space-y-1.5 min-h-[50px]">
                  <div class="p-2 rounded bg-noir-950 text-[11px] text-gray-300 border border-white/5 flex justify-between items-center">
                    <span>Charcoal portrait sketch session</span>
                    <button onclick="this.parentElement.remove()" class="text-gray-500 hover:text-red-400">&times;</button>
                  </div>
                </div>
              </div>

              <!-- General Column -->
              <div class="p-3 rounded-xl bg-noir-900 border border-gray-500/20 space-y-2">
                <div class="flex items-center justify-between text-gray-300 font-bold text-[11px]">
                  <span>📋 GENERAL</span>
                  <span id="badgeGeneral" class="text-[10px] px-1.5 py-0.5 rounded bg-white/10 border border-white/20">1</span>
                </div>
                <div id="colGeneral" class="space-y-1.5 min-h-[50px]">
                  <div class="p-2 rounded bg-noir-950 text-[11px] text-gray-300 border border-white/5 flex justify-between items-center">
                    <span>Sync calendar reminders</span>
                    <button onclick="this.parentElement.remove()" class="text-gray-500 hover:text-red-400">&times;</button>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 6: OBSERVATIONAL SKETCH STUDIO (INSTAGRAM FEED) -->
    <!-- ======================================================================= -->
    <section id="sketches" class="py-12">
      
      <div class="mb-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-1">
          <span class="text-xs font-mono text-gold-400 tracking-wider uppercase font-bold">ACT V &bull; OBSERVATIONAL SKETCHBOOK</span>
          <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">Graphite &amp; Drawing Studio</h2>
          <p class="text-xs text-gray-400 font-mono">Instagram-style feed of Shreyas\'s original drawings. Double-tap to like, leave comments, or post your own.</p>
        </div>

        <button onclick="openNewPostModal()" class="px-5 py-2.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider flex items-center space-x-2 shadow-lg self-start sm:self-auto transition-transform hover:scale-105">
          <i data-lucide="plus-circle" class="w-4 h-4"></i>
          <span>POST NEW DRAWING</span>
        </button>
      </div>

      <!-- Feed Controls -->
      <div class="flex flex-wrap items-center justify-between gap-3 mb-8 border-b border-white/10 pb-4">
        <div class="flex flex-wrap items-center gap-1.5 text-xs font-mono">
          <button onclick="filterDrawingCategory('all')" class="draw-filter-btn active px-3 py-1 rounded-lg bg-gold-500 text-noir-950 font-bold transition-all">ALL</button>
          <button onclick="filterDrawingCategory('portrait')" class="draw-filter-btn px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-gray-300 hover:text-white transition-all">PORTRAITS</button>
          <button onclick="filterDrawingCategory('perspective')" class="draw-filter-btn px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-gray-300 hover:text-white transition-all">PERSPECTIVE</button>
          <button onclick="filterDrawingCategory('cyber')" class="draw-filter-btn px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-gray-300 hover:text-white transition-all">CYBERNETIC</button>
          <button onclick="filterDrawingCategory('charcoal')" class="draw-filter-btn px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-gray-300 hover:text-white transition-all">CHARCOAL</button>
        </div>

        <button onclick="loadSampleSketches()" class="text-xs font-mono text-gray-400 hover:text-gold-400 flex items-center space-x-1.5 transition-colors">
          <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
          <span>LOAD SAMPLES</span>
        </button>
      </div>

      <!-- Posts Container -->
      <div id="postsFeedContainer" class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Empty State -->
      <div id="emptyFeedState" class="hidden text-center py-16 theme-card rounded-2xl space-y-3">
        <i data-lucide="image" class="w-10 h-10 text-gold-400/50 mx-auto"></i>
        <h4 class="text-base font-display font-bold text-white dark:text-white">No Drawings In Feed</h4>
        <p class="text-xs text-gray-400 max-w-xs mx-auto">Click "+ POST NEW DRAWING" above to publish your original art, or click below to load curated sketches.</p>
        <button onclick="loadSampleSketches()" class="px-4 py-2 rounded-xl bg-gold-500 text-noir-950 font-bold text-xs uppercase">
          LOAD SAMPLES
        </button>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 7: CONTACT & APPRECIATION -->
    <!-- ======================================================================= -->
    <section id="contact" class="py-12">
      
      <div class="mb-10 text-center space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">CONNECT &bull; TRANSMISSION</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white dark:text-white tracking-tight">Let\'s Build Together</h2>
        <p class="text-xs text-gray-400 font-mono">Available for machine learning collaborations, computer vision systems, and creative discussions.</p>
      </div>

      <!-- Appreciation Beacon Button -->
      <div class="mb-12 text-center">
        <button id="globalLikeBtn" onclick="triggerGlobalLikeCount(event)" class="inline-flex items-center space-x-3 px-6 py-3.5 rounded-2xl bg-noir-900 border border-white/15 hover:border-heart text-white transition-all shadow-lg group">
          <div class="p-2 rounded-full bg-heart/10 text-heart group-hover:scale-125 transition-transform">
            <i data-lucide="heart" class="w-5 h-5 fill-heart"></i>
          </div>
          <div class="text-left font-mono text-xs">
            <span class="text-gray-400 text-[10px] block uppercase">SEND PORTFOLIO APPRECIATION</span>
            <span class="font-bold text-white text-sm"><span id="globalLikeCount">1,482</span> TRANSMISSIONS</span>
          </div>
        </button>
      </div>

      <!-- Contact Dossier & Form -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Channels -->
        <div class="theme-card p-7 rounded-2xl space-y-5 flex flex-col justify-between">
          <div class="space-y-4">
            <h3 class="text-lg font-display font-bold text-white dark:text-white">Direct Channels</h3>
            
            <div class="space-y-3 font-mono text-xs">
              <div class="flex items-center justify-between p-3.5 rounded-xl bg-noir-950 dark:bg-noir-950 border border-white/10">
                <div class="flex items-center space-x-2.5 text-gray-300">
                  <i data-lucide="mail" class="w-4 h-4 text-cyan-400"></i>
                  <span class="select-all">shreyasbj03@gmail.com</span>
                </div>
                <button onclick="copyToClipboard('shreyasbj03@gmail.com', 'Email copied!')" class="text-cyan-400 hover:text-white text-[11px] font-bold">COPY</button>
              </div>

              <div class="flex items-center justify-between p-3.5 rounded-xl bg-noir-950 dark:bg-noir-950 border border-white/10">
                <div class="flex items-center space-x-2.5 text-gray-300">
                  <i data-lucide="phone" class="w-4 h-4 text-gold-400"></i>
                  <span class="select-all">+91 9110464228</span>
                </div>
                <a href="tel:+919110464228" class="text-gold-400 hover:text-white text-[11px] font-bold">CALL</a>
              </div>

              <div class="flex items-center justify-between p-3.5 rounded-xl bg-noir-950 dark:bg-noir-950 border border-white/10 text-gray-300">
                <div class="flex items-center space-x-2.5">
                  <i data-lucide="map-pin" class="w-4 h-4 text-emerald-400"></i>
                  <span>Bangalore &bull; Chikkamagaluru, India</span>
                </div>
                <span class="text-emerald-400 text-[11px]">IST (UTC+5:30)</span>
              </div>
            </div>
          </div>

          <!-- Socials -->
          <div class="pt-4 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-mono text-gray-400">DIGITAL REACH:</span>
            <div class="flex items-center space-x-2">
              <a href="https://linkedin.com/in/shreyas-b-j-975988226" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-cyan-400 border border-white/10 transition-colors" title="LinkedIn">
                <i data-lucide="linkedin" class="w-4 h-4"></i>
              </a>
              <a href="https://github.com/shreyasbj03" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-cyan-400 border border-white/10 transition-colors" title="GitHub">
                <i data-lucide="github" class="w-4 h-4"></i>
              </a>
              <a href="#sketches" class="p-2.5 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-gold-400 border border-white/10 transition-colors" title="Sketches">
                <i data-lucide="instagram" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Form -->
        <div class="theme-card p-7 rounded-2xl space-y-4">
          <h3 class="text-lg font-display font-bold text-white dark:text-white">Send a Message</h3>
          
          <form onsubmit="handleContactSubmit(event)" class="space-y-3 font-mono text-xs">
            <div>
              <label class="block text-gray-400 mb-1">NAME</label>
              <input type="text" id="contactName" required placeholder="Your Name" class="w-full bg-noir-950 dark:bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-cyan-400">
            </div>
            <div>
              <label class="block text-gray-400 mb-1">EMAIL</label>
              <input type="email" id="contactEmail" required placeholder="your.email@domain.com" class="w-full bg-noir-950 dark:bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-cyan-400">
            </div>
            <div>
              <label class="block text-gray-400 mb-1">MESSAGE</label>
              <textarea id="contactMessage" required rows="3" placeholder="Hello Shreyas, I would like to discuss..." class="w-full bg-noir-950 dark:bg-noir-950 border border-white/15 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-400 resize-none font-sans"></textarea>
            </div>
            <button type="submit" class="w-full py-3.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all">
              SEND MESSAGE
            </button>
          </form>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- FOOTER -->
    <!-- ======================================================================= -->
    <footer class="py-12 border-t border-white/10 text-center font-mono text-xs text-gray-400 space-y-1.5">
      <p class="text-gray-300">SHREYAS B J &bull; AI / ML ENGINEER &bull; B.E. ECE (8.89 CGPA)</p>
      <p class="text-[11px]">BANGALORE &bull; CHIKKAMAGALURU, KARNATAKA, INDIA</p>
    </footer>

  </main>

  <!-- ========================================================================= -->
  <!-- MODAL: POST NEW DRAWING -->
  <!-- ========================================================================= -->
  <div id="newPostModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="theme-card max-w-lg w-full p-6 sm:p-7 rounded-2xl space-y-5 relative max-h-[90vh] overflow-y-auto">
      
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <h3 class="text-lg font-display font-bold text-white flex items-center space-x-2">
          <i data-lucide="plus-circle" class="w-5 h-5 text-gold-400"></i>
          <span>Post New Drawing</span>
        </h3>
        <button onclick="closeNewPostModal()" class="p-1.5 text-gray-400 hover:text-white transition-colors">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form onsubmit="handleCreatePost(event)" class="space-y-4 font-mono text-xs">
        
        <!-- Image Upload -->
        <div class="space-y-1">
          <label class="block text-gray-400">DRAWING IMAGE</label>
          <div onclick="document.getElementById('postImageInput').click()" class="border border-dashed border-white/20 hover:border-gold-400 rounded-xl p-5 text-center cursor-pointer bg-noir-950 transition-colors">
            <input type="file" id="postImageInput" accept="image/*" class="hidden" onchange="handlePreviewPostImage(event)" required>
            <div id="uploadPlaceholder">
              <i data-lucide="image" class="w-6 h-6 text-gold-400 mx-auto mb-1"></i>
              <span class="text-white block font-bold">Select Drawing Photo</span>
              <span class="text-gray-500 text-[10px]">PNG, JPG, or WEBP</span>
            </div>
            <div id="imagePreviewContainer" class="hidden">
              <img id="imagePreviewEl" src="" class="max-h-48 mx-auto rounded-lg object-contain">
            </div>
          </div>
        </div>

        <div>
          <label class="block text-gray-400 mb-1">TITLE</label>
          <input type="text" id="postTitleInput" required placeholder="e.g. Portrait Study in 6B Graphite" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2 text-white focus:outline-none focus:border-gold-400">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-gray-400 mb-1">CATEGORY</label>
            <select id="postCategorySelect" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-gold-400">
              <option value="portrait">Portraits</option>
              <option value="perspective">Perspective</option>
              <option value="cyber">Cybernetic</option>
              <option value="charcoal">Charcoal</option>
            </select>
          </div>
          <div>
            <label class="block text-gray-400 mb-1">MEDIUM</label>
            <input type="text" id="postMediumInput" required placeholder="e.g. Graphite on Paper" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-gold-400">
          </div>
        </div>

        <div>
          <label class="block text-gray-400 mb-1">CAPTION</label>
          <textarea id="postCaptionInput" rows="2" placeholder="Notes on lighting, cross-hatching, anatomy..." class="w-full bg-noir-950 border border-white/15 rounded-xl p-3 text-white focus:outline-none focus:border-gold-400 resize-none font-sans text-xs"></textarea>
        </div>

        <button type="submit" class="w-full py-3 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all">
          PUBLISH TO STUDIO
        </button>
      </form>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: LIGHTBOX -->
  <!-- ========================================================================= -->
  <div id="lightboxModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex flex-col items-center justify-center p-4">
    <button onclick="closeLightbox()" class="absolute top-5 right-5 p-2 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors">
      <i data-lucide="x" class="w-6 h-6"></i>
    </button>
    <div class="max-w-4xl max-h-[80vh] w-full flex items-center justify-center">
      <img id="lightboxImg" src="" class="max-h-[75vh] max-w-full object-contain rounded-xl shadow-2xl">
    </div>
    <div class="mt-3 text-center">
      <h4 id="lightboxTitle" class="text-base font-display font-bold text-white">Artwork Title</h4>
      <p id="lightboxDetails" class="text-xs font-mono text-gold-400">Medium</p>
    </div>
  </div>

  <!-- Toast -->
  <div id="toastMessage" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 pointer-events-none">
    <div class="bg-noir-900 border border-cyan-400/50 px-4 py-2.5 rounded-xl shadow-xl flex items-center space-x-2.5 text-xs font-mono text-white">
      <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
      <span id="toastText">Notification message</span>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT MASTER CONTROLLER -->
  <!-- ========================================================================= -->
  <script>
    lucide.createIcons();

    // -------------------------------------------------------------------------
    // 1. LIGHT / DARK MODE CONTROLLER
    // -------------------------------------------------------------------------
    function initTheme() {
      const savedTheme = localStorage.getItem('shreyas_theme_pref');
      if (savedTheme === 'light') {
        document.documentElement.classList.remove('dark');
        updateThemeIcon(false);
      } else {
        document.documentElement.classList.add('dark');
        updateThemeIcon(true);
      }
    }

    function toggleThemeMode() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('shreyas_theme_pref', isDark ? 'dark' : 'light');
      updateThemeIcon(isDark);
      showToast(isDark ? 'Dark Mode Activated' : 'Light Mode Activated');
    }

    function updateThemeIcon(isDark) {
      const icon = document.getElementById('themeIcon');
      if (!icon) return;
      if (isDark) {
        icon.setAttribute('data-lucide', 'sun');
        icon.className = 'w-4 h-4 text-amber-300';
      } else {
        icon.setAttribute('data-lucide', 'moon');
        icon.className = 'w-4 h-4 text-indigo-600';
      }
      lucide.createIcons();
    }
    initTheme();

    // -------------------------------------------------------------------------
    // 2. TWINKLING STARFIELD ENGINE (DOTS SHINING LIKE STARS)
    // -------------------------------------------------------------------------
    (function initStarfield() {
      const canvas = document.getElementById('starfieldCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let width, height;

      function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      let mouse = { x: width / 2, y: height / 2, targetX: width / 2, targetY: height / 2 };
      window.addEventListener('mousemove', (e) => {
        mouse.targetX = e.clientX;
        mouse.targetY = e.clientY;
      });

      const starColors = [
        { r: 255, g: 255, b: 255 },
        { r: 253, g: 224, b: 139 },
        { r: 186, g: 230, b: 253 },
        { r: 240, g: 249, b: 255 },
      ];

      const count = window.innerWidth < 768 ? 95 : 175;
      const stars = [];

      for (let i = 0; i < count; i++) {
        const isBrightFocal = Math.random() < 0.12;
        const radius = isBrightFocal ? (Math.random() * 0.7 + 1.6) : (Math.random() * 0.7 + 0.7);
        const rgb = starColors[Math.floor(Math.random() * starColors.length)];
        const z = Math.random() * 0.8 + 0.2;

        stars.push({
          x: Math.random() * width,
          y: Math.random() * height,
          baseRadius: radius,
          rgb,
          z,
          baseAlpha: Math.random() * 0.3 + 0.25,
          twinkleSpeed: Math.random() * 0.035 + 0.015,
          phase: Math.random() * Math.PI * 2,
          driftY: -(Math.random() * 0.15 + 0.04) * z,
          driftX: (Math.random() - 0.5) * 0.05 * z,
          isFocal: isBrightFocal
        });
      }

      let time = 0;
      function renderStars() {
        ctx.clearRect(0, 0, width, height);
        time += 1;

        const isDark = document.documentElement.classList.contains('dark');

        mouse.x += (mouse.targetX - mouse.x) * 0.04;
        mouse.y += (mouse.targetY - mouse.y) * 0.04;
        const parallaxOffsetX = (mouse.x - width / 2) * 0.018;
        const parallaxOffsetY = (mouse.y - height / 2) * 0.018;

        for (let i = 0; i < stars.length; i++) {
          const s = stars[i];

          s.y += s.driftY;
          s.x += s.driftX;

          if (s.y < -10) s.y = height + 10;
          if (s.y > height + 10) s.y = -10;
          if (s.x < -10) s.x = width + 10;
          if (s.x > width + 10) s.x = -10;

          const drawX = s.x - parallaxOffsetX * s.z;
          const drawY = s.y - parallaxOffsetY * s.z;

          const wave = Math.sin(time * s.twinkleSpeed + s.phase);
          const alpha = Math.max(0.12, Math.min(1.0, s.baseAlpha + wave * (1 - s.baseAlpha) * 0.65));

          // Draw glow halo for brighter focal stars
          if (s.isFocal && alpha > 0.5 && isDark) {
            const glowRadius = s.baseRadius * 3.8;
            const grad = ctx.createRadialGradient(drawX, drawY, 0, drawX, drawY, glowRadius);
            grad.addColorStop(0, `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha * 0.45})`);
            grad.addColorStop(0.5, `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha * 0.12})`);
            grad.addColorStop(1, 'rgba(0,0,0,0)');

            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(drawX, drawY, glowRadius, 0, Math.PI * 2);
            ctx.fill();

            // 4-point cross glint
            if (alpha > 0.72) {
              const glintLen = s.baseRadius * 3.2 * (alpha - 0.6);
              ctx.strokeStyle = `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha * 0.4})`;
              ctx.lineWidth = 0.65;
              ctx.beginPath();
              ctx.moveTo(drawX - glintLen, drawY);
              ctx.lineTo(drawX + glintLen, drawY);
              ctx.moveTo(drawX, drawY - glintLen);
              ctx.lineTo(drawX, drawY + glintLen);
              ctx.stroke();
            }
          }

          // Star Dot
          ctx.beginPath();
          ctx.arc(drawX, drawY, s.baseRadius, 0, Math.PI * 2);
          if (isDark) {
            ctx.fillStyle = `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha})`;
          } else {
            // In light mode, subtle slate shimmer stars
            ctx.fillStyle = `rgba(100, 116, 139, ${alpha * 0.35})`;
          }
          ctx.fill();
        }

        requestAnimationFrame(renderStars);
      }
      renderStars();
    })();

    // -------------------------------------------------------------------------
    // 3. ADAPTIVE PROFILE PHOTO CONTROLLER
    // -------------------------------------------------------------------------
    const profilePhotoInput = document.getElementById('profilePhotoInput');
    const profilePhotoImg = document.getElementById('profilePhotoImg');
    const aspectRatioTag = document.getElementById('aspectRatioTag');

    function updateAspect(w, h) {
      if (!aspectRatioTag) return;
      const ratio = (w / h).toFixed(2);
      if (ratio > 1.15) aspectRatioTag.textContent = `LANDSCAPE (${ratio}:1)`;
      else if (ratio < 0.85) aspectRatioTag.textContent = `PORTRAIT (1:${(h/w).toFixed(1)})`;
      else aspectRatioTag.textContent = 'SQUARE (1:1)';
    }

    if (profilePhotoImg) {
      profilePhotoImg.onload = function() {
        updateAspect(this.naturalWidth || 400, this.naturalHeight || 400);
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
          } catch (err) {}
          showToast('Profile photo updated successfully!');
        };
        reader.readAsDataURL(file);
      });
    }

    // -------------------------------------------------------------------------
    // 4. CERTIFICATE IMAGE UPLOAD HANDLER
    // -------------------------------------------------------------------------
    function handleCertUpload(e, certIndex) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (event) => {
        const dataUrl = event.target.result;
        const imgEl = document.getElementById('certImg_' + certIndex);
        const placeholderEl = document.getElementById('certPlaceholder_' + certIndex);
        if (imgEl && placeholderEl) {
          imgEl.src = dataUrl;
          imgEl.classList.remove('hidden');
          placeholderEl.classList.add('hidden');
        }
        try {
          localStorage.setItem('shreyas_cert_img_' + certIndex, dataUrl);
        } catch (err) {}
        showToast(`Certificate #${certIndex} uploaded and saved!`);
      };
      reader.readAsDataURL(file);
    }

    // Restore saved certificates from localStorage
    for (let i = 1; i <= 6; i++) {
      const savedCert = localStorage.getItem('shreyas_cert_img_' + i);
      if (savedCert) {
        const imgEl = document.getElementById('certImg_' + i);
        const placeholderEl = document.getElementById('certPlaceholder_' + i);
        if (imgEl && placeholderEl) {
          imgEl.src = savedCert;
          imgEl.classList.remove('hidden');
          placeholderEl.classList.add('hidden');
        }
      }
    }

    // -------------------------------------------------------------------------
    // 5. PROJECT 1: TRAVEL AI AGENT SIMULATOR
    // -------------------------------------------------------------------------
    function runTravelSim() {
      const input = document.getElementById('travelInput').value.trim();
      const output = document.getElementById('travelOutput');
      if (!input) return;

      output.innerHTML = `
        <p class="text-cyan-400">&gt; Query dispatched: "${input}"</p>
        <p class="text-gray-400">&gt; ChromaDB Vector search: querying 1,420 grounded destination embeddings...</p>
      `;

      setTimeout(() => {
        output.innerHTML += `
          <p class="text-emerald-400">&gt; Cosine similarity 0.942 &bull; 3 relevant policy &amp; itinerary matches retrieved.</p>
          <div class="p-2.5 mt-2 rounded bg-noir-950 border border-cyan-400/30 text-white font-sans text-xs space-y-1">
            <span class="font-bold text-cyan-400 block font-mono">&check; PERSONALIZED AGENT ITINERARY:</span>
            <p class="text-gray-300 leading-relaxed">&bull; Day 1: Arashiyama Bamboo Grove &amp; Tenryu-ji Temple (Budget Entry).<br>&bull; Day 2: Fushimi Inari morning hike &bull; Gion cultural archives photography.<br>&bull; Day 3: Golden Pavilion (Kinkaku-ji) &bull; Local Matcha tasting &bull; Advisory: Clear skies, 18&deg;C.</p>
          </div>
        `;
      }, 700);
    }

    // -------------------------------------------------------------------------
    // 6. PROJECT 2: PORTFOLIO TYPEWRITER
    // -------------------------------------------------------------------------
    const typewriterRoles = ['AI/ML Engineer', 'Full-Stack Developer', 'Hardware Reliability Analyst', 'Observational Sketch Artist'];
    let twIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const twElement = document.getElementById('portfolioTypewriterText');

    function stepTypewriter() {
      if (!twElement) return;
      const currentWord = typewriterRoles[twIndex];

      if (isDeleting) {
        twElement.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
      } else {
        twElement.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
      }

      let speed = isDeleting ? 40 : 90;

      if (!isDeleting && charIndex === currentWord.length) {
        speed = 1800;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        twIndex = (twIndex + 1) % typewriterRoles.length;
        speed = 400;
      }

      setTimeout(stepTypewriter, speed);
    }
    stepTypewriter();

    // -------------------------------------------------------------------------
    // 7. PROJECT 3: BUSINESS INTELLIGENCE PLATFORM SIMULATOR
    // -------------------------------------------------------------------------
    function runBiSim() {
      const query = document.getElementById('biQueryInput').value.trim();
      const output = document.getElementById('biOutput');
      if (!query) return;

      output.innerHTML = `
        <span class="text-emerald-400">&gt; Query: "${query}"</span><br>
        &gt; Running Pandas aggregation over 48,219 Excel records...<br>
        <span class="text-white font-bold">&gt; Insights Generated:</span> Top Categories: [Electronics: $480k, Cloud Services: $340k, IoT Kits: $220k]. Next quarter forecast: +18.5% confidence based on moving averages.
      `;
    }

    // -------------------------------------------------------------------------
    // 8. PROJECT 4: TASK MANAGEMENT AUTOMATIC CATEGORIZATION
    // -------------------------------------------------------------------------
    function addTaskInteractive() {
      const input = document.getElementById('taskInput');
      const text = input.value.trim();
      if (!text) return;

      const lower = text.toLowerCase();
      let category = 'general';

      // Keyword detection based on user project specifications
      if (lower.includes('work') || lower.includes('tcs') || lower.includes('code') || lower.includes('pipeline') || lower.includes('deploy') || lower.includes('client') || lower.includes('meeting')) {
        category = 'work';
      } else if (lower.includes('study') || lower.includes('university') || lower.includes('ncet') || lower.includes('exam') || lower.includes('assignment') || lower.includes('cert') || lower.includes('learn')) {
        category = 'study';
      } else if (lower.includes('personal') || lower.includes('sketch') || lower.includes('draw') || lower.includes('art') || lower.includes('health') || lower.includes('gym') || lower.includes('home')) {
        category = 'personal';
      }

      let colId = 'colGeneral';
      let badgeId = 'badgeGeneral';

      if (category === 'work') { colId = 'colWork'; badgeId = 'badgeWork'; }
      else if (category === 'study') { colId = 'colStudy'; badgeId = 'badgeStudy'; }
      else if (category === 'personal') { colId = 'colPersonal'; badgeId = 'badgePersonal'; }

      const col = document.getElementById(colId);
      const card = document.createElement('div');
      card.className = 'p-2 rounded bg-noir-950 text-[11px] text-gray-300 border border-white/5 flex justify-between items-center transition-all';
      card.innerHTML = `<span>${text}</span><button onclick="this.parentElement.remove()" class="text-gray-500 hover:text-red-400">&times;</button>`;
      col.prepend(card);

      showToast(`Task categorized under: ${category.toUpperCase()}`);
      input.value = '';
    }

    // -------------------------------------------------------------------------
    // 9. INSTAGRAM SKETCH FEED STUDIO
    // -------------------------------------------------------------------------
    const POSTS_KEY = 'shreyas_sketch_feed_v4';
    let currentFilter = 'all';
    let draftImage = null;

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
        showToast('Storage quota reached. Please use a smaller image file.');
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
      const filtered = currentFilter === 'all' ? posts : posts.filter(p => p.category === currentFilter);

      if (filtered.length === 0) {
        container.innerHTML = `<p class="col-span-2 text-center text-gray-500 py-10 font-mono text-xs">No sketches in this category.</p>`;
        return;
      }

      container.innerHTML = filtered.map(post => `
        <article class="theme-card rounded-2xl overflow-hidden shadow-xl" id="post-${post.id}">
          <div class="px-5 py-3.5 border-b border-white/10 flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <img src="${profilePhotoImg ? profilePhotoImg.src : './assets/profile-avatar.svg'}" class="w-8 h-8 rounded-full object-cover border border-gold-400/50">
              <div>
                <span class="font-display font-bold text-white dark:text-white text-xs block">Shreyas B J</span>
                <span class="text-[10px] font-mono text-gray-400">@shreyas.sketches &bull; ${post.date || 'Studio'}</span>
              </div>
            </div>
            <button onclick="deletePost('${post.id}')" class="p-1.5 text-gray-500 hover:text-red-400 transition-colors" title="Delete">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          </div>

          <div class="relative bg-noir-950 dark:bg-noir-950 flex items-center justify-center overflow-hidden cursor-pointer select-none" 
               ondblclick="doubleTapLikePost(event, '${post.id}')"
               onclick="handleMediaClick(event, '${post.id}')">
            <img src="${post.image}" alt="${post.title}" class="max-h-[460px] w-auto h-auto max-w-full object-contain mx-auto block">
            
            <div id="heartPop-${post.id}" class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none hidden">
              <i data-lucide="heart" class="w-20 h-20 text-heart fill-heart filter drop-shadow-xl"></i>
            </div>
          </div>

          <div class="p-4 space-y-2.5 font-mono text-xs">
            <div class="flex items-center justify-between text-gray-300">
              <div class="flex items-center space-x-3">
                <button onclick="toggleLikePost(event, '${post.id}')" class="flex items-center space-x-1 hover:text-heart transition-colors">
                  <i data-lucide="heart" class="w-4 h-4 ${post.isLiked ? 'text-heart fill-heart' : ''}"></i>
                  <span class="font-bold text-xs ${post.isLiked ? 'text-heart' : 'text-white'}">${post.likes}</span>
                </button>
                <button onclick="toggleComments('${post.id}')" class="hover:text-white transition-colors flex items-center space-x-1">
                  <i data-lucide="message-circle" class="w-4 h-4"></i>
                  <span>${(post.comments || []).length}</span>
                </button>
                <button onclick="copyPostLink('${post.id}')" class="hover:text-white transition-colors">
                  <i data-lucide="share-2" class="w-4 h-4"></i>
                </button>
              </div>
              <span class="text-[10px] text-gray-400 bg-white/5 px-2 py-0.5 rounded border border-white/10">${post.medium}</span>
            </div>

            <div class="text-xs space-y-0.5 font-sans">
              <p class="text-white dark:text-white font-medium"><span class="font-bold font-display mr-1">shreyas.sketches</span>${post.title}</p>
              <p class="text-gray-300 dark:text-gray-300 text-xs text-justify-pretty">${post.caption}</p>
            </div>

            <div id="comments-${post.id}" class="hidden pt-2.5 border-t border-white/10 space-y-2">
              <div class="space-y-1 max-h-28 overflow-y-auto text-[11px]">
                ${(post.comments || []).map(c => `
                  <div class="bg-noir-950 p-1.5 rounded border border-white/5">
                    <span class="font-bold text-cyan-400 mr-1">${c.user}:</span>
                    <span class="text-gray-300">${c.text}</span>
                  </div>
                `).join('')}
              </div>
              <div class="flex items-center space-x-1.5 pt-1">
                <input type="text" id="commentInput-${post.id}" placeholder="Add a reflection..." class="flex-1 bg-noir-950 border border-white/15 rounded-lg px-2.5 py-1 text-xs text-white focus:outline-none focus:border-gold-400">
                <button onclick="submitComment('${post.id}')" class="px-2.5 py-1 rounded-lg bg-gold-500 hover:bg-gold-400 text-noir-950 font-bold text-xs uppercase">
                  POST
                </button>
              </div>
            </div>

          </div>
        </article>
      `).join('');

      lucide.createIcons();
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
        if (target.isLiked) triggerGlobalLikeCount(e);
      }
    }

    function doubleTapLikePost(e, postId) {
      const heartPop = document.getElementById('heartPop-' + postId);
      if (heartPop) {
        heartPop.classList.remove('hidden');
        heartPop.classList.remove('pop-heart-anim');
        void heartPop.offsetWidth;
        heartPop.classList.add('pop-heart-anim');
        setTimeout(() => heartPop.classList.add('hidden'), 750);
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
      if (e.detail === 2) return;
      const posts = getStoredPosts();
      if (!posts) return;
      const p = posts.find(x => x.id === postId);
      if (!p) return;

      document.getElementById('lightboxImg').src = p.image;
      document.getElementById('lightboxTitle').textContent = p.title;
      document.getElementById('lightboxDetails').textContent = `${p.medium} • ${p.date || 'Studio'}`;
      document.getElementById('lightboxModal').classList.remove('hidden');
    }

    function closeLightbox() {
      document.getElementById('lightboxModal').classList.add('hidden');
    }

    function toggleComments(postId) {
      const el = document.getElementById(`comments-${postId}`);
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
        showToast('Reflection posted!');
      }
    }

    function copyPostLink(postId) {
      navigator.clipboard.writeText(`${window.location.origin}${window.location.pathname}#post-${postId}`);
      showToast('Artwork link copied!');
    }

    function deletePost(postId) {
      if (!confirm('Delete this drawing from feed?')) return;
      let posts = getStoredPosts();
      if (!posts) return;
      posts = posts.filter(p => p.id !== postId);
      saveStoredPosts(posts);
      renderFeed();
      showToast('Drawing removed.');
    }

    function filterDrawingCategory(cat) {
      currentFilter = cat;
      document.querySelectorAll('.draw-filter-btn').forEach(b => {
        b.classList.remove('bg-gold-500', 'text-noir-950', 'font-bold');
        b.classList.add('bg-noir-900', 'text-gray-300');
      });
      event.target.classList.add('bg-gold-500', 'text-noir-950', 'font-bold');
      event.target.classList.remove('bg-noir-900', 'text-gray-300');
      renderFeed();
    }

    function openNewPostModal() {
      document.getElementById('newPostModal').classList.remove('hidden');
    }
    function closeNewPostModal() {
      document.getElementById('newPostModal').classList.add('hidden');
    }

    function handlePreviewPostImage(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        draftImage = event.target.result;
        const previewEl = document.getElementById('imagePreviewEl');
        previewEl.src = draftImage;
        document.getElementById('uploadPlaceholder').classList.add('hidden');
        document.getElementById('imagePreviewContainer').classList.remove('hidden');
      };
      reader.readAsDataURL(file);
    }

    function handleCreatePost(e) {
      e.preventDefault();
      if (!draftImage) {
        alert('Please choose an image file.');
        return;
      }

      const newPost = {
        id: 'post_' + Date.now(),
        title: document.getElementById('postTitleInput').value.trim(),
        medium: document.getElementById('postMediumInput').value.trim(),
        caption: document.getElementById('postCaptionInput').value.trim(),
        category: document.getElementById('postCategorySelect').value,
        image: draftImage,
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
      showToast('Drawing published successfully!');

      e.target.reset();
      draftImage = null;
      document.getElementById('uploadPlaceholder').classList.remove('hidden');
      document.getElementById('imagePreviewContainer').classList.add('hidden');
    }

    function loadSampleSketches() {
      const samplePosts = [
        {
          id: 'sample_portrait_01',
          title: 'Forensic Study: Human Facial Anatomy & Shadows',
          category: 'portrait',
          medium: '6B & 2B Graphite on Cold-Pressed',
          caption: 'Exploration of light fall-off, corneal specular reflections, and bone structure under low-key single-source lighting.',
          image: './assets/drawings/drawing-portrait.svg',
          date: 'Studio Study',
          likes: 42,
          isLiked: false,
          comments: [{ user: 'Kavya', text: 'Stunning tonal transitions!' }]
        },
        {
          id: 'sample_perspective_02',
          title: '3-Point Architectural Perspective & Axial Grid',
          category: 'perspective',
          medium: '0.3mm Fine Fineliner & Marker',
          caption: 'Strict vanishing-point discipline mapping concrete structural cantilevers.',
          image: './assets/drawings/drawing-architecture.svg',
          date: 'Studio Study',
          likes: 38,
          isLiked: false,
          comments: []
        },
        {
          id: 'sample_cyber_03',
          title: 'Cybernetic Cerebral Interface & Neural Traces',
          category: 'cyber',
          medium: 'Charcoal & Gouache Highlights',
          caption: 'Visualizing synthetic neural synapses interwoven with biological cortical layers.',
          image: './assets/drawings/drawing-cybernetic.svg',
          date: 'Lab Study',
          likes: 56,
          isLiked: false,
          comments: []
        },
        {
          id: 'sample_nature_04',
          title: 'Chikkamagaluru Western Ghats Ridge Line',
          category: 'charcoal',
          medium: 'Willow Charcoal on 300 GSM',
          caption: 'Morning mist drifting over the coffee slopes of Mullayanagiri.',
          image: './assets/drawings/drawing-landscape.svg',
          date: 'Western Ghats',
          likes: 67,
          isLiked: false,
          comments: []
        }
      ];

      saveStoredPosts(samplePosts);
      renderFeed();
      showToast('Curated sketches loaded!');
    }

    if (!getStoredPosts() || getStoredPosts().length === 0) {
      loadSampleSketches();
    } else {
      renderFeed();
    }

    // -------------------------------------------------------------------------
    // 10. APPRECIATION BEACON & BALLISTIC PARTICLES
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
      firePhysicalHeartBurst(clientX, clientY, 18);
      showToast('Appreciation transmitted! Thank you.');
    }

    const activeParticles = [];
    let particleAnimRunning = false;

    function firePhysicalHeartBurst(originX, originY, count = 14) {
      const chars = ['❤️', '✨', '💛', '💖', '⭐'];

      for (let i = 0; i < count; i++) {
        const el = document.createElement('div');
        el.className = 'phys-heart-particle';
        el.textContent = chars[Math.floor(Math.random() * chars.length)];
        document.body.appendChild(el);

        const angle = (Math.PI * 2 * i) / count + (Math.random() - 0.5) * 0.5;
        const speed = Math.random() * 8 + 3;

        activeParticles.push({
          el,
          x: originX,
          y: originY,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 4,
          gravity: 0.35,
          drag: 0.94,
          rot: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 14,
          opacity: 1,
          scale: Math.random() * 0.4 + 0.8,
          life: 0,
          maxLife: 55 + Math.random() * 20
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
    // 11. UTILS & CONTACT
    // -------------------------------------------------------------------------
    function handleContactSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('contactName').value;
      showToast(`Thank you, ${name}. Message received!`);
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
      }, 3000);
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('#newPostModal, #lightboxModal').forEach(m => m.classList.add('hidden'));
      }
    });

  </script>
</body>
</html>
'''

target_path = r"C:\Users\Sneha Nishani\.gemini\antigravity\scratch\shreyas-cinematic-portfolio\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated complete enhanced portfolio at {target_path} ({len(html_content)} bytes)")
