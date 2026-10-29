import React from 'react';
import { ArrowDown, Palette } from 'lucide-react';

export const Prologue: React.FC = () => {
  return (
    <section id="prologue" className="min-h-[85vh] flex items-center justify-center relative px-4 sm:px-6 lg:px-8 pt-20">
      <div className="max-w-4xl mx-auto text-center relative z-10">
        
        <div className="inline-flex items-center space-x-2 px-3.5 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-gray-300 mb-8">
          <span className="w-2 h-2 rounded-full bg-gold-400 animate-pulse" />
          <span>CHIKKAMAGALURU &bull; BENGALURU, INDIA</span>
          <span className="text-white/20">|</span>
          <span className="text-gold-400 font-semibold">ECE B.E. (8.89 CGPA)</span>
        </div>

        <h1 className="text-5xl sm:text-7xl md:text-8xl font-display font-extrabold tracking-tight text-white mb-6 uppercase">
          SHREYAS <span className="bg-gradient-to-r from-gold-400 via-white to-cyan-400 bg-clip-text text-transparent">B J</span>
        </h1>

        <p className="text-lg sm:text-xl md:text-2xl text-gray-300 font-light max-w-2xl mx-auto mb-10 leading-relaxed">
          Bridging the deterministic rigor of <span className="text-white font-medium border-b border-gold-400/50">Electronics Engineering</span> with the creative frontiers of <span className="text-white font-medium border-b border-cyan-400/50">Artificial Intelligence</span> and <span className="text-white font-medium border-b border-heart/50">Visual Design</span>.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <a
            href="#biography"
            className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-sm tracking-wide transition-all shadow-lg flex items-center justify-center space-x-2"
          >
            <span>EXPLORE PROFILE &amp; STORY</span>
            <ArrowDown className="w-4 h-4" />
          </a>

          <a
            href="#drawings"
            className="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-white font-mono text-sm tracking-wide transition-all flex items-center justify-center space-x-2"
          >
            <Palette className="w-4 h-4 text-gold-400" />
            <span>VIEW DRAWINGS FEED</span>
          </a>
        </div>

      </div>
    </section>
  );
};
