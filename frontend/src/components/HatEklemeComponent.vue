<script setup>

import {useLineState} from "@/stores/line_state";
import {ref} from "vue";

const lineStore = useLineState();
lineStore.yukle();

const eklenecek_hat = ref({
    hat_ad: "",
    hat_no : ""
})

function kaydet(){
    lineStore.addLines(eklenecek_hat.value)
    eklenecek_hat.value = {
        hat_ad: "",
        hat_no : ""
    }
}


</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <h1>Hat Ekle</h1>
      <hr class="style">
      <div class="row">
        <div class="col-3">
          <label for="fadi">Hat Adı</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Hattın Adını Giriniz" v-model="eklenecek_hat.hat_ad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fsoyad">No</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Hattın Nosunu Giriniz" v-model="eklenecek_hat.hat_no">
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