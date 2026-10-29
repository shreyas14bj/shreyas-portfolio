import React from 'react';
import { EXPERIENCES } from '../data/portfolioData';

export const JourneyTimeline: React.FC = () => {
  return (
    <section id="journey" className="min-h-screen py-24 px-4 sm:px-6 lg:px-8 relative border-t border-white/5">
      <div className="max-w-6xl mx-auto">
        
        <div className="flex items-center space-x-3 mb-4">
          <span className="px-2.5 py-0.5 rounded bg-accent-violet/10 border border-accent-violet/30 text-accent-violet font-mono text-xs font-semibold">ACT II</span>
          <span className="font-mono text-xs text-gray-400 tracking-wider uppercase">// THE JOURNEY</span>
        </div>

        <h2 className="text-3xl sm:text-5xl font-display font-bold text-white mb-4">
          Battlegrounds of Experience.
        </h2>
        <p className="text-gray-400 max-w-2xl text-base sm:text-lg mb-16">
          Every stage of the journey forged a distinct capability: from raw hardware uptime and statistical failure diagnosis to modern generative intelligence.
        </p>

        {/* Timeline */}
        <div className="relative border-l border-white/15 ml-4 sm:ml-8 pl-6 sm:pl-10 space-y-12">
          {EXPERIENCES.map((exp, idx) => {
            const dotColors = [
              'bg-accent-cyan glow-cyan',
              'bg-accent-amber glow-amber',
              'bg-accent-violet glow-violet',
              'bg-accent-emerald'
            ];
            const badgeColors = [
              'bg-accent-cyan/10 text-accent-cyan',
              'bg-accent-amber/10 text-accent-amber',
              'bg-accent-violet/10 text-accent-violet',
              'bg-accent-emerald/10 text-accent-emerald'
            ];

            return (
              <div key={exp.id} className="relative group">
                <div className={`absolute -left-[31px] sm:-left-[47px] top-1.5 w-4 h-4 rounded-full border-4 border-void group-hover:scale-125 transition-transform ${dotColors[idx % dotColors.length]}`} />

                <div className="p-6 rounded-2xl bg-card/80 hover:bg-card border border-white/10 hover:border-accent-cyan/40 transition-all shadow-lg">
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
                    <div>
                      {exp.statusBadge && (
                        <span className={`px-2 py-0.5 rounded font-mono text-[10px] font-bold uppercase tracking-wider ${badgeColors[idx % badgeColors.length]}`}>
                          {exp.statusBadge}
                        </span>
                      )}
                      <h3 className="text-xl font-display font-bold text-white mt-1">{exp.role}</h3>
                      <h4 className="text-accent-cyan font-mono text-sm">{exp.organization}</h4>
                    </div>
                    <div className="font-mono text-xs text-gray-400 sm:text-right">
                      <span className="block text-white font-semibold">{exp.domain}</span>
                      <span>{exp.period}</span>
                    </div>
                  </div>

                  <ul className="space-y-2 text-sm text-gray-300 list-disc list-inside leading-relaxed">
                    {exp.bullets.map((bullet, bIdx) => (
                      <li key={bIdx}>{bullet}</li>
                    ))}
                  </ul>

                  <div className="mt-4 flex flex-wrap gap-2 pt-3 border-t border-white/5 font-mono text-xs text-gray-400">
                    {exp.tags.map(tag => (
                      <span key={tag} className="px-2 py-1 rounded bg-white/5">{tag}</span>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
};
