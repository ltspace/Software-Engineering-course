<template>
  <div class="card edit-field">
    <div class="card-body">
      <label for="edit-post" class="form-label"><h3>发表待救助动物</h3></label>
      <div class="mb-3">
        <label for="formFile" class="form-label"></label>
        <input v-on="img" class="form-control"  type="file" id="formFile">

      </div>
      <div class="mb-3 row">
        <label for="inputPassword" class="col-sm-2 col-form-label">出现地点</label>
        <div class="col-sm-10">
          <input type="text" v-model="address" class="form-control">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="inputPassword" class="col-sm-2 col-form-label">症状</label>
        <div class="col-sm-10">
          <input type="text" v-model="symptom" class="form-control">
        </div>
      </div>
      <button  type="button" class="btn btn-primary" style="letter-spacing: 5px">发帖</button>
      <!-- @click="post_a_post" -->
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
export default {
  name: 'HomeWrite',
  setup()
  {
    let address = ref();
    let img =ref();
    let symptom = ref();
    return {
      img,
      symptom,
      address
    }
  },

}
</script>

<style>
.card-body {
  margin-top: 0;
  padding-top: 0;
}
.card{
  border: 0ch;
}

.card {
  font-family: YouYuan, Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  transform-origin: 0 0;
  font-weight: bolder;
}
.btn-primary{
  background-color: black;
}

</style>