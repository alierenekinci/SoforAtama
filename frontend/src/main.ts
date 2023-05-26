import { createApp } from 'vue'
import {createPinia} from "pinia";

import App from './App.vue'

import './assets/main.css'

import {
    faTruck,
    faList,
    faUserPlus,
    faPlus,
    faPaperPlane,
    faPenToSquare,
    faTrash,
    faUpRightAndDownLeftFromCenter,
    faArrowsLeftRight,
    faArrowsUpDown,
    faWeightHanging,
    faCube,
    faCircle,
    faSquare,
    faHashtag,
    faArrowsRotate,
    faChevronRight,
    faChevronLeft,
    faPhone,
    faInbox,
    faMapLocationDot,
    faUsers

} from '@fortawesome/free-solid-svg-icons'


import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

library.add(faTruck, faList, faUserPlus, faPlus, faPaperPlane, faPenToSquare, faTrash, faUpRightAndDownLeftFromCenter,
    faArrowsLeftRight, faArrowsUpDown, faWeightHanging, faCube, faCircle, faSquare, faHashtag, faArrowsRotate,
    faChevronRight, faChevronLeft, faPhone, faInbox, faMapLocationDot, faUsers)



import SoforListesiComponent from "@/components/SoforListesiComponent.vue";
import SoforDuzenlemeComponent from "@/components/SoforDuzenlemeComponent.vue";
import SoforEklemeComponent from "@/components/SoforEklemeComponent.vue";

import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path : '/', component : SoforListesiComponent}
    ]
});
const app = createApp(App)
    .use(createPinia())
    .use(router)
    .component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
