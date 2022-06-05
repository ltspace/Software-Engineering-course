<template>
  <UNavBar />
<div class="set">
  <div class="card text-center">
    <div class="card-body">
      <h3 class="card-title">任何关于本系统的意见与建议，以及相关合作事宜，请通过以下方式与我们联系：</h3>
      <p class="card-text">
      <pre class="content">
      <h4 class="stretch">
<strong >商务及合作：</strong>请发送邮件至tj13132069459@163.com
<br>
<strong>品牌广告投放：</strong>请发送邮件至2417769953@qq.com 
<br>
<strong>管理员邮箱：</strong>发送邮件至tj13132069459@163.com
<br>
<strong>联系客服：</strong>在线客服请拨打18853813036
<br>
<strong>公司地址：</strong>山东省威海市环翠区文化西路180号山东大学威海校区</h4>
 </pre>
      </p>
      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>
  </div>
</div>
</template>

<script>
import UNavBar from '../components/UNavBar';
export default {
  name: 'ContactUs',
  components: {
    UNavBar
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
.card{
  background-color: transparent;
  padding-top: 5em;
}
</style>
