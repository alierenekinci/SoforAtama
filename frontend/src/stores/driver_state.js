import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";


export const useDriverState = defineStore('driver',
    {
        state: () => ({
            drivers: [],
            selectedDriver: null
        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/sofor/').then((response) => {
                    this.drivers = response.data;
                    load.yuklemeyiBitir();
                })
            },
            searchDriver(id) {
                for (let i = 0; i < this.drivers.length; i++) {

                    if (this.drivers[i].sofor_id === id) {
                        return this.drivers[i].sofor_ad + " " + this.drivers[i].sofor_soyad
                    }
                }
            },
            addDrivers(driver) {
                axios.post('http://127.0.0.1:5000/api/v1/sofor/', driver).then((response) => {
                    const new_driver = response.data;
                    console.log(new_driver);
                    this.yukle();
                })
            },
            editDriver(driver, driver_id) {
                axios.put('http://127.0.0.1:5000/api/v1/sofor/' + driver_id, driver).then((response) => {
                    const new_driver = response.data;
                    this.drivers.push(new_driver);
                    this.yukle();
                })
            },
            deleteDriver(driver){
                axios.delete('http://127.0.0.1:5000/api/v1/sofor/' + driver["sofor_id"]).then((response) => {
                    const new_driver = response.data;
                    console.log(new_driver);
                    this.yukle();
                })
            }
        }
    })