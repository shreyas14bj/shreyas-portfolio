import { ExperienceItem, Project, Certification, SkillCategory, Drawing } from '../types';

export const PERSONAL_INFO = {
  name: 'Shreyas B J',
  role: 'AI / ML Engineer & Creative Technologist',
  tagline: 'Bridging Hardware Precision, Generative AI, and Visual Artistry',
  location: 'Chikkamagaluru & Bengaluru, Karnataka, India',
  email: 'shreyasbjckm@gmail.com',
  phone: '+91 7204424892',
  avatar: './assets/profile-avatar.svg',
  education: {
    degree: 'Bachelor of Engineering in Electronics and Communications Engineering',
    institution: 'Nagarjuna College of Engineering and Technology, Bangalore',
    cgpa: '8.89 / 10',
    graduation: 'July 2025',
    coursework: ['Python Programming', 'Networks', 'Object-Oriented Programming (OOPs)', 'Digital Marketing']
  },
  social: {
    linkedin: 'https://linkedin.com',
    github: 'https://github.com',
    netlify: 'https://netlify.com',
    streamlit: 'https://streamlit.io'
  }
};

export const DRAWINGS: Drawing[] = [
  {
    id: 'art_portrait',
    title: "The Architect’s Gaze",
    subtitle: "Portrait & Contour Study",
    medium: "Graphite & Charcoal on 220gsm paper",
    hoursSpent: "~18 Hours",
    reflection: "Studying facial bone structures, contours, and micro-expressions trained my eye to spot micro-anomalies in high-dimensional vector spaces and model loss plateaus.",
    imageSrc: "./assets/drawings/drawing-portrait.svg",
    defaultLikes: 324,
    tag: "PORTRAIT STUDY",
    location: "Chikkamagaluru Studio"
  },
  {
    id: 'art_landscape',
    title: "Misty Canopies of Baba Budangiri",
    subtitle: "Highland Canopy Study",
    medium: "Graphite Wash & Fineliner on Bristol Vellum",
    hoursSpent: "~22 Hours",
    reflection: "Drawing the recursive branching of shade-grown coffee canopies taught me graph theory and tree traversals long before I wrote my first search algorithm.",
    imageSrc: "./assets/drawings/drawing-landscape.svg",
    defaultLikes: 288,
    tag: "LANDSCAPE",
    location: "Western Ghats Highlands"
  },
  {
    id: 'art_cybernetic',
    title: "Cybernetic Synapse & Cognitive Receptor",
    subtitle: "Biomechatronic Conceptual Art",
    medium: "Technical Drafting & Ink Stippling",
    hoursSpent: "~16 Hours",
    reflection: "Visualizing the exact interface between organic human perception and computational silicon cores. The visual inspiration for my work in LLM AI Agents.",
    imageSrc: "./assets/drawings/drawing-cybernetic.svg",
    defaultLikes: 412,
    tag: "CONCEPT ART",
    location: "AI Conceptual Series"
  },
  {
    id: 'art_architecture',
    title: "Perspective & Isometric Drafting",
    subtitle: "Geometric Hardware Spec",
    medium: "Drafting Compass & Architectural Grid on Linen",
    hoursSpent: "~14 Hours",
    reflection: "Drafting strict isometric lines trained the exact discipline I relied on for Boxplot statistical failure analysis and hardware diagnostics at Foxconn.",
    imageSrc: "./assets/drawings/drawing-architecture.svg",
    defaultLikes: 195,
    tag: "ISOMETRIC SPEC",
    location: "Precision Series"
  }
];

