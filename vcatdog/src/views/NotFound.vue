<template>
  <UNavBar/>
<h1 class="center-in-center" style="font-family:Youyuan;">您访问的页面不存在！</h1>

</template>

<script>
import UNavBar from '../components/UNavBar';
export default {
  name: 'NotFound',
  components: {
    UNavBar
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
</style>
