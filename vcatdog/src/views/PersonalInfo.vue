<template>
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
            <div class="mb-3 ">
              <label for="exampleFormControlInput1" class="form-label">用户名:</label>
              <input type="text" class="form-control" id="exampleFormControlInput1"
                :placeholder="$store.state.user.username" disabled
                style="text-align:center; font-weight:border;letter-spacing: 3px;">
            </div>
            <div class="media">
              <label for="exampleFormControlInput1" class="form-label">头像:</label>
              <img :src="$store.state.user.photo" class="mb-3" style="width:50px;height:50px;border-radius: 100%;margin-left: 50px;">
              <div class="media-body">
                <input v-model="photo" type="text" class="form-control" :placeholder="$store.state.user.photo" />
              </div>
            </div>

            <div class="form-group zu2" id="sex" v-if="$store.state.user.sex=='男'" style="margin-top:10px">
              <label for="formFile" class="form-label">性别:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="1" checked>
                <label class="form-check-label" for="inlineRadio1">男</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="2">
                <label class="form-check-label" for="inlineRadio2">女</label>
              </div>
            </div>

            <div class="form-group zu2" id="sex" v-else style="margin-top:10px">
              <label for="formFile" class="form-label">性别:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="1" >
                <label class="form-check-label" for="inlineRadio1">男</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="2" checked>
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
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-5" style="margin-right:25px;">
              更新基本信息
            </button>
          </div>
        </form>
        <router-link class="btn btn-primary col-md-5" :to="{ name: 'home' }" role="button" style="margin-left:25px;">返回主页面</router-link>
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
    let photo = ref('');
    var selectedSex = $('#sex input:radio:checked').val();
    let sex = "男";
    if (selectedSex==1)
    {
      sex = "男";
    }
    else 
    {
      sex = "女";
    }

    const userinfoselfchge = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/userinfoselfchge/",
        type: "POST",
        data: {
          // id: id,
          username: username,
          sex: sex,
          phonum: phonum.value,
          email: email.value,
          addr: addr.value,
          job: job.value,
          photo: photo.value,
        },
        success (resp) {
          if (resp.result == "1") {
            
            if(phonum.value!=null&&email.value!=null&&addr.value!=null&&job.value!=null)
            {
              store.state.user.crepoint=1;
              message.value = "更新成功!您的信用积分为1!";
              store.state.user.phonum=phonum.value;
              store.state.user.sex=sex.value;
              store.state.user.photo=photo.value;
              store.state.user.job=job.value;
              store.state.user.email=email.value;
              store.state.user.addr=addr.value;
            }
            else{
              store.state.user.crepoint=0;
              message.value = "更新成功!存在部分必要个人领养信息未填,您的信用积分为0!";
            }
          } else {
            message.value = resp.result;
          }
        }
      })
    };

    return {
      // id,
      sex,
      username,
      phonum,
      email,
      addr,
      job,
      message,
      photo,
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