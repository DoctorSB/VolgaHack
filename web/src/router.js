import { createRouter, createWebHashHistory} from "vue-router";

import residents_main from "./vue/residents_main.vue";
import resident1 from "./vue/resident1.vue"
import resident2 from "./vue/resident2.vue"
import resident3 from "./vue/resident3.vue";
import resident4 from "./vue/resident4.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/resident-main', component: residents_main, alias: '/' },
        { path: '/resident-one', component: resident1 },
        { path: '/resident-two', component: resident2 },
        { path: '/resident-three', component: resident3 },
        { path: '/resident-four', component: resident4 }
    ]
})