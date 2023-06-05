<script setup>
import {useLoadingState} from "@/stores/loading_state";
import {useAssigmentState} from "@/stores/assignment_state";

const load = useLoadingState();
const assignmentStore = useAssigmentState();

assignmentStore.yukle();

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="assignmentStore.selectedAssigment === null"></div>
    <div class="col-10" v-if="assignmentStore.selectedAssigment !== null ">
      <div class="right">
        <button class="btn" @click="assignmentStore.selectedAssigment = null">Kapat</button>
      </div>
      <h1>Atama Sonucu</h1>
      <hr class="style">


      <table>
        <tr>
          <th>Şöför</th>
          <th>Gün</th>
          <th>Otobüs</th>
          <th>Hat</th>
          <th>Sefer</th>

        </tr>
        <tr v-for="sonuc in JSON.parse(assignmentStore.selectedAssigment['atama_sonuc'])">
          <td>{{ sonuc[0]["sofor"]}}</td>
          <td>{{ sonuc[0]["gun"]}}</td>
          <td>{{ sonuc[0]["otobus"]}}</td>
          <td>{{ sonuc[0]["hat"]}}</td>
          <td>{{ sonuc[0]["sefer"]}}</td>

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