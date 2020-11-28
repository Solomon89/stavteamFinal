<template>
    <div>
        <div class="tools">
            <ul class="sort">
                <li id="name-sort">По фамилии</li>
                <li id="date-sort">По дате</li>
                <li id="risk-sort">По уровню риска</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-tools',
    data() {
        return {
            
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
        margin-bottom: 15px;
    }
    .sort li {
        display: inline-block;
        font-size: 12px;
        padding-left: 20px;
    }
    #name-sort {
        background-image: "/static/img/sort-alpha-down.png";
    }
    #date-sort {
        background-image: "/static/img/sort-calendar-ascending.png";
    }
    #risk-sort {
        background-image: "/static/img/sort-ascending.png";
    }
</style>