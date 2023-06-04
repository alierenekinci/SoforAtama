<script setup>
import {useBusState} from "@/stores/bus_state";
import {ref} from "vue";


const busStore = useBusState();

const duzenlenecek_otobus = ref({
  otobus_plaka: "",
  otobus_tur: "",
  otobus_kapasite: ""
});

function duzenle() {
  busStore.editBuses(duzenlenecek_otobus.value, busStore.selectedBus.otobus_id);
  duzenlenecek_otobus.value = {
    otobus_plaka: "",
    otobus_tur: "",
    otobus_kapasite: ""
  }
}
</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="busStore.selectedBus === null">Düzenlenecek otobüsü seçiniz..</div>
    <div class="col-10" v-if="busStore.selectedBus !== null">
      <div class="right">
        <button class="btn" @click="busStore.selectedBus = null">
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
          <label for="fplaka">Plaka</label>
        </div>
        <div class="col-9">
          <input type="text" id="fplaka" name="plaka" v-model="duzenlenecek_otobus.otobus_plaka"
                 :placeholder="busStore.selectedBus.otobus_plaka">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="ftur">Tür</label>
        </div>
        <div class="col-9">
          <input type="text" id="ftur" name="tur" v-model="duzenlenecek_otobus.otobus_tur"
                 :placeholder="busStore.selectedBus.otobus_tur">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fkapasite">Kapasite</label>
        </div>
        <div class="col-9">
          <input type="text" id="fkapasite" name="kapasite" v-model="duzenlenecek_otobus.otobus_kapasite"
                 :placeholder="busStore.selectedBus.otobus_kapasite">
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