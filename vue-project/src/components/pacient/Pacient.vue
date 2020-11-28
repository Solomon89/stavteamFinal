<template>
    <div>
        <app-header></app-header>
        <div class="menu">
            <a href="/">Вернуться к списку пациентов</a>
        </div>
        <div class="pacient-block">
            <div class="left-block">
                <div class="pacient">
                    <div class="header-info">
                        <div class="image">
                            <img src="/static/img/pacient-no-img.png">
                        </div>
                        <div class="text-block">
                            <div class="info">
                                <span>{{ pacients[pacientId].name }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="pacient-info">
                        <table>
                            <thead>
                                <tr><td colspan="2"><strong>Основные сведения</strong></td><td></td></tr>
                            </thead>
                            <tbody>
                                <tr><td>Место проживания:</td><td>{{ pacients[pacientId].name }}</td></tr>
                                <tr><td>Пол:</td><td>{{ pacients[pacientId].gender }}</td></tr>
                                <tr><td>Семья:</td><td>{{ pacients[pacientId].family }}</td></tr>
                                <tr><td>Образование:</td><td>{{ pacients[pacientId].education }}</td></tr>
                                <tr><td>Профессия:</td><td>{{ pacients[pacientId].profession }}</td></tr>
                                <tr><td>Количество человек в домохозяйстве:</td><td>{{ pacients[pacientId].livingPeople }}</td></tr>
                                <tr><td>Ежемесячный доход:</td><td>{{ pacients[pacientId].salary }}</td></tr>
                            </tbody>
                        </table>
                        <table>
                            <thead>
                                <tr><td colspan="2"><strong>Заболевания</strong></td><td></td></tr>
                            </thead>
                            <tbody>
                                <tr><td>Диагноз:</td><td>{{ pacients[pacientId].diagnosis }}</td></tr>
                                <tr><td>Код по МКБ-10:</td><td>{{ pacients[pacientId].mkb }}</td></tr>
                            </tbody>
                        </table>
                        <table>
                            <thead>
                                <tr><td colspan="2"><strong>Образ жизни</strong></td><td></td></tr>
                            </thead>
                            <tbody>
                                <tr><td>Курение:</td><td>{{ pacients[pacientId].smoke }}</td></tr>
                                <tr><td>Алкоголь:</td><td>{{ pacients[pacientId].alkohol }}</td></tr>
                                <tr><td>Сон:</td><td>{{ pacients[pacientId].sleep }}</td></tr>
                                <tr><td>Спорт:</td><td>{{ pacients[pacientId].sport }}</td></tr>
                                <tr><td>Питание:</td><td>{{ pacients[pacientId].eat }}</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="right-block"></div>
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
                    status: '/static/img/heart-red.png',
                    address: 'г. Москва',
                    gender: 'мужской',
                    family: 'В разводе',
                    education: 'Высшее',
                    profession: 'Инженер',
                    livingPeople: '2',
                    salary: '50000 руб',
                    diagnosis: 'Эссенциальная (первичная) гипертензия',
                    mkb: 'I10',
                    smoke: 'Нет',
                    alkohol: 'Регулярно, легкий',
                    sleep: 'Засыпание 23:00, просыпание 6:10',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '2',
                    photo: '',
                    name: 'Николаенко Александр Александрович',
                    status: '/static/img/heart-green.png',
                    address: 'г. Люберцы',
                    gender: 'мужской',
                    family: 'В браке',
                    education: 'Среднее-специальное',
                    profession: 'Механик-водитель',
                    livingPeople: '1',
                    salary: '25000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Да',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:42, просыпание 6:47',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '3',
                    photo: '',
                    name: 'Коновалова Любава Витальевна',
                    status: '/static/img/heart-red.png',
                    address: 'г. Курск',
                    gender: 'женский',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'экономист',
                    livingPeople: '3',
                    salary: '35000',
                    diagnosis: 'Бессимптомная ишемия миокарда',
                    mkb: 'I25.6',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 23:24, просыпание 6:07',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '4',
                    photo: '',
                    name: 'Волков Руслан Антонинович',
                    status: '/static/img/heart-red.png',
                    address: 'г. Москва',
                    gender: 'мужской',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Военнослужаший',
                    livingPeople: '2',
                    salary: '40000',
                    diagnosis: 'Повторный инфаркт миокарда',
                    mkb: 'I22',
                    smoke: 'Да, 5-6 сигарет в день',
                    alkohol: 'Редко, легкий',
                    sleep: 'Засыпание 23:02, просыпание 5:34',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '5',
                    photo: '',
                    name: 'Ермакова Владислава Владленовна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Москва',
                    gender: 'женский',
                    family: 'В браке',
                    education: 'среднее',
                    profession: 'Медицинский работник',
                    livingPeople: '4',
                    salary: '24000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:02, просыпание 5:57',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '6',
                    photo: '',
                    name: 'Ефимова Ландыш Валерьевна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Москва',
                    gender: 'Женский',
                    family: 'Разведена',
                    education: 'Среднее',
                    profession: 'Разнорабочая',
                    livingPeople: '1',
                    salary: '18000',
                    diagnosis: 'Алкогольная кардиомиопатия',
                    mkb: 'I42.6',
                    smoke: 'Да, регулярно',
                    alkohol: 'Крепкий, регулярно',
                    sleep: 'Засыпание 00:02, просыпание 8:57',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '7',
                    photo: '',
                    name: 'Степанов Илларион Ярославович',
                    status: '/static/img/heart-green.png',
                    address: 'г. Белгород',
                    gender: 'мужской',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Юрист',
                    livingPeople: '3',
                    salary: '42000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:56, просыпание 6:45',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '8',
                    photo: '',
                    name: 'Тихонова Калерия Рудольфовна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Санкт-Петербург',
                    gender: 'Женский',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Юрист',
                    livingPeople: '3',
                    salary: '38000 руб',
                    diagnosis: 'Кардиомиопатия',
                    mkb: 'I42',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:42, просыпание 6:15',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '9',
                    photo: '',
                    name: 'Максимов Оскар Евсеевич',
                    status: '/static/img/heart-red.png',
                    address: 'г. Москва',
                    gender: 'мужской',
                    family: 'Разведен',
                    education: 'Среднее-специальное',
                    profession: 'Электрик',
                    livingPeople: '1',
                    salary: '22000',
                    diagnosis: 'Острый перикардит',
                    mkb: 'I30',
                    smoke: 'Нет',
                    alkohol: 'Легкий, 1-2 раза в неделю',
                    sleep: 'Засыпание 22:57, просыпание 6:33',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '10',
                    photo: '',
                    name: 'Веселова Виргиния Степановна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Краснодар',
                    gender: 'женский',
                    family: 'В браке',
                    education: 'Среднее-специальное',
                    profession: 'Продавец',
                    livingPeople: '2',
                    salary: '21000',
                    diagnosis: 'Кардиомиопатия',
                    mkb: 'I42',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:42, просыпание 6:15',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '11',
                    photo: '',
                    name: 'Овчинникова Ландыш Ивановна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Москва',
                    gender: 'Женский',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Служащий',
                    livingPeople: '3',
                    salary: '32000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 22:56, просыпание 6:45',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '12',
                    photo: '',
                    name: 'Козлов Осип Андреевич',
                    status: '/static/img/heart-green.png',
                    address: 'г. Москва',
                    gender: 'мужской',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Военнослужаший',
                    livingPeople: '2',
                    salary: '40000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Да, 5-6 сигарет в день',
                    alkohol: 'Редко, легкий',
                    sleep: 'Засыпание 23:02, просыпание 5:34',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '13',
                    photo: '',
                    name: 'Дьячкова Глория Игоревна',
                    status: '/static/img/heart-red.png',
                    address: 'г. Москва',
                    gender: 'Женский',
                    family: 'Разведена',
                    education: 'Среднее',
                    profession: 'Уборщица',
                    livingPeople: '1',
                    salary: '16000',
                    diagnosis: 'Повторный инфаркт миокарда',
                    mkb: 'I22',
                    smoke: 'Нет',
                    alkohol: 'Редко, легкий',
                    sleep: 'Засыпание 22:57, просыпание 6:33',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '14',
                    photo: '',
                    name: 'Зайцева Ева Мэлоровна',
                    status: '/static/img/heart-green.png',
                    address: 'г. Ростов-на-Дону',
                    gender: 'Женский',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Бухгалтер',
                    livingPeople: '2',
                    salary: '35000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Нет',
                    alkohol: 'Редко',
                    sleep: 'Засыпание 22:59, просыпание 6:10',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                },
                {
                    id: '15',
                    photo: '',
                    name: 'Беспалов Леонтий Мэлорович',
                    status: '/static/img/heart-green.png',
                    address: 'г. Москва',
                    gender: 'мужской',
                    family: 'В браке',
                    education: 'Высшее',
                    profession: 'Экономист',
                    livingPeople: '',
                    salary: '45000',
                    diagnosis: 'Митральная (клапанная) недостаточность',
                    mkb: 'I34.0',
                    smoke: 'Нет',
                    alkohol: 'Нет',
                    sleep: 'Засыпание 23:15, просыпание 6:00',
                    sport: 'Данные о спорте',
                    eat: 'Данные о питании'
                }
            ],
            pacientId: 0
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
        };
    },
    created() {
        this.pacientId = this.$route.params.id - 1;
    }
}
</script>

<style>
.left-block, .right-block {
    display: inline-block;
}
.left-block {
    float: left;
}
.pacient .image {
    float: left;
    display: inline-block;
    border-radius: 25px;
    padding: 10px;
    width: 50px;
    height: 50px;
    background-color: #e5e5e5;
    margin-right: 10px;
    position: relative;
}
.pacient .image span {
    position: absolute;
    top: 0;
}
.pacient .image span img {
    width: 20px;
}
.pacient .text-block {
    display: inline-block;
}
.menu {
    height: 40px;
    background-color: #E5E5E5;
    margin-bottom: 15px;
    padding: 5px 5px 5px 25px;
}
.menu a {
    text-decoration: none;
    color: #ffffff;
    padding-left: 27px;
    background: url(/static/img/arrow-left.png) no-repeat;
}
</style>