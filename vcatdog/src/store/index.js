import { createStore } from 'vuex'
import ModuleUser from './user';

export default createStore({
  state: {//存所有数据
  },
  getters: {//需要计算处理的数据
  },
  mutations: {//对state的直接修改操作，无法进行异步操作
  },
  actions: {//对state的各种操作,更新方式
  },//完整复杂修改
  modules: {//对state进行分割
    user: ModuleUser,
  }
});
