import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";

export const useAssigmentState = defineStore('assignment',
    {
        state: () => ({
            assigments : [],
            selectedAssigment: null

        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/atama/').then((response) => {
                    this.assigments = response.data;
                    load.yuklemeyiBitir();
                })
            },
            addAssigment(assign) {
                axios.post('http://127.0.0.1:5000/api/v1/atama/', assign).then((response) => {
                    const assigment = response.data;
                    console.log(assigment);
                    this.yukle();
                })
            },
            listAssigment(assign, assign_id) {
                for (let i = 0; i < this.assigments; i++) {
                    if(this.assigments[i].atama_id === assign_id){
                        return this.assigments[i].atama_id
                    }

                }
            },
        }
    })