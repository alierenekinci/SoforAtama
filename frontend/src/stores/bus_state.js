import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";


export const useBusState = defineStore('bus',
    {
        state: () => ({
            buses: [],
            selectedBus: null
        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/otobus/').then((response) => {
                    this.buses = response.data;
                    load.yuklemeyiBitir();
                })
            },
            searchBus(id) {
                for (let i = 0; i < this.buses.length; i++) {

                    if (this.buses[i].otobus_id === id) {
                        return this.buses[i].otobus_plaka
                    }
                }
            },
            addBuses(bus) {
                axios.post('http://127.0.0.1:5000/api/v1/otobus/', bus).then((response) => {
                    const new_bus = response.data;
                    console.log(new_bus);
                    this.yukle();
                })
            },
            editBuses(bus, bus_id) {
                axios.put('http://127.0.0.1:5000/api/v1/otobus/' + bus_id, bus).then((response) => {
                    const new_bus = response.data;
                    this.buses.push(new_bus);
                    this.yukle();
                })
            },
            deleteBus(bus){
                axios.delete('http://127.0.0.1:5000/api/v1/otobus/' + bus["otobus_id"]).then((response) => {
                    const new_bus = response.data;
                    console.log(new_bus);
                    this.yukle();
                })
            }
        }
    })