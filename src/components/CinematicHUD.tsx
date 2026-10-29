import React, { useState } from 'react';
import { FileText, Menu, X, Heart, Palette } from 'lucide-react';

interface Props {
  onOpenExecutiveModal: () => void;
  likesCount: number;
  onLike: (e: React.MouseEvent) => void;
}

export const CinematicHUD: React.FC<Props> = ({ onOpenExecutiveModal, likesCount, onLike }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 w-full z-40 bg-noir-950/85 backdrop-blur-xl border-b border-white/10 transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand & Title */}
        <a href="#prologue" className="flex items-center space-x-3 group">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-gold-500/20 to-cyan-500/20 border border-white/15 flex items-center justify-center font-display font-bold text-sm text-gold-400 group-hover:border-gold-500 transition-colors">
            SB
          </div>
          <div>
            <span className="font-display font-bold text-sm sm:text-base tracking-tight text-white group-hover:text-gold-400 transition-colors">SHREYAS B J</span>
            <span className="text-[11px] text-gray-400 block -mt-0.5 font-mono">AI / ML Engineer &bull; TCS</span>
          </div>
        </a>

        {/* Navigation Links (Desktop) */}
        <nav className="hidden lg:flex items-center space-x-1 font-mono text-xs">
          <a href="#biography" className="px-3 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition-all">BIOGRAPHY</a>
          <a href="#journey" className="px-3 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition-all">EXPERIENCE</a>
          <a href="#matrix" className="px-3 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition-all">ARSENAL</a>
          <a href="#vault" className="px-3 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition-all">PROJECTS</a>
          <a href="#drawings" className="px-3 py-1.5 rounded-lg text-gold-400 hover:text-white hover:bg-white/5 transition-all font-semibold flex items-center space-x-1">
            <Palette className="w-3.5 h-3.5" />
            <span>SKETCH FEED</span>
          </a>
          <a href="#transmission" className="px-3 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition-all">CONTACT</a>
        </nav>

        {/* Right Action Docks */}
        <div className="flex items-center space-x-2 sm:space-x-3">
          
          {/* Like Button */}
          <button
            onClick={onLike}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-heart/10 hover:bg-heart/20 border border-heart/40 text-heart text-xs font-mono font-medium transition-all group"
            title="Leave appreciation"
          >
            <Heart className="w-3.5 h-3.5 fill-heart group-hover:scale-125 transition-transform" />
            <span className="font-bold">{likesCount.toLocaleString()}</span>
            <span className="hidden sm:inline text-[10px] text-gray-400">LIKES</span>
          </button>

          {/* Executive Mode */}
          <button
            onClick={onOpenExecutiveModal}
            className="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/15 text-white font-mono text-xs transition-all flex items-center space-x-1.5"
          >
            <FileText className="w-3.5 h-3.5 text-gold-400" />
            <span className="hidden md:inline">EXECUTIVE RESUME</span>
            <span className="md:hidden">RESUME</span>
          </button>

          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden p-2 text-gray-400 hover:text-white"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>

      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-b border-white/10 bg-noir-900/95 backdrop-blur-xl px-4 py-4 space-y-2 font-mono text-sm">
          <a onClick={() => setMobileMenuOpen(false)} href="#biography" className="block px-3 py-2 rounded text-gray-300 hover:bg-white/5 hover:text-white">BIOGRAPHY</a>
          <a onClick={() => setMobileMenuOpen(false)} href="#journey" className="block px-3 py-2 rounded text-gray-300 hover:bg-white/5 hover:text-white">EXPERIENCE</a>
          <a onClick={() => setMobileMenuOpen(false)} href="#matrix" className="block px-3 py-2 rounded text-gray-300 hover:bg-white/5 hover:text-white">ARSENAL &amp; CERTS</a>
          <a onClick={() => setMobileMenuOpen(false)} href="#vault" className="block px-3 py-2 rounded text-gray-300 hover:bg-white/5 hover:text-white">FEATURED PROJECTS</a>
          <a onClick={() => setMobileMenuOpen(false)} href="#drawings" className="block px-3 py-2 rounded text-gold-400 hover:bg-white/5 font-semibold">SKETCH FEED (INSTAGRAM POSTS)</a>
          <a onClick={() => setMobileMenuOpen(false)} href="#transmission" className="block px-3 py-2 rounded text-gray-300 hover:bg-white/5 hover:text-white">CONTACT</a>
        </div>
      )}
    </header>
  );
};
