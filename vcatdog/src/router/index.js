import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserLoginView from '../views/UserLogin.vue'
import AdminLoginView from '../views/AdminLogin.vue'
import ContactUs from '../views/ContactUs'
import UserRegister from '../views/UserRegister.vue'
import AnimalShow from '../views/AnimalShow.vue'
import ChangePwd from '../views/ChangePwd.vue'
import PersonalInfo from '../views/PersonalInfo.vue'
import FillHelpForm from '../views/FillHelpForm.vue'
import ViewHelpForm from '../views/ViewHelpForm.vue'
import AdoptionInfo from '../views/AdoptionInfo.vue'
import NotFound from '../views/NotFound.vue'
import AssistAni from '../views/AssitAni.vue'
import AniShow from '../views/AniShow.vue';
import AdoptionForm from '../views/AdoptionForm.vue';
import AdoptFormView from '../views/Adoptformview.vue'


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
  {
    path: '/adoptformview/',
    name: 'adoptformview',
    component: AdoptFormView
  },
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
    path: '/adoptionform/:adoptid/:aniid',
    name: 'adoptionform',
    component: AdoptionForm
  },

{
    path: '/assistani/:assistid/:aniid',
    name: 'assistani',
    component: AssistAni
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
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

