<template>
    <div>
        <app-header></app-header>
        <div class="pacient-block">
            Инфо о пациенте
        </div>
    </div>
</template>

<script>
//import Vue from 'vue'
//import Router from 'vue-router'
import AppHeader from '../main/Header.vue';

//Vue.use(Router);

export default {
    data() {
        return {

        }
    },
    components: {
        AppHeader
    },
    methods: {

    },
    mounted() {
        let data = {
            session: sessionStorage.getItem('sessionId')
        };
        console.log(this.$route.params);
    }
}
</script>