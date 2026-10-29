import React from 'react';
import { Award, BrainCircuit, Cpu, Palette, CheckCircle } from 'lucide-react';
import { SKILL_CATEGORIES, CERTIFICATIONS } from '../data/portfolioData';

export const SkillsMatrix: React.FC = () => {
  return (
    <section id="matrix" className="min-h-screen py-24 px-4 sm:px-6 lg:px-8 relative border-t border-white/5">
      <div className="max-w-6xl mx-auto">
        
        <div className="flex items-center space-x-3 mb-4">
          <span className="px-2.5 py-0.5 rounded bg-accent-amber/10 border border-accent-amber/30 text-accent-amber font-mono text-xs font-semibold">ACT III</span>
          <span className="font-mono text-xs text-gray-400 tracking-wider uppercase">// SKILLS &amp; WEAPONRY</span>
        </div>

        <h2 className="text-3xl sm:text-5xl font-display font-bold text-white mb-4">
          The Verified Arsenal.
        </h2>
        <p className="text-gray-400 max-w-2xl text-base sm:text-lg mb-12">
          An orchestrated spectrum spanning frontier LLMs, distributed machine learning, backend enterprise architecture, and creative UI engineering.
        </p>

        {/* 3 Categories */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
          {SKILL_CATEGORIES.map((cat, idx) => {
            const icons = [
              <BrainCircuit className="w-6 h-6 text-accent-cyan" />,
              <Cpu className="w-6 h-6 text-accent-violet" />,
              <Palette className="w-6 h-6 text-accent-amber" />
            ];
            const borderColors = [
              'hover:border-accent-cyan/50',
              'hover:border-accent-violet/50',
              'hover:border-accent-amber/50'
            ];
            const barColors = ['bg-accent-cyan', 'bg-accent-violet', 'bg-accent-amber'];

            return (
              <div key={cat.title} className={`p-6 rounded-2xl bg-card border border-white/10 ${borderColors[idx]} transition-all group`}>
                <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                  {icons[idx]}
                </div>
                <h3 className="text-xl font-display font-bold text-white mb-1">{cat.title}</h3>
                <p className="text-xs text-gray-400 font-mono mb-4">{cat.subtitle}</p>
                <div className="space-y-3 font-mono text-xs">
                  {cat.skills.map(s => (
                    <div key={s.name}>
                      <div className="flex justify-between text-gray-300 mb-1">
                        <span>{s.name}</span>
                        <span className="text-gray-400">{s.level}</span>
                      </div>
                      <div className="w-full h-1.5 bg-white/5 rounded-full overflow-hidden">
                        <div className={`h-full ${barColors[idx]} rounded-full`} style={{ width: `${s.percent}%` }} />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* Official Certifications Vault */}
        <div>
          <div className="flex items-center space-x-2 mb-6">
            <Award className="w-5 h-5 text-accent-cyan" />
            <h3 className="text-xl font-display font-bold text-white uppercase tracking-wide">Verified Certifications &amp; Credentials</h3>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {CERTIFICATIONS.map(cert => {
              const borderStyles = {
                amber: 'border-accent-amber/30 hover:border-accent-amber',
                violet: 'border-accent-violet/30 hover:border-accent-violet',
                cyan: 'border-accent-cyan/30 hover:border-accent-cyan',
                gray: 'border-white/10 hover:border-white/30'
              };
              const textColors = {
                amber: 'text-accent-amber',
                violet: 'text-accent-violet',
                cyan: 'text-accent-cyan',
                gray: 'text-gray-400'
              };

              return (
                <div key={cert.id} className={`p-5 rounded-xl bg-surface border ${borderStyles[cert.badgeColor]} transition-all relative overflow-hidden group`}>
                  <div className="flex items-start justify-between">
                    <span className={`font-mono text-[10px] ${textColors[cert.badgeColor]} font-semibold block mb-1 uppercase`}>
                      {cert.issuer} &bull; {cert.period}
                    </span>
                    <CheckCircle className={`w-4 h-4 ${textColors[cert.badgeColor]}`} />
                  </div>
                  <h4 className="text-base font-bold text-white group-hover:text-accent-cyan transition-colors mt-1">
                    {cert.title}
                  </h4>
                  <p className="text-xs text-gray-400 mt-2 leading-relaxed">
                    {cert.description}
                  </p>
                </div>
              );
            })}
          </div>
        </div>

      </div>
    </section>
  );
};
