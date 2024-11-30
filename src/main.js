import Vue from 'vue';
import App from './App.vue';
import ElementUI from 'element-ui';
import router from './router/index.js';

Vue.config.productionTip = false;
Vue.use(ElementUI);




// 全局路由守卫
router.beforeEach((to, from, next) => {
  // 检查路由是否需要登录
  if (to.matched.some(record => record.meta.needLogin)) {
    const isAuthenticated = !!localStorage.getItem('access_token'); // 检查 token 是否存在

    if (!isAuthenticated) {
      // 如果没有 token，跳转到登录页面
      alert('还没有登录，请先登录');
      return next({
        path: '/login',
        query: { redirect: to.fullPath } // 保存原目标路径
      });
    }
    
    // 检查是否需要管理员权限
    else if (to.matched.some(record => record.meta.requiresAdmin)) {
      const isAdmin = localStorage.getItem('is_superuser') === 'true'; // 强对比管理员权限

      if (!isAdmin) {
        alert('您没有访问该页面的权限');
        return next('/main'); // 无权限则跳转到主页面
      }
    }
  }
  
  // 如果已登录或不需要登录权限，继续访问
  next();
});

// 路由守卫
// router.beforeEach((to, from, next) => {
//   // 设置页面默认标题
//   document.title = to.meta.title || '会议室管理';

//   const isLogin = localStorage.getItem('isLogin') === 'true';
//   const isAdmin = localStorage.getItem('userRole') === 'admin'; // 检查用户角色

//   // 判断是否需要登录，且用户未登录
//   if (to.meta.needLogin && !isLogin) {
//     alert('还没有登录，请先登录');
//     next('/login'); // 重定向到登录页面
//   } else if (to.meta.requiresAdmin && !isAdmin) {
//     alert('您没有权限访问该页面');
//     next('/main'); // 普通用户跳转到主页面
//   } else {
//     next(); // 继续跳转
//   }
// });

new Vue({
  render: h => h(App),
  router,
}).$mount('#app');
