webpackJsonp([1],{J0Tl:function(e,t){},NHnr:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=s("7+uW"),a={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]},r=s("VU/8")({name:"App"},a,!1,null,null,null).exports,i=s("/ocq"),o={name:"app-header",data:function(){return{userName:sessionStorage.getItem("userName")}},methods:{logout:function(){sessionStorage.removeItem("sessionId"),this.$router.push({name:"Login"})}}},u={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("div",{staticClass:"header-container"},[e._m(0),e._v(" "),s("div",{staticClass:"header-user-panel"},[s("span",{staticClass:"header-user-name"},[s("strong",[e._v(e._s(e.userName))])]),e._v(" "),s("img",{attrs:{src:"/static/img/person.png",width:"auto",height:"30px"}}),e._v(" "),s("ul",[s("li",{on:{click:e.logout}},[e._v("Выход")])])])])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"header-logo"},[t("img",{attrs:{src:"/static/img/logo.png",width:"52px",height:"auto"}})])}]};var l={data:function(){return{dataStations:{},dataLines:{}}},components:{AppHeader:s("VU/8")(o,u,!1,function(e){s("J0Tl")},"data-v-7a1f06a4",null).exports},methods:{},mounted:function(){sessionStorage.getItem("sessionId")}},c={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",[t("app-header")],1)},staticRenderFns:[]},m=s("VU/8")(l,c,!1,null,null,null).exports,d={data:function(){return{userName:"",userPass:""}},methods:{login:function(){if(""==this.userName||""==this.userPass)alert("Поле логина или пароля не должно быть пустым");else{var e={userName:this.userName,userPass:this.userPass};"admin"==e.userName&&"123456"==e.userPass?this.loginSuccess():alert("Не верный логин или пароль")}},loginSuccess:function(){sessionStorage.setItem("sessionId",!0),sessionStorage.setItem("userName","administrator"),this.$router.push({name:"Main"})},logout:function(){sessionStorage.removeItem("sessionId")}}},p={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("div",{staticClass:"login-form-container col-md-4 col-md-offset-0"},[s("div",{staticClass:"card row",attrs:{id:"login-form"}},[e._m(0),e._v(" "),s("div",{staticClass:"card-body"},[s("div",{staticClass:"form-group"},[s("label",[e._v("Логин:")]),e._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:e.userName,expression:"userName"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:e.userName},on:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.login(t)},input:function(t){t.target.composing||(e.userName=t.target.value)}}})]),e._v(" "),s("div",{staticClass:"form-group"},[s("label",[e._v("Пароль:")]),e._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:e.userPass,expression:"userPass"}],staticClass:"form-control",attrs:{type:"password"},domProps:{value:e.userPass},on:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.login(t)},input:function(t){t.target.composing||(e.userPass=t.target.value)}}})]),e._v(" "),s("div",{staticClass:"form-group"},[s("button",{staticClass:"btn btn-primary",on:{click:e.login}},[e._v("Войти")])])])])])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"card-header"},[t("h5",{staticClass:"card-title"},[this._v("Авторизация")])])}]};var v=s("VU/8")(d,p,!1,function(e){s("q5JU")},"data-v-1d38fbfe",null).exports;n.a.use(i.a);var f=new i.a({mode:"hash",routes:[{path:"/",name:"Main",component:m,meta:{requiresAuth:!0}},{path:"/login",name:"Login",component:v,meta:{guest:!0,requiresAuth:!1}}]});f.beforeEach(function(e,t,s){e.matched.some(function(e){e.meta.requiresAuth&&("null"===sessionStorage.getItem("sessionId")||null===sessionStorage.getItem("sessionId"))?s({path:"/login"}):s()})});var g=f;n.a.config.productionTip=!1,new n.a({el:"#app",router:g,components:{App:r},template:"<App/>"})},q5JU:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.9f502dfaa4140bed6464.js.map