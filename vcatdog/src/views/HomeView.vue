<template>
  <UNavBar />
  <div class="container-fluid">
    <!-- <div class="card ">
      <div class="card-body"> -->
        <div class="row">
          <div class="col-8">
            <HomeCar />
          </div>
          <div class="col-4">
            <HomeWrite />
          </div>
        <!-- </div>
      </div> -->
    </div>
  </div>

</template>

<script>
import UNavBar from '../components/UNavBar';
import HomeCar from '../components/HomeCar';
import HomeWrite from '../components/HomeWrite';
export default {
  name: 'HomeView',
  components: {
    UNavBar,
    HomeCar,
    HomeWrite,
  }
}
</script>

<style scoped>
.a.router-link-exact-active {
  color: black;
}

</style>