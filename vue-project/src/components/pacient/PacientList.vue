<template>
    <div>
        <div class="pacients">
            <ul>
                <li v-for="pacient in pacients">
                    <div class="pacient">
                        <div class="image"></div>
                        <div class="text-block">
                            <div class="info">
                                <span>{{ pacient.name }}</span>
                                <span></span>
                            </div>
                            <div class="control">
                                <input type="button" value="Написать">
                                <input type="button" value="Отправть напоминание">
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-pacients',
    data() {
        return {
            pacients: [
                {
                    photo: '',
                    name: 'Крестовоздвиженский Николай Константинович',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Николаенко Александр Александрович',
                    status: 'ok'
                }
            ]
        }
    },
    methods: {

    }
}
</script>

<style scoped>
    .tools {
        height: 40px;
        background-color: #E5E5E5;
    }
</style>