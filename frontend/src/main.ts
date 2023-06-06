import { createApp } from 'vue'
import {createPinia} from "pinia";

import App from './App.vue'

import './assets/main.css'

import {
    faChevronRight,
    faChevronLeft,
    faCompassDrafting,
    faBusAlt,
    faBus,
    faMapSigns,
    faRoad,
    faCaretDown,
    faList,
    faUserPlus,
    faPlus,
    faPaperPlane,
    faPenToSquare,
    faTrash,
    faArrowsRotate,
    faUsers,
    faHashtag,
    faTableList,
    faTimes

} from '@fortawesome/free-solid-svg-icons'


import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

library.add(faTimes, faHashtag, faBusAlt, faCompassDrafting, faBus, faMapSigns, faCaretDown, faRoad, faList, faUserPlus, faPlus,
    faPaperPlane, faPenToSquare, faTrash, faArrowsRotate, faUsers, faTableList, faChevronRight, faChevronLeft)



import SoforListesiComponent from "@/components/SoforListesiComponent.vue";
import SoforEklemeComponent from "@/components/SoforEklemeComponent.vue";

import {createRouter, createWebHistory} from "vue-router";
import AtamaComponent from "@/components/AtamaComponent.vue";
import OtobusEklemeComponent from "@/components/OtobusEklemeComponent.vue";
import OtobusListesiComponet from "@/components/OtobusListesiComponent.vue";
import HatListesiComponent from "@/components/HatListesiComponent.vue";
import HatEklemeComponent from "@/components/HatEklemeComponent.vue";
import SeferListesiComponent from "@/components/SeferListesiComponent.vue";
import SeferEklemeComponent from "@/components/SeferEklemeComponent.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path : '/', component : AtamaComponent},
        { path : '/soforler', component: SoforListesiComponent},
        { path : '/soforekle', component: SoforEklemeComponent},
        { path : '/otobusler', component: OtobusListesiComponet},
        { path : '/otobusekle', component: OtobusEklemeComponent},
        { path : '/hatlar', component: HatListesiComponent},
        { path : '/hatekle', component: HatEklemeComponent},
        { path : '/seferler', component: SeferListesiComponent},
        { path : '/seferekle', component: SeferEklemeComponent  }

    ]
});
const app = createApp(App)
    .use(createPinia())
    .use(router)
    .component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
