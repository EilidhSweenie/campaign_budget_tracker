import { createApp } from 'vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Icons
import '@mdi/font/css/materialdesignicons.css'

// Components
import App from './App.vue'

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'myLightTheme',
    themes: {
      myLightTheme: {
        dark: false,
        colors: {
          primary: '#FFFCEB',
          secondary: '#FFDD33',  
          surface: '#ffffff',
          background: '#ffffff',
          error: '#b00020',
        },
      },
    },
  },
})

createApp(App).use(vuetify).mount('#app')
