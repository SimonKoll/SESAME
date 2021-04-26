const {
  colors:defaultColors
} = require('tailwindcss/defaultTheme')

const colors = {
  ...defaultColors,
  ...{
    "sesame-light": {
      "500": "#5DDDE2",
    },
    "sesame-dark": {
      "500": "#5DADE2",
    },
  },
}

module.exports = {
  prefix: '',
  purge: {
    content: [
      './src/**/*.{html,ts}',
    ]
  },
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    "colors": colors,
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'), 
    require('@tailwindcss/forms'), 
    require('@tailwindcss/line-clamp'), 
    require('@tailwindcss/typography')
  ],
};
