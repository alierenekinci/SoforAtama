import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";

export const useLineState = defineStore('line',
    {
        state: () => ({
            lines: [],
            selectedLine: null
        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/hat/').then((response) => {
                    this.lines = response.data;
                    load.yuklemeyiBitir();
                })
            },
            searchLine(id) {
                for (let i = 0; i < this.lines.length; i++) {

                    if (this.lines[i].hat_id === id) {
                        return this.lines[i].hat_ad
                    }
                }
            },
            addLines(line) {
                axios.post('http://127.0.0.1:5000/api/v1/hat/', line).then((response) => {
                    const new_line = response.data;
                    console.log(new_line);
                    this.yukle();
                })
            },
            editLine(line, line_id) {
                axios.put('http://127.0.0.1:5000/api/v1/hat/' + line_id, line).then((response) => {
                    const new_line = response.data;
                    this.lines.push(new_line);
                    console.log(new_line);
                    this.yukle();
                })
            },
            deleteLine(line){
                axios.delete('http://127.0.0.1:5000/api/v1/hat/' + line["hat_id"]).then((response) => {
                    const new_line = response.data;
                    console.log(new_line);
                    this.yukle();
                })
            }
        }
    })