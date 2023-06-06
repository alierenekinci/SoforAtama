<script setup>
import { ref } from 'vue';
import { useAssigmentState} from "@/stores/assignment_state";
import AtamaSonucComponent from "@/components/AtamaSonucComponent.vue";

const assignmentStore = useAssigmentState();
assignmentStore.yukle();

function currentDate() {
    const current = new Date();
    const date = `${current.getDate()}/${current.getMonth()+1}/${current.getFullYear()} ${current.getHours()}:${current.getMinutes()}`;
    return date;

};

const eklenecek_atama = ref({
    atama_durum : "",
    atama_tarih : "",
    atama_gun : "",
    atama_sonuc : ""

})

function  kaydet() {
    eklenecek_atama.value.atama_tarih = currentDate();
    eklenecek_atama.value.atama_durum = false;
    assignmentStore.addAssigment(eklenecek_atama.value)
    eklenecek_atama.value = {
        atama_durum : false,
        atama_tarih : "",
        atama_gun: "",
        atama_sonuc : "",
    }
}




</script>

<template>
  <div class="row">
      <div class="col-1"></div>
      <div class="col-10">
        <div class="col-3">
            <h1>Yeni Atama </h1>
            <hr class="style">
            <div class="row">
                <div class="col-12">
                    <input type="text" placeholder="Gün sayısını giriniz" v-model="eklenecek_atama.atama_gun">
                </div>
            </div>
            <div class="right">
                <button class="btn" @click="kaydet"><font-awesome-icon icon="fa-solid fa-paper-plane" /> Atama Yap</button>
            </div>
        </div>
        <div class="col-9">
            <h1>Son 5 istek</h1>
            <hr class="style">
            <table>
                <tr>
                    <th>Atama Id</th>
                    <th>Atama Gün Sayısı</th>
                    <th>Atama Tarihi</th>
                    <th>Durum</th>
                    <th><button class="btn white right" @click="assignmentStore.yukle()"><font-awesome-icon icon="fa-solid fa-arrows-rotate" /> Yenile</button></th>
                </tr>
                <tr v-for="atama in assignmentStore.assigments.reverse().slice(0,5)">
                    <td>{{atama.atama_id}}</td>
                    <td>{{atama.atama_gun}}</td>
                    <td>{{atama.atama_tarih}}</td>
                    <td>{{atama.atama_durum == false ? 'İşlem daha devam ediyor.' : 'İşlem tamamladı.'}}</td>
                    <td class="right">
                        <button class="btn" @click="assignmentStore.selectedAssigmentDetail = null, assignmentStore.selectedAssigment = atama" v-if='atama.atama_durum==true'><font-awesome-icon icon="fa-solid fa-table-list" /> Göster</button>
                    </td>
                </tr>
            </table>
        </div>
      </div>
      <div class="col-1"></div>
  </div>
  <AtamaSonucComponent></AtamaSonucComponent>
</template>

<style scoped>



</style>