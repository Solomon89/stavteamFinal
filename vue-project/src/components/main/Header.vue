<template>
    <div>
        <div class='header-container'>
            <div class="header-logo">
                <img src="/static/img/logo.png" width="52px" height="auto">
            </div>
            <div class="search">
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="Поиск по пациентам">
                    <div class="input-group-append">
                        <span class="input-group-text">
                            <a href="#">
                                <img src="/static/img/search.png">
                            </a>
                        </span>
                    </div>
                </div>
            </div>
            <div class="header-user-panel">
                <span class="header-user-name"><strong>{{ userName }}</strong></span>
                <img src="/static/img/person.png" width="auto" height="30px">
                <ul>
                    <li v-on:click="logout">Выход</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-header',
    data() {
        return {
            userName: sessionStorage.getItem('userName')
        }
    },
    methods: {
        logout() {
            sessionStorage.removeItem('sessionId');
            this.$router.push({name: 'Login'});
        }
    }
}
</script>

<style scoped>
    .header-container {
        padding: 0 20px;
        height: 60px;
        background-color: #2F80ED;
        color: #ffffff;
    }
    .header-logo {
        display: inline-block;
        float: left;
    }
    .header-user-panel {
        float: right;
    }

    .header-user-panel img{
        margin: 12px 0;
    }
    .header-user-panel ul {
        display: none;
        list-style: none;
    }
    .header-user-panel ul li {
        cursor: pointer;
    }
    .header-user-panel:hover ul {
        display: block;
        margin: 0;
    }
    .header-user-name {
        padding-right: 15px;
    }
    .search {
        display: inline-block;
        margin: 10px;
    }
    .search input {
        background-color: #e9ecef;
    }
</style>