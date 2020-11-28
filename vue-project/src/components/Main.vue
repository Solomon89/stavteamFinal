<template>
    <div>
        <app-header></app-header>
        <app-tools></app-tools>
    </div>
</template>

<script>
import AppHeader from './main/Header.vue';
import AppTools from './main/Tools.vue';
export default {
    data() {
        return {
            dataStations: {},
            dataLines: {}
        }
    },
    components: {
        AppHeader,
        AppTools
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