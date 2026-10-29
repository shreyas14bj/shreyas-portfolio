import React, { useState } from 'react';
import { Camera, RotateCcw, User } from 'lucide-react';
import { PERSONAL_INFO } from '../data/portfolioData';

export const Genesis: React.FC = () => {
  const [profilePhoto, setProfilePhoto] = useState<string>(() => {
    return localStorage.getItem('shreyas_uploaded_profile_photo') || PERSONAL_INFO.avatar;
  });

  const handlePhotoUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const dataUrl = event.target?.result as string;
        setProfilePhoto(dataUrl);
        try {
          localStorage.setItem('shreyas_uploaded_profile_photo', dataUrl);
        } catch {
          console.warn('LocalStorage quota reached, photo active in memory');
        }
      };
      reader.readAsDataURL(file);
    }
  };

  const handleResetPhoto = () => {
    localStorage.removeItem('shreyas_uploaded_profile_photo');
    setProfilePhoto(PERSONAL_INFO.avatar);
  };

  return (
    <section id="biography" className="py-24 px-4 sm:px-6 lg:px-8 border-t border-white/10">
      <div className="max-w-6xl mx-auto">
        
        <div className="flex items-center space-x-2 font-mono text-xs text-gold-400 mb-3 uppercase tracking-wider">
          <User className="w-4 h-4" />
          <span>ACT I &bull; BIOGRAPHY &amp; IDENTITY</span>
        </div>

        <h2 className="text-3xl sm:text-4xl font-display font-bold text-white mb-10">
          The Story Behind the Systems.
        </h2>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          
          {/* Left: Dynamically Sized Profile Photo Container */}
          <div className="lg:col-span-5 flex flex-col items-center">
            
            <div className="max-w-sm w-fit inline-block transition-all duration-300 rounded-3xl p-2 bg-gradient-to-b from-white/15 to-white/5 border border-white/15 shadow-2xl overflow-hidden group">
              <div className="rounded-2xl bg-noir-900 overflow-hidden relative flex items-center justify-center">
                <img
                  src={profilePhoto}
                  alt="Shreyas B J - Profile Portrait"
                  className="max-h-[460px] w-auto h-auto max-w-full object-contain rounded-2xl block group-hover:scale-[1.02] transition-transform duration-300"
                />
              </div>
            </div>

            {/* Upload Controls */}
            <div className="mt-4 flex items-center space-x-3">
              <label
                htmlFor="profilePhotoInputReact"
                className="cursor-pointer px-4 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-xs font-mono text-gray-200 hover:text-white transition-all flex items-center space-x-2"
              >
                <Camera className="w-3.5 h-3.5 text-gold-400" />
                <span>Upload Profile Photo</span>
              </label>
              <input
                type="file"
                id="profilePhotoInputReact"
                accept="image/*"
                onChange={handlePhotoUpload}
                className="hidden"
              />

              <button
                onClick={handleResetPhoto}
                className="p-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-gray-400 hover:text-white transition-all"
                title="Reset to default portrait"
              >
                <RotateCcw className="w-3.5 h-3.5" />
              </button>
            </div>
            <p className="text-[11px] font-mono text-gray-500 mt-2 text-center">
              Frame automatically resizes to fit your photo's exact aspect ratio
            </p>

          </div>

          {/* Right: Single Paragraph Biography & Key Credentials */}
          <div className="lg:col-span-7 space-y-6">
            
            <div className="p-6 sm:p-8 rounded-3xl bg-noir-900 border border-white/10 shadow-xl">
              <span className="font-mono text-xs text-gold-400 font-semibold uppercase tracking-wider block mb-3">
                BIOGRAPHICAL NARRATIVE
              </span>
              
              <p className="text-base sm:text-lg text-gray-200 font-normal leading-relaxed text-justify sm:text-left">
                Born in the tranquil coffee highlands of <span className="text-white font-medium">Chikkamagaluru, Karnataka</span>, I am an AI/ML Engineer and Creative Technologist who bridges the rigorous precision of hardware engineering with the cognitive frontiers of artificial intelligence. Graduating with an <span className="text-gold-400 font-mono font-semibold">8.89 / 10 CGPA</span> in Electronics and Communication Engineering from Nagarjuna College of Engineering and Technology, Bangalore, I developed an instinct for deterministic systems that deepened during industrial hardware failure analysis and statistical boxplot diagnostics at <span className="text-white font-medium">Foxconn</span>. Currently advancing enterprise machine learning workflows at <span className="text-cyan-400 font-medium">Tata Consultancy Services (TCS)</span> and certified in Databricks Machine Learning, Anthropic Claude, and Google Cloud Gemini, I architect production-grade Retrieval-Augmented Generation (RAG) agents and intuitive analytics platforms. Outside the terminal, my lifelong discipline of fine-art sketching directly informs my engineering philosophy — observing micro-anomalies before they escalate, refining subtle details, and architecting solutions where technical depth meets aesthetic elegance.
              </p>
            </div>

            {/* Badges */}
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono text-xs">
              <div className="p-3.5 rounded-xl bg-noir-850 border border-white/10">
                <span className="text-gray-400 block mb-0.5">LOCATION</span>
                <span className="text-white font-semibold">Chikkamagaluru &bull; BLR</span>
              </div>
              <div className="p-3.5 rounded-xl bg-noir-850 border border-white/10">
                <span className="text-gray-400 block mb-0.5">CURRENT ROLE</span>
                <span className="text-cyan-400 font-semibold">ASET @ TCS (AI/ML)</span>
              </div>
              <div className="p-3.5 rounded-xl bg-noir-850 border border-white/10 col-span-2 sm:col-span-1">
                <span className="text-gray-400 block mb-0.5">CERTIFICATIONS</span>
                <span className="text-gold-400 font-semibold">Databricks &bull; Claude</span>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
};
