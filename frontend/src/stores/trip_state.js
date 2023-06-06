import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";


export const useTripState = defineStore('trip',
    {
        state: () => ({
            trips : [],
            selectedTrip: null

        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/sefer').then((response) => {
                    this.trips = response.data;
                    load.yuklemeyiBitir();
                })
            },
            addTrip(trip) {
                axios.post('http://127.0.0.1:5000/api/v1/sefer/', trip).then((response) => {
                    const new_trip = response.data;
                    console.log(new_trip);
                    this.yukle();
                })
            },
            searchTrip(id) {
                for (let i = 0; i < this.trips.length; i++) {
                    if(this.trips[i].sefer_id === id){
                        return this.trips[i].sefer_tarih + " " + this.trips[i].sefer_saat
                    }

                }
            },
            editTrip(trip, trip_id) {
                axios.put('http://127.0.0.1:5000/api/v1/sefer/' + trip_id, trip).then((response) => {
                    const new_trip = response.data;
                    this.buses.push(new_trip);
                    this.yukle();
                })
            },
            deleteTrip(trip){
                axios.delete('http://127.0.0.1:5000/api/v1/sefer/' + trip["sefer_id"]).then((response) => {
                    const new_trip = response.data;
                    console.log(new_trip);
                    this.yukle();
                })
            }
        }
    })