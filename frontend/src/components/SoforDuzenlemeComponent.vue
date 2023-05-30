<script setup>


import {useDriverState} from "@/stores/driver_state";
import {ref} from "vue";

const driverStore = useDriverState();

const duzenlenecek_kargo = ref({
    kargo_gonderici_id: "",
    kargo_alici_id: "",
    kargo_en: "",
    kargo_yukseklik: "",
    kargo_boy: "",
    kargo_agirlik: "",
})

function duzenle() {

    driverStore.editDriver(duzenlenecek_kargo.value, driverStore.selectedDriver.kargo_id);
    duzenlenecek_kargo.value = {
        kargo_gonderici_id: "",
        kargo_alici_id: "",
        kargo_en: "",
        kargo_yukseklik: "",
        kargo_boy: "",
        kargo_agirlik: "",
    }
}


</script>

<template>
    <div class="row">
        <div class="col-1"></div>
        <div class="col-10" v-if="cargoStore.selectedCargo === null">Düzenlenecek kargoyu seçiniz..</div>
        <div class="col-10" v-if="cargoStore.selectedCargo !== null">
            <h1>Düzenle</h1>
            <hr class="style">

            <p> Tüm alanları şuan doldurmak gerekiyor. Daha sonra düzenleme yapılacak.</p>
            <br>

            <div class="row">
                <div class="col-3">
                    <label for="fgonderici">Gönderici --- Seçili: {{
                        personStore.kisiBul(cargoStore.selectedCargo.kargo_gonderici_id)
                        }} </label>
                </div>
                <div class="col-9">
                    <select name="fgonderici" v-model="duzenlenecek_kargo.kargo_gonderici_id">
                        <option selected="selected" value="">Değiştirmek için seçim yapın</option>
                        <option v-for="kisi in personStore.persons" :value="kisi.kisi_id"> {{ kisi.kisi_ad + ' ' + kisi.kisi_soyad}}</option>
                    </select>

                </div>
            </div>
            <div class="row">
                <div class="col-3">
                    <label for="falici">Alıcı --- Seçili: {{ personStore.kisiBul(cargoStore.selectedCargo.kargo_alici_id) }}</label>
                </div>
                <div class="col-9">


                    <select name="falici" v-model="duzenlenecek_kargo.kargo_alici_id">
                        <option selected="selected" value="">Değiştirmek için seçim yapın</option>
                        <option v-for="kisi in personStore.persons" :value="kisi.kisi_id"> {{ kisi.kisi_ad + ' ' + kisi.kisi_soyad }}</option>
                    </select>

                </div>
            </div>
            <div class="row">
                <div class="col-3">
                    <label for="fen">En</label>
                </div>
                <div class="col-9">
                    <input type="number" id="fen" name="en" v-model="duzenlenecek_kargo.kargo_en"
                           :placeholder="'Şuan ki en: ' + cargoStore.selectedCargo.kargo_en + ' cm'">
                </div>
            </div>
            <div class="row">
                <div class="col-3">
                    <label for="fgenislik">Genişlik</label>
                </div>
                <div class="col-9">

                    <input type="number" id="fgenislik" name="genislik" v-model="duzenlenecek_kargo.kargo_boy"
                           :placeholder="'Şuan ki genişlik: ' +cargoStore.selectedCargo.kargo_boy + ' cm'">
                </div>
            </div>

            <div class="row">
                <div class="col-3">
                    <label for="fyukseklik">Yükseklik</label>
                </div>
                <div class="col-9">

                    <input type="number" id="fyukseklik" name="yukseklik" v-model="duzenlenecek_kargo.kargo_yukseklik"
                           :placeholder=" 'Şuan ki yükseklik: ' + cargoStore.selectedCargo.kargo_yukseklik + ' cm'">
                </div>
            </div>

            <div class="row">
                <div class="col-3">
                    <label for="fagirlik">Ağırlık</label>
                </div>
                <div class="col-9">

                    <input type="number" id="fagirlik" name="agirlik" v-model="duzenlenecek_kargo.kargo_agirlik"
                           :placeholder="'Şuan ki agırlık: ' + cargoStore.selectedCargo.kargo_agirlik + ' kg'">
                </div>
            </div>

            <div class="right">
                <button class="btn" @click="duzenle">
                    <font-awesome-icon icon="fa-solid fa-paper-plane"/>
                    Yolla
                </button>
            </div>

        </div>
        <div class="col-1"></div>
    </div>
</template>

<style scoped>

</style>