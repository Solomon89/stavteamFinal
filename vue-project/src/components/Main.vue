<template>
    <div>
        <app-header></app-header>
    </div>
</template>

<script>
import AppHeader from './main/Header.vue';
export default {
    data() {
        return {
            dataStations: {},
            dataLines: {}
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
    }
}
</script>