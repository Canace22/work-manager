import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import {
  Container,
  Header,
  Footer,
  Main,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  Table,
  TableColumn,
  Button,
  Pagination,
  DatePicker,
  Form,
  FormItem,
  Input,
} from 'element-ui'
import "element-ui/lib/theme-chalk/index.css";
import router from './router'

Vue.config.productionTip = false

Vue.use(Container)
Vue.use(Dropdown)
Vue.use(Footer)
Vue.use(Header)
Vue.use(Main)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(Pagination)
Vue.use(Button)
Vue.use(DatePicker)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
