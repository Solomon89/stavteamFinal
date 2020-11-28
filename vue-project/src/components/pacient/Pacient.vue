<template>
    <div>
        <app-header></app-header>
        <div class="pacient-block">
            {{ pacients[data.pacientId].name }}
        </div>
    </div>
</template>

<script>
import AppHeader from '../main/Header.vue';

export default {
    data() {
        return {
            pacients: [
                {
                    id: '1',
                    photo: '',
                    name: 'Крестовоздвиженский Николай Константинович',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '2',
                    photo: '',
                    name: 'Николаенко Александр Александрович',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '3',
                    photo: '',
                    name: 'Коновалова Любава Витальевна',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '4',
                    photo: '',
                    name: 'Волков Руслан Антонинович',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '5',
                    photo: '',
                    name: 'Ермакова Владислава Владленовна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '6',
                    photo: '',
                    name: 'Ефимова Ландыш Валерьевна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '7',
                    photo: '',
                    name: 'Степанов Илларион Ярославович',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '8',
                    photo: '',
                    name: 'Тихонова Калерия Рудольфовна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '9',
                    photo: '',
                    name: 'Максимов Оскар Евсеевич',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '10',
                    photo: '',
                    name: 'Веселова Виргиния Степановна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '11',
                    photo: '',
                    name: 'Овчинникова Ландыш Ивановна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '12',
                    photo: '',
                    name: 'Козлов Осип Андреевич',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '13',
                    photo: '',
                    name: 'Дьячкова Глория Игоревна',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '14',
                    photo: '',
                    name: 'Зайцева Ева Мэлоровна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '15',
                    photo: '',
                    name: 'Беспалов Леонтий Мэлорович',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '16',
                    photo: '',
                    name: 'Сафонов Вольдемар Кириллович',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '17',
                    photo: '',
                    name: 'Ершов Пантелей Парфеньевич',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '18',
                    photo: '',
                    name: 'Тетерин Ян Игнатьевич',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '19',
                    photo: '',
                    name: 'Романова Ярослава Рубеновна',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '20',
                    photo: '',
                    name: 'Назаров Овидий Николаевич',
                    status: '/static/img/heart-green.png'
                },
                {
                    id: '21',
                    photo: '',
                    name: 'Кондратьева Евгения Агафоновна',
                    status: '/static/img/heart-red.png'
                },
                {
                    id: '22',
                    photo: '',
                    name: 'Лукин Иосиф Платонович',
                    status: '/static/img/heart-green.png'
                }
            ]
        }
    },
    components: {
        AppHeader
    },
    methods: {

    },
    mounted() {
        let data = {
            session: sessionStorage.getItem('sessionId'),
            pacientId: this.$route.params - 1
        };
        console.log(this.$route.params);
    }
}
</script>