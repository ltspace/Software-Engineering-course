import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserLoginView from '../views/UserLogin.vue'
import AdminLoginView from '../views/AdminLogin.vue'
import ContactUs from '../views/ContactUs'
import UserRegister from '../views/UserRegister.vue'
import AnimalShow from '../views/AnimalShow.vue'
// import ImproveInfo from '../views/ImproveInfo.vue'
import ChangePwd from '../views/ChangePwd.vue'
import PersonalInfo from '../views/PersonalInfo.vue'
import FillHelpForm from '../views/FillHelpForm.vue'
import ViewHelpForm from '../views/ViewHelpForm.vue'
import AdoptionInfo from '../views/AdoptionInfo.vue'
import NotFound from '../views/NotFound.vue'
// import AdminShow from '../views/AdminShow.vue'
// import AdminCheck from '../views/AdminCheck.vue'
// import AdminModify from '../views/AdminModify.vue'
// import AnimalCheck from '../views/AnimalCheck.vue'
// import AnimalModify from '../views/AnimalModify.vue'
import UserCheck from '../views/UserCheck.vue'
import UserCheck1 from '../views/UserCheck1.vue'
import UserModify from '../views/UserModify.vue'
import AniShow from '../views/AniShow.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/userlogin/',
    name: 'userlogin',
    component: UserLoginView
  },
  {
    path: '/adminlogin/',
    name: 'adminlogin',
    component: AdminLoginView
  },
  {
    path: '/contactus/',
    name: 'contactus',
    component: ContactUs
  },
  {
    path: '/registerview/',
    name: 'registerview',
    component: UserRegister
  },
  {
    path: '/show/',
    name: 'show',
    component: AnimalShow
  },
  // {
  //   path: '/improveinfo/',
  //   name: 'improveinfo',
  //   component: ImproveInfo
  // },
  {

    path: '/404/',
    name: '404',
    component: NotFound
  },
{
    path: '/changepwd',
    name: 'changepwd',
    component: ChangePwd
  },
  {
    path: '/personalinfo',
    name: 'personalinfo',
    component: PersonalInfo
  },
  {
    path: '/fillhelpform',
    name: 'fillhelpform',
    component: FillHelpForm
  },
  {
    path: '/viewhelpform',
    name: 'viewhelpform',
    component: ViewHelpForm
  },

  {
    path: '/adoptioninfo/:aniid/',
    name: 'adoptioninfo',
    component: AdoptionInfo
  },
  {
    path: '/adoptionform/:adoptid/',
    name: 'adoptioninfo',
    component: AdoptionInfo
  },

// {
//     path: '/Administrator',
//     name: 'Administrator',
//     component: AdminShow
//   },
//   {
//     path: '/admincheck',
//     name: 'admincheck',
//     component: AdminCheck
//   },
//   {
//     path: '/adminModify',
//     name: 'adminModify',
//     component: AdminModify
//   },
  // {
  //   path: '/animalCheck',
  //   name: 'animalCheck',
  //   component: AnimalCheck
  // },
  // {
  //   path: '/animalModify',
  //   name: 'animalModify',
  //   component: AnimalModify
  // },
  {
    path: '/userCheck',
    name: 'userCheck',
    component: UserCheck
  },
  {
    path: '/userCheck1',
    name: 'userCheck1',
    component: UserCheck1
  },
  {
    path: '/userModify',
    name: 'userModify',
    component: UserModify
  },
  {
    path: '/anishow',
    name: 'anishow',
    component: AniShow
  },

  {
    path: '/:catchAll(.*)',
    redirect:"/404"
  },
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

