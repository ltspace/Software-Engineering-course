<template>
  <!-- <link rel="stylesheet" media="screen" href="bootstrap/dist/css/bootstrap.min.css"> -->
  <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
  <div class="container center-in-center">
    <div class="row">
      <label class="slogan">填写新救助单</label>
      <div class="col-md-4 center-in-center">
        <form @submit.prevent="fillhelp">
          <fieldset>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">
                动物名：
              </label>
              <input v-model="name" type="name" class="form-control" id="exampleFormControlInput1" placeholder="例：旺财">
            </div>
            <label for="formFile" class="form-label">照片:</label>
            <!-- <input type="file" class="face" accept="image/*" @change="upload_photo" ref="inputer">
             -->
            <input v-model="photo" type="text" class="form-control" placeholder="请填入URL" />
            <div class="form-group" id="sex">
              <label for="formFile" class="form-label">性别:&emsp;&emsp;&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions1" id="inlineRadio1" value="1">
                <label class="form-check-label" for="inlineRadio1">公</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions1" id="inlineRadio2" value="2">
                <label class="form-check-label" for="inlineRadio2">母</label>
              </div>
            </div>
            <div class="form-group" id="cd">
              <label for="formFile" class="form-label">动物类别:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions2" id="inlineRadio1" value="1">
                <label class="form-check-label" for="inlineRadio3">猫</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions2" id="inlineRadio2" value="2">
                <label class="form-check-label" for="inlineRadio4">狗</label>
              </div>
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">品种：</label>
              <input v-model="type" type="text" class="form-control" placeholder="例：哈士奇" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">毛色：</label>
              <input v-model="fur" type="text" class="form-control" placeholder="例：黑白相间" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">年龄：</label>
              <input v-model="age" type="text" class="form-control" placeholder="例: 6个月" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">性格：</label>
              <input v-model="chara" type="text" class="form-control" placeholder="例：过于活泼" />
            </div>

            <div class="form-group " id="baby">
              <label for="formFile" class="form-label">绝育情况:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions3" id="inlineRadio1" value="1">
                <label class="form-check-label" for="inlineRadio5">已绝育</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions3" id="inlineRadio2" value="2">
                <label class="form-check-label" for="inlineRadio6">未绝育</label>
              </div>
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疫苗情况：</label>
              <input v-model="vacc" type="text" class="form-control" placeholder="例：已打狂犬疫苗" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疾病情况：</label>
              <input v-model="ill" type="text" class="form-control" placeholder="例：健康" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">地址：</label>
              <input v-model="addr" type="text" class="form-control" placeholder="例：山东大学（威海）18号楼312宿舍" />
            </div>
            <div class="form-group " id="can_adopt">
              <label for="formFile" class="form-label">可否被领养:&emsp;&emsp;</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions4" id="inlineRadio1" value="1">
                <label class="form-check-label" for="inlineRadio7">可</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions4" id="inlineRadio2" value="2">
                <label class="form-check-label" for="inlineRadio8">否</label>
              </div>
            </div>
          </fieldset>
          <div class="container-fluid" style="text-align: center">
            <button type="submit" class="btn btn-primary col-md-5">
              提交
            </button>
          </div>
        </form>
        <router-link class="btn btn-primary col-md-5" :to="{ name: 'home' }" role="button" style="margin-left:25px;">
          返回主页面</router-link>
      </div>
    </div>
  </div>
  <!-- <div class="alert alert-warning"> {{ message }}</div> -->
</template>
<!-- <script src="..\dist\static\js\jquery-3.5.1.js" type="text/javascript" charset="utf-8"></script> -->
<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
// import router from '@/router/index';
import $ from 'jquery';

export default {

  name: 'FillHelpForm',
  setup () {
    const store = useStore();
    let username = store.state.user.username;
    let name = ref('');
    let message = ref('');
    let photo = ref('');
    let fur = ref('');
    let age = ref('');
    let chara = ref('');
    let type = ref('');
    let vacc = ref('');
    let ill = ref('');
    let addr = ref('');
    let sex = "";
    let cd = "";
    let jveyu = "";
    let can_adopt = "";
    const fillhelp = () => {
      var selectedSex = $('#sex input:radio:checked').val();
      var selectedcd = $('#cd input:radio:checked').val();
      var selectedjveyu = $('#baby input:radio:checked').val();
      var selectedadopt = $('#can_adopt input:radio:checked').val();
      if (selectedSex == 1) {
        sex = "公";
      }
      else {
        sex = "母";
      }
      if (selectedcd == 1) {
        cd = "猫";
      }
      else {
        cd = "狗";
      }
      if (selectedjveyu == 1) {
        jveyu = "已绝育";
      }
      else {
        jveyu = "未绝育";
      }
      if (selectedadopt == 1) {
        can_adopt = "1";
      }
      else {
        can_adopt = "0";
      }
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/saveassit/",
        type: "POST",
        data: {
          // id: id,
          username: username,
          name: name.value,
          photo: photo.value,
          fur: fur.value,
          age: age.value,
          chara: chara.value,
          type: type.value,
          vacc: vacc.value,
          ill: ill.value,
          addr: addr.value,
          sex: sex,
          cd: cd,
          can_adopt: can_adopt,
          jveyu: jveyu,
        },
        success (resp) {
            message.value = resp.result;
            alert(message.value);
        }
      })
    };
    return {
      username,
      name,
      photo,
      fur,
      age,
      chara,
      type,
      vacc,
      ill,
      addr,
      sex,
      cd,
      jveyu,
      message,
      can_adopt,
      fillhelp,
    }
  }
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

.head {
  transform: scale(1, 1.1);
  text-align: center;
}


.slogan {
  font-size: 2em;
  font-family: Youyuan;
  color: rgba(0, 0, 0, 0.619);
  transform: scale(1, 1.1);
  letter-spacing: 3px;
}

.padd {
  /* padding-top: 5px; */
  /* padding-bottom: 1em; */
  padding-left: 20em;
  font-weight: normal;
}
</style>
