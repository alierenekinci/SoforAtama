<script setup>
import {useLoadingState} from "@/stores/loading_state";
import {useAssigmentState} from "@/stores/assignment_state";
import {useDriverState} from "@/stores/driver_state";
import {useBusState} from "@/stores/bus_state";
import {useLineState} from "@/stores/line_state";
import {useTripState} from "@/stores/trip_state";

const load = useLoadingState();
const assignmentStore = useAssigmentState();
const driverStore = useDriverState();
const busStore = useBusState();
const lineStore = useLineState();
const tripStore = useTripState();

assignmentStore.yukle();
driverStore.yukle();
busStore.yukle();
lineStore.yukle();
tripStore.yukle();



</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="assignmentStore.selectedAssigment === null"></div>
    <div class="col-10" v-if="assignmentStore.selectedAssigment !== null ">
      <div class="right">
        Alternatif Sonuçlar:
        <button class="btn" @click="assignmentStore.selectedAssigmentDetail = JSON.parse(assignmentStore.selectedAssigment['atama_sonuc'])[0]">1. Sonuç</button>
        <button class="btn" @click="assignmentStore.selectedAssigmentDetail = JSON.parse(assignmentStore.selectedAssigment['atama_sonuc'])[1]">2. Sonuç</button>
        <button class="btn" @click="assignmentStore.selectedAssigmentDetail = JSON.parse(assignmentStore.selectedAssigment['atama_sonuc'])[2]">3. Sonuç</button>
        <button class="btn" @click="assignmentStore.selectedAssigment = null, assignmentStore.selectedAssigmentDetail = null ">Kapat</button>
      </div>
      <h1>Atama Sonucu</h1>
      <hr class="style">
      <table>
        <tr>
          <th></th>
          <th>Şoför</th>  
          <th>Gün</th>
          <th>Otobüs</th>
          <th>Hat</th>
          <th>Sefer</th>

        </tr>
        <tr v-for="(assigment, index ) in assignmentStore.selectedAssigmentDetail">
          <td>{{ index }}</td>
          <td>{{ driverStore.searchDriver(assigment["sofor"]) }}</td>
          <td>{{ assigment["gun"] }}</td>
          <td>{{ busStore.searchBus(assigment["otobus"]) }}</td>
          <td>{{ lineStore.searchLine(assigment["hat"]) }}</td>
          <td>{{ tripStore.searchTrip(assigment["sefer"], assigment["gun"])}}</td>
          {{ console.log(assigment) }}
        </tr>
      </table>

      <br class="space">
      <br class="space">
      <br class="space">


    </div>
    <div class="col-1"></div>

  </div>

</template>

<style scoped>

</style>