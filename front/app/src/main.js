import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

// axios configuration
const baseURL = 'http://localhost:5000';
Vue.prototype.$axios = axios.create({ baseURL });

Vue.config.productionTip = true;
Vue.config.devtools = false;

new Vue({
  render: function (h) { return h(App) }
}).$mount('#app');
