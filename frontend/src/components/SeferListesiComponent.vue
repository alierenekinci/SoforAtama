<script setup>
import SeferDuzenlemeComponent from "@/components/SeferDuzenlemeComponent.vue";
import {useLoadingState} from "@/stores/loading_state";
import {useTripState} from "@/stores/trip_state";

const load = useLoadingState();
const tripStore = useTripState();

tripStore.yukle();

function deleteTrip(trip_id) {
  tripStore.deleteTrip(trip_id)
}


</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <div class="loader" v-if="load.loading"></div>
      <div class="col-12" v-else>
        <h1>Seferler</h1>
        <hr class="style">
        <table>
          <tr>
            <th>
              <font-awesome-icon icon="fa-solid fa-hashtag"/>
            </th>
            <th>Sefer Tarih</th>
            <th>Sefer Saat</th>
            <th>
              <button class="btn white right" @click="tripStore.yukle()">
                <font-awesome-icon icon="fa-solid fa-arrows-rotate"/>
                Yenile
              </button>
            </th>
          </tr>
          <div class="col-12" v-if="tripStore.trips.length === 0">Sefer bulunamadı eklenmesi gerekiyor.</div>
          <tr v-for="trip in tripStore.trips">
            <td>{{ trip["sefer_id"] }}</td>
            <td>{{ trip["sefer_tarih"] }}</td>
            <td>{{ trip["sefer_saat"] }}</td>
            <td class="right">
              <button class="btn" @click="tripStore.selectedTrip=trip">
                <font-awesome-icon icon="fa-solid fa-pen-to-square"/>
                Düzenle
              </button>
              /
              <button class="btn red" @click="deleteTrip(trip)">
                <font-awesome-icon icon="fa-solid fa-trash"/>
                Sil
              </button>
            </td>
          </tr>
        </table>
        <br class="space">

        <button class="btn"><a href="">
          <font-awesome-icon icon="fa-solid fa-chevron-left"/>
          Önceki</a></button>
        <button class="btn">Sonraki
          <font-awesome-icon icon="fa-solid fa-chevron-right"/>
        </button>
        <br class="space">


      </div>
    </div>
    <div class="col-1"></div>
  </div>
  <SeferDuzenlemeComponent></SeferDuzenlemeComponent>

</template>

<style scoped>

</style>