// Procedural Web Audio API Synthesizer Engine
class AudioEngine {
  private ctx: AudioContext | null = null;
  private droneOsc1: OscillatorNode | null = null;
  private droneOsc2: OscillatorNode | null = null;
  private droneGain: GainNode | null = null;
  private droneFilter: BiquadFilterNode | null = null;
  private isPlaying: boolean = false;
  private listeners: ((playing: boolean) => void)[] = [];

  public subscribe(fn: (playing: boolean) => void) {
    this.listeners.push(fn);
    return () => {
      this.listeners = this.listeners.filter(l => l !== fn);
    };
  }

  private notify() {
    this.listeners.forEach(fn => fn(this.isPlaying));
  }

  public getIsPlaying(): boolean {
    return this.isPlaying;
  }

  public toggle(): boolean {
    if (this.isPlaying) {
      this.stop();
    } else {
      this.start();
    }
    return this.isPlaying;
  }

  public start() {
    try {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (!this.ctx) {
        this.ctx = new AudioCtx();
      }

      if (this.ctx.state === 'suspended') {
        this.ctx.resume();
      }

      if (!this.droneOsc1) {
        this.droneGain = this.ctx.createGain();
        this.droneGain.gain.setValueAtTime(0.0001, this.ctx.currentTime);

        this.droneFilter = this.ctx.createBiquadFilter();
        this.droneFilter.type = 'lowpass';
        this.droneFilter.frequency.setValueAtTime(150, this.ctx.currentTime);

        // Sub bass oscillator (55Hz)
        this.droneOsc1 = this.ctx.createOscillator();
        this.droneOsc1.type = 'sawtooth';
        this.droneOsc1.frequency.setValueAtTime(55, this.ctx.currentTime);

        // Harmonic oscillator (82.4Hz)
        this.droneOsc2 = this.ctx.createOscillator();
        this.droneOsc2.type = 'sine';
        this.droneOsc2.frequency.setValueAtTime(82.4, this.ctx.currentTime);

        this.droneOsc1.connect(this.droneFilter);
        this.droneOsc2.connect(this.droneFilter);
        this.droneFilter.connect(this.droneGain);
        this.droneGain.connect(this.ctx.destination);

        this.droneOsc1.start();
        this.droneOsc2.start();
      }

      if (this.droneGain && this.ctx) {
        this.droneGain.gain.linearRampToValueAtTime(0.07, this.ctx.currentTime + 2.5);
      }

      this.isPlaying = true;
      this.notify();
    } catch (e) {
      console.warn('Audio Engine could not start:', e);
    }
  }

  public stop() {
    if (this.droneGain && this.ctx) {
      this.droneGain.gain.linearRampToValueAtTime(0.0001, this.ctx.currentTime + 0.8);
      this.isPlaying = false;
      this.notify();
    }
  }

  public playTone(freq = 880, duration = 0.08, type: OscillatorType = 'sine') {
    if (!this.ctx || !this.isPlaying) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(freq * 1.4, this.ctx.currentTime + duration);

      gain.gain.setValueAtTime(0.02, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch {
      // Ignore audio glitch
    }
  }
}

export const audioEngine = new AudioEngine();
