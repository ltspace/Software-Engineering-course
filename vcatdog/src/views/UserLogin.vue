<template>

  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form @submit.prevent="login">
          <fieldset>
            <div class="head container col-md-11">
              <h4>
                <img src="../assets/logo.png" alt="" width="60" />&nbsp;
                流浪猫狗领养救助平台
              </h4>
              <label class="slogan">Hold out our hands, leave a love, and keep a life</label>
            </div>
            <div class="zu1">
              <button type="submit" class="btn col-md-6">
                <router-link :to="{ name: 'userlogin' }" style="text-decoration: none;color:black">用户登录</router-link>
              </button>
              <button type="submit" class="btn col-md-6">
                <router-link :to="{ name: 'adminlogin' }" style="text-decoration: none ">管理员登陆</router-link>
              </button>
            </div>
            <div class="form-group zu2">
              <input v-model="username" type="text" class="form-control ID" placeholder="ID" />
            </div>
            <div class="form-group zu2">
              <input v-model="password" type="password" class="form-control pwd" placeholder="Password" />
            </div>
          </fieldset>
          <label for="" class="padd zu2"><a href="" style="text-decoration: none">忘记密码</a></label>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;&nbsp;&nbsp;&nbsp;登&nbsp;&nbsp;&nbsp;&nbsp;录&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
          </div>
          <label for="" class="zu3 padd zu2">
            <router-link :to="{ name: 'registerview' }" style="text-decoration: none">注册新用户</router-link>
          </label>
        </form>
        <div class="alert alert-warning"> {{ message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';



export default {
  name: 'UserLoginView',
  setup () {
    const store = useStore();
    // let id = ref('');
    let password = ref('');
    let username = ref('');
    let message = ref('');

    const login = () => {
      message.value = "";
      store.dispatch("login", {
        username: username.value,
        password: password.value,
        success () {
          router.push({ name: 'home' })
        },
        error () {
          message.value = '用户名或密码错误'
        }
      })
    }

    return {
      username,
      password,
      message,
      login
    }
  }

}
</script>

<style scoped>
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
  padding-bottom: 3.5em;
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
  padding-left: 20em;
  font-weight: normal;
}
</style>
