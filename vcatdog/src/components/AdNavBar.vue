<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        <img src="../assets/logo.png" alt="" width="50" height="30">
      </router-link>
      <router-link class="navbar-brand stretch" :to="{ name: 'home' }">流浪猫狗领养救助平台</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse " id="navbarText">
        <ul class=" navbar-nav  me-auto center">
          <li class="nav-item distent">
            <div class="dropdown">
  <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    动物信息管理
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">动物信息查看</a></li>
    <li><a class="dropdown-item" href="#">动物信息修改</a></li>
  </ul>
</div>
          </li>
         
          <li class="nav-item">
            <div class="dropdown">
  <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    用户信息管理
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">用户信息查看</a></li>
    <li><a class="dropdown-item" href="#">用户信息修改</a></li>
  </ul>
</div>
          </li>
          <li class="nav-item">
                     <div class="dropdown">
  <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    管理员信息管理
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">管理员信息查看</a></li>
    <li><a class="dropdown-item" href="#">管理员信息修改</a></li>
  </ul>
</div>
          </li>
         
        </ul>
        
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AdNavBar',
}
</script>

<style scoped>
nav.navbar.navbar-expand-lg.bg-light {
  font-family: YouYuan;
  background-color: transparent !important;
}

.navbar-expand-lg .navbar-nav .nav-link {
  padding-left: 1em;
  padding-right: 1em;
}

.stretch {
  transform: scale(1, 1.1);
  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
  color: black;
}

.container-fluid {
  padding-left: 5em;
  padding-right: 5em;
}

.center {
  margin: 0 auto;
}

.smallcard {
  background: transparent;
  padding-top: 0%;
  padding-bottom: 0%;
  line-height: 50px;
}

.dropdown-menu {
  background: linear-gradient(180deg, rgba(218, 212, 236, 1) 0%, rgba(218, 212, 236, 1) 1%, rgba(243, 231, 233, 1) 100%);
}

.nav-link {
  color: black;
  padding-left: 1em;
  padding-right: 1em;
}

</style>