import React, { useState, useEffect } from 'react';
import { Heart, PlusCircle, Trash2, MessageCircle, Send, UploadCloud, X, Plus } from 'lucide-react';
import { PERSONAL_INFO } from '../data/portfolioData';

interface SketchPost {
  id: string;
  title: string;
  medium: string;
  caption: string;
  image: string;
  likes: number;
  isLiked: boolean;
  date: string;
}

const POSTS_STORAGE_KEY = 'shreyas_sketch_feed_posts_v1';

export const ArtGallery: React.FC = () => {
  const [posts, setPosts] = useState<SketchPost[]>(() => {
    const raw = localStorage.getItem(POSTS_STORAGE_KEY);
    if (raw) {
      try { return JSON.parse(raw); } catch { return []; }
    }
    return [];
  });

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [title, setTitle] = useState('');
  const [medium, setMedium] = useState('');
  const [caption, setCaption] = useState('');
  const [imageDraft, setImageDraft] = useState<string | null>(null);

  useEffect(() => {
    localStorage.setItem(POSTS_STORAGE_KEY, JSON.stringify(posts));
  }, [posts]);

  const handleImageSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setImageDraft(event.target?.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleCreatePost = (e: React.FormEvent) => {
    e.preventDefault();
    if (!imageDraft) {
      alert('Please select an image for your drawing.');
      return;
    }

    const newPost: SketchPost = {
      id: 'post_' + Date.now(),
      title: title.trim(),
      medium: medium.trim(),
      caption: caption.trim(),
      image: imageDraft,
      likes: 1,
      isLiked: true,
      date: 'Just now'
    };

    setPosts([newPost, ...posts]);
    setIsModalOpen(false);
    setTitle('');
    setMedium('');
    setCaption('');
    setImageDraft(null);
  };

  const handleToggleLike = (postId: string) => {
    setPosts(prev =>
      prev.map(p => {
        if (p.id === postId) {
          const isLiked = !p.isLiked;
          return {
            ...p,
            isLiked,
            likes: isLiked ? p.likes + 1 : Math.max(0, p.likes - 1)
          };
        }
        return p;
      })
    );
  };

  const handleDeletePost = (postId: string) => {
    if (confirm('Delete this drawing post?')) {
      setPosts(prev => prev.filter(p => p.id !== postId));
    }
  };

  const loadSampleSketches = () => {
    const samples: SketchPost[] = [
      {
        id: 'demo_portrait',
        title: "The Architect’s Gaze — Portrait Study",
        medium: "Graphite & Charcoal on 220gsm paper",
        caption: "Studying facial bone structures, contours, and micro-expressions trained my eye to spot anomalies in high-dimensional vector spaces and model loss plateaus.",
        image: "./assets/drawings/drawing-portrait.svg",
        likes: 42,
        isLiked: true,
        date: 'Yesterday'
      },
      {
        id: 'demo_landscape',
        title: "Misty Canopies of Baba Budangiri",
        medium: "Graphite Wash & Bristol Vellum",
        caption: "Drawing the recursive branching of shade-grown coffee canopies taught me graph theory and tree traversals long before I wrote my first search algorithm.",
        image: "./assets/drawings/drawing-landscape.svg",
        likes: 38,
        isLiked: false,
        date: '3 days ago'
      }
    ];
    setPosts(samples);
  };

  return (
    <section id="drawings" className="py-24 px-4 sm:px-6 lg:px-8 border-t border-white/10 bg-noir-900/50">
      <div className="max-w-4xl mx-auto">
        
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-10 pb-6 border-b border-white/10">
          <div>
            <div className="flex items-center space-x-2 font-mono text-xs text-gold-400 mb-2 uppercase tracking-wider">
              <span>ACT V &bull; THE OBSERVATIONAL SKETCH FEED</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-display font-bold text-white">
              Shreyas’s Drawing Feed.
            </h2>
            <p className="text-gray-400 text-sm mt-1">
              Fine-art sketches, observational studies, and visual engineering notes posted directly by Shreyas.
            </p>
          </div>

          <button
            onClick={() => setIsModalOpen(true)}
            className="px-4 py-2.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-mono text-xs font-bold transition-all shadow flex items-center space-x-2"
          >
            <PlusCircle className="w-4 h-4" />
            <span>POST NEW DRAWING</span>
          </button>
        </div>

        {/* Empty State */}
        {posts.length === 0 ? (
          <div className="text-center py-16 px-6 rounded-3xl border border-dashed border-white/20 bg-noir-900">
            <h3 className="text-xl font-display font-bold text-white mb-2">No Drawings Posted Yet</h3>
            <p className="text-gray-400 text-sm max-w-md mx-auto mb-6">
              Share your graphite, charcoal, or digital sketches! Click below to create your first Instagram-style drawing post.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 font-mono text-xs">
              <button
                onClick={() => setIsModalOpen(true)}
                className="px-5 py-2.5 rounded-xl bg-gold-500 text-noir-950 font-bold hover:bg-gold-400 transition-all flex items-center space-x-2"
              >
                <Plus className="w-4 h-4" />
                <span>CREATE FIRST POST</span>
              </button>
              <button
                onClick={loadSampleSketches}
                className="px-4 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 text-gray-300 hover:text-white transition-all"
              >
                Load Demo Sketches
              </button>
            </div>
          </div>
        ) : (
          /* Instagram Feed */
          <div className="space-y-12">
            {posts.map(post => (
              <article
                key={post.id}
                className="bg-noir-900 border border-white/15 rounded-3xl overflow-hidden shadow-2xl transition-all"
              >
                {/* Header */}
                <div className="px-5 py-4 border-b border-white/10 flex items-center justify-between">
                  <div className="flex items-center space-x-3">
                    <img
                      src="./assets/profile-avatar.svg"
                      alt={PERSONAL_INFO.name}
                      className="w-10 h-10 rounded-full object-cover border border-gold-400/40 p-0.5"
                    />
                    <div>
                      <div className="flex items-center space-x-2">
                        <span className="font-display font-bold text-white text-sm">Shreyas B J</span>
                        <span className="w-1.5 h-1.5 rounded-full bg-gold-400" />
                        <span className="text-[11px] font-mono text-gold-400 font-medium">Follow</span>
                      </div>
                      <span className="text-[11px] font-mono text-gray-400">
                        @shreyas.sketches &bull; {post.date}
                      </span>
                    </div>
                  </div>

                  <button
                    onClick={() => handleDeletePost(post.id)}
                    className="p-2 text-gray-500 hover:text-red-400 transition-colors"
                    title="Delete post"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>

                {/* Media */}
                <div
                  onDoubleClick={() => handleToggleLike(post.id)}
                  className="relative bg-noir-950 flex items-center justify-center overflow-hidden group select-none cursor-pointer"
                >
                  <img
                    src={post.image}
                    alt={post.title}
                    className="max-h-[640px] w-auto h-auto max-w-full object-contain mx-auto block group-hover:scale-[1.01] transition-transform duration-300"
                  />
                </div>

                {/* Action Bar */}
                <div className="p-5 space-y-3 font-mono">
                  <div className="flex items-center justify-between text-gray-300">
                    <div className="flex items-center space-x-4">
                      <button
                        onClick={() => handleToggleLike(post.id)}
                        className="flex items-center space-x-1.5 group focus:outline-none"
                      >
                        <Heart
                          className={`w-5 h-5 transition-transform group-hover:scale-125 ${
                            post.isLiked ? 'text-heart fill-heart' : 'hover:text-heart'
                          }`}
                        />
                        <span className={`font-bold text-xs ${post.isLiked ? 'text-heart' : 'text-white'}`}>
                          {post.likes}
                        </span>
                      </button>
                      <button className="hover:text-white transition-colors">
                        <MessageCircle className="w-5 h-5" />
                      </button>
                      <button className="hover:text-white transition-colors">
                        <Send className="w-5 h-5" />
                      </button>
                    </div>
                    <span className="text-[11px] text-gray-400 bg-white/5 px-2.5 py-1 rounded-md border border-white/10">
                      {post.medium}
                    </span>
                  </div>

                  {/* Caption */}
                  <div className="text-xs space-y-1 pt-1 font-sans">
                    <p className="text-white font-medium">
                      <span className="font-bold font-display mr-1.5">shreyas.sketches</span>
                      {post.title}
                    </p>
                    <p className="text-gray-300 leading-relaxed">{post.caption}</p>
                  </div>
                </div>
              </article>
            ))}
          </div>
        )}

      </div>

      {/* Upload Post Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 bg-noir-950/90 backdrop-blur-xl flex items-center justify-center p-4">
          <div className="max-w-lg w-full bg-noir-900 border border-white/20 rounded-3xl p-6 sm:p-8 shadow-2xl relative my-auto">
            <button
              onClick={() => setIsModalOpen(false)}
              className="absolute top-5 right-5 p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            <h3 className="text-2xl font-display font-bold text-white mb-6">Post to Sketch Feed</h3>

            <form onSubmit={handleCreatePost} className="space-y-4 font-mono text-xs">
              <div>
                <label className="block text-gray-300 mb-1.5 font-medium">Select Drawing / Sketch Photo</label>
                <label
                  htmlFor="postPhotoInputReact"
                  className="border-2 border-dashed border-white/20 hover:border-gold-400/60 rounded-2xl p-6 text-center cursor-pointer transition-colors bg-noir-950 block"
                >
                  {imageDraft ? (
                    <div>
                      <img src={imageDraft} alt="Draft" className="max-h-56 mx-auto rounded-xl object-contain mb-3" />
                      <span className="text-xs text-gold-400 block">Click to choose a different photo</span>
                    </div>
                  ) : (
                    <div>
                      <UploadCloud className="w-8 h-8 text-gold-400 mx-auto mb-2" />
                      <span className="text-white font-medium block">Click to select photo from computer</span>
                      <span className="text-gray-500 text-[11px] block mt-1">Supports JPG, PNG, SVG, WebP</span>
                    </div>
                  )}
                </label>
                <input
                  type="file"
                  id="postPhotoInputReact"
                  accept="image/*"
                  onChange={handleImageSelect}
                  className="hidden"
                />
              </div>

              <div>
                <label className="block text-gray-300 mb-1">Title / Subject</label>
                <input
                  type="text"
                  value={title}
                  onChange={e => setTitle(e.target.value)}
                  placeholder="e.g. Portrait Study of Mullayanagiri"
                  required
                  className="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2.5 text-white text-xs focus:outline-none focus:border-gold-400"
                />
              </div>

              <div>
                <label className="block text-gray-300 mb-1">Medium / Materials</label>
                <input
                  type="text"
                  value={medium}
                  onChange={e => setMedium(e.target.value)}
                  placeholder="e.g. 2B Graphite & Charcoal on 200gsm paper"
                  required
                  className="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2.5 text-white text-xs focus:outline-none focus:border-gold-400"
                />
              </div>

              <div>
                <label className="block text-gray-300 mb-1">Caption &amp; Reflection</label>
                <textarea
                  rows={3}
                  value={caption}
                  onChange={e => setCaption(e.target.value)}
                  placeholder="What did you observe or learn while sketching this piece?"
                  required
                  className="w-full bg-noir-950 border border-white/15 rounded-xl px-3.5 py-2.5 text-white text-xs focus:outline-none focus:border-gold-400"
                />
              </div>

              <div className="pt-2 flex items-center justify-end space-x-3">
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  className="px-4 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-6 py-2.5 rounded-xl bg-gold-500 hover:bg-gold-400 text-noir-950 font-bold transition-all shadow flex items-center space-x-1.5"
                >
                  <span>PUBLISH POST</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </section>
  );
};
