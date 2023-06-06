<script setup>
import {useTripState} from "@/stores/trip_state";
import {ref} from "vue";

const tripStore = useTripState();
tripStore.yukle();

const eklenecek_sefer = ref({
    sefer_tarih : "",
    sefer_saat : ""
})

function kaydet(){
  tripStore.addTrip(eklenecek_sefer.value);
  eklenecek_sefer.value = {
    sefer_tarih : "",
    sefer_saat : ""
  }
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <h1>Sefer Ekle</h1>
      <hr class="style">
      <div class="row">
        <div class="col-3">
          <label for="fsaat">Sefer Saati</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Sefer Saatini Giriniz" v-model="eklenecek_sefer.sefer_saat">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="ftarih">Sefer Tarih</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Sefer Tarihini Giriniz" v-model="eklenecek_sefer.sefer_tarih">
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