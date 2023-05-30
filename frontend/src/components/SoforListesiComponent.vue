<script setup>
import SoforDuzenlemeComponent from "@/components/SoforDuzenlemeComponent.vue";
import {useLoadingState} from "@/stores/loading_state";
import {useDriverState} from "@/stores/driver_state";

const load = useLoadingState();
const driverStore = useDriverState();


driverStore.yukle();


function deleteDriver(driver_id){
    cargoStore.kargoSil(driver_id)
}
</script>

<template>
    <div class="row">
        <div class="col-1"></div>
        <div class="col-10">
            <div class="loader" v-if="load.loading"></div>
            <div class="col-12" v-else>
                <h1>Şoförler</h1>
                <hr class="style">


                <table>
                    <tr>
                        <th> <font-awesome-icon icon="fa-solid fa-hashtag" /></th>
                        <th>Ad</th>
                        <th>Soyad</th>
                        <th>Cinsiyet</th>
                        <th><button class="btn white right" @click="driverStore.yukle()"><font-awesome-icon icon="fa-solid fa-arrows-rotate" /> Yenile</button></th>
                    </tr>
                    <div class="col-12" v-if="driverStore.drivers.length === 0">Şoför bulunamadı eklenmesi gerekiyor.</div>
                    <tr v-for="driver in driverStore.drivers">
                        <td>{{ driver["sofor_id"] }}</td>
                        <td>{{ driver["sofor_ad"]}}</td>
                        <td>{{ driver["sofor_soyad"]}}</td>
                        <td>{{ driver["cinsiyet"]}}</td>
                        <td class="right">
                            <button class="btn" @click="driverStore.selectedDriver=driver" ><font-awesome-icon icon="fa-solid fa-pen-to-square" /> Düzenle</button>
                            /
                            <button class="btn red" @click="deleteCargo(kargo)"><font-awesome-icon icon="fa-solid fa-trash" /> Sil</button>
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
    <!--- <SoforDuzenlemeComponent></SoforDuzenlemeComponent> -->



</template>

<style scoped>
/* Table */




table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    /* border: 1px solid #d4d4d4; */
}

th {
    background-color: #161612;
    color: #f2f2f2;
}

th, td {

    text-align: left;
    padding: 16px;
    transition: all 300ms ease-out;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

/* ---Table */

</style>