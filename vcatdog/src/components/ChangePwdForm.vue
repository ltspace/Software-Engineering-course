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
            <div class="zuu1" style="float:center">
              <label class="" slogan>修改密码</label>
            </div>
            <!-- <div class="mb-3">
              <label for="formFile" class="form-label"></label>
              <input class="form-control" type="file" id="formFile">
            </div> -->
            <div class="row g-3 align-items-center">
  <div class="col-auto">
    <label for="inputPassword6" class="col-form-label">输入当前密码</label>
  </div>
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
    <div class="col-auto">
    <label for="inputPassword6" class="col-form-label">请输入新密码</label>
  </div>
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
    <div class="col-auto">
    <label for="inputPassword6" class="col-form-label">请确认新密码</label>
  </div>
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
</div>
 
          </fieldset>
           <div class="zuu3" style="float:center">
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;提&nbsp;&nbsp;交&nbsp;
            </button>
          </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImproveForm',
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

.zuu1 {
  padding-top: 11em;
  padding-bottom: 2em;
}

.zuu2 {
  padding-bottom: 10px;
}

.zuu3 {
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
