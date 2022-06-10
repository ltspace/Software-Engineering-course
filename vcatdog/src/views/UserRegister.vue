<template>
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form @submit.prevent="register">
          <fieldset>
            <div class="head container col-md-11">
              <h4>
                <img src="../assets/logo.png" alt="" width="60" />&nbsp;
                流浪猫狗领养救助平台
              </h4>
              <label class="slogan">Hold
                out our hands, leave a love, and keep a life</label>
            </div>
            <div class="zu1" style="float:center">
              <label class="slogan">注册</label>
            </div>
            <div class="form-group zu2">
              <input v-model="username" type="text" class="form-control" placeholder="用户名,唯一值,注册之后不可修改" />
            </div>
            <div class="form-group zu2">
              <input v-model="password" type="password" class="form-control" placeholder="6-16位密码,区分大小写" />
            </div>
            <div class="form-group zu2">
              <input v-model="password_confirm" type="password" class="form-control password_confirm"
                placeholder="确认密码" />
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;&nbsp;&nbsp;&nbsp;注&nbsp;&nbsp;&nbsp;&nbsp;册&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
          </div>
          <button type="submit" class="btn col-md-6">
            <router-link :to="{ name: 'userlogin' }" style="text-decoration: none ">使用已有账户登陆</router-link>
          </button>
          <!-- <div class="alert alert-warning "> {{ message }}</div> -->
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import $ from 'jquery';

export default {
  name: 'RegisterView',
  setup () {
    const store = useStore();
    let username = ref('');
    let password = ref('');
    let password_confirm = ref('');
    let message = ref('');

    const register = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/register/",
        type: "POST",
        data: {
          username: username.value,
          password: password.value,
          password_confirm: password_confirm.value,
        },
        success (resp) {
          if (resp.result === "success") {
            store.dispatch("login", {
              username: username.value,
              password: password.value,
              success () {
                router.push({ name: 'home' });
              },
              error () {
                message.value = "系统异常，请稍后重试";
              }
            });
          } else {
            message.value = resp.result;
            alert(message.value);
          }
        }
      })
    };


    return {
      username,
      password,
      password_confirm,
      message,
      register,
      alert,
    }
  }
}

</script>


<style scoped>
.alert {
  margin-top: 5em;
}

.center-in-center {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.zu1 {
  padding-top: 7em;
  padding-bottom: 1em;
}

.zu2 {
  padding-bottom: 10px;
}

.zu3 {
  padding-top: 2em;
}

.head {
  transform: scale(1, 1.1);
  text-align: center;
}


.slogan {
  font-size: 1px;
  color: grey;
  transform: scale(1, 1.1);
}

.padd {
  /* padding-top: 5px; */
  /* padding-bottom: 1em; */
  padding-left: 20em;
  font-weight: normal;
}
</style>

