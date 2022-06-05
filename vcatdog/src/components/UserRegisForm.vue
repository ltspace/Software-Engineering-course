<template>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form action="" role="form">
          <fieldset>
            <div class="head container col-md-11">
              <h4>
                <img src="../assets/logo.png" alt="" width="60" />&nbsp;
                流浪猫狗领养救助平台
              </h4>
              <label class="slogan">Hold
                out our hands, leave a love, and keep a life</label>
            </div>
            <div class="zu1" style="float:center">
                <label class="slogan">注册</label>
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="用户名" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="邮箱" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="6-16位密码，区分大小写" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="确认密码" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="11位手机号" />
            </div>
            <div>
            <div class="form-group zu2" style="float:left">
              <input type="text" class="form-control" placeholder="输入验证码" />
            </div>
            <div class="form-group zu2" style="float:right">
                <button type="button" class="btn btn-light">获取验证码</button>
            </div>
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;&nbsp;&nbsp;&nbsp;注&nbsp;&nbsp;&nbsp;&nbsp;册&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
          </div>
          <button type="submit" class="btn col-md-6">
                <router-link :to="{name:'userlogin'}" style="text-decoration: none ">使用已有账户登陆</router-link>
              </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserRegisForm',
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
  padding-bottom: 1em;
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

