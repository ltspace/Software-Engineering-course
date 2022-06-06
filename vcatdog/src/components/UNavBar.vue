<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        <img src="../assets/logo.png" alt="" width="30" height="24">
      </router-link>
      <router-link class="navbar-brand stretch" :to="{ name: 'home' }">流浪猫狗领养救助平台</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse " id="navbarText">
        <ul class=" navbar-nav  me-auto center">
          <li class="nav-item distent">
            <router-link class="nav-link active stretch" aria-current="page" :to="{ name: 'home' }">主页</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link stretch" :to="{ name: '' }">我要领养</router-link>
          </li>
          <li class="nav-item dropdown">
            <router-link class="nav-link stretch dropdown-toggle" :to="{ name: '' }" id="navbarDropdownMenuLink"
              role="button" data-bs-toggle="dropdown" aria-expanded="false">
              我要救助
            </router-link>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink" data-bs-toggle="dropdown">
              <li><a class="dropdown-item stretch smallcard" href="#">填写新救助单</a></li>
              <li><a class="dropdown-item stretch smallcard" href="#">查看救助单</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link class="nav-link stretch" :to="{ name: 'show' }">动物展示</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link stretch" :to="{ name: 'contactus' }">联系我们</router-link>
          </li>
        </ul>
        <ul class="navbar-nav" v-if="!$store.state.user.is_login" >
          <li class="nav-item">
            <router-link class="nav-link active stretch" aria-current="page" :to="{ name: 'userlogin' }">登陆</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link stretch" :to="{ name: 'registerview' }">注册</router-link>
          </li>
        </ul>
        <ul class="navbar-nav" v-else >
          <li class="nav-item">
            <router-link class="nav-link active stretch" 
            aria-current="page" :to="{ name: 'personalinfo',params:{userID:$store.state.user.username}}">
            ID:{{ $store.state.user.username }}</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link stretch" style="cursor:pointer" @click="logout">退出</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useStore } from 'vuex';

export default {
    name: "UNavBar",
    setup() {
      const store = useStore();
      const logout = () => {
        store.commit('logout');
      };

      return {
        logout,
        
      }
    }
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