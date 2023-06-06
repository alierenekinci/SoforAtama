<script setup>
import HatDuzenlemeComponent from "@/components/HatDuzenlemeComponent.vue";
import {useLoadingState} from "@/stores/loading_state";
import {useLineState} from "@/stores/line_state";

const load = useLoadingState();
const lineStore = useLineState();

lineStore.yukle();

function deleteLine(line_id) {
  lineStore.deleteLine(line_id)
}


</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <div class="loader" v-if="load.loading"></div>
      <div class="col-12" v-else>
        <h1>Hatlar</h1>
        <hr class="style">
        <table>
          <tr>
            <th>
              <font-awesome-icon icon="fa-solid fa-hashtag"/>
            </th>
            <th>Hat Adı</th>
            <th>Hat No</th>
            <th>
              <button class="btn white right" @click="lineStore.yukle()">
                <font-awesome-icon icon="fa-solid fa-arrows-rotate"/>
                Yenile
              </button>
            </th>
          </tr>
          <div class="col-12" v-if="lineStore.lines.length === 0">Hat bulunamadı eklenmesi gerekiyor.</div>
          <tr v-for="line in lineStore.lines">
            <td>{{ line["hat_id"] }}</td>
            <td>{{ line["hat_ad"] }}</td>
            <td>{{ line["hat_no"] }}</td>
            <td class="right">
              <button class="btn" @click="lineStore.selectedLine = line">
                <font-awesome-icon icon="fa-solid fa-pen-to-square"/>
                Düzenle
              </button>
              /
              <button class="btn red" @click="deleteLine(line)">
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
  <HatDuzenlemeComponent></HatDuzenlemeComponent>

</template>

<style scoped>

</style>