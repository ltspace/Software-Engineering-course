<template>
  <UNavBar />
  <div class="container center-in-center">
    <div class="card">
      <div class="row g-0">
        <div class="col-md-6">
          <div class="container-fluid">
            <img :src="photo" class="img-fluid" style="border-radius: 72px;margin-top: 5em;width: 100%;">
          </div>
        </div>
        <div class="col-md-6">
          <div class="card-body item">
            <h2 class="card-title"
              style="margin-bottom: 20px;font-family: Youyuan;font-weight: bolder;letter-spacing: 5px;">领养单</h2>
            <form>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">动物ID</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="aniid" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">名字</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="name" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">类型</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="cd" disabled>
                </div>

                <label for="inputEmail3" class="col-sm-2 col-form-label">年龄</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="age" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">地址</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="addr" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">品种</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="type" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">毛色</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="fur" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">性别</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="sex" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">性格</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="chara" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">疾病情况</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="ill" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">绝育情况</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="jveyu" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">疫苗情况</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="vacc" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">领养编号</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="adoptid" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">领养日期</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="day" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">领养用户</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="username" disabled>
                </div>
                <label for="inputEmail3" class="col-sm-2 col-form-label">领养状态</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" :value="status" disabled>
                </div>
              </div>
              <!-- <div class="form-group row" v-if="!state"> -->
              <!-- <button type="button" class="btn btn-dark control col-sm-3" @click="adosuccess" disabled>领养成功</button>
                <div class="col-sm-1">
                </div>
                <button type="button" class="btn btn-dark control col-sm-3" @click="assist" disabled>查看救助信息</button>
                <div class="col-sm-1">
                </div>
                <button type="button" class="btn btn-dark control col-sm-3" @click="adofail" disabled>领养失败</button>
                <div class="col-sm-1">
                </div> -->
              <!-- </div>-->
              <div class="form-group row">
              <button type="button" class="btn btn-dark control col-sm-3" @click="adosuccess">领养成功</button>
              <div class="col-sm-1">
              </div>

              <button type="button" class="btn btn-dark control col-sm-3" @click="assist">查看救助信息</button>
              <div class="col-sm-1">
              </div>
              <button type="button" class="btn btn-dark control col-sm-3" @click="adofail">领养失败</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UNavBar from '../components/UNavBar';
import { ref } from 'vue';
// import router from '@/router/index';
import { useRoute } from 'vue-router';
// import { useStore } from 'vuex';
import $ from 'jquery';


export default {
  name: 'AdoptionForm',
  components: {
    UNavBar
  },
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
    let phonum = ref();
    let status = ref();
    let username = ref();
    let day = ref();
    const route = useRoute();
    const aniid = route.params.aniid;
    const adoptid = route.params.adoptid;
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
      },
    });
    $.ajax({
      url: "http://127.0.0.1:8000/adoone/",
      type: "GET",
      data: {
        adoptid: adoptid,
      },
      success (resp) {
        status.value = resp.status;
        day.value = resp.day;
        username.value = resp.username;
        if (status.value === "正在领养") {
          alert("您要领养的动物正在救助者所在地址生活!\n请点击下方查看救助信息按钮查询救助者信息，以进行领养对接");
        }
      },
    });
    function assist () {
      if (status.value != "正在领养") {
        alert("领养完毕！您无法再查看救助者信息！");
      }
      else {
        $.ajax({
          url: "http://127.0.0.1:8000/assone/",
          type: "GET",
          data: {
            aniid: aniid,
          },
          success (resp) {
            // console.log(resp);
            phonum.value = resp.phonum;
            alert("救助者的手机号是：" + phonum.value + "，请尽快与他联系，商讨领养事宜！\n领养成功或失败请点击下方对应按钮！")
          },
        });
      }
    }
    function adosuccess () {
      if (status.value != "正在领养") {
        alert("领养完毕！您无法再次修改！");
      }
      else {
        var photo = prompt("您想将自己与已领养的动物合照展示在网站的照片墙吗?若想,请输入照片url:", "");
        $.ajax({
          url: "http://127.0.0.1:8000/adosucc/",
          type: "POST",
          data: {
            photo: photo,
            adoptid: adoptid,
            aniid: aniid,
          },
          success () {
            alert("恭喜您领养成功！");
            window.location.reload();
          },
        });
      }
    }
    function adofail () {
      if (status.value != "正在领养") {
        alert("领养完毕！您无法再次修改！");
      }
      else {
        $.ajax({
          url: "http://127.0.0.1:8000/adofail/",
          type: "POST",
          data: {
            adoptid: adoptid,
            aniid: aniid,
          },
          success () {
            alert("可以去看看其它可领养的动物！");
            window.location.reload();
          },
        });
      }
    }
    return {
      username,
      adoptid,
      status,
      day,
      aniid,
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
      jveyu,
      alert,
      assist,
      adofail,
      adosuccess,
    }
  },

}

</script>

<style scoped>
.a.router-link-exact-active {
  color: black;
}


.card {
  background: linear-gradient(180deg, rgba(251, 200, 212, 1) 0%, rgba(151, 149, 240, 1) 100%);
  box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.33);
  border-radius: 72px;
  border: 0ch;

}

.col-form-label {
  font-size: large;
}

.item {
  margin-top: 5%;
}

.form-control {
  background: transparent;
  font-size: large;
  border-width: 0px;
}


.center-in-center {
  position: absolute;
  top: 55%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.control {
  border-radius: 10px;
  letter-spacing: 5px;
  text-align: center;
}

.control:hover {
  box-shadow: 2px 2px 10px grey;
  transition: 500ms;
}


.form-group {
  margin-top: 20px;
  margin-bottom: 30px;
}
</style>





