<template>
    <div>
        <div class="tools">
            <ul class="sort">
                <li id="name-sort"><a href="#">По фамилии</a></li>
                <li id="date-sort"><a href="#">По дате</a></li>
                <li id="risk-sort"><a href="#">По уровню риска</a></li>
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
    .sort {
        padding: 5px;
        margin-left: 50px;
    }
    .sort li {
        display: inline-block;
        font-size: 12px;
        padding-left: 20px;
        background-repeat: no-repeat;
        background-repeat: no-repeat;
        background-size: 16px;
        margin-right: 10px;
    }
    #name-sort {
        background-image: url(/static/img/sort-alpha-down.png);
    }
    #date-sort {
        background-image: url(/static/img/sort-calendar-ascending.png);
    }
    #risk-sort {
        background-image: url(/static/img/sort-ascending.png);
    }
</style>