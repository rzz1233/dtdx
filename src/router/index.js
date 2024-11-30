import Vue from 'vue';
import VueRouter from 'vue-router';

// 引入界面
import pageLogin from '@/view/PageLogin.vue';
import PageRegister from '@/view/PageRegister.vue';
import PageMain from '@/view/PageMain.vue';
import PageList from '@/view/PageList.vue';
import PageOrder from '@/view/PageOrder.vue';
import Page1 from '@/view/Page-1.vue';
import Page2 from '@/view/Page-2.vue';
import PageDetails from '@/view/PageDetails.vue';
import BackstageView from '@/view/BackstageView.vue';
import PageDept from '@/Backstage/PageDept.vue';
import PageMeeting from '@/Backstage/PageMeeting.vue';
import PageLogin1 from '@/Backstage/PageLogin1.vue';
import PageUser from '@/Backstage/PageUser.vue';
import PageAttendee from '@/Backstage/PageAttendee.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: '/login',
      component: pageLogin,
      meta: { title: '会议室登录' },
    },
    {
      path: '/register',
      component: PageRegister,
      meta: { title: '注册' },
    },
    {
      path: '/backstageview',
      redirect: "/backstageview/pagemeeting",
      component: BackstageView,
      meta: { title: '后台', requiresAdmin: true }, // 添加管理员权限检查
      children: [
        {
          path: 'pagemeeting',
          component: PageMeeting,
          meta: { needLogin: true, title: '会议室管理后台', requiresAdmin: true }, // 添加管理员检查
        },
        {
          path: 'pagedept',
          component: PageDept,
          meta: { needLogin: true, title: '部门管理', requiresAdmin: true }, // 添加管理员检查
        },
        {
          path: 'pagelogin1',
          component: PageLogin1,
          meta: { needLogin: true, title: '登录管理', requiresAdmin: true }, // 添加管理员检查
        },
        {
          path: 'pageuser',
          component: PageUser,
          meta: { needLogin: true, title: '用户管理', requiresAdmin: true }, // 添加管理员检查
        },
        {
          path: 'pageattendee',
          component: PageAttendee,
          meta: { needLogin: true, title: '签到管理', requiresAdmin: true }, // 添加签到检查
        },
      ]
    },
    {
      path: '/main',
      redirect: "/main/list",
      component: PageMain,
      children: [ 
        {
          path: 'page1',
          component: Page1,
          meta: { needLogin: true },
        },
        {
          path: 'list',
          component: PageList,
          meta: { needLogin: true },
        },
        {
          path: 'page2',
          component: Page2,
          meta: { needLogin: true },
        },
        {
          path: 'order',
          component: PageOrder,
          meta: { needLogin: true },
        },
        {
          path: 'details',
          component: PageDetails,
          meta: { needLogin: true },
        },
      ]
    },
    { path: '*', redirect: '/login' },
  ]
});

export default router;
