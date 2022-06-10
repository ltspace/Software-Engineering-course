<template>
  <AdNavBar />
      <div class="set">
  <div class="card text-center">
    <div class="card-body">
      <h2 class="card-title" style="float:center">管理员信息查看</h2>

      <pre class="content">
      <h4 class="stretch">
<strong >工号：</strong>001

<strong>性别：</strong>女

<strong>电话：</strong>15848530635

<strong>投诉邮箱：</strong>2417769953@qq.com

<strong>工龄：</strong>1年

<strong>年龄：</strong>20岁

<strong>在线时间：</strong>8：00-21:00</h4>
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
