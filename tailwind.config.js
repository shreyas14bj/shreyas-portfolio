/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        noir: {
          950: '#060709',
          900: '#0B0D12',
          850: '#11141B',
          800: '#171B24',
          700: '#232936',
          600: '#323B4E',
        },
        gold: {
          400: '#F5C563',
          500: '#E5A93C',
          600: '#C88A22',
        },
        cyan: {
          400: '#38BDF8',
          500: '#0EA5E9',
        },
        heart: '#FF3366',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        display: ['Space Grotesk', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
