<template>
    <div>
        <div class="pacients">
            <ul>
                <li v-for="pacient in pacients">
                    <a v-bind:href="'/pacient/' + pacient.id" target="_blank">
                        <div class="pacient">
                            <div class="image">
                                <img src="/static/img/pacient-no-img.png">
                                <span><img v-bind:src="pacient.status"></span>
                            </div>
                            <div class="text-block">
                                <div class="info">
                                    <span>{{ pacient.name }}</span>
                                    <span></span>
                                </div>
                                <div class="control">
                                    <input type="button" class="btn btn-primary" value="Написать">
                                    <input type="button" class="btn btn-outline-warning" value="Отправить напоминание">
                                </div>
                            </div>
                        </div>
                    </a>
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
    methods: {

    }
}
</script>

<style scoped>
    .pacients li {
        display: inline-block;
        width: 32%;
        padding: 7px;
        font-size: 14px;
    }
    .pacient input {
        font-size: 12px;
        padding: 2px;
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
</style>