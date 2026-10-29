import React from 'react';
import { Copy, Phone, Linkedin, Github, Activity, Globe, Send } from 'lucide-react';
import { PERSONAL_INFO } from '../data/portfolioData';

export const TransmissionFinale: React.FC = () => {
  const handleCopyEmail = () => {
    navigator.clipboard.writeText(PERSONAL_INFO.email);
    alert('Email copied to clipboard!');
  };

  return (
    <section id="transmission" className="py-24 px-4 sm:px-6 lg:px-8 border-t border-white/10">
      <div className="max-w-4xl mx-auto text-center">
        
        <div className="inline-flex items-center space-x-2 font-mono text-xs text-gold-400 mb-4 uppercase tracking-wider">
          <Send className="w-4 h-4" />
          <span>ACT VI &bull; THE TRANSMISSION</span>
        </div>

        <h2 className="text-3xl sm:text-5xl font-display font-extrabold text-white mb-6">
          Direct Collaboration.
        </h2>
        <p className="text-gray-300 text-base sm:text-lg max-w-xl mx-auto mb-10 leading-relaxed font-light">
          Whether you are seeking an engineer for frontier AI systems, distributed pipelines, or creative technical products — let’s build together.
        </p>

        {/* Transmission Card */}
        <div className="max-w-xl mx-auto p-6 sm:p-8 rounded-3xl bg-noir-900 border border-white/15 shadow-2xl text-left font-mono text-sm space-y-4">
          
          <div className="p-3.5 rounded-xl bg-noir-850 border border-white/10 flex items-center justify-between">
            <div>
              <span className="text-[10px] text-gray-400 block uppercase">PRIMARY INBOX</span>
              <span className="text-white font-medium select-all">{PERSONAL_INFO.email}</span>
            </div>
            <button
              onClick={handleCopyEmail}
              className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white transition-colors"
              title="Copy Email"
            >
              <Copy className="w-4 h-4" />
            </button>
          </div>

          <div className="p-3.5 rounded-xl bg-noir-850 border border-white/10 flex items-center justify-between">
            <div>
              <span className="text-[10px] text-gray-400 block uppercase">TELEPHONE</span>
              <span className="text-white font-medium select-all">{PERSONAL_INFO.phone}</span>
            </div>
            <a
              href={`tel:${PERSONAL_INFO.phone.replace(/[^0-9]/g, '')}`}
              className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white transition-colors"
              title="Call"
            >
              <Phone className="w-4 h-4" />
            </a>
          </div>

          {/* Social Portals */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
            <a
              href={PERSONAL_INFO.social.linkedin}
              target="_blank"
              rel="noreferrer"
              className="p-3 rounded-xl bg-noir-850 hover:bg-white/10 border border-white/10 text-center text-xs text-gray-300 hover:text-gold-400 transition-all"
            >
              <Linkedin className="w-4 h-4 mx-auto mb-1" />
              <span>LinkedIn</span>
            </a>
            <a
              href={PERSONAL_INFO.social.github}
              target="_blank"
              rel="noreferrer"
              className="p-3 rounded-xl bg-noir-850 hover:bg-white/10 border border-white/10 text-center text-xs text-gray-300 hover:text-gold-400 transition-all"
            >
              <Github className="w-4 h-4 mx-auto mb-1" />
              <span>GitHub</span>
            </a>
            <a
              href={PERSONAL_INFO.social.streamlit}
              target="_blank"
              rel="noreferrer"
              className="p-3 rounded-xl bg-noir-850 hover:bg-white/10 border border-white/10 text-center text-xs text-gray-300 hover:text-gold-400 transition-all"
            >
              <Activity className="w-4 h-4 mx-auto mb-1" />
              <span>Streamlit</span>
            </a>
            <a
              href={PERSONAL_INFO.social.netlify}
              target="_blank"
              rel="noreferrer"
              className="p-3 rounded-xl bg-noir-850 hover:bg-white/10 border border-white/10 text-center text-xs text-gray-300 hover:text-gold-400 transition-all"
            >
              <Globe className="w-4 h-4 mx-auto mb-1" />
              <span>Netlify</span>
            </a>
          </div>

          <a
            href={`mailto:${PERSONAL_INFO.email}?subject=Opportunity%20Discussion%20with%20Shreyas%20B%20J`}
            className="mt-3 w-full py-3.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-display font-bold text-center block text-sm transition-all shadow-lg"
          >
            INITIATE COLLABORATION
          </a>

        </div>

        <p className="mt-16 text-xs font-mono text-gray-500">
          &copy; 2026 SHREYAS B J &bull; ENGINEERED &amp; DESIGNED WITH RIGOR
        </p>

      </div>
    </section>
  );
};
