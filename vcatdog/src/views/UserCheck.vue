<template>
  <AdNavBar />
  
      <div class="set">
  <div class="card text-center">
    <div class="card-body">
      <img src="../assets/logo.png" class="rounded float-end" alt="...">
<label class="rounded float-end">头像</label>

      <h2 class="card-title" style="float:center">用户信息查看</h2>
      <pre class="content">
      <h5 class="stretch">
<strong >用户ID：</strong>001

<strong>用户名：</strong>Monica Simons

<strong>性别：</strong>女

<strong>电话：</strong>15848530635

<strong>邮箱：</strong>2417769953@qq.com

<strong>地址：</strong>山东大学（威海）

<strong>职业：</strong>驯兽师

<strong>信用积分：</strong>100

<strong>已领养动物：</strong>10只

<strong>已救助动物：</strong>1只</h5>
 </pre>
 

      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>
  </div>
</div>

</template>

<script>
import AdNavBar from '../components/AdNavBar';
export default {
  name: 'AdminCheck',
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

.card {
  background-color: transparent;
  padding-top: 5em;
}

</style>
