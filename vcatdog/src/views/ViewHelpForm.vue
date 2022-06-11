<template>
  <div style=" height:100%; overflow:auto;">
    <UNavBar />
    <div class="container">
      <h3 style="font-family:Youyuan;text-align: center;">救助单列表</h3>
      <div class="card" style="cursor:pointer" v-for="assist in assists" :key="assist.num"
        @click="open_user_profile(assist.num, assist.id)">
        <div class="card-body">
          <div class="row">
            <div class="col-1 img-field">
              <img class="img-fluid" :src="assist.photo" alt="">
            </div>
            <div class="col-11">
              <div class="username">救助单编号：{{ assist.num }}</div>
              <div class="username">救助日期：{{ assist.day }}</div>
              <!-- <div class="username">救助状态：{{ assist.state }}</div> -->
              <!-- <div class="follower-count">{{ user.followerCount }}</div> -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="row row-cols-1 row-cols-md-3 g-4 ">
      <div class="col" v-for="assist in assists" :key="assist.id" @click="open_user_profile(assist.id)">
        <div class="card" style="cursor:pointer" id="1">
          <img :src="assist.photo" class="card-img-top">
          <button class="btn btn-primary how">救助我</button>
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
  name: 'ViewHelpForm',
  components: {
    UNavBar
  },
  setup () {
    const store = useStore();
    let assists = ref([]);
    const username = store.state.user.username;
    $.ajax({
      url: 'http://127.0.0.1:8000/assistlist/',
      type: "get",
      data: {
        username: username,
      },
      success (resp) {
        assists.value = resp;
        // console.log(resp);
      }
    });

    const open_user_profile = (assistid, aniid) => {
      router.push({
        name: "assistani",
        params: {
          assistid,
          aniid
        }
      })
    };
    return {
      assists,
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
  background: linear-gradient(90deg, rgba(227, 253, 245, 1) 0%, rgba(255, 230, 250, 1) 100%);
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
