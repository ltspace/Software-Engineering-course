<template> 

 
  <AdNavBar />
  
      <div class="set">
  <div class="card text-center">
    <div class="card-body ">
      <h2 class="card-title" style="float:center">用户信息修改</h2>
      
<strong >用户ID：</strong>001

<br>
<br>
<strong >用户名：</strong>
<input type="text" value="Monica Simons" placeholder="用户名"  name="name">
<br>
<br>
<strong >性别：</strong>
<input type="text" value="女" placeholder="性别"  name="sex">
<br>
<br>
<strong>电话：</strong>
<input type="text" value="15848530635" placeholder="电话"  name="phone">
<br>
<br>
<strong>邮箱：</strong>
<input type="text" value="2417769953@qq.com" placeholder="邮箱"  name="email">
<br>
<br>
<strong>地址：</strong>
<input type="text" value="山东大学（威海）" placeholder="地址"  name="address">
<br>
<br>
<strong>职业：</strong>
<input type="text" value="驯兽师" placeholder="职业"  name="profession">
<br>
<br>
<strong>信用积分：</strong>100
<br>
<br>
<strong>已领养动物：</strong>10只
<br>
<br>
<strong>已救助动物：</strong>1只
<br>
<br>
<button type="button" class="btn-lg">
    <router-link :to="{name:'userCheck'}" style="text-decoration: none ">确认修改</router-link></button>
      <pre class="content ">
      <h5 class="stretch">

</h5>
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
