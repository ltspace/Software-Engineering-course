<template>
  <AdNavBar>
  </AdNavBar>
  <div class="head container col-md-11">
              <h2>动物信息查看</h2>
            </div>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="zu1 justify-content-center">
              <h5 class="stretch">
                <ul class="nav justify-content-center">
                  <div class="container ">
                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4" style="width: 1000px;">
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：001</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：002</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：003</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：004</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                        </div>
                        </div>
                        </div>
                        </ul>
                        </h5>
                        </div>



                         <div class="form-group zu2">
              <h5 class="stretch">
                <ul class="nav justify-content-center">
                  <div class="container">
                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4" style="width: 1000px;">
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：005</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：006</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：007</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                      <div class="card" style="width: 20rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">动物ID：008</p>
                          <router-link :to="{name:''}" style="text-decoration: none ">查看</router-link>
                        </div>
                      </div>
                    </div>
                  </div>
                </ul>
              </h5>
            </div>
            <div class="mx-auto" style="width: 200px; ">
            <ul class="pagination">
              <li class="page-item"><a class="page-link" href="#">1</a></li>
              <li class="page-item"><a class="page-link" href="#">2</a></li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>

          </div>
</template>

<script>
import AdNavBar from '../components/AdNavBar';
export default {
  name: 'AnimalCheck',
  components: {
    AdNavBar
  }
}
</script>
<style scoped>
.stretch {
  transform: scale(1, 1.1);
  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
  color: black;
}


.zu1 {
  padding-top: 5em;
  padding-left:350px;
  padding-bottom: 0em;
}

.zu2 {
  padding-bottom: 10px;
  padding-left:350px;
}

.head {
  transform: scale(1, 1.1);
  text-align: center;
}

.card {
  background-color: transparent;
  padding-top: 5em;
}
</style>
