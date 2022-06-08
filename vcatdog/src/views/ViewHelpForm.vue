<template>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <div class="col-md-4 center-in-center">
        <form action="" role="form">
          <fieldset>
            <div class="mb-3">
              <label for="exampleFormControlInput1" class="form-label">
                动物名：
              </label>
              <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="例：旺财">
            </div>
            <div class="mb-3">
              <label for="formFile" class="form-label">照片:</label>
              <input class="form-control" type="file" id="formFile">
            </div>
            <div class="form-group zu2">
              <label for="formFile" class="form-label">性别:&emsp;&emsp;&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="option1">
                <label class="form-check-label" for="inlineRadio1">公</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="option2">
                <label class="form-check-label" for="inlineRadio2">母</label>
              </div>
            </div>
            <div class="form-group zu2">
              <label for="formFile" class="form-label">动物类别:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="option1">
                <label class="form-check-label" for="inlineRadio1">猫</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="option2">
                <label class="form-check-label" for="inlineRadio2">狗</label>
              </div>
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">品种：</label>
              <input type="text" class="form-control" placeholder="例：哈士奇" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">毛色：</label>
              <input type="text" class="form-control" placeholder="例：黑白相间" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">年龄：</label>
              <input type="text" class="form-control" placeholder="例：6个月" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">性格：</label>
              <input type="text" class="form-control" placeholder="例：过于活泼" />
            </div>
            <div class="form-group zu2">
              <label for="formFile" class="form-label">绝育情况:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1"
                  value="option1">
                <label class="form-check-label" for="inlineRadio1">已绝育</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2"
                  value="option2">
                <label class="form-check-label" for="inlineRadio2">未绝育</label>
              </div>
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">疫苗情况：</label>
              <input type="text" class="form-control" placeholder="例：已打狂犬疫苗" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">疾病情况：</label>
              <input type="text" class="form-control" placeholder="例：健康" />
            </div>
            <div class="form-group zu2">
              <label for="exampleFormControlInput1" class="form-label">地址：</label>
              <input type="text" class="form-control" placeholder="例：山东大学（威海）18号楼312宿舍" />
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-12">
              提交
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <div class="vzu1">
    <div class="mb-3 row">
      <label class="" slogan>查看救助单</label>
    </div>
    <span class="badge text-bg-primary">动物ID:</span>
    <span class="badge text-bg-info">002</span>

    <span class="badge text-bg-primary">领养情况</span>
    <span class="badge text-bg-info">否</span>

  </div>
</template>

<script>
// import HelpForm from '../components/HelpForm';
export default {
  name: 'ViewHelpForm',
  components: {
    // HelpForm
  }
}
</script>

<style scoped>
.vzu1 {
  position: absolute;
  left: 200px;
  top: 60px;
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
