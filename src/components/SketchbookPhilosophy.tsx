import React, { useState } from 'react';
import { Eye, RefreshCw, Pencil, Code2 } from 'lucide-react';
import { audioEngine } from '../utils/audioEngine';

export const SketchbookPhilosophy: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'sketch' | 'code'>('sketch');

  const handleTabChange = (tab: 'sketch' | 'code') => {
    setActiveTab(tab);
    audioEngine.playTone(tab === 'sketch' ? 700 : 1100, 0.08);
  };

  return (
    <section id="philosophy" className="min-h-screen py-24 px-4 sm:px-6 lg:px-8 relative border-t border-white/5 flex items-center">
      <div className="max-w-6xl mx-auto w-full">
        
        <div className="flex items-center space-x-3 mb-4">
          <span className="px-2.5 py-0.5 rounded bg-accent-cyan/10 border border-accent-cyan/30 text-accent-cyan font-mono text-xs font-semibold">ACT V</span>
          <span className="font-mono text-xs text-gray-400 tracking-wider uppercase">// BEHIND THE SCENES</span>
        </div>

        <h2 className="text-3xl sm:text-5xl font-display font-bold text-white mb-6">
          The Artist’s Eye, The Engineer’s Rigor.
        </h2>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center mt-8">
          
          <div className="lg:col-span-6 space-y-6 text-gray-300 text-base sm:text-lg leading-relaxed">
            <p>
              In my personal time, I immerse myself in <span className="text-white font-medium border-b border-accent-cyan/40">Drawing and Sketching</span>. What might appear as a simple artistic hobby is actually the cornerstone of how I approach engineering challenges.
            </p>
            <blockquote className="p-4 rounded-xl bg-surface border-l-4 border-accent-cyan text-sm sm:text-base font-light italic text-white/90">
              &ldquo;The practice of refining small pencil details, assessing proportions, and learning from mistakes directly mirrors debugging code, optimizing machine learning weights, and pursuing continuous learning.&rdquo;
            </blockquote>
            <p>
              When diagnosing machine failure modes at Foxconn, designing an AI agent at TCS, or structuring a scalable React component tree, the instinct is always identical: <span className="text-accent-cyan font-medium">look deeper than the surface anomaly</span>, trace the underlying lines of tension, and iterate until the solution is both structurally sound and aesthetically refined.
            </p>

            <div className="grid grid-cols-2 gap-4 pt-4 font-mono text-xs">
              <div className="p-4 rounded-xl bg-card border border-white/10">
                <Eye className="w-5 h-5 text-accent-cyan mb-2" />
                <h4 className="text-white font-bold mb-1">Visual Observation</h4>
                <p className="text-gray-400">Noticing micro-anomalies in data distributions and hardware telemetry before they escalate.</p>
              </div>
              <div className="p-4 rounded-xl bg-card border border-white/10">
                <RefreshCw className="w-5 h-5 text-accent-violet mb-2" />
                <h4 className="text-white font-bold mb-1">Continuous Learning</h4>
                <p className="text-gray-400">Relentless curiosity across LLMs, Databricks Lakehouse, and emerging generative paradigms.</p>
              </div>
            </div>
          </div>

          {/* Right Interactive Comparison */}
          <div className="lg:col-span-6">
            <div className="rounded-2xl bg-card border border-white/15 p-6 shadow-2xl relative overflow-hidden">
              <div className="flex items-center justify-between pb-4 border-b border-white/10 font-mono text-xs">
                <span className="text-gray-400">INTERACTIVE CONCEPT COMPARISON</span>
                <span className="text-accent-cyan">OBSERVATION &bull; CODE</span>
              </div>

              {/* Tabs */}
              <div className="mt-4 flex gap-2 font-mono text-xs">
                <button
                  onClick={() => handleTabChange('sketch')}
                  className={`px-3 py-1.5 rounded-lg transition-all ${
                    activeTab === 'sketch'
                      ? 'bg-accent-cyan text-void font-bold'
                      : 'bg-white/5 text-gray-300 hover:bg-white/10'
                  }`}
                >
                  THE SKETCH (PENCIL)
                </button>
                <button
                  onClick={() => handleTabChange('code')}
                  className={`px-3 py-1.5 rounded-lg transition-all ${
                    activeTab === 'code'
                      ? 'bg-accent-cyan text-void font-bold'
                      : 'bg-white/5 text-gray-300 hover:bg-white/10'
                  }`}
                >
                  THE CODE (LOGIC)
                </button>
              </div>

              {/* Content */}
              {activeTab === 'sketch' ? (
                <div className="mt-6 p-6 rounded-xl bg-void/80 border border-white/10 font-mono text-xs space-y-4">
                  <div className="flex items-center justify-between text-gray-400">
                    <span>CANVAS: GRAPHITE &amp; CROSS-HATCH</span>
                    <span className="text-accent-amber">ANALOG PRECISION</span>
                  </div>
                  <div className="py-8 text-center text-gray-400 border border-dashed border-white/20 rounded-lg">
                    <Pencil className="w-12 h-12 mx-auto mb-2 text-accent-amber/70" />
                    <p className="text-white font-medium text-sm">Visualizing Vector Topologies &amp; Gradients</p>
                    <p className="text-[11px] text-gray-500 mt-1">&quot;Every line is a hypothesis tested against reality.&quot;</p>
                  </div>
                  <ul className="text-[11px] text-gray-300 space-y-1.5 list-disc list-inside">
                    <li>Patience to build depth through incremental layering</li>
                    <li>Zero fear of erasing and re-drafting flawed fundamentals</li>
                    <li>Heightened spatial awareness for UI/UX information architecture</li>
                  </ul>
                </div>
              ) : (
                <div className="mt-6 p-6 rounded-xl bg-void/90 border border-white/10 font-mono text-xs space-y-4">
                  <div className="flex items-center justify-between text-gray-400">
                    <span>SYNTAX: PYTHON / RAG VECTOR RETRIEVAL</span>
                    <span className="text-accent-cyan">DIGITAL EXECUTION</span>
                  </div>
                  <pre className="p-3 rounded bg-surface text-[11px] text-accent-cyan/90 overflow-x-auto leading-relaxed border border-white/5">
<code>{`def build_rag_agent(query: str):
    # Synthesize observation into vector search
    vector_db = Chroma(persist_dir="./travel_kb")
    context_docs = vector_db.similarity_search(query, k=4)
    
    # Grounded LLM synthesis
    response = llm_chain.run(
        query=query, 
        context=context_docs
    )
    return response`}</code>
                  </pre>
                  <ul className="text-[11px] text-gray-300 space-y-1.5 list-disc list-inside">
                    <li>Deterministic error handling and test coverage</li>
                    <li>Clean separation of concerns with Object-Oriented patterns</li>
                    <li>Performance benchmarking against real customer datasets</li>
                  </ul>
                </div>
              )}

            </div>
          </div>

        </div>

      </div>
    </section>
  );
};
