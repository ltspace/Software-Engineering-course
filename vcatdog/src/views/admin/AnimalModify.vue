<template>


  <AdNavBar />
  <div class="head container col-md-11">
    <br>
    <h3>动物信息修改</h3>
    <h5>
      <strong>动物ID：</strong>001
    </h5><br>
    <strong>动物名：</strong>
    <input type="text" value="旺财" placeholder="动物名" name="name">
    <strong>年龄：</strong>
    <input type="text" value="8个月" placeholder="年龄" name="age">
    <br>
    <br>
    <strong>动物类别：</strong>
    <input type="text" value="公" placeholder="性别" name="sex">
    <input type="text" value="猫" placeholder="<猫或狗>" name="kind">
    <br>
    <br>
    <strong>品种：</strong>
    <input type="text" value="哈士奇" placeholder="品种" name="breed">
    <br>
    <br>
    <strong>毛色：</strong>
    <input type="text" value="黑白相间" placeholder="毛色" name="color">
    <br>
    <br>
    <strong>性格：</strong>
    <input type="text" value="过于活泼" placeholder="性格" name="character">
    <br>
    <br>
    <strong>绝育情况：</strong>
    <input type="text" value="已绝育" placeholder="是否绝育" name="1">
    <br>
    <br>
    <strong>疫苗情况：</strong>
    <input type="text" value="已接种狂犬疫苗" placeholder="接种何种疫苗" name="2">
    <br>
    <br>
    <strong>疾病情况：</strong>
    <input type="text" value="健康" placeholder="是否有疾病" name="illness">
    <br>
    <br>
    <strong>地址：</strong>
    <input type="text" value="山东大学（威海）18号楼312" placeholder="地址" name="address">
    <br>
    <br>
    <strong>是否被领养：</strong>否
    <br>
    <button type="button" class="btn-lg">
      <router-link :to="{ name: 'animalCheck' }" style="text-decoration: none ">确认修改</router-link>
    </button>
  </div>
  <div class="set">
    <div class="card text-center">
      <div class="card-body ">



        <br>
        <br>

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

.head {
  transform: scale(1, 1.1);
  text-align: center;
}
</style>
