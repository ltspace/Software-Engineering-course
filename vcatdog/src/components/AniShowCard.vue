<template>
  <UNavBar>
  </UNavBar>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form action="" role="form">
          <fieldset>
            <div class="head container col-md-11">
              <h2>照片墙</h2>
              <label class="slogan">这是已经被领养过的猫狗们</label>
            </div>
            <div class="zu1 justify-content-center">

              <h5 class="stretch">
                <ul class="nav justify-content-center">
                  <div class="container ">
                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4" style="width: 750px;">
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">1</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">2</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">3</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">4</p>
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
                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4" style="width: 750px;">
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">5</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">6</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">7</p>
                        </div>
                      </div>
                      <div class="card" style="width: 18rem;">
                        <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                          <p class="card-text">8</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </ul>
              </h5>
            </div>
            <div class="form-group zu2">

            </div>
          </fieldset>

          <div class="mx-auto ">
            <ul class="pagination">
              <li class="page-item"><a class="page-link" href="#">1</a></li>
              <li class="page-item"><a class="page-link" href="#">2</a></li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>

          </div>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AniShowCard',
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
  padding-top: 7em;
  padding-bottom: 3.5em;
}

.zu2 {
  padding-bottom: 10px;
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
