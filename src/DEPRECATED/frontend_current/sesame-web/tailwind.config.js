const {
  colors: defaultColors
} = require('tailwindcss/defaultTheme')

const colors = {
  ...defaultColors,
  ...{
    "sesame-light": {
      "500": "#5DDDE2 ",
    },
    "sesame-dark": {
      "500": "#5DADE2",
    },
  },
}

module.exports = {
  purge: [],
  darkMode: 'class', // or 'media' or 'class'
  "theme": {
    "colors": colors,
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
