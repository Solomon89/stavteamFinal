<template>
    <div>
        <app-header></app-header>
        <div class="pacient-block">
            Инфо о пациенте
        </div>
    </div>
</template>

<script>
import AppHeader from '../main/Header.vue';

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
        console.log(router.prop);
    }
}
</script>