<template>
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
      <div class="carousel-item active">
        <img src="../assets/R-C.jpg" class="d-block w-100" style="border-radius: 5%" alt="...">
        <div class="carousel-caption d-none d-md-block">

          <h1>最后出现地点：汤臣一品东侧花坛</h1>
          <h3>症状：走路不稳，流清涕</h3>
        </div>
      </div>
      <div class="carousel-item">
        <img src="../assets/R-C.jpg" class="d-block w-100" style="border-radius: 5%" alt="...">
        <div class="carousel-caption d-none d-md-block">

          <h1>Second slide label</h1>
          <h3>Some representative placeholder content for the second slide.</h3>
        </div>
      </div>
      <div class="carousel-item ">
        <img src="../assets/R-C.jpg" class="d-block w-100" style="border-radius: 5%" alt="...">
        <div class="carousel-caption d-none d-md-block">

          <h1>Third slide label</h1>
          <h3>Some representative placeholder content for the third slide.</h3>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>


</template>

<script>
export default {
  name:'HomeCar',
}
</script>


<style>
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

</style>