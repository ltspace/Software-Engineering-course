<template>
  <UNavBar />
  <div class="container">
    <h3 style="font-family:Youyuan;text-align: center;">可领养动物</h3>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col">
        <div class="card" id="1">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>

      <div class="col">
        <div class="card" id="2">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>
      <div class="col">
        <div class="card" id="3">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>

      <div class="col">
        <div class="card" id="4">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>

      <div class="col">
        <div class="card" id="5">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>
      <div class="col">
        <div class="card" id="6">
          <img src="../assets/R-C.jpg" class="card-img-top" alt="...">
          <a href="#" class="btn btn-primary how">领养我</a>
        </div>
      </div>
    </div>
  </div>


  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center ">
      <li class="page-item disabled">
        <a class="page-link">&laquo;</a>
      </li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item">
        <a class="page-link" href="#">&raquo;</a>
      </li>
    </ul>
  </nav>

</template>


<script>
import UNavBar from '../components/UNavBar.vue'
export default {
  name: 'AniShow',
  components: {
    UNavBar
  },
  
  setup () {
    const store = useStore();
    // let id = store.state.user_id;
    let username = store.state.user.username;
    let phonum = ref('');
    let email = ref('');
    let addr = ref('');
    let job = ref('');
    let message = ref('');
    let photo = ref('');
    var selectedSex = $('#sex input:radio:checked').val();
    let sex = "男";
    if (selectedSex==1)
    {
      sex = "男";
    }
    else 
    {
      sex = "女";
    }

    const userinfoselfchge = () => {
      message.value = "";
      $.ajax({
        url: "http://127.0.0.1:8000/userinfoselfchge/",
        type: "POST",
        data: {
          // id: id,
          username: username,
          sex: sex,
          phonum: phonum.value,
          email: email.value,
          addr: addr.value,
          job: job.value,
          photo: photo.value,
        },
        success (resp) {
          if (resp.result == "1") {
            
            if(phonum.value!=null&&email.value!=null&&addr.value!=null&&job.value!=null)
            {
              store.state.user.crepoint=1;
              message.value = "更新成功!您的信用积分为1!";
              store.state.user.phonum=phonum.value;
              store.state.user.sex=sex.value;
              store.state.user.photo=photo.value;
              store.state.user.job=job.value;
              store.state.user.email=email.value;
              store.state.user.addr=addr.value;
            }
            else{
              store.state.user.crepoint=0;
              message.value = "更新成功!存在部分必要个人领养信息未填,您的信用积分为0!";
            }
          } else {
            message.value = resp.result;
          }
        }
      })
    };

    return {
      // id,
      sex,
      username,
      phonum,
      email,
      addr,
      job,
      message,
      photo,
      userinfoselfchge,
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

.how {
  background: linear-gradient(90deg, rgba(255, 236, 210, 1) 0%, rgba(252, 182, 159, 1) 100%);
  border-radius: 5%;
  border-color: transparent;
  color: black;
}


</style>
