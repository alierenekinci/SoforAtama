<script setup lang="ts">

</script>

<template>
    <div class="topnav">
        <div class="col-1 col-s-3"></div>
        <div class="col-10 col-s-6">
            <div class="left">
                <router-link to="/"><font-awesome-icon icon="fa-solid fa-bus-alt" /> Şoför Atama Paneli</router-link>
            </div>

            <div class="right">
                <router-link to="/"><font-awesome-icon icon="fa-solid fa-compass-drafting" /> Atama</router-link>
                <div class="dropdown">
                    <button class="dropbtn">Şoförler <font-awesome-icon icon="fa-solid fa-caret-down" /></button>
                    <div class="dropdown-content">
                        <router-link to="/soforler"><font-awesome-icon icon="fa-solid fa-users" /> Şoför Listesi</router-link>
                        <router-link to="/soforekle"><font-awesome-icon icon="fa-solid fa-plus" /> Şoför Ekle</router-link>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Otobüsler <font-awesome-icon icon="fa-solid fa-caret-down" /></button>
                    <div class="dropdown-content">
                        <router-link to="/otobusler"><font-awesome-icon icon="fa-solid fa-bus"/> Otobüs Listesi</router-link>
                        <router-link to="/otobusekle"><font-awesome-icon icon="fa-solid fa-plus" /> Otobüs Ekle</router-link>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Hatlar <font-awesome-icon icon="fa-solid fa-caret-down" /></button>
                    <div class="dropdown-content">
                        <router-link to="/hatlar"><font-awesome-icon icon="fa-solid fa-road"/> Hat Listesi</router-link>
                        <router-link to="/hatekle"><font-awesome-icon icon="fa-solid fa-plus" /> Hat Ekle</router-link>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Seferler <font-awesome-icon icon="fa-solid fa-caret-down" /></button>
                    <div class="dropdown-content">
                        <router-link to="/seferler"><font-awesome-icon icon="fa-solid fa-map-signs"/> Sefer Listesi</router-link>
                        <router-link to="/seferekle"><font-awesome-icon icon="fa-solid fa-plus" /> Sefer Ekle</router-link>
                    </div>
                </div>


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

/* Dropdown */


/* The dropdown container */
.dropdown {
    float: left;
    overflow: hidden;
}

/* Dropdown button */
.dropdown .dropbtn {
    font-size: 16px;
    font-weight: 600;
    border: none;
    outline: none;
    color: #d4d4d4;
    padding: 14px 16px;
    background-color: inherit;
    cursor: pointer;
    transition: all 1000ms ease;
    font-family: inherit; /* Important for vertical align on mobile phones */
    margin: 0; /* Important for vertical align on mobile phones */
}

/* Add a red background color to navbar links on hover */
.navbar a:hover, .dropdown:hover .dropbtn {
    color: #161612;
    background-color: #f2f2f2;
}

/* Dropdown content (hidden by default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f2f2f2;
    min-width: 160px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
    z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
    float: none;
    color: #161612;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
    transition: all 1000ms ease;
}

/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
    color: #161612;
    background-color: #d4d4d4;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
    display: block;
}


/* --Dropdown */
</style>
