<template>
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form @submit.prevent="changepwd">
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
              <label class="slogan">修改密码</label>
            </div>
            <div class="form-group zu2">
              <input v-model="password" type="password" class="form-control" placeholder="原密码" />
            </div>
            <div class="form-group zu2">
              <input v-model="new_password" type="password" class="form-control" placeholder="新密码" />
            </div>
            <div class="form-group zu2">
              <input v-model="password_confirm" type="password" class="form-control password_confirm"
                placeholder="确认新密码" />
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-6">
              修改
            </button>
            <router-link  class="btn btn-primary col-md-6" :to="{ name: 'home' }" >
              返回
            </router-link>
          </div>
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
    let password = ref('');
    let new_password = ref('');
    let password_confirm = ref('');
    let message = ref('');
    let username = store.state.user.username;

    const changepwd = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/changepwdapi/",
        type: "POST",
        data: {
          username: username,
          password: password.value,
          new_password: new_password.value,
          password_confirm: password_confirm.value,
        },
        success (resp) {
          if (resp.result === "success") {
            alert("修改密码成功！");
            store.state.user.password=new_password.value;
            store.dispatch("login", {
              username: username,
              password: new_password.value,
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
      new_password,
      password_confirm,
      message,
      changepwd,
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

