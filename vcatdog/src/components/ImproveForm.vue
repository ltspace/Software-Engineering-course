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
              <label class="" slogan>完善信息</label>
            </div>
            <div class="mb-3">
              <label for="formFile" class="form-label"></label>
              <input class="form-control" type="file" id="formFile">
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="年龄（选填）" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="地址（选填）" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="职业（选填）" />
            </div>
            <div class="form-group zu2">
              <input type="text" class="form-control" placeholder="性别（必填）" />
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              &nbsp;&nbsp;&nbsp;&nbsp;提&nbsp;&nbsp;&nbsp;&nbsp;交&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
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

.zu1 {
  padding-top: 7em;
  padding-bottom: 3.5em;
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
