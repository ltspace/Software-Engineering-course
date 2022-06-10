<template> 

 
  <AdNavBar />
   
      <div class="set">
  <div class="card text-center">
    <div class="card-body ">
      <h2 class="card-title" style="float:center">管理员信息修改</h2>
<h5><strong >工号：</strong>001</h5>
<br>
<br>
<strong>性别：</strong>
<input type="text" value="女" placeholder="性别"  name="sex">
<br>
<br>
<strong>电话：</strong>
<input type="text" value="15848530635" placeholder="电话"  name="phone">
<br>
<br>
<strong>投诉邮箱：</strong>
<input type="text" value="2417769953@qq.com" placeholder="投诉邮箱"  name="email">
<br>
<br>
<strong>工龄：</strong>
<input type="text" value="1年" placeholder="工龄"  name="gage">
<br>
<br>
<strong>年龄：</strong>
<input type="text" value="20" placeholder="年龄"  name="age">
<br>
<br>
<strong>在线时间：</strong>
<input type="text" value="8:00-21:00" placeholder="在线时间"  name="time">
<br>
<br>
<button type="button" class="btn-lg">
    <router-link :to="{name:'adminCheck'}" style="text-decoration: none ">确认修改</router-link></button>
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
