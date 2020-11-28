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
                },
                {
                    photo: '',
                    name: 'Коновалова Любава Витальевна',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Волков Руслан Антонинович',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Ермакова Владислава Владленовна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Ефимова Ландыш Валерьевна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Степанов Илларион Ярославович',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Тихонова Калерия Рудольфовна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Максимов Оскар Евсеевич',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Веселова Виргиния Степановна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Овчинникова Ландыш Ивановна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Козлов Осип Андреевич',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Дьячкова Глория Игоревна',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Зайцева Ева Мэлоровна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Беспалов Леонтий Мэлорович',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Сафонов Вольдемар Кириллович',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Ершов Пантелей Парфеньевич',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Тетерин Ян Игнатьевич',
                    status: 'alert'
                },
                {
                    photo: '',
                    name: 'Романова Ярослава Рубеновна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Назаров Овидий Николаевич',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Кондратьева Евгения Агафоновна',
                    status: 'ok'
                },
                {
                    photo: '',
                    name: 'Лукин Иосиф Платонович',
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

</style>