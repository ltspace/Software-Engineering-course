<template>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form @submit.prevent="userinfoselfchge">
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
              <label class="" slogan>个人信息</label>
            </div>
            <!-- <div class="mb-3 row">
              <label for="staticEmail" class="col-sm-4 col-form-label">用户ID:</label>
              <div class="col-sm-5">
                {{ $store.state.user_id }}
              </div>
            </div> -->

            <div class="mb-3 ">
              <label for="exampleFormControlInput1" class="form-label">用户名:</label>
              <input type="text" class="form-control" id="exampleFormControlInput1"
                :placeholder="$store.state.user.username" disabled
                style="text-align:center; font-weight:border;letter-spacing: 3px;">
              <!-- <h3 style="text-align:center; font-weight:border;letter-spacing: 3px;">{{ $store.state.user.username }}</h3> -->
            </div>


            <div class="mb-3">
              <label for="formFile" class="form-label">头像</label>
              <input class="form-control" type="file" id="formFile">
            </div>

            <div class="form-group zu2">
              <label for="formFile" class="form-label">性别:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="option1">
                <label class="form-check-label" for="inlineRadio1">男</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="option2">
                <label class="form-check-label" for="inlineRadio2">女</label>
              </div>
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">电话：</label>
              <input v-model="phonum" type="text" class="form-control" :placeholder="$store.state.user.phonum" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">邮箱：</label>
              <input v-model="email" type="text" class="form-control" :placeholder="$store.state.user.email" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">地址：</label>
              <input v-model="addr" type="text" class="form-control" :placeholder="$store.state.user.addr" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">职业：</label>
              <input v-model="job" type="text" class="form-control" :placeholder="$store.state.user.job" />
            </div>
            <div class="mb-3 row">
              <label for="staticEmail" class="col-sm-4 col-form-label">信用积分：</label>
              <div class="col-sm-5">
                <input type="text" class="form-control" id="exampleFormControlInput1"
                  :placeholder="$store.state.user.crepoint" disabled
                  style="text-align:center; font-weight:border;letter-spacing: 3px;">
              </div>
              <!-- <label for="staticEmail" class="col-sm-4 col-form-label">已领养动物：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="10只">
              </div>
              <label for="staticEmail" class="col-sm-4 col-form-label">已救助动物：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="1只">
              </div> -->
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-5" style="margin-right:25px;">
              更新基本信息
            </button>
          </div>
        </form>
        <button type="submit" class="btn btn-primary col-md-5" style="margin-left:25px;">
          返回主页面
        </button>
      </div>
    </div>
    
  </div>
  <div class="alert alert-warning"> {{ message }}</div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
// import router from '@/router/index';
import $ from 'jquery';

export default {
  name: 'PersonalInfo',
  setup () {
    const store = useStore();
    // let id = store.state.user_id;
    let username = store.state.user.username;
    let phonum = ref('');
    let email = ref('');
    let addr = ref('');
    let job = ref('');
    let message = ref('');

    const userinfoselfchge = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/userinfoselfchge/",
        type: "POST",
        data: {
          // id: id,
          username: username,
          phonum: phonum.value,
          email: email.value,
          addr: addr.value,
          job: job.value,
        },
        success (resp) {
          if (resp.result === "1") {
            message.value = "更新成功！";

          } else {
            message.value = "更新失败！请检查您的个人信息！";
          }
        }
      })
    };

    return {
      // id,
      username,
      phonum,
      email,
      addr,
      job,
      message,
      userinfoselfchge,
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
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}

.zu2 {
  padding-bottom: 1px;
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