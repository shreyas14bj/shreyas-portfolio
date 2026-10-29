import React, { useState, useEffect } from 'react';
import { CinematicHUD } from './components/CinematicHUD';
import { NeuralCanvas } from './components/NeuralCanvas';
import { Prologue } from './components/Prologue';
import { Genesis } from './components/Genesis';
import { JourneyTimeline } from './components/JourneyTimeline';
import { SkillsMatrix } from './components/SkillsMatrix';
import { ProjectVault } from './components/ProjectVault';
import { ArtGallery } from './components/ArtGallery';
import { TransmissionFinale } from './components/TransmissionFinale';
import { ExecutiveDossierModal } from './components/ExecutiveDossierModal';

export const App: React.FC = () => {
  const [executiveModalOpen, setExecutiveModalOpen] = useState(false);
  const [likesCount, setLikesCount] = useState<number>(() => {
    return parseInt(localStorage.getItem('shreyas_global_portfolio_likes') || '1482');
  });
  const [showToast, setShowToast] = useState(false);

  const handleGlobalLike = (e?: React.MouseEvent) => {
    const newCount = likesCount + 1;
    setLikesCount(newCount);
    localStorage.setItem('shreyas_global_portfolio_likes', String(newCount));

    const clientX = e ? e.clientX : window.innerWidth / 2;
    const clientY = e ? e.clientY : window.innerHeight / 2;
    createFloatingHeart(clientX, clientY);

    setShowToast(true);
    setTimeout(() => setShowToast(false), 2500);
  };

  const createFloatingHeart = (x: number, y: number) => {
    const heart = document.createElement('div');
    heart.className = 'floating-heart text-heart text-2xl font-bold';
    heart.innerHTML = '❤️';
    heart.style.left = `${Math.min(window.innerWidth - 40, Math.max(20, x - 12))}px`;
    heart.style.top = `${Math.min(window.innerHeight - 40, Math.max(20, y - 12))}px`;
    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 1200);
  };

  return (
    <div className="bg-noir-950 text-gray-200 antialiased overflow-x-hidden selection:bg-gold-500/25 selection:text-white font-sans relative min-h-screen">
      
      {/* Background Synaptic Particle Canvas */}
      <NeuralCanvas />

      {/* Film Vignette */}
      <div className="fixed inset-0 w-full h-full film-grain pointer-events-none z-10" />

      {/* Top HUD */}
      <CinematicHUD
        onOpenExecutiveModal={() => setExecutiveModalOpen(true)}
        likesCount={likesCount}
        onLike={handleGlobalLike}
      />

      {/* Toast */}
      <div
        className={`fixed bottom-6 right-6 z-50 bg-noir-850 border border-white/15 text-white font-mono text-xs px-4 py-3 rounded-xl shadow-2xl flex items-center space-x-3 transition-all duration-300 pointer-events-none ${
          showToast ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'
        }`}
      >
        <div className="w-6 h-6 rounded-full bg-heart flex items-center justify-center text-white shrink-0">
          ❤️
        </div>
        <span className="font-medium">Appreciation transmitted! Thank you.</span>
      </div>

      {/* Main Acts */}
      <main className="relative z-20">
        <Prologue />
        <Genesis />
        <JourneyTimeline />
        <SkillsMatrix />
        <ProjectVault />
        <ArtGallery />
        <TransmissionFinale />
      </main>

      {/* Executive Recruiter Dossier Modal */}
      <ExecutiveDossierModal
        isOpen={executiveModalOpen}
        onClose={() => setExecutiveModalOpen(false)}
      />
    </div>
  );
};
