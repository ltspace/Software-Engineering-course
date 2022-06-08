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
              <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="例：旺财">
            </div>
            <label for="formFile" class="form-label">照片:</label>
            <input class="form-control" type="file" id="formFile">
            <div class="form-group ">
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
            <div class="form-group ">
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
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">品种：</label>
              <input type="text" class="form-control" placeholder="例：哈士奇" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">毛色：</label>
              <input type="text" class="form-control" placeholder="例：黑白相间" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">年龄：</label>
              <input type="text" class="form-control" placeholder="例:
              6个月" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">性格：</label>
              <input type="text" class="form-control" placeholder="例：过于活泼" />
            </div>
            <div class="form-group ">
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
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疫苗情况：</label>
              <input type="text" class="form-control" placeholder="例：已打狂犬疫苗" />
            </div>
            <div class="form-group ">
              <label for="exampleFormControlInput1" class="form-label">疾病情况：</label>
              <input type="text" class="form-control" placeholder="例：健康" />
            </div>
            <div class="form-group ">
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
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import $ from 'jquery';

export default {
  name: 'FillHelpForm',
  setup() {
    const store = useStore();
    let username = ref('');
    let password = ref('');
    let password_confirm = ref('');
    let message = ref('');
    
    const register = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/register/",
        type: "POST",
        data: {
          username: username.value,
          password: password.value,
          password_confirm: password_confirm.value,
        },
        success(resp) {
          if (resp.result === "success") {
            store.dispatch("login", {
              username: username.value,
              password: password.value,
              success() {
                router.push({name: 'home'});
              },
              error() {
                message.value = "系统异常，请稍后重试";
              }
            });
          } else {
            message.value = resp.result;
          }
        }
      })
    };

    return {
      username,
      password,
      password_confirm,
      message,
      register,
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
