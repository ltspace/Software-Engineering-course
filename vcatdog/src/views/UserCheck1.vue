<template>
 <AdNavBar />
   
      <div class="set">
  <div class="card text-center">
    <div class="card-body ">
      <h2 class="card-title" style="float:center">输入需要查看的用户ID</h2>

      <pre class="content ">
      <h5 class="stretch">

<input type="text" value="" placeholder="ID"  name="ID">

</h5>
 </pre>
<button type="button" class="btn-lg">
    <router-link :to="{name:'userCheck'}" style="text-decoration: none ">确认</router-link></button>

      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>
  </div>
</div>
</template>

<script>
import AdNavBar from '../components/AdNavBar';
export default {
  name: 'UserCheck1',
  components: {
    AdNavBar
  }
}
</script>

<style>
</style>
