<script setup>
import {useBusState} from "@/stores/bus_state";
import {ref} from "vue";

const busStore = useBusState();
busStore.yukle();

const eklenecek_otobus = ref({
    otobus_plaka: "",
    otobus_tur: "",
    otobus_kapasite: ""});

function kaydet() {
    busStore.addBuses(eklenecek_otobus.value)
    eklenecek_otobus.value = {
        otobus_plaka: "",
        otobus_tur: "",
        otobus_kapasite: ""
    }
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <h1>Otobüs Ekle</h1>
      <hr class="style">
      <div class="row">
        <div class="col-3">
          <label for="fplaka">Plaka</label>
        </div>
        <div class="col-9">
          <input type="text" id="fplaka" placeholder="Otobüsün Plakasını Giriniz" v-model="eklenecek_otobus.otobus_plaka">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="ftur">Tür</label>
        </div>
        <div class="col-9">
          <input type="text" id="ftur" placeholder="Otobüsün Türünü Giriniz" v-model="eklenecek_otobus.otobus_tur">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fkapasite">Kapasite</label>
        </div>
        <div class="col-9">
          <input type="text" id="fkapasite" placeholder="Otobüsün Kapasitesini Giriniz" v-model="eklenecek_otobus.otobus_kapasite">
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