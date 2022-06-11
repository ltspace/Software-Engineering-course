<template>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <label class="slogan">查看救助单</label>
      <div class="col-md-4 center-in-center">
        <form>
          <fieldset>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">
                动物名：
              </label>
              <input type="name" class="form-control" id="exampleFormControlInput1" disabled :value="name">
            </div>
            <label for="formFile" class="form-label">照片:</label>
            <input type="text" class="form-control" disabled :value="photo" />
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">类别：</label>
              <input type="text" class="form-control" disabled :value="cd" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">品种：</label>
              <input type="text" class="form-control" disabled :value="type" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">毛色：</label>
              <input type="text" class="form-control" disabled :value="fur" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">年龄：</label>
              <input type="text" class="form-control" disabled :value="age" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">性格：</label>
              <input type="text" class="form-control" disabled :value="chara" />
            </div>

            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">性别：</label>
              <input type="text" class="form-control" disabled :value="sex" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疫苗情况：</label>
              <input type="text" class="form-control" disabled :value="vacc" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疾病情况：</label>
              <input type="text" class="form-control" disabled :value="ill" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">地址：</label>
              <input type="text" class="form-control" disabled :value="addr" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">可否被领养：</label>
              <input type="text" class="form-control" disabled :value="can_adopt" />
            </div>
            <router-link class="btn btn-primary col-md-12" :to="{ name: 'home' }" role="button">
          返回主页面</router-link>
          </fieldset>
        </form>
        
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
// import { useStore } from 'vuex';
// import router from '@/router/index';
import { useRoute } from 'vue-router';
import $ from 'jquery';

export default {
  name: 'AssistAni',
  setup () {
    let name = ref();
    let photo = ref();
    let fur = ref();
    let age = ref();
    let chara = ref();
    let type = ref();
    let vacc = ref();
    let ill = ref();
    let addr = ref();
    let sex = ref();
    let cd = ref();
    let jveyu = ref();
    let can_adopt = ref();
    // let status = ref();
    // let username = ref();
    let day = ref();
    const route = useRoute();
    const aniid = route.params.aniid;
    const assistid = route.params.assistid;
    $.ajax({
      url: "http://127.0.0.1:8000/anione/",
      type: "GET",
      data: {
        aniid: aniid,
      },
      success (resp) {
        name.value = resp.name;
        photo.value = resp.photo;
        fur.value = resp.fur;
        age.value = resp.age;
        chara.value = resp.chara;
        type.value = resp.type;
        vacc.value = resp.vacc;
        ill.value = resp.ill;
        addr.value = resp.addr;
        sex.value = resp.sex;
        cd.value = resp.cd;
        jveyu.value = resp.jveyu;
        if (resp.can_adopt == 0) {
          can_adopt.value = "不可被领养";
        }
        else if (resp.can_adopt == 1) {
          can_adopt.value = "可被领养";
        }
        else if (resp.can_adopt == 2) {
          can_adopt.value = "正在被领养";
        }
        else if (resp.can_adopt == 3) {
          can_adopt.value = "已被领养";
        }
      },
    });
    $.ajax({
      url: "http://127.0.0.1:8000/assistone/",
      type: "GET",
      data: {
        assistid: assistid,
      },
      success (resp) {
        day.value = resp.day;
      },
    });
    return {
      // username,
      name,
      photo,
      fur,
      age,
      chara,
      type,
      vacc,
      ill,
      addr,
      sex,
      cd,
      day,
      jveyu,
      // message,
      can_adopt,
      // fillhelp,
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

.head {
  transform: scale(1, 1.1);
  text-align: center;
}


.slogan {
  font-size: 2em;
  font-family: Youyuan;
  color: rgba(0, 0, 0, 0.619);
  transform: scale(1, 1.1);
  letter-spacing: 3px;
}

.padd {
  /* padding-top: 5px; */
  /* padding-bottom: 1em; */
  padding-left: 20em;
  font-weight: normal;
}
</style>
