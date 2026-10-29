import React from 'react';
import { X, Printer } from 'lucide-react';
import { PERSONAL_INFO, EXPERIENCES, PROJECTS, CERTIFICATIONS } from '../data/portfolioData';

interface Props {
  isOpen: boolean;
  onClose: () => void;
}

export const ExecutiveDossierModal: React.FC<Props> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-void/95 backdrop-blur-2xl flex items-center justify-center p-4 sm:p-6 overflow-y-auto">
      <div className="max-w-4xl w-full bg-surface border border-white/20 rounded-2xl p-6 sm:p-10 shadow-2xl relative my-8">
        
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-6 right-6 p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors"
          title="Close Executive View"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Header */}
        <div className="border-b border-white/15 pb-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 className="text-3xl font-display font-bold text-white">{PERSONAL_INFO.name}</h2>
              <p className="font-mono text-sm text-accent-cyan mt-1">AI / ML Engineer &bull; Assistant System Engineer Trainee at TCS</p>
              <p className="text-xs text-gray-400 mt-1">{PERSONAL_INFO.location} &bull; {PERSONAL_INFO.phone} &bull; {PERSONAL_INFO.email}</p>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={() => window.print()}
                className="px-4 py-2 rounded bg-white/10 hover:bg-white/20 text-white font-mono text-xs flex items-center space-x-1.5 transition-colors"
              >
                <Printer className="w-3.5 h-3.5" />
                <span>PRINT DOSSIER</span>
              </button>
            </div>
          </div>
        </div>

        {/* Body */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8 mt-6 text-xs text-gray-300">
          
          {/* Left Column: Experience & Projects */}
          <div className="md:col-span-7 space-y-6">
            
            <div>
              <h3 className="font-mono text-xs font-bold text-accent-cyan tracking-wider uppercase mb-3">PROFESSIONAL EXPERIENCE</h3>
              <div className="space-y-4">
                {EXPERIENCES.map(exp => (
                  <div key={exp.id}>
                    <div className="flex justify-between font-semibold text-white">
                      <span>{exp.role} — {exp.organization}</span>
                      <span className="text-gray-400">{exp.period}</span>
                    </div>
                    <p className="text-accent-cyan font-mono text-[11px]">{exp.domain}</p>
                    <p className="text-gray-400 mt-1">{exp.bullets.join(' ')}</p>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h3 className="font-mono text-xs font-bold text-accent-cyan tracking-wider uppercase mb-3">KEY ENGINEERING PROJECTS</h3>
              <div className="space-y-3">
                {PROJECTS.map(proj => (
                  <div key={proj.id}>
                    <h4 className="font-semibold text-white">{proj.title} ({proj.technologies.slice(0, 4).join(', ')})</h4>
                    <p className="text-gray-400 mt-0.5">{proj.description}</p>
                  </div>
                ))}
              </div>
            </div>

          </div>

          {/* Right Column: Education, Certifications & Skills */}
          <div className="md:col-span-5 space-y-6">
            
            <div>
              <h3 className="font-mono text-xs font-bold text-accent-cyan tracking-wider uppercase mb-3">EDUCATION</h3>
              <div className="p-3 rounded-lg bg-void border border-white/10">
                <span className="font-semibold text-white block">Bachelor of Engineering (ECE)</span>
                <span className="text-gray-400 block">{PERSONAL_INFO.education.institution}</span>
                <div className="mt-1 flex justify-between font-mono text-[11px]">
                  <span className="text-accent-amber font-bold">CGPA: {PERSONAL_INFO.education.cgpa}</span>
                  <span className="text-gray-500">Grad: {PERSONAL_INFO.education.graduation}</span>
                </div>
              </div>
            </div>

            <div>
              <h3 className="font-mono text-xs font-bold text-accent-cyan tracking-wider uppercase mb-3">CERTIFICATIONS</h3>
              <ul className="space-y-2 text-gray-300">
                {CERTIFICATIONS.map(cert => (
                  <li key={cert.id} className="pb-1.5 border-b border-white/5">
                    <span className="font-semibold text-white block">{cert.title}</span>
                    <span className="text-gray-400 text-[10px]">{cert.issuer} &bull; {cert.period}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <h3 className="font-mono text-xs font-bold text-accent-cyan tracking-wider uppercase mb-3">SKILLS &amp; TOOLS</h3>
              <div className="flex flex-wrap gap-1.5 font-mono text-[11px]">
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Python + AI</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Machine Learning</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Java &amp; Spring Boot</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">SQL</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">React.js</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">UI/UX</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Streamlit</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Power BI</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Git</span>
                <span className="px-2 py-0.5 rounded bg-white/10 text-white">Linux</span>
              </div>
            </div>

          </div>

        </div>

      </div>
    </div>
  );
};
