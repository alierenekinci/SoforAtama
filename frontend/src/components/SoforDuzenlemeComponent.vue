<script setup>


import {useDriverState} from "@/stores/driver_state";
import {ref} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

const driverStore = useDriverState();

const duzenlenecek_surucu = ref({
  sofor_ad: "",
  sofor_soyad: "",
  cinsiyet: ""
})

function duzenle() {

  driverStore.editDriver(duzenlenecek_surucu.value, driverStore.selectedDriver.sofor_id);
  duzenlenecek_surucu.value = {
    sofor_ad: "",
    sofor_soyad: "",
    cinsiyet: "",
  }
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="driverStore.selectedDriver === null">Düzenlenecek şoförü seçiniz..</div>
    <div class="col-10" v-if="driverStore.selectedDriver !== null">
      <div class="right">
        <button class="btn" @click="driverStore.selectedDriver = null">
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
          <label for="fad">Ad</label>
        </div>
        <div class="col-9">
          <input type="text" id="fad" name="ad" v-model="duzenlenecek_surucu.sofor_ad"
                 :placeholder="driverStore.selectedDriver.sofor_ad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fsoyad">Soyadı</label>
        </div>
        <div class="col-9">
          <input type="text" id="fsoyad" name="soyad" v-model="duzenlenecek_surucu.sofor_soyad"
                 :placeholder="driverStore.selectedDriver.sofor_soyad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fcinsiyet">Cinsiyet</label>
        </div>
        <div class="col-9">
          <input type="text" id="fcinsiyet" name="cinsiyet" v-model="duzenlenecek_surucu.cinsiyet"
                 :placeholder="driverStore.selectedDriver.cinsiyet">
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