export const EXPERIENCES: ExperienceItem[] = [
  {
    id: 'tcs',
    role: 'Assistant System Engineer Trainee',
    organization: 'Tata Consultancy Services (TCS)',
    period: 'Currently Working',
    domain: 'Artificial Intelligence & Machine Learning',
    statusBadge: 'CURRENT MISSION',
    bullets: [
      'Working as an Assistant System Engineer Trainee in the Artificial Intelligence and Machine Learning domain.',
      'Gained deep exposure to Python, AI/ML concepts, data analysis, model development, and enterprise machine learning workflows.',
      'Hands-on engineering across AI/ML fundamentals, Python, SQL, Linux environments, and UI/UX design.'
    ],
    tags: ['Python', 'AI/ML Workflows', 'Model Development', 'SQL', 'Linux', 'UI/UX']
  },
  {
    id: 'foxconn',
    role: 'AAE Trainee',
    organization: 'Foxconn Hon Hai Technology',
    period: 'June 2025 – May 2026',
    domain: 'Industrial Hardware & Reliability',
    statusBadge: 'HARDWARE PRECISION',
    bullets: [
      'Troubleshot and resolved complex industrial machine anomalies, ensuring smooth continuous line operations and minimizing operational downtime.',
      'Authored Failure Analysis documentation and conducted statistical Boxplot analysis to diagnose variance and degradation trends.',
      'Developed critical instincts for fault isolation, high-reliability systems, and edge-case prevention.'
    ],
    tags: ['Failure Analysis', 'Boxplot Analysis', 'Machine Troubleshooting', 'Downtime Minimization']
  },
  {
    id: 'vtu',
    role: 'React Development & AI Integration',
    organization: 'Skill Enhancement Course by VTU',
    period: 'December 2024 – May 2025',
    domain: 'Intelligent Web Applications',
    bullets: [
      'Mastered building intelligent, dynamic, and responsive web applications by integrating AI-powered features into modern React workflows.',
      'Implemented fluid component architectures, state hooks, and client-side data streaming.'
    ],
    tags: ['React.js', 'AI Integration', 'Dynamic UI', 'Responsive Design']
  },
  {
    id: 'skillcraft',
    role: 'Web Developer Intern',
    organization: 'Skill Craft Technology',
    period: 'October 2024 (1 Month)',
    domain: 'Frontend Engineering',
    bullets: [
      'Completed practical responsive applications including dynamic Landing Pages, precision Stopwatches, Tic Tac Toe game logic, and interactive To-Do lists.',
      'Solidified fundamentals in semantic HTML, modern CSS styling, and asynchronous JavaScript DOM manipulation.'
    ],
    tags: ['HTML5/CSS3', 'JavaScript ES6', 'DOM Manipulation', 'UI Engineering']
  }
];

export const PROJECTS: Project[] = [
  {
    id: 'travel-ai',
    title: 'Travel AI Recommendation Agent',
    tagline: 'RAG-Powered Conversational Vector Agent',
    category: 'Frontier AI & RAG',
    description: 'An AI-powered travel recommendation agent that suggests destinations, attractions, and tailored activities based on user preferences. Implemented a RAG-based knowledge system with vector search to provide grounded information on travel policies, attractions, and advisories.',
    keyHighlights: [
      'Vector search retrieval using ChromaDB for zero-hallucination travel advice',
      'LangChain orchestration for conversational multi-turn travel planning',
      'Deployed responsive Streamlit interface with interactive itinerary rendering'
    ],
    technologies: ['Python', 'LangChain', 'ChromaDB', 'Scikit-learn', 'Streamlit'],
    badge: 'FEATURED AI AGENT'
  },
  {
    id: 'bi-platform',
    title: 'Business Intelligence Platform',
    tagline: 'Automated Analytics & Single-Prompt NLQ',
    category: 'Enterprise Data Analytics',
    description: 'A responsive Business Intelligence Platform built in Python to process and visualize data uploaded via Excel files. Automates generation of data visualizations and analytical insights, enabling rapid interpretation with AI-powered natural language querying.',
    keyHighlights: [
      'Automated statistical data profiling using Pandas and NumPy',
      'Natural Language Querying (NLQ) allowing users to ask plain questions and receive charts',
      'Instant drag-and-drop file ingestion in Streamlit'
    ],
    technologies: ['Python', 'Pandas', 'NumPy', 'Streamlit', 'Data Visualization', 'AI NLQ']
  },
  {
    id: 'task-system',
    title: 'Intelligent Task Management System',
    tagline: 'OOP Console & Streamlit Application',
    category: 'Software Architecture',
    description: 'A robust task management architecture developed with strict Object-Oriented Programming (OOP) in Python. Automatically classifies tasks into Work, Study, Personal, or General using keyword-based detection with complete search and lifecycle handling.',
    keyHighlights: [
      'Clean separation of concerns with OOP principles and state handlers',
      'Automatic keyword-based category classifier',
      'Streamlit interactive control console'
    ],
    technologies: ['Python OOP', 'Streamlit', 'NLP Keyword Classification', 'File Handling']
  },
  {
    id: 'portfolio-labs',
    title: 'Personal Web Portfolio & Micro-Labs',
    tagline: 'Responsive UI Design & Creative Micro-Apps',
    category: 'Creative Frontend',
    description: 'Personal web space showcasing interactive layout systems, AI-powered typewriter effects, and dark mode toggles, alongside a suite of micro-tools: Weather forecasts, Bill Calculators, and Python data visualization scripts.',
    keyHighlights: [
      'Interactive typewriter simulation and theme persistence',
      'Micro-apps exploring algorithmic counters and reactive UI elements',
      'Continuous deployment via Netlify'
    ],
    technologies: ['HTML5', 'CSS3', 'JavaScript', 'Netlify', 'Power BI', 'AI Tools']
  }
];

