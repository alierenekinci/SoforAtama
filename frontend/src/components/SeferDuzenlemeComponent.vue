<script setup>

import {useTripState} from "@/stores/trip_state";
import {ref} from "vue";

const tripStore = useTripState();

const duzenlecek_sefer = ref({
    sefer_tarih : "",
    sefer_saat : ""
})

function duzenle(){
  tripStore.editTrip(duzenlecek_sefer.value, tripStore.selectedTrip.sefer_id);
  duzenlecek_sefer.value = {
    sefer_tarih : "",
    sefer_saat : ""
  }
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="tripStore.selectedTrip === null">Düzenlenecek şoförü seçiniz..</div>
    <div class="col-10" v-if="tripStore.selectedTrip !== null">
      <div class="right">
        <button class="btn" @click="tripStore.selectedTrip = null">
          <font-awesome-icon icon="fa-solid fa-times"/>
          Kapat
        </button>
      </div>
      <h1>Düzenle</h1>

      <hr class="style">

      <p> Tüm alanları şuan doldurmak gerekiyor. Daha sonra düzenleme yapılacak.</p>
      <br>
      <div class="row">
        <div class="col-3">
          <label for="fad">Sefer Saati</label>
        </div>
        <div class="col-9">
          <input type="text" id="fsaat" name="saat" v-model="duzenlecek_sefer.sefer_saat"
                 :placeholder="tripStore.selectedTrip.sefer_saat">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fsoyad">Sefer Tarihi</label>
        </div>
        <div class="col-9">
          <input type="text" id="ftarih" name="tarih" v-model="duzenlecek_sefer.sefer_tarih"
                 :placeholder="tripStore.selectedTrip.sefer_tarih">
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