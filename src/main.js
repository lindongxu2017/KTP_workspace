import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import router from '@/router'
import section from 'com/section.vue'
import '@/assets/reset.css'

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mixin({
  components: {
    mySection: section
  }
})
app.mount('#app')
