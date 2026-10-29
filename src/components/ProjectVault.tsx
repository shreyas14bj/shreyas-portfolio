import React, { useState } from 'react';
import { Check, Terminal, ExternalLink, Activity } from 'lucide-react';
import { PROJECTS } from '../data/portfolioData';
import { audioEngine } from '../utils/audioEngine';

export const ProjectVault: React.FC = () => {
  const [queryInput, setQueryInput] = useState('Plan a 3-day coffee trail & scenic trek in Chikkamagaluru');
  const [terminalLogs, setTerminalLogs] = useState<string[]>([
    '> [RAG Pipeline]: Initializing ChromaDB vector search...',
    '> Retrieving embeddings for "Chikkamagaluru coffee trail"...',
    '> Grounded Match: Mullayanagiri peak trek & Baba Budangiri estate.',
    '> 3-Day Plan ready: Day 1 Coffee Museum, Day 2 Mullayanagiri sunrise, Day 3 Hebbe Falls.'
  ]);

  const handleSimulateQuery = () => {
    if (!queryInput.trim()) return;
    audioEngine.playTone(1200, 0.1);
    setTerminalLogs([
      `> [Query Ingested]: "${queryInput}"`,
      '> Computing cosine similarity over LangChain vector indices...'
    ]);

    setTimeout(() => {
      setTerminalLogs(prev => [
        ...prev,
        '> Context Retrieved: 3 semantic matches (0.892 confidence)',
        '> Agent Response: Custom itinerary synthesized with localized insights & weather advisory check completed.'
      ]);
      audioEngine.playTone(1450, 0.1);
    }, 600);
  };

  const travelProject = PROJECTS.find(p => p.id === 'travel-ai')!;
  const biProject = PROJECTS.find(p => p.id === 'bi-platform')!;
  const otherProjects = PROJECTS.filter(p => p.id !== 'travel-ai' && p.id !== 'bi-platform');

  return (
    <section id="vault" className="min-h-screen py-24 px-4 sm:px-6 lg:px-8 relative border-t border-white/5">
      <div className="max-w-6xl mx-auto">
        
        <div className="flex items-center space-x-3 mb-4">
          <span className="px-2.5 py-0.5 rounded bg-accent-rose/10 border border-accent-rose/30 text-accent-rose font-mono text-xs font-semibold">ACT IV</span>
          <span className="font-mono text-xs text-gray-400 tracking-wider uppercase">// CINEMATIC SHOWCASES</span>
        </div>

        <h2 className="text-3xl sm:text-5xl font-display font-bold text-white mb-4">
          The Production Vault.
        </h2>
        <p className="text-gray-400 max-w-2xl text-base sm:text-lg mb-12">
          Real engineered systems. Each project represents an intentional fusion of architecture, algorithmic intelligence, and interactive utility.
        </p>

        {/* Featured Project 1: Travel AI Agent */}
        <div className="mb-16 p-8 rounded-3xl bg-gradient-to-br from-panel via-card to-void border border-accent-cyan/30 shadow-2xl relative overflow-hidden group">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <div className="lg:col-span-7 space-y-4">
              <div className="flex items-center space-x-2">
                <span className="px-3 py-1 rounded-full bg-accent-cyan/15 border border-accent-cyan/40 text-accent-cyan font-mono text-xs font-bold tracking-wider uppercase">
                  {travelProject.badge}
                </span>
                <span className="text-xs font-mono text-gray-400">RAG &bull; VECTOR SEARCH</span>
              </div>
              <h3 className="text-2xl sm:text-4xl font-display font-bold text-white">{travelProject.title}</h3>
              <p className="text-gray-300 text-sm sm:text-base leading-relaxed">
                {travelProject.description}
              </p>
              
              <div className="space-y-2 pt-2 text-xs font-mono text-gray-300">
                {travelProject.keyHighlights.map((hl, i) => (
                  <div key={i} className="flex items-center space-x-2">
                    <Check className="w-4 h-4 text-accent-cyan shrink-0" />
                    <span>{hl}</span>
                  </div>
                ))}
              </div>

              <div className="flex flex-wrap gap-2 pt-3 font-mono text-xs">
                {travelProject.technologies.map(tech => (
                  <span key={tech} className="px-2.5 py-1 rounded-md bg-accent-cyan/10 text-accent-cyan border border-accent-cyan/20">
                    {tech}
                  </span>
                ))}
              </div>
            </div>

            {/* Right Mini Simulator */}
            <div className="lg:col-span-5 bg-void/90 rounded-2xl p-5 border border-white/10 font-mono text-xs">
              <div className="flex items-center justify-between pb-3 border-b border-white/10 text-gray-400">
                <span className="flex items-center space-x-1.5">
                  <Terminal className="w-3.5 h-3.5 text-accent-cyan" />
                  <span>AI AGENT LIVE SIMULATION</span>
                </span>
                <span className="text-accent-emerald text-[10px]">ONLINE</span>
              </div>

              <div className="mt-4 space-y-3">
                <label className="block text-gray-400 text-[11px]">Test Agent Query:</label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={queryInput}
                    onChange={e => setQueryInput(e.target.value)}
                    className="w-full bg-surface border border-white/20 rounded px-2.5 py-2 text-white focus:outline-none focus:border-accent-cyan text-xs"
                  />
                  <button
                    onClick={handleSimulateQuery}
                    className="px-3 py-2 bg-accent-cyan text-void font-bold rounded hover:bg-accent-cyan/90 transition-colors whitespace-nowrap"
                  >
                    QUERY
                  </button>
                </div>

                <div className="p-3 bg-surface/80 rounded border border-white/5 text-[11px] text-gray-300 space-y-1 h-32 overflow-y-auto">
                  {terminalLogs.map((log, idx) => (
                    <p key={idx} className={idx === 0 ? 'text-accent-cyan' : idx === terminalLogs.length - 1 ? 'text-accent-emerald' : 'text-gray-400'}>
                      {log}
                    </p>
                  ))}
                </div>
              </div>
            </div>

          </div>
        </div>

        {/* Featured Project 2: BI Platform */}
        <div className="mb-16 p-8 rounded-3xl bg-gradient-to-br from-panel via-card to-void border border-accent-violet/30 shadow-2xl relative overflow-hidden group">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <div className="lg:col-span-7 space-y-4">
              <div className="flex items-center space-x-2">
                <span className="px-3 py-1 rounded-full bg-accent-violet/15 border border-accent-violet/40 text-accent-violet font-mono text-xs font-bold tracking-wider uppercase">
                  ENTERPRISE ANALYTICS
                </span>
                <span className="text-xs font-mono text-gray-400">AUTOMATED VISUALIZATION &bull; NLQ</span>
              </div>
              <h3 className="text-2xl sm:text-4xl font-display font-bold text-white">{biProject.title}</h3>
              <p className="text-gray-300 text-sm sm:text-base leading-relaxed">
                {biProject.description}
              </p>
              
              <div className="space-y-2 pt-2 text-xs font-mono text-gray-300">
                {biProject.keyHighlights.map((hl, i) => (
                  <div key={i} className="flex items-center space-x-2">
                    <Check className="w-4 h-4 text-accent-violet shrink-0" />
                    <span>{hl}</span>
                  </div>
                ))}
              </div>

              <div className="flex flex-wrap gap-2 pt-3 font-mono text-xs">
                {biProject.technologies.map(tech => (
                  <span key={tech} className="px-2.5 py-1 rounded-md bg-accent-violet/10 text-accent-violet border border-accent-violet/20">
                    {tech}
                  </span>
                ))}
              </div>
            </div>

            {/* Right Mini Chart Preview */}
            <div className="lg:col-span-5 bg-void/90 rounded-2xl p-5 border border-white/10 font-mono text-xs">
              <div className="flex items-center justify-between pb-3 border-b border-white/10 text-gray-400">
                <span>DATA SYNTHESIS PREVIEW</span>
                <span className="text-accent-violet font-semibold">STREAMLIT APP</span>
              </div>

              <div className="mt-4 space-y-4">
                <div className="grid grid-cols-2 gap-3 text-center">
                  <div className="p-3 rounded bg-surface border border-white/5">
                    <span className="text-gray-400 text-[10px] block">TOTAL RECORDS</span>
                    <span className="text-lg font-bold text-white">48,250</span>
                    <span className="text-accent-emerald text-[10px] block">+14.2% YoY</span>
                  </div>
                  <div className="p-3 rounded bg-surface border border-white/5">
                    <span className="text-gray-400 text-[10px] block">ANOMALY RATIO</span>
                    <span className="text-lg font-bold text-accent-amber">0.024%</span>
                    <span className="text-gray-400 text-[10px] block">Boxplot Filtered</span>
                  </div>
                </div>

                <div className="p-3 rounded bg-surface border border-white/5 space-y-2">
                  <div className="flex justify-between text-[11px] text-gray-300">
                    <span>Revenue Velocity by Region</span>
                    <span className="text-accent-cyan">Automated Graph</span>
                  </div>
                  <div className="flex items-end gap-2 h-16 pt-2">
                    <div className="w-1/4 bg-accent-violet/40 hover:bg-accent-violet transition-colors h-8 rounded-t" />
                    <div className="w-1/4 bg-accent-violet/60 hover:bg-accent-violet transition-colors h-14 rounded-t" />
                    <div className="w-1/4 bg-accent-cyan hover:bg-accent-cyan/90 transition-colors h-16 rounded-t" />
                    <div className="w-1/4 bg-accent-violet/80 hover:bg-accent-violet transition-colors h-10 rounded-t" />
                  </div>
                </div>

                <div className="text-[11px] text-gray-400 italic">
                  &quot;Natural Language Query: Show top 5 performing product lines this quarter&quot;
                </div>
              </div>
            </div>

          </div>
        </div>

        {/* 2-Column Grid for Secondary Projects */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {otherProjects.map(proj => (
            <div key={proj.id} className="p-6 rounded-2xl bg-card border border-white/10 hover:border-accent-cyan/50 transition-all flex flex-col justify-between">
              <div className="space-y-3">
                <span className="px-2.5 py-0.5 rounded bg-white/5 text-accent-amber font-mono text-[10px] font-bold tracking-wider uppercase">
                  {proj.category}
                </span>
                <h4 className="text-xl font-display font-bold text-white">{proj.title}</h4>
                <p className="text-sm text-gray-300 leading-relaxed">
                  {proj.description}
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-white/10 flex items-center justify-between font-mono text-xs">
                <div className="flex flex-wrap gap-1.5">
                  {proj.technologies.slice(0, 3).map(t => (
                    <span key={t} className="px-2 py-0.5 rounded bg-white/5 text-gray-300">{t}</span>
                  ))}
                </div>
                <span className="text-accent-cyan font-semibold">{proj.tagline.split(' ')[0]}</span>
              </div>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
};
