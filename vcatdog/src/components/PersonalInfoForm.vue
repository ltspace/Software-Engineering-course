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
              <label class="" slogan>个人信息</label>
            </div>
            <div class="mb-3 row">
              <label for="staticEmail" class="col-sm-4 col-form-label">用户ID：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="001">
              </div>
            </div>

            <div class="mb-3">
              <label for="exampleFormControlInput1" class="form-label">用户名：</label>
              <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="请输入用户名">
            </div>


            <div class="mb-3">
              <label for="formFile" class="form-label">头像</label>
              <input class="form-control" type="file" id="formFile">
            </div>
            <div class="form-group zu2">
              <label for="formFile" class="form-label">性别&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="option1">
                <label class="form-check-label" for="inlineRadio1">男</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="option2">
                <label class="form-check-label" for="inlineRadio2">女</label>
              </div>
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">电话：</label>
              <input type="text" class="form-control" placeholder="11位电话号码" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">邮箱：</label>
              <input type="text" class="form-control" placeholder="邮箱" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">地址：</label>
              <input type="text" class="form-control" placeholder="地址" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">职业：</label>
              <input type="text" class="form-control" placeholder="职业" />
            </div>
            <div class="mb-3 row">
              <label for="staticEmail" class="col-sm-4 col-form-label">信用积分：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="100">
              </div>
              <label for="staticEmail" class="col-sm-4 col-form-label">已领养动物：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="10只">
              </div>
              <label for="staticEmail" class="col-sm-4 col-form-label">已救助动物：</label>
              <div class="col-sm-5">
                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="1只">
              </div>
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;&nbsp;&nbsp;&nbsp;更新基本信息&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonalInfoForm',
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
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}

.zu2 {
  padding-bottom: 1px;
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