export const CERTIFICATIONS: Certification[] = [
  {
    id: 'databricks',
    title: 'Machine Learning Engineer Associate',
    issuer: 'Databricks',
    period: 'October 2026 – October 2028',
    description: 'Hands-on experience building end-to-end ML workflows on the Databricks Lakehouse platform. Skilled in distributed data processing, automated feature engineering, and model lifecycle governance via MLflow and Unity Catalog.',
    badgeColor: 'amber'
  },
  {
    id: 'claude',
    title: 'Claude Certified Developer Foundations',
    issuer: 'Anthropic Claude',
    period: 'August 2026 – August 2027',
    description: 'Certified in foundational concepts of Claude AI, prompt engineering, LLM-based application development, and responsible AI practices.',
    badgeColor: 'violet'
  },
  {
    id: 'gemini',
    title: 'Build With Gemini',
    issuer: 'Google Cloud',
    period: 'October 2026',
    description: 'Hands-on experience developing AI-powered solutions using Google Gemini and generative AI capabilities.',
    badgeColor: 'cyan'
  },
  {
    id: 'genai',
    title: 'Introduction to Generative AI',
    issuer: 'NXT Wave',
    period: 'September 2024',
    description: 'Fundamentals of Generative AI, building neural network models, deep learning foundations, and AI-generated content.',
    badgeColor: 'gray'
  },
  {
    id: 'java',
    title: 'Programming in Java',
    issuer: 'NPTEL',
    period: 'October 2024',
    description: 'Core Java programming concepts, object-oriented principles, and algorithmic problem-solving.',
    badgeColor: 'gray'
  },
  {
    id: 'python',
    title: 'Python Programming',
    issuer: 'Technical Hub',
    period: 'December 2023 – February 2024',
    description: 'Advanced Python problem-solving, debugging complex logic, and algorithmic optimizations.',
    badgeColor: 'gray'
  }
];

export const SKILL_CATEGORIES: SkillCategory[] = [
  {
    title: 'Frontier AI & Machine Learning',
    subtitle: 'Agents, RAG & Lakehouse Architecture',
    icon: 'brain-circuit',
    skills: [
      { name: 'Python + AI', level: 'Advanced', percent: 94 },
      { name: 'LangChain & Vector RAG', level: 'Advanced', percent: 92 },
      { name: 'ChromaDB & Embeddings', level: 'Proficient', percent: 90 },
      { name: 'Databricks ML & MLflow', level: 'Certified', percent: 88 },
      { name: 'Prompt Engineering (Claude/Gemini)', level: 'Certified', percent: 92 }
    ]
  },
  {
    title: 'Systems & Core Engineering',
    subtitle: 'OOP, Persistence & Industrial Reliability',
    icon: 'cpu',
    skills: [
      { name: 'Java + Spring Boot', level: 'Proficient', percent: 86 },
      { name: 'SQL & Database Design', level: 'Proficient', percent: 88 },
      { name: 'Hardware Failure Analysis (Foxconn)', level: 'Applied', percent: 90 },
      { name: 'Linux & Shell Scripting', level: 'Proficient', percent: 85 },
      { name: 'Git & Version Control', level: 'Proficient', percent: 90 }
    ]
  },
  {
    title: 'Creative Frontend & UI/UX',
    subtitle: 'Dynamic Web & Data Visualization',
    icon: 'palette',
    skills: [
      { name: 'React.js Development', level: 'Proficient', percent: 88 },
      { name: 'Streamlit Analytics UI', level: 'Expert', percent: 95 },
      { name: 'UI / UX & Visual Precision', level: 'Advanced', percent: 92 },
      { name: 'Data Viz (NumPy, Pandas, Power BI)', level: 'Advanced', percent: 90 },
      { name: 'Drawing & Observational Design', level: 'Passionate', percent: 96 }
    ]
  }
];
