<template>
  <div style=" height:100%; overflow:auto;">
    <UNavBar />
    <div class="container">
      <h3 style="font-family:Youyuan;text-align: center;">领养单列表</h3>
      <div class="card" style="cursor:pointer" v-for="adopt in adopts" :key="adopt.num"
        @click="open_user_profile(adopt.num, adopt.id)">
        <div class="card-body">
          <div class="row">
            <div class="col-1 img-field">
              <img class="img-fluid" :src="adopt.photo" alt="">
            </div>
            <div class="col-11">
              <div class="username">领养单编号：{{ adopt.num }}</div>
              <div class="username">领养日期：{{ adopt.day }}</div>
              <div class="username">领养状态：{{ adopt.state }}</div>
              <!-- <div class="follower-count">{{ user.followerCount }}</div> -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="row row-cols-1 row-cols-md-3 g-4 ">
      <div class="col" v-for="adopt in adopts" :key="adopt.id" @click="open_user_profile(adopt.id)">
        <div class="card" style="cursor:pointer" id="1">
          <img :src="adopt.photo" class="card-img-top">
          <button class="btn btn-primary how">领养我</button>
        </div>
      </div>
    </div> -->

    <!-- <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center ">
        <li class="page-item disabled">
          <a class="page-link">&laquo;</a>
        </li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item">
          <a class="page-link" href="#">&raquo;</a>
        </li>
      </ul>
    </nav> -->
  </div>
</template>


<script>
import $ from 'jquery';
import { ref } from 'vue';
import router from '@/router/index';
import { useStore } from 'vuex';
import UNavBar from '../components/UNavBar.vue'
export default {
  name: 'AdoptFormView',
  components: {
    UNavBar
  },
  setup () {
    const store = useStore();
    let adopts = ref([]);
    const username = store.state.user.username;
    $.ajax({
      url: 'http://127.0.0.1:8000/selectadopt/',
      type: "get",
      data: {
        username: username,
      },
      success (resp) {
        adopts.value = resp;
        // console.log(resp);
      }
    });

    const open_user_profile = (adoptid, aniid) => {
      router.push({
        name: "adoptionform",
        params: {
          adoptid,
          aniid
        }
      })
    };
    return {
      adopts,
      open_user_profile
    };
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

.how {
  background: linear-gradient(90deg, rgba(255, 236, 210, 1) 0%, rgba(252, 182, 159, 1) 100%);
  border-radius: 5%;
  border-color: transparent;
  color: black;
}

.card {
  background: linear-gradient(90deg, rgba(238, 156, 167, 1) 0%, rgba(255, 221, 225, 1) 100%);
  margin-bottom: 20px;
  font-weight: bolder;
  font-family:Youyuan;
}

.card:hover {
  box-shadow: 2px 2px 10px grey;
  transition: 500ms;
}

.img-field {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

</style>
