<template>
  <div style=" height:100%; overflow:auto">
  <UNavBar />
  <div class="container">
    <h3 style="font-family:Youyuan;text-align: center;">这是我们网站的领养者与他们领养的动物</h3>
    <div class="row row-cols-1 row-cols-md-3 g-4 ">
      <div class="col" v-for="animal in animals" :key="animal.id">
        <div class="card" style="cursor:pointer" id="1">
          <img :src="animal.photo" class="card-img-top">
          <!-- <div class="cardbody" v-for="animal in animals" :key="animal.id">{{ animal.name }}</div> -->
          <!-- <button class="btn btn-primary how">领养我</button> -->
        </div>
      </div>
    </div>
  </div>

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
// import router from '@/router/index';
// import { useStore } from 'vuex';
import UNavBar from '../components/UNavBar.vue'
export default {
  name: 'AnimalShow',
  components: {
    UNavBar
  },
  setup () {
    // const store = useStore();
    let animals = ref([]);

    $.ajax({
      url: 'http://127.0.0.1:8000/photolist/',
      type: "get",
      success (resp) {
        animals.value = resp;
      }
    });

    return {
      animals,
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

.card:hover{
  box-shadow: 2px 2px 10px grey;
  transition:500ms;
}
</style>
