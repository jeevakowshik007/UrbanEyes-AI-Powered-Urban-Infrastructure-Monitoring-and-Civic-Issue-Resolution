/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        celadon: '#7FBF9B',
        celadonDark: '#5DA87F',
        mustard: '#D8C46A',
        delft: '#4567A8',
        delftDark: '#33497e',
        navy: '#0F1B2D',
        ink: '#1B2740',
        cream: '#FAF7F0',
        weak: '#22a06b',
        medium: '#c9a227',
        critical: '#d64545',
      },
      fontFamily: {
        display: ['Sora', 'Inter', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        float: '0 12px 40px -12px rgba(15,27,45,.25)',
        card: '0 6px 24px -8px rgba(15,27,45,.18)',
      },
    },
  },
  plugins: [],
};
