import {defineStore} from "pinia";

export const useLoadingState = defineStore('loading',
    {
        state: () => ({loading : false}),
        actions: {
            yuklemeyeBasla(){
                this.loading = true;
            },
            yuklemeyiBitir(){
                this.loading = false
            }

        },
    });

