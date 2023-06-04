<script setup>


import {useLoadingState} from "@/stores/loading_state";
import {useBusState} from "@/stores/bus_state";

import OtobusDuzenlemeComponent from "@/components/OtobusDuzenlemeComponent.vue";

const load = useLoadingState();
const busStore = useBusState();

busStore.yukle();

function deleteBus(bus) {
    busStore.deleteBus(bus);
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <div class="loader" v-if="load.loading"></div>
      <div class="col-12" v-else>
        <h1>Otobüsler</h1>
        <hr class="style">
        <table>
          <tr>
            <th> <font-awesome-icon icon="fa-solid fa-hashtag" /></th>
            <th>Plaka</th>
            <th>Tür</th>
            <th>Kapasite</th>
            <th><button class="btn white right" @click="busStore.yukle()"><font-awesome-icon icon="fa-solid fa-arrows-rotate" /> Yenile</button></th>
          </tr>
          <div class="col-12" v-if="busStore.buses.length === 0">Otobüs bulunamadı eklenmesi gerekiyor.</div>
          <tr v-for="bus in busStore.buses">
            <td>{{ bus["otobus_id"] }}</td>
            <td>{{ bus["otobus_plaka"]}}</td>
            <td>{{ bus["otobus_tur"]}}</td>
            <td>{{ bus["otobus_kapasite"]}}</td>
            <td class="right">
              <button class="btn" @click="busStore.selectedBus=bus" ><font-awesome-icon icon="fa-solid fa-pen-to-square" /> Düzenle</button>
              /
              <button class="btn red" @click="deleteBus(bus)"><font-awesome-icon icon="fa-solid fa-trash" /> Sil</button>
            </td>
          </tr>
        </table>
        <br class="space">

        <button class="btn"><a href=""><font-awesome-icon icon="fa-solid fa-chevron-left" /> Önceki</a></button>
        <button class="btn">Sonraki <font-awesome-icon icon="fa-solid fa-chevron-right" /></button>
        <br class="space">


      </div>
    </div>
    <div class="col-1"></div>
  </div>
  <OtobusDuzenlemeComponent></OtobusDuzenlemeComponent>

</template>

<style scoped>

</style>