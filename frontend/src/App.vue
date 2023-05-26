<script setup lang="ts">

</script>

<template>
    <div class="topnav">
        <div class="col-1 col-s-3"></div>
        <div class="col-10 col-s-6">
            <div class="left">
                <router-link to="/"><font-awesome-icon icon="fa-solid fa-truck" /> Şoför Atama Paneli</router-link>
            </div>
            <div class="right">

                <router-link to="/"><font-awesome-icon icon="fa-solid fa-list" /> Şoförler</router-link>
                <router-link to="/kargo-ekle"><font-awesome-icon icon="fa-solid fa-plus" /> Kargo Ekle</router-link>

                <router-link to="/kisiler"><font-awesome-icon icon="fa-solid fa-users" /> Kişiler</router-link>
                <router-link to="/kisi-ekle"><font-awesome-icon icon="fa-solid fa-user-plus" /> Kişi Ekle</router-link>
            </div>
        </div>
        <div class="col-1 col-s-3"></div>

    </div>
    <router-view></router-view>
</template>

<style scoped>
/* br */
br.space {
    margin-top: 3px;
    margin-bottom: 3px;
    color: inherit;
}
/* --br */
</style>
