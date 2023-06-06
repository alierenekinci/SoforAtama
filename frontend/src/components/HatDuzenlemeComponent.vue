<script setup>
import {useLineState} from "@/stores/line_state";
import {ref} from "vue";


const lineStore = useLineState();

const duzenlecek_hat = ref({
  hat_ad: "",
  hat_no: ""
});

function duzenle() {
  lineStore.updateLine(duzenlecek_hat.value)
  duzenlecek_hat.value = {
    hat_ad: "",
    hat_no: ""
  }
}


</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="lineStore.selectedLine === null">Düzenlenecek hattı seçiniz..</div>
    <div class="col-10" v-if="lineStore.selectedLine !== null">
      <div class="right">
        <button class="btn" @click="lineStore.selectedLine = null">
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
          <label for="fad">Hat Adı</label>
        </div>
        <div class="col-9">
          <input type="text" id="fad" name="ad" v-model="duzenlecek_hat.hat_ad"
                 :placeholder="lineStore.selectedLine.hat_ad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fno">Hat No</label>
        </div>
        <div class="col-9">
          <input type="text" id="fno" name="no" v-model="duzenlecek_hat.hat_no"
                 :placeholder="lineStore.selectedLine.hat_no">
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