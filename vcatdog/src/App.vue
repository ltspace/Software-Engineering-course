<template>
<div class="build">
  
  <router-view/>
  
  <!-- 内容区 -->
</div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';


export default {
  name:"App",
  components:{
    
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

.build{
  background: linear-gradient(180deg, rgba(218, 212, 236, 1) 0%, rgba(218, 212, 236, 1) 1%, rgba(243, 231, 233, 1) 100%);
  width:100%;
  height:100%;
  position:fixed;
}

nav {
  position: fixed;
  width: 100%;
  line-height: 70px;
}

nav a {
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}


</style>
