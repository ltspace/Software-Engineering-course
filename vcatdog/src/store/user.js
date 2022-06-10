import $ from 'jquery';
import jwt_decode from 'jwt-decode';

const ModuleUser = {
  state: {
    id: "",
    username: "",
    addr: "",
    phonum:"",
    sex:"",
    job:"",
    email:"",
    photo:"",
    age:"",
    crepoint:"",
    access: "",
    refresh: "",
    is_login: false,
  },
  getters: {
  },
  mutations: {
      updateUser(state, user) {
          state.id = user.id;
          state.username = user.username;
          state.photo = user.photo;
          state.crepoint=user.crepoint;
          state.addr=user.addr;
          state.phonum=user.phonum;
          state.sex=user.sex;
          state.age=user.age;
          state.email=user.email;
          state.job=user.job;
          // state.followerCount = user.followerCount;
          state.access = user.access;
          state.refresh = user.refresh;
          state.is_login = user.is_login;
      },
      updateAccess(state, access) {
          state.access = access;
      },
      logout(state) {
          state.id = "";
          state.username = "";
          state.photo = "";
          // state.followerCount = 0;
          state.access = "";
          state.refresh = "";
          state.is_login = false;
      }
  },
  actions: {
      login(context, data) {//第一个api,第二个传信息
        $.ajax({
            url: "http://127.0.0.1:8000/api/token/",
            type: "POST",
            data: {
                username: data.username,
                password: data.password,
            },
            success(resp) {
                const {access,refresh} = resp;
                const access_obj = jwt_decode(access);
                setInterval(() => {
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/token/refresh/",
                        type: "POST",
                        data: {
                            refresh,
                        },
                        success(resp) {
                            context.commit('updateAccess', resp.access);
                        }
                    });
                }, 4.5 * 60 * 1000);
                $.ajax({
                    url: "http://127.0.0.1:8000/getinfo/",
                    type: "GET",
                    data: {
                        user_id: access_obj.user_id,
                    },
                    headers: {
                        'Authorization': "Bearer " + access,
                    },
                    success(resp,refresh) {
                    //   console.log(resp);
                        context.commit("updateUser", {
                            ...resp,
                            access: access,
                            refresh: refresh,
                            is_login: true,
                        });
                        data.success();
                    },
                })
            },
            error() {
                data.error();
            }
        });
      },
  },
  modules: {
  }
};

export default ModuleUser;
