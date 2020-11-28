<template>
    <div>
        <div class='login-form-container col-md-4 col-md-offset-0'>
            <div id='login-form' class="card row">
                <div class="card-header">
                    <h5 class="card-title">Авторизация</h5>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label>Логин:</label>
                        <input v-model="userName" @keyup.enter="login" type="text" class="form-control" >
                    </div>
                    <div class="form-group">
                        <label>Пароль:</label>
                        <input v-model="userPass" @keyup.enter="login" type="password" class="form-control" >
                    </div>
                    <div class="form-group">
                        <button v-on:click="login" class="btn btn-primary">Войти</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userName: '',
            userPass: ''
        }
    },
    methods: {
        login() {
            if (this.userName == '' || this.userPass == '') {
                alert('Поле логина или пароля не должно быть пустым')
            } else {
                let data = {
                    userName: this.userName,
                    userPass: this.userPass
                };
                axios.post('/login', data)
                .then(Response => (
                    this.loginSuccess(Response.data) 
                ))
                .catch(error => (
                    alert('Не верный логин или пароль')
                ));
            }
        },   
        loginSuccess(data) {
            sessionStorage.setItem('sessionId', data.SESSION);
            sessionStorage.setItem('userName', data.IM + ' ' + data.OT + ' ' + data.FAM);
            sessionStorage.setItem('position', data.ROLE);
            this.$router.push({name: 'Main'});
        },
        logout() {
            sessionStorage.removeItem('sessionId');
        }
    }
};
</script>

<style scoped>
    .login-form-container{
        margin: 10% auto;
    }
</style>