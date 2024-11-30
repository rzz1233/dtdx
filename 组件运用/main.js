import Vue from 'vue'
import App from './App.vue'
//导入全局组件
import HmButton from './components/HmButton.vue'

Vue.config.productionTip = false

//全局组件vue.component('组件名',组件对象)
Vue.component('HmButton',HmButton)

new Vue({
  render: h => h(App),
}).$mount('#app')
