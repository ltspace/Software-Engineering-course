<template>
  <!-- <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet"> -->
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
            <h2 class="card-title" style="margin-bottom: 20px;">Adopt me</h2>
            <form>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-2 col-form-label">ID</label>
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
                <button type="button" class="btn btn-dark control col-sm-3" @click="apply">申请领养</button>
                <div class="col-sm-3">
                  <input type="text" class="form-control" id="inputEmail3" disabled>
                </div>
                <router-link type="button" class="btn btn-dark control col-sm-3" :to="{ name: 'anishow' }">返回
                </router-link>
                <div class="col-sm-4">
                  <input type="text" class="form-control" id="inputEmail3" disabled>
                </div>
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
import router from '@/router/index';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';


export default {
  name: 'AdoptionInfo',
  components: {
    UNavBar
  },
  setup () {
    const store = useStore();
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
    const route = useRoute();
    const aniid = route.params.aniid;
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
    const apply = () => {
      if (store.state.user.crepoint == 0) {
        router.push({
          name: "personalinfo",
        })
      }
      // else{

      // }
    };
    
    return {
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
      apply,
    }
  }
}

</script>

<style scoped>
.a.router-link-exact-active {
  color: black;
}

.carousel {

  width: 100rem;
  text-align: center;
  border-radius: 20%;

  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
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
  border-width: 0;
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
  margin-bottom: px;
}
</style>





