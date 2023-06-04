<script setup>
import {useDriverState} from "@/stores/driver_state";
import {ref} from "vue";

const driverStore = useDriverState();
driverStore.yukle();

const eklenecek_surucu = ref({
    sofor_ad: "",
    sofor_soyad : "",
    cinsiyet : ""
})


function kaydet() {
    driverStore.addDrivers(eklenecek_surucu.value)
    eklenecek_surucu.value = {
        sofor_ad: "",
        sofor_soyad : "",
        cinsiyet : ""
    }
}
</script>

<template>
    <div class="row">
        <div class="col-1"></div>
        <div class="col-10">
            <h1>Şoför Ekle</h1>
            <hr class="style">
            <div class="row">
                <div class="col-3">
                    <label for="fadi">Adı</label>
                </div>
                <div class="col-9">
                    <input type="text" placeholder="Şoförün Adını Giriniz" v-model="eklenecek_surucu.sofor_ad">
                </div>
            </div>
            <div class="row">
                <div class="col-3">
                    <label for="fsoyad">Soyad</label>
                </div>
                <div class="col-9">
                    <input type="text" placeholder="Şoförün Soyadını Giriniz" v-model="eklenecek_surucu.sofor_soyad">
                </div>
            </div>

            <div class="row">
                <div class="col-3">
                    <label for="fcinsiyet">Cinsiyet</label>
                </div>
                <div class="col-9">
                    <input type="text" placeholder="Cinsiyet" v-model="eklenecek_surucu.cinsiyet">
                </div>
            </div>
            <div class="right">
                <button class="btn" @click="kaydet"><font-awesome-icon icon="fa-solid fa-paper-plane" /> Yolla</button>
            </div>

        </div>
        <div class="col-1"></div>
    </div>
</template>

<style scoped>

</style>