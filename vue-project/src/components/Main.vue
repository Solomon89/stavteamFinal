<template>
    <div>
        <app-header></app-header>
        <app-tools></app-tools>
        <app-pacients></app-pacients>
    </div>
</template>

<script>
import AppHeader from './main/Header.vue';
import AppTools from './main/Tools.vue';
import AppPacients from './pacient/PacientList.vue';
export default {
    data() {
        return {

        }
    },
    components: {
        AppHeader,
        AppTools,
        AppPacients
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