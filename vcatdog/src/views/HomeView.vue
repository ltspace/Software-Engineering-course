<template>
  <UNavBar />
  <div class="container-fluid">
    <div class="row">
      <div class="col-8">
        <div id="carouselExampleCaptions" class="carousel slide center-in-center" data-bs-ride="false">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
              aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
              aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
              aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <h3>待救助动物</h3>
            <div class="carousel-item active" v-for="wait0 in waits" :key="wait0.id">
              <img :src="wait0.img" class="d-block w-100" style="border-radius: 5%" alt="...">
              <div class="carousel-caption d-none d-md-block">
                <h1>最后出现地点：{{ wait0.addr }}</h1>
                <h3>症状：{{ wait0.sym }}</h3>
              </div>
            </div>
            <div class="carousel-item" v-for="wait1 in waitss" :key="wait1.id">
              <img :src="wait1.img" class="d-block w-100" style="border-radius: 5%" alt="...">
              <div class="carousel-caption d-none d-md-block">
                <h1>最后出现地点：{{ wait1.addr }}</h1>
                <h3>症状：{{ wait1.sym }}</h3>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>

      </div>
      <div class="col-4">
        <div class="card edit-field">
          <div class="card-body">
            <label for="edit-post" class="form-label">
              <h3>发表待救助动物</h3>
            </label>
            <form @submit.prevent="fill">
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">照片URL</label>
                <div class="col-sm-10">
                  <input type="text" v-model="pho" class="form-control">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">出现地点</label>
                <div class="col-sm-10">
                  <input type="text" v-model="loc" class="form-control">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">症状</label>
                <div class="col-sm-10">
                  <input type="text" v-model="ill" class="form-control">
                </div>
              </div>
              <button type="submit" class="btn btn-primary" style="letter-spacing: 5px">发帖</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { ref } from 'vue';
import $ from 'jquery';
import UNavBar from '../components/UNavBar';
export default {
  name: 'HomeView',
  components: {
    UNavBar,
  },
  setup () {
    let loc = ref();
    let pho = ref();
    let ill = ref();
    let waits = ref([]);
    let waitss = ref([]);
    let message = ref();
    $.ajax({
      url: 'http://127.0.0.1:8000/homeview/',
      type: "get",
      success (resp) {
        waits.value = resp;
        // waitss.value =resp.anii;
        // alert(message.value);
      }
    });
    $.ajax({
      url: 'http://127.0.0.1:8000/homeview1/',
      type: "get",
      success (resp) {
        // waits.value = resp.ani;
        waitss.value = resp;
        // alert(message.value);
      }
    });
    const fill = () => {
      $.ajax({
        url: "http://127.0.0.1:8000/rhomeview/",
        type: "POST",
        data: {
          loc: loc.value,
          ill: ill.value,
          pho: pho.value,
        },
        success (resp) {
          message.value = resp.result;
          alert(message.value);
          window.location.reload();
        }
      })
    }
    return {
      loc,
      pho,
      ill,
      waits,
      waitss,
      fill
    }
  },
}
</script>

<style scoped>
.a.router-link-exact-active {
  color: black;
}

.carousel {
  font-family: YouYuan, Avenir, Helvetica, Arial, sans-serif;
  /* width: 75rem; */
  text-align: center;
  border-radius: 10%;
  /* transform: scale(1, 1.1); */
  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
}

.card-body {
  margin-top: 0;
  padding-top: 0;
}

.card {
  border: 0ch;
  background: transparent;
  margin-top: 10em;
}

.card {
  font-family: YouYuan, Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  transform-origin: 0 0;
  font-weight: bolder;
}

.btn-primary {
  background-color: black;
}
</style>