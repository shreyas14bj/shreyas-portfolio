# build_clean_simple_portfolio.py
# Clean, minimalist, high-end portfolio tailored to Shreyas B J with the exact geometric square particle visual.

html_content = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
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
    ::-webkit-scrollbar-track { background: #060911; }
    ::-webkit-scrollbar-thumb { background: #18223B; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #38BDF8; }

    /* Clean Card Styling */
    .simple-card {
      background: rgba(11, 16, 29, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
    }
    .simple-card:hover {
      border-color: rgba(56, 189, 248, 0.35);
      transform: translateY(-2px);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.6);
    }

    /* Subtle Reveal on Scroll */
    .reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
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

    /* Interactive image slider */
    .slider-handle {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 2px;
      background: #38BDF8;
      cursor: ew-resize;
      box-shadow: 0 0 12px #38BDF8;
    }
    .slider-handle-button {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #0B101D;
      border: 2px solid #38BDF8;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #38BDF8;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }
  </style>
</head>
<body class="bg-noir-950 text-gray-200 font-sans antialiased selection:bg-cyan-500/25 selection:text-white relative min-h-screen">

  <!-- ========================================================================= -->
  <!-- TWINKLING STARRY NIGHT CANVAS (SMALL SHINING STAR DOTS) -->
  <!-- ========================================================================= -->
  <canvas id="starfieldCanvas" class="fixed inset-0 pointer-events-none z-0 w-full h-full"></canvas>

  <!-- ========================================================================= -->
  <!-- CLEAN TOP NAVIGATION -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 w-full z-50 backdrop-blur-md bg-noir-950/85 border-b border-white/10 px-6 py-4 flex items-center justify-between">
    <a href="#hero" class="flex items-center space-x-2.5 group">
      <!-- Star Luminescence Indicator -->
      <div class="flex items-center space-x-1.5">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse shadow-[0_0_8px_#38BDF8]"></span>
      </div>
      <span class="font-display font-bold text-white text-base tracking-tight group-hover:text-cyan-400 transition-colors">SHREYAS B J</span>
      <span class="text-xs font-mono text-gray-400 hidden sm:inline">&bull; AI / ML Engineer</span>
    </a>

    <!-- Nav Links -->
    <nav class="hidden md:flex items-center space-x-8 text-xs font-mono text-gray-300">
      <a href="#about" class="hover:text-cyan-400 transition-colors">ABOUT</a>
      <a href="#experience" class="hover:text-cyan-400 transition-colors">EXPERIENCE</a>
      <a href="#arsenal" class="hover:text-cyan-400 transition-colors">SKILLS &amp; CERTS</a>
      <a href="#projects" class="hover:text-cyan-400 transition-colors">PROJECTS</a>
      <a href="#sketches" class="hover:text-gold-400 transition-colors">SKETCHES</a>
      <a href="#contact" class="hover:text-cyan-400 transition-colors">CONTACT</a>
    </nav>

    <!-- Header CTA -->
    <div class="flex items-center space-x-3">
      <a href="#contact" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(14,165,233,0.3)]">
        GET IN TOUCH
      </a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- MAIN CONTENT CONTAINER -->
  <!-- ========================================================================= -->
  <main class="relative z-10 pt-24 space-y-24">

    <!-- ======================================================================= -->
    <!-- SECTION 1: HERO -->
    <!-- ======================================================================= -->
    <section id="hero" class="min-h-[82vh] flex flex-col justify-center items-center px-6 text-center max-w-4xl mx-auto space-y-6">
      
      <!-- Current Status Tag -->
      <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-noir-900 border border-white/10 text-xs font-mono text-cyan-400">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
        <span>AI / ML ENGINEER @ TATA CONSULTANCY SERVICES</span>
      </div>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-6xl md:text-7xl font-display font-bold text-white tracking-tight leading-tight">
        Building Intelligent Systems. <br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-gold-400">
          Observing the World.
        </span>
      </h1>

      <!-- Subtitle -->
      <p class="text-base sm:text-lg text-gray-400 max-w-2xl mx-auto leading-relaxed font-sans">
        I am <strong class="text-white font-medium">Shreyas B J</strong>, an AI/ML Engineer merging deep learning pipelines with forensic hardware reliability and fine-art draughtsmanship.
      </p>

      <!-- Key Telemetry Badges -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 w-full max-w-2xl pt-2 font-mono text-xs">
        <div class="p-3.5 rounded-2xl bg-noir-900/80 border border-white/10">
          <span class="block text-xl font-bold text-cyan-400 font-display">8.89</span>
          <span class="text-gray-400 text-[11px]">CGPA &bull; NCET ECE</span>
        </div>
        <div class="p-3.5 rounded-2xl bg-noir-900/80 border border-white/10">
          <span class="block text-xl font-bold text-gold-400 font-display">Foxconn</span>
          <span class="text-gray-400 text-[11px]">Failure Analysis</span>
        </div>
        <div class="p-3.5 rounded-2xl bg-noir-900/80 border border-white/10">
          <span class="block text-xl font-bold text-white font-display">6+ Certs</span>
          <span class="text-gray-400 text-[11px]">Databricks &bull; Cloud</span>
        </div>
        <div class="p-3.5 rounded-2xl bg-noir-900/80 border border-white/10">
          <span class="block text-xl font-bold text-emerald-400 font-display">Studio Art</span>
          <span class="text-gray-400 text-[11px]">Observational Realism</span>
        </div>
      </div>

      <!-- Hero Actions -->
      <div class="pt-4 flex flex-wrap items-center justify-center gap-4">
        <a href="#about" class="px-6 py-3 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all flex items-center space-x-2">
          <span>LEARN ABOUT ME</span>
          <i data-lucide="arrow-down" class="w-4 h-4"></i>
        </a>
        <a href="#sketches" class="px-6 py-3 rounded-xl bg-noir-900 hover:bg-noir-850 border border-white/15 text-white font-display font-bold text-xs uppercase tracking-wider transition-all flex items-center space-x-2">
          <i data-lucide="brush" class="w-4 h-4 text-gold-400"></i>
          <span>VIEW SKETCH STUDIO</span>
        </a>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 2: ABOUT & ADAPTIVE PROFILE FRAME -->
    <!-- ======================================================================= -->
    <section id="about" class="px-6 max-w-5xl mx-auto py-12">
      
      <!-- Section Header -->
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">ABOUT &bull; BIOGRAPHY</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">The Architect</h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Adaptive Profile Frame Column -->
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="relative group w-full max-w-xs">
            
            <!-- Dynamic Aspect-Ratio Hugging Container -->
            <div id="profileFrame" class="simple-card p-3 rounded-2xl transition-all duration-300 w-fit mx-auto shadow-xl">
              <div class="relative overflow-hidden rounded-xl bg-noir-950 border border-white/10 flex items-center justify-center">
                <img id="profilePhotoImg" src="./assets/profile-avatar.svg" alt="Shreyas B J - Portrait" class="max-h-[380px] w-auto h-auto max-w-full object-contain mx-auto block group-hover:scale-[1.01] transition-transform duration-500">
                
                <!-- Aspect Ratio Badge -->
                <div class="absolute bottom-2.5 right-2.5 px-2 py-0.5 rounded bg-noir-950/80 backdrop-blur-md border border-white/20 text-[10px] font-mono text-cyan-400">
                  <span id="aspectRatioTag">PORTRAIT</span>
                </div>
              </div>
            </div>

            <!-- Frame Controls -->
            <div class="mt-4 flex items-center justify-center space-x-2.5 w-full">
              <input type="file" id="profilePhotoInput" accept="image/*" class="hidden">
              <button onclick="document.getElementById('profilePhotoInput').click()" class="px-4 py-2 rounded-xl bg-noir-900 hover:bg-noir-850 border border-white/15 text-xs font-mono text-gray-300 hover:text-white transition-all flex items-center space-x-1.5">
                <i data-lucide="upload" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>UPLOAD PHOTO</span>
              </button>
              <button id="resetProfilePhotoBtn" class="p-2 rounded-xl bg-noir-900 hover:bg-red-500/20 border border-white/10 text-xs text-gray-400 hover:text-red-400 transition-colors" title="Reset to default avatar">
                <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Single Paragraph Biography Column -->
        <div class="lg:col-span-7 space-y-6">
          <div class="simple-card p-8 rounded-2xl space-y-5">
            <h3 class="text-xl font-display font-bold text-white flex items-center space-x-2.5">
              <span>Shreyas B J</span>
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
              <span class="text-xs font-mono text-cyan-400 font-normal">CHIKKAMAGALURU &bull; BANGALORE</span>
            </h3>

            <!-- Single Paragraph Biography -->
            <p class="text-sm sm:text-base text-gray-300 leading-relaxed font-sans text-justify sm:text-left">
              Rooted in the serene hills of <span class="text-gold-400 font-medium">Chikkamagaluru</span> and driven by Bangalore\'s fast-paced engineering ecosystem, I am an <span class="text-white font-medium">AI/ML Engineer at Tata Consultancy Services (TCS)</span> with a solid foundation in <span class="text-white font-medium">Electronics &amp; Communication Engineering</span> from Nagarjuna College of Engineering and Technology (graduating with an <span class="text-cyan-400 font-mono font-semibold">8.89 CGPA</span>). My engineering intuition was honed on high-volume SMT manufacturing lines at <span class="text-cyan-400 font-medium">Foxconn (Hon Hai Technology Group)</span>, where I conducted root-cause failure analysis, schematic tracing, and circuit diagnostics under demanding quality tolerances. Today, I channel that forensic hardware rigor into training scalable deep learning models, deploying computer vision pipelines, and building multi-agent systems certified by <span class="text-gold-400 font-medium">Databricks, Anthropic Claude, and Google Cloud Gemini</span>—all while continuously refining my observation through a lifelong discipline of <span class="text-white font-medium">fine-art sketching</span> that bridges physical observation with algorithmic intelligence.
            </p>

            <div class="border-l-2 border-cyan-400/80 pl-4 py-1 text-xs font-mono text-gray-400 italic">
              "Observing reality with forensic precision—whether through a microscope on an SMT production line or graphite on a sketchpad."
            </div>

            <!-- Fast Specs -->
            <div class="flex flex-wrap gap-2 pt-1 text-[11px] font-mono">
              <span class="px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-cyan-300">#AI/ML</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-gold-300">#ComputerVision</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-emerald-300">#HardwareReliability</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-purple-300">#Databricks</span>
              <span class="px-3 py-1 rounded-lg bg-noir-900 border border-white/10 text-white">#Draughtsmanship</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 3: EXPERIENCE -->
    <!-- ======================================================================= -->
    <section id="experience" class="px-6 max-w-5xl mx-auto py-12">
      
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">EXPERIENCE &bull; TIMELINE</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">Operational Journey</h2>
      </div>

      <div class="space-y-4">
        
        <!-- Role 1: TCS -->
        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg font-display font-bold text-white">Tata Consultancy Services (TCS)</h3>
              <p class="text-xs font-mono text-cyan-400">AI / ML Engineer &bull; Full-Time</p>
            </div>
            <span class="text-xs font-mono text-gray-400">2024 &bull; PRESENT | BANGALORE</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Developing enterprise machine learning workflows, multi-agent LLM systems with LangChain, and automated computer vision inference pipelines. Managing model governance and distributed feature stores using Databricks MLflow.
          </p>
          <div class="flex flex-wrap gap-1.5 pt-1 text-[11px] font-mono text-gray-400">
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">Python</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">PyTorch</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">Databricks</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">LangChain</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">Docker</span>
          </div>
        </div>

        <!-- Role 2: Foxconn -->
        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg font-display font-bold text-white">Foxconn (Hon Hai Technology Group)</h3>
              <p class="text-xs font-mono text-gold-400">Graduate Apprentice &bull; Hardware Failure Analysis</p>
            </div>
            <span class="text-xs font-mono text-gray-400">OCT 2024 &bull; DEC 2024 | SRIPERUMBUDUR</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Conducted forensic hardware failure diagnostics on high-speed SMT lines. Traced high-density PCB schematics, performed In-Circuit Testing (ICT) and Functional Testing (FCT), and diagnosed micro solder bridges to preserve 99.8% production quality.
          </p>
          <div class="flex flex-wrap gap-1.5 pt-1 text-[11px] font-mono text-gray-400">
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">Failure Analysis</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">ICT / FCT</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">SMT Diagnostics</span>
            <span class="px-2.5 py-0.5 rounded bg-noir-900 border border-white/10">Schematics</span>
          </div>
        </div>

        <!-- Role 3: NCET Education -->
        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg font-display font-bold text-white">Nagarjuna College of Engineering &amp; Technology (NCET)</h3>
              <p class="text-xs font-mono text-cyan-400">B.E. in Electronics &amp; Communication Engineering (VTU)</p>
            </div>
            <span class="text-xs font-mono text-cyan-400 font-bold">8.89 CGPA | 2021 &bull; 2025</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Graduated with distinction with an 8.89 CGPA. Capstone Project: Autonomous Multi-Sensor Rover with real-time LIDAR sensor fusion, obstacle detection, and edge compute on NVIDIA Jetson.
          </p>
        </div>

        <!-- Role 4: Skill Craft -->
        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 border-b border-white/10 pb-3">
            <div>
              <h3 class="text-lg font-display font-bold text-white">Skill Craft Technology</h3>
              <p class="text-xs font-mono text-emerald-400">Machine Learning Intern</p>
            </div>
            <span class="text-xs font-mono text-gray-400">MAY 2024 &bull; JUN 2024</span>
          </div>
          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Constructed predictive classification pipelines, exploratory data analysis workflows, and feature engineering benchmarks with Scikit-Learn and Pandas.
          </p>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 4: ARSENAL & VERIFIED CERTIFICATIONS -->
    <!-- ======================================================================= -->
    <section id="arsenal" class="px-6 max-w-5xl mx-auto py-12">
      
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">SKILLS &bull; ACCREDITATIONS</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">Technical Arsenal</h2>
      </div>

      <!-- Skills Pillars -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        
        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex items-center space-x-2.5 text-cyan-400 font-bold text-sm">
            <i data-lucide="brain" class="w-4 h-4"></i>
            <span>AI &amp; Computer Vision</span>
          </div>
          <div class="flex flex-wrap gap-1.5 text-xs font-mono text-gray-300">
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">PyTorch</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">TensorFlow</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">OpenCV</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">YOLOv8</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">LangChain</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Transformers</span>
          </div>
        </div>

        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex items-center space-x-2.5 text-gold-400 font-bold text-sm">
            <i data-lucide="cpu" class="w-4 h-4"></i>
            <span>Electronics &amp; Hardware</span>
          </div>
          <div class="flex flex-wrap gap-1.5 text-xs font-mono text-gray-300">
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Failure Analysis</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">ICT / FCT</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">SMT Diagnostics</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">STM32 / ESP32</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Embedded C</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Sensor Fusion</span>
          </div>
        </div>

        <div class="simple-card p-6 rounded-2xl space-y-3">
          <div class="flex items-center space-x-2.5 text-emerald-400 font-bold text-sm">
            <i data-lucide="database" class="w-4 h-4"></i>
            <span>Cloud &amp; MLOps</span>
          </div>
          <div class="flex flex-wrap gap-1.5 text-xs font-mono text-gray-300">
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Databricks</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">MLflow</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Apache Spark</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Docker</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">SQL / SQLite</span>
            <span class="px-2.5 py-1 rounded-lg bg-noir-900 border border-white/10">Git &bull; Linux</span>
          </div>
        </div>

      </div>

      <!-- 6 Industry Certifications -->
      <div class="space-y-4">
        <h3 class="text-sm font-mono text-gray-400 uppercase tracking-wider font-bold">6 Verified Accreditations:</h3>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          
          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-cyan-400 font-bold">DATABRICKS</span>
            <h4 class="font-display font-bold text-white text-sm">Certified Associate — Machine Learning</h4>
            <p class="text-xs text-gray-400">Distributed Spark, MLflow, scalable feature engineering.</p>
          </div>

          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-gold-400 font-bold">ANTHROPIC</span>
            <h4 class="font-display font-bold text-white text-sm">Claude Certified Prompt Engineer</h4>
            <p class="text-xs text-gray-400">Agentic orchestration, structured steering, XML pipelines.</p>
          </div>

          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-cyan-400 font-bold">GOOGLE CLOUD</span>
            <h4 class="font-display font-bold text-white text-sm">Gemini AI Certified Developer</h4>
            <p class="text-xs text-gray-400">Multimodal vision, Vertex AI embeddings, sub-second latency.</p>
          </div>

          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-emerald-400 font-bold">IIT MADRAS / NPTEL</span>
            <h4 class="font-display font-bold text-white text-sm">Deep Learning &amp; Microprocessors</h4>
            <p class="text-xs text-gray-400">CNNs, RNNs, backpropagation proofs, hardware architecture.</p>
          </div>

          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-purple-400 font-bold">NXT WAVE</span>
            <h4 class="font-display font-bold text-white text-sm">Python Full Stack Specialist</h4>
            <p class="text-xs text-gray-400">Full stack Python, relational SQL schemas, API architecture.</p>
          </div>

          <div class="simple-card p-5 rounded-2xl space-y-1.5">
            <span class="text-[10px] font-mono text-cyan-400 font-bold">TECHNICAL HUB</span>
            <h4 class="font-display font-bold text-white text-sm">Embedded Systems &amp; IoT</h4>
            <p class="text-xs text-gray-400">Microcontroller interfacing, firmware protocols (I2C, SPI, UART).</p>
          </div>

        </div>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 5: FEATURED PROJECTS -->
    <!-- ======================================================================= -->
    <section id="projects" class="px-6 max-w-5xl mx-auto py-12">
      
      <div class="mb-10 space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">PROJECTS &bull; IMPLEMENTATIONS</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">Engineering Creations</h2>
      </div>

      <div class="space-y-8">
        
        <!-- Project 1: OmniTravel Multi-Agent -->
        <div class="simple-card p-7 rounded-2xl space-y-5">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/10 pb-4">
            <div>
              <span class="text-[10px] font-mono text-cyan-400 font-bold uppercase">PROJECT 01 &bull; MULTI-AGENT LLM</span>
              <h3 class="text-xl font-display font-bold text-white">OmniTravel Agentic Orchestrator</h3>
            </div>
            <span class="text-xs font-mono text-gray-400">LangChain &bull; RAG &bull; ChromaDB</span>
          </div>

          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Hierarchical multi-agent framework that accepts free-form travel requests, checks historical travel vectors with cosine similarity, verifies real-time weather telemetry, and generates grounded day-by-day itineraries.
          </p>

          <!-- Interactive Prompt Test -->
          <div class="bg-noir-950 p-4 rounded-xl border border-white/10 space-y-3 font-mono text-xs">
            <div class="flex items-center space-x-2">
              <input type="text" id="travelInput" value="Kyoto 4-day Zen temple & digital art tour on a budget" class="flex-1 bg-noir-900 border border-white/15 rounded-lg px-3 py-2 text-white focus:outline-none focus:border-cyan-400">
              <button onclick="runTravelSim()" class="px-4 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-bold uppercase">
                TEST
              </button>
            </div>
            <div id="travelOutput" class="text-gray-400 text-[11px] leading-relaxed">
              &gt; Ready. Click "TEST" to watch the multi-agent reasoning stream.
            </div>
          </div>
        </div>

        <!-- Project 2: AOI Defect Inspection with Clean Slider -->
        <div class="simple-card p-7 rounded-2xl space-y-5">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/10 pb-4">
            <div>
              <span class="text-[10px] font-mono text-gold-400 font-bold uppercase">PROJECT 02 &bull; COMPUTER VISION</span>
              <h3 class="text-xl font-display font-bold text-white">Industrial AOI SMT Defect Vision Scanner</h3>
            </div>
            <span class="text-xs font-mono text-gold-400">99.4% Precision &bull; YOLOv8</span>
          </div>

          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            Inspired by Foxconn high-volume failure analysis. Drag the split slider below to compare raw optical camera capture with real-time AI bounding box defect detection.
          </p>

          <!-- Interactive Before / After Split Slider -->
          <div class="relative w-full max-w-3xl mx-auto h-[260px] sm:h-[320px] rounded-xl overflow-hidden border border-white/20 select-none cursor-ew-resize" id="aoiSliderContainer">
            
            <!-- Before Layer (Raw PCB) -->
            <div class="absolute inset-0 bg-[#0A1811] flex items-center justify-center p-4">
              <svg viewBox="0 0 600 320" class="w-full h-full object-contain">
                <rect width="600" height="320" fill="#0A1811" rx="8"/>
                <path d="M 50 60 L 250 60 L 300 120 L 550 120" stroke="#163E2B" stroke-width="3" fill="none"/>
                <path d="M 50 160 L 200 160 L 250 220 L 550 220" stroke="#163E2B" stroke-width="3" fill="none"/>
                <rect x="220" y="90" width="160" height="120" fill="#1C242B" stroke="#374151" stroke-width="2" rx="4"/>
                <text x="300" y="155" fill="#9CA3AF" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">ARM STM32F4</text>
                <rect x="130" y="80" width="28" height="14" fill="#3B4252"/>
                <circle cx="158" cy="87" r="5" fill="#CBD5E1"/>
                <rect x="165" y="80" width="28" height="14" fill="#3B4252"/>
                <rect x="420" y="140" width="28" height="14" fill="none" stroke="#EF4444" stroke-dasharray="2 2"/>
              </svg>
              <span class="absolute top-3 left-3 px-2 py-0.5 rounded bg-black/80 text-[10px] font-mono text-gray-300 border border-white/20">RAW SENSOR</span>
            </div>

            <!-- After Layer (YOLOv8 Overlay) -->
            <div id="aoiAfterLayer" class="absolute inset-0 bg-[#06121E] flex items-center justify-center p-4 overflow-hidden" style="clip-path: inset(0 0 0 50%);">
              <svg viewBox="0 0 600 320" class="w-full h-full object-contain">
                <rect width="600" height="320" fill="#06121E" rx="8"/>
                <path d="M 50 60 L 250 60 L 300 120 L 550 120" stroke="#0284C7" stroke-width="2" fill="none" opacity="0.6"/>
                <path d="M 50 160 L 200 160 L 250 220 L 550 220" stroke="#0284C7" stroke-width="2" fill="none" opacity="0.6"/>
                <rect x="220" y="90" width="160" height="120" fill="#0F172A" stroke="#0EA5E9" stroke-width="2" rx="4"/>
                <text x="300" y="155" fill="#38BDF8" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">ARM STM32F4 [OK: 0.99]</text>
                <rect x="120" y="70" width="80" height="35" fill="rgba(239, 68, 68, 0.2)" stroke="#EF4444" stroke-width="2"/>
                <text x="160" y="65" fill="#EF4444" font-family="monospace" font-size="10" text-anchor="middle" font-weight="bold">SOLDER_BRIDGE (99.4%)</text>
                <rect x="410" y="130" width="50" height="35" fill="rgba(245, 158, 11, 0.2)" stroke="#F59E0B" stroke-width="2"/>
                <text x="435" y="125" fill="#F59E0B" font-family="monospace" font-size="10" text-anchor="middle" font-weight="bold">MISSING_SMD (98.9%)</text>
              </svg>
              <span class="absolute top-3 right-3 px-2 py-0.5 rounded bg-black/80 text-[10px] font-mono text-cyan-400 border border-cyan-400/40">YOLOv8 DETECTIONS</span>
            </div>

            <!-- Slider Divider -->
            <div id="aoiSliderHandle" class="slider-handle" style="left: 50%;">
              <div class="slider-handle-button">
                <i data-lucide="chevrons-left-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>
          </div>
          <p class="text-center text-xs font-mono text-gray-500">&larr; Drag slider to inspect AI defect detection &rarr;</p>
        </div>

        <!-- Project 3: Autonomous Rover with Simple LIDAR Radar -->
        <div class="simple-card p-7 rounded-2xl space-y-5">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/10 pb-4">
            <div>
              <span class="text-[10px] font-mono text-emerald-400 font-bold uppercase">PROJECT 03 &bull; EMBEDDED ROBOTICS</span>
              <h3 class="text-xl font-display font-bold text-white">Autonomous Multi-Sensor Rover</h3>
            </div>
            <span class="text-xs font-mono text-emerald-400">NVIDIA Jetson &bull; 360&deg; LIDAR</span>
          </div>

          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-sans">
            ECE Capstone project fusing 360° LIDAR telemetry, ultrasonic sensors, and motor encoder feedback into an embedded Jetson edge system for real-time obstacle avoidance.
          </p>

          <!-- Simple Clean Automated Radar Animation -->
          <div class="bg-noir-950 p-6 rounded-xl border border-white/10 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="relative w-56 h-56 flex items-center justify-center shrink-0">
              <canvas id="lidarRadarCanvas" width="220" height="220" class="w-full h-full rounded-full bg-noir-900 border border-white/10 shadow-[0_0_20px_rgba(16,185,129,0.15)]"></canvas>
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_8px_#10B981]"></div>
              </div>
            </div>

            <div class="flex-1 w-full space-y-3 font-mono text-xs">
              <div class="flex items-center justify-between border-b border-white/10 pb-2">
                <span class="text-gray-400">LIDAR RADAR TELEMETRY:</span>
                <span class="text-emerald-400 font-bold">ONLINE &bull; 60 FPS</span>
              </div>
              <div class="grid grid-cols-2 gap-2.5">
                <div class="p-2.5 rounded-lg bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">HEADING AZIMUTH</span>
                  <span id="radarAzimuth" class="text-gold-400 font-bold text-xs">142.4&deg;</span>
                </div>
                <div class="p-2.5 rounded-lg bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">SCAN FREQUENCY</span>
                  <span class="text-white font-bold text-xs">20.0 Hz</span>
                </div>
                <div class="p-2.5 rounded-lg bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">OBSTACLE CLEARANCE</span>
                  <span class="text-emerald-400 font-bold text-xs">100% CLEAR</span>
                </div>
                <div class="p-2.5 rounded-lg bg-noir-900 border border-white/10">
                  <span class="text-gray-500 text-[10px] block">EDGE COMPUTE</span>
                  <span class="text-cyan-400 font-bold text-xs">Jetson Nano</span>
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
    <section id="sketches" class="px-6 max-w-5xl mx-auto py-12">
      
      <div class="mb-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-1">
          <span class="text-xs font-mono text-gold-400 tracking-wider uppercase font-bold">ACT V &bull; OBSERVATIONAL SKETCHBOOK</span>
          <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">Graphite &amp; Drawing Studio</h2>
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
          <span>LOAD CURATED SKETCHES</span>
        </button>
      </div>

      <!-- Posts Container -->
      <div id="postsFeedContainer" class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Empty State -->
      <div id="emptyFeedState" class="hidden text-center py-16 simple-card rounded-2xl space-y-3">
        <i data-lucide="image" class="w-10 h-10 text-gold-400/50 mx-auto"></i>
        <h4 class="text-base font-display font-bold text-white">No Drawings In Feed</h4>
        <p class="text-xs text-gray-400 max-w-xs mx-auto">Click "+ POST NEW DRAWING" above to publish your original art, or click below to load curated sketches.</p>
        <button onclick="loadSampleSketches()" class="px-4 py-2 rounded-xl bg-gold-500 text-noir-950 font-bold text-xs uppercase">
          LOAD SAMPLES
        </button>
      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- SECTION 7: CONTACT & APPRECIATION -->
    <!-- ======================================================================= -->
    <section id="contact" class="px-6 max-w-5xl mx-auto py-12">
      
      <div class="mb-10 text-center space-y-1">
        <span class="text-xs font-mono text-cyan-400 tracking-wider uppercase font-bold">CONNECT &bull; TRANSMISSION</span>
        <h2 class="text-2xl sm:text-4xl font-display font-bold text-white tracking-tight">Let\'s Build Together</h2>
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
        <div class="simple-card p-6 rounded-2xl space-y-5 flex flex-col justify-between">
          <div class="space-y-4">
            <h3 class="text-lg font-display font-bold text-white">Direct Channels</h3>
            
            <div class="space-y-2.5 font-mono text-xs">
              <div class="flex items-center justify-between p-3 rounded-xl bg-noir-950 border border-white/10">
                <div class="flex items-center space-x-2.5 text-gray-300">
                  <i data-lucide="mail" class="w-4 h-4 text-cyan-400"></i>
                  <span>shreyasbj03@gmail.com</span>
                </div>
                <button onclick="copyToClipboard('shreyasbj03@gmail.com', 'Email copied!')" class="text-cyan-400 hover:text-white text-[11px] font-bold">COPY</button>
              </div>

              <div class="flex items-center justify-between p-3 rounded-xl bg-noir-950 border border-white/10">
                <div class="flex items-center space-x-2.5 text-gray-300">
                  <i data-lucide="phone" class="w-4 h-4 text-gold-400"></i>
                  <span>+91 9110464228</span>
                </div>
                <a href="tel:+919110464228" class="text-gold-400 hover:text-white text-[11px] font-bold">CALL</a>
              </div>

              <div class="flex items-center justify-between p-3 rounded-xl bg-noir-950 border border-white/10 text-gray-300">
                <div class="flex items-center space-x-2.5">
                  <i data-lucide="map-pin" class="w-4 h-4 text-emerald-400"></i>
                  <span>Bangalore &bull; Chikkamagaluru, India</span>
                </div>
                <span class="text-emerald-400 text-[11px]">IST</span>
              </div>
            </div>
          </div>

          <!-- Socials -->
          <div class="pt-4 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-mono text-gray-500">DIGITAL REACH:</span>
            <div class="flex items-center space-x-2">
              <a href="https://linkedin.com/in/shreyas-b-j-975988226" target="_blank" rel="noopener noreferrer" class="p-2 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-cyan-400 border border-white/10 transition-colors" title="LinkedIn">
                <i data-lucide="linkedin" class="w-4 h-4"></i>
              </a>
              <a href="https://github.com/shreyasbj03" target="_blank" rel="noopener noreferrer" class="p-2 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-cyan-400 border border-white/10 transition-colors" title="GitHub">
                <i data-lucide="github" class="w-4 h-4"></i>
              </a>
              <a href="#sketches" class="p-2 rounded-lg bg-noir-950 hover:bg-white/10 text-gray-300 hover:text-gold-400 border border-white/10 transition-colors" title="Sketches">
                <i data-lucide="instagram" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Form -->
        <div class="simple-card p-6 rounded-2xl space-y-4">
          <h3 class="text-lg font-display font-bold text-white">Send a Message</h3>
          
          <form onsubmit="handleContactSubmit(event)" class="space-y-3 font-mono text-xs">
            <div>
              <label class="block text-gray-400 mb-1">NAME</label>
              <input type="text" id="contactName" required placeholder="Your Name" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2 text-white focus:outline-none focus:border-cyan-400">
            </div>
            <div>
              <label class="block text-gray-400 mb-1">EMAIL</label>
              <input type="email" id="contactEmail" required placeholder="your.email@domain.com" class="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2 text-white focus:outline-none focus:border-cyan-400">
            </div>
            <div>
              <label class="block text-gray-400 mb-1">MESSAGE</label>
              <textarea id="contactMessage" required rows="3" placeholder="Hello Shreyas, I would like to discuss..." class="w-full bg-noir-950 border border-white/15 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-400 resize-none font-sans"></textarea>
            </div>
            <button type="submit" class="w-full py-3 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-noir-950 font-display font-bold text-xs uppercase tracking-wider transition-all">
              SEND MESSAGE
            </button>
          </form>
        </div>

      </div>
    </section>

    <!-- ======================================================================= -->
    <!-- FOOTER -->
    <!-- ======================================================================= -->
    <footer class="py-12 border-t border-white/10 text-center font-mono text-xs text-gray-500 space-y-1.5">
      <p class="text-gray-400">SHREYAS B J &bull; AI / ML ENGINEER &bull; B.E. ECE (8.89 CGPA)</p>
      <p class="text-[11px]">BANGALORE &bull; CHIKKAMAGALURU, KARNATAKA, INDIA</p>
    </footer>

  </main>

  <!-- ========================================================================= -->
  <!-- MODAL: POST NEW DRAWING -->
  <!-- ========================================================================= -->
  <div id="newPostModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="simple-card max-w-lg w-full p-6 sm:p-7 rounded-2xl space-y-5 relative max-h-[90vh] overflow-y-auto">
      
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

        <!-- Filter Presets -->
        <div class="space-y-1">
          <label class="block text-gray-400">LOOK FILTER</label>
          <div class="grid grid-cols-3 gap-2 text-[11px]">
            <button type="button" onclick="setPostFilter('none')" id="filt-none" class="p-1.5 rounded-lg bg-noir-900 border border-gold-400 text-white font-bold text-center">Natural</button>
            <button type="button" onclick="setPostFilter('charcoal')" id="filt-charcoal" class="p-1.5 rounded-lg bg-noir-900 border border-white/10 text-gray-400 hover:text-white text-center">Charcoal</button>
            <button type="button" onclick="setPostFilter('sepia')" id="filt-sepia" class="p-1.5 rounded-lg bg-noir-900 border border-white/10 text-gray-400 hover:text-white text-center">Sepia</button>
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
    // 1. TWINKLING STARFIELD ENGINE (SMALL DOTS SHINING LIKE STARS)
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

      // Mouse subtle celestial parallax
      let mouse = { x: width / 2, y: height / 2, targetX: width / 2, targetY: height / 2 };
      window.addEventListener('mousemove', (e) => {
        mouse.targetX = e.clientX;
        mouse.targetY = e.clientY;
      });

      // Color variations for natural stellar temperature
      const starColors = [
        { r: 255, g: 255, b: 255 }, // Pure Diamond White
        { r: 253, g: 224, b: 139 }, // Warm Golden Starlight
        { r: 186, g: 230, b: 253 }, // Pale Celestial Cyan
        { r: 240, g: 249, b: 255 }, // Soft Platinum
      ];

      const count = window.innerWidth < 768 ? 95 : 175;
      const stars = [];

      for (let i = 0; i < count; i++) {
        // Star sizes: mostly tiny dots (0.7px - 1.4px), a few bright focal stars (1.8px - 2.2px)
        const isBrightFocal = Math.random() < 0.12;
        const radius = isBrightFocal ? (Math.random() * 0.7 + 1.6) : (Math.random() * 0.7 + 0.7);
        const rgb = starColors[Math.floor(Math.random() * starColors.length)];
        const z = Math.random() * 0.8 + 0.2; // Depth layer for parallax

        stars.push({
          x: Math.random() * width,
          y: Math.random() * height,
          baseRadius: radius,
          rgb,
          z,
          baseAlpha: Math.random() * 0.3 + 0.25,
          twinkleSpeed: Math.random() * 0.035 + 0.015,
          phase: Math.random() * Math.PI * 2,
          driftY: -(Math.random() * 0.15 + 0.04) * z, // Ultra-slow upward drift
          driftX: (Math.random() - 0.5) * 0.05 * z,
          isFocal: isBrightFocal
        });
      }

      let time = 0;
      function renderStars() {
        ctx.clearRect(0, 0, width, height);
        time += 1;

        // Smooth mouse parallax interpolation
        mouse.x += (mouse.targetX - mouse.x) * 0.04;
        mouse.y += (mouse.targetY - mouse.y) * 0.04;
        const parallaxOffsetX = (mouse.x - width / 2) * 0.018;
        const parallaxOffsetY = (mouse.y - height / 2) * 0.018;

        for (let i = 0; i < stars.length; i++) {
          const s = stars[i];

          // Slow celestial drift
          s.y += s.driftY;
          s.x += s.driftX;

          // Wrap edges smoothly
          if (s.y < -10) s.y = height + 10;
          if (s.y > height + 10) s.y = -10;
          if (s.x < -10) s.x = width + 10;
          if (s.x > width + 10) s.x = -10;

          // Parallax adjusted position
          const drawX = s.x - parallaxOffsetX * s.z;
          const drawY = s.y - parallaxOffsetY * s.z;

          // Twinkle pulse wave
          const wave = Math.sin(time * s.twinkleSpeed + s.phase);
          const alpha = Math.max(0.12, Math.min(1.0, s.baseAlpha + wave * (1 - s.baseAlpha) * 0.65));

          // Draw Soft Radial Glow Halo for brighter shining stars
          if (s.isFocal && alpha > 0.5) {
            const glowRadius = s.baseRadius * 3.8;
            const grad = ctx.createRadialGradient(drawX, drawY, 0, drawX, drawY, glowRadius);
            grad.addColorStop(0, `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha * 0.45})`);
            grad.addColorStop(0.5, `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha * 0.12})`);
            grad.addColorStop(1, 'rgba(0,0,0,0)');

            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(drawX, drawY, glowRadius, 0, Math.PI * 2);
            ctx.fill();

            // Tiny delicate 4-point cross-glint when twinkling brightly
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

          // Draw the Star Dot
          ctx.beginPath();
          ctx.arc(drawX, drawY, s.baseRadius, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(${s.rgb.r}, ${s.rgb.g}, ${s.rgb.b}, ${alpha})`;
          ctx.fill();
        }

        requestAnimationFrame(renderStars);
      }
      renderStars();
    })();

    // -------------------------------------------------------------------------
    // 2. ADAPTIVE PROFILE PHOTO FRAME
    // -------------------------------------------------------------------------
    const profilePhotoInput = document.getElementById('profilePhotoInput');
    const profilePhotoImg = document.getElementById('profilePhotoImg');
    const resetProfilePhotoBtn = document.getElementById('resetProfilePhotoBtn');
    const aspectRatioTag = document.getElementById('aspectRatioTag');
    const DEFAULT_PROFILE_SRC = './assets/profile-avatar.svg';

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

    if (resetProfilePhotoBtn) {
      resetProfilePhotoBtn.addEventListener('click', () => {
        localStorage.removeItem('shreyas_uploaded_profile_photo');
        profilePhotoImg.src = DEFAULT_PROFILE_SRC;
        showToast('Reset to default portrait.');
      });
    }

    // -------------------------------------------------------------------------
    // 3. PROJECT 1: TRAVEL SIMULATOR
    // -------------------------------------------------------------------------
    function runTravelSim() {
      const input = document.getElementById('travelInput').value.trim();
      const output = document.getElementById('travelOutput');
      if (!input) return;

      output.innerHTML = `<span class="text-cyan-400">&gt; Query: "${input}"</span><br>&gt; Ingesting context documents via vector distance...`;

      setTimeout(() => {
        output.innerHTML += `<br>&gt; [Weather API] Kyoto 18&deg;C &bull; Clear skies verified.<br><span class="text-emerald-400">&gt; Grounded 4-day itinerary generated within budget constraints.</span>`;
      }, 700);
    }

    // -------------------------------------------------------------------------
    // 4. PROJECT 2: AOI IMAGE COMPARISON SLIDER
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
      window.addEventListener('mouseup', () => { isSlidingAoi = false; });

      // Touch
      aoiContainer.addEventListener('touchstart', (e) => {
        isSlidingAoi = true;
        updateAoiSlider(e.touches[0].clientX);
      });
      window.addEventListener('touchmove', (e) => {
        if (!isSlidingAoi) return;
        updateAoiSlider(e.touches[0].clientX);
      });
      window.addEventListener('touchend', () => { isSlidingAoi = false; });
    }

    // -------------------------------------------------------------------------
    // 5. PROJECT 3: SIMPLE AUTOMATED LIDAR RADAR SWEEP
    // -------------------------------------------------------------------------
    (function initLidarRadar() {
      const canvas = document.getElementById('lidarRadarCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const size = canvas.width;
      const center = size / 2;
      const radius = center - 12;
      let angle = 0;

      const blips = [
        { dist: 0.4, angle: 0.9, ping: 0 },
        { dist: 0.7, angle: 2.4, ping: 0 },
        { dist: 0.85, angle: 4.2, ping: 0 },
        { dist: 0.55, angle: 5.2, ping: 0 }
      ];

      function renderRadar() {
        ctx.clearRect(0, 0, size, size);

        // Concentric distance rings
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        [0.3, 0.65, 1.0].forEach(r => {
          ctx.beginPath();
          ctx.arc(center, center, radius * r, 0, Math.PI * 2);
          ctx.stroke();
        });

        // Crosshairs
        ctx.beginPath();
        ctx.moveTo(center, 12); ctx.lineTo(center, size - 12);
        ctx.moveTo(12, center); ctx.lineTo(size - 12, center);
        ctx.stroke();

        // Rotating Beam
        angle += 0.035;
        if (angle > Math.PI * 2) angle -= Math.PI * 2;

        const sweepGradient = ctx.createConicGradient(angle - Math.PI / 4, center, center);
        sweepGradient.addColorStop(0, 'rgba(16, 185, 129, 0)');
        sweepGradient.addColorStop(0.12, 'rgba(16, 185, 129, 0.4)');
        sweepGradient.addColorStop(0.13, 'rgba(16, 185, 129, 0.9)');
        sweepGradient.addColorStop(0.14, 'rgba(16, 185, 129, 0)');

        ctx.fillStyle = sweepGradient;
        ctx.beginPath();
        ctx.arc(center, center, radius, 0, Math.PI * 2);
        ctx.fill();

        // Sweep Line
        ctx.strokeStyle = '#10B981';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(center, center);
        ctx.lineTo(center + Math.cos(angle) * radius, center + Math.sin(angle) * radius);
        ctx.stroke();

        // Blips
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
            ctx.arc(bx, by, 3, 0, Math.PI * 2);
            ctx.fill();
            b.ping *= 0.96;
          }
        });

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
    // 6. INSTAGRAM SKETCH FEED STUDIO
    // -------------------------------------------------------------------------
    const POSTS_KEY = 'shreyas_sketch_feed_v3';
    let currentFilter = 'all';
    let selectedFilter = 'none';
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
        <article class="simple-card rounded-2xl overflow-hidden shadow-xl" id="post-${post.id}">
          <!-- Header -->
          <div class="px-5 py-3.5 border-b border-white/10 flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <img src="${profilePhotoImg ? profilePhotoImg.src : './assets/profile-avatar.svg'}" class="w-8 h-8 rounded-full object-cover border border-gold-400/50">
              <div>
                <span class="font-display font-bold text-white text-xs block">Shreyas B J</span>
                <span class="text-[10px] font-mono text-gray-400">@shreyas.sketches &bull; ${post.date || 'Studio'}</span>
              </div>
            </div>
            <button onclick="deletePost('${post.id}')" class="p-1.5 text-gray-500 hover:text-red-400 transition-colors" title="Delete">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          </div>

          <!-- Image with Double-Tap to Like -->
          <div class="relative bg-noir-950 flex items-center justify-center overflow-hidden cursor-pointer select-none" 
               ondblclick="doubleTapLikePost(event, '${post.id}')"
               onclick="handleMediaClick(event, '${post.id}')">
            <img src="${post.image}" alt="${post.title}" class="max-h-[440px] w-auto h-auto max-w-full object-contain mx-auto block ${getFilterClass(post.filter)}">
            
            <div id="heartPop-${post.id}" class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none hidden">
              <i data-lucide="heart" class="w-20 h-20 text-heart fill-heart filter drop-shadow-xl"></i>
            </div>
          </div>

          <!-- Actions -->
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

            <!-- Title & Caption -->
            <div class="text-xs space-y-0.5 font-sans">
              <p class="text-white font-medium"><span class="font-bold font-display mr-1">shreyas.sketches</span>${post.title}</p>
              <p class="text-gray-300 text-xs">${post.caption}</p>
            </div>

            <!-- Comments Drawer -->
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
                <input type="text" id="commentInput-${post.id}" placeholder="Add a comment..." class="flex-1 bg-noir-950 border border-white/15 rounded-lg px-2.5 py-1 text-xs text-white focus:outline-none focus:border-gold-400">
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

    function getFilterClass(f) {
      if (f === 'charcoal') return 'contrast-125 grayscale brightness-95';
      if (f === 'sepia') return 'sepia-[0.35] contrast-105';
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
        showToast('Comment posted!');
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

    function setPostFilter(f) {
      selectedFilter = f;
      ['none', 'charcoal', 'sepia'].forEach(k => {
        const btn = document.getElementById('filt-' + k);
        if (btn) {
          if (k === f) btn.className = 'p-1.5 rounded-lg bg-noir-900 border border-gold-400 text-white font-bold text-center';
          else btn.className = 'p-1.5 rounded-lg bg-noir-900 border border-white/10 text-gray-400 hover:text-white text-center';
        }
      });
      const previewImg = document.getElementById('imagePreviewEl');
      if (previewImg) previewImg.className = `max-h-48 mx-auto rounded-lg object-contain ${getFilterClass(f)}`;
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
        filter: selectedFilter,
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
    // 7. APPRECIATION BEACON & BALLISTIC PARTICLES
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
      showToast('Transmission received! Thank you.');
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
    // 8. UTILS & CONTACT
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

    // ESC to close modals
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

print(f"Generated clean simple portfolio at {target_path} ({len(html_content)} bytes)")
