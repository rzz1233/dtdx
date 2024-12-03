<template>
  <div id="app">
    <div class="bottom">
      <div class="b-1">
        <div class="logo">
          <h2>会议管理系统</h2>
        </div>
        <ul class="nav-menu">
          <li @click="topage('page1')" :class="{active: isActive('/main/page1')}">
            <i class="el-icon-s-home"></i>
            <span>主页</span>
          </li>
          <li @click="topage('page2')" :class="{active: isActive('/main/page2')}">
            <i class="el-icon-video-camera"></i>
            <span>会议使用中</span>
          </li>
          <li @click="topage('order')" :class="{active: isActive('/main/order')}">
            <i class="el-icon-time"></i>
            <span>即将开始</span>
          </li>
          <li @click="topage('details')" :class="{active: isActive('/main/details')}">
            <i class="el-icon-document"></i>
            <span>会议详情</span>
          </li>
          <li @click="topage('list')" :class="{active: isActive('/main/list')}">
            <i class="el-icon-menu"></i>
            <span>会议列表</span>
          </li>
        </ul>
        <div class="nav-footer">
          <button class="logout-button" @click="logout">
            <i class="el-icon-switch-button"></i>
            <span>退出登录</span>
          </button>
        </div>
      </div>
      <div class="main-container">
        <div class="header">
          <div class="header-left">
            <h2>{{ getCurrentPageTitle() }}</h2>
          </div>
          <div class="header-right">
            <el-dropdown trigger="click">
              <span class="user-dropdown">
                <i class="el-icon-user"></i>
                <span>用户中心</span>
                <i class="el-icon-arrow-down"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>
                  <i class="el-icon-user"></i> 个人信息
                </el-dropdown-item>
                <el-dropdown-item>
                  <i class="el-icon-setting"></i> 设置
                </el-dropdown-item>
                <el-dropdown-item divided @click.native="logout">
                  <i class="el-icon-switch-button"></i> 退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </div>
        <div class="content-container">
          <div class="content-wrapper">
            <router-view></router-view>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from './api';

export default {
  
  data() {
    return {
      num: 0,
      statusUpdateTimer: null,
    };
  },
  
  created() {
    this.startStatusUpdateTimer();
  },

  beforeDestroy() {
    this.clearStatusUpdateTimer();
  },

  methods: {
    topage(path) {
      const targetPath = '/main/' + path;
      // 检查目标路径是否与当前路径相同
      if (this.$route.fullPath !== targetPath) {
        this.$router.push(targetPath);
      }
    },
    isActive(path) {
      return this.$route.fullPath === path; // 检查当前路径是否为激活状态
    },
    logout() {
      // 执行登出逻辑，比如清除登录状态
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      this.$router.push('/login'); // 跳转到登录页面
    },
    backstage(){
      this.$router.push('/backstageview');
    },
    getCurrentPageTitle() {
      const path = this.$route.path;
      const titles = {
        '/main/page1': '主页',
        '/main/page2': '会议使用中',
        '/main/order': '即将开始',
        '/main/details': '会议详情',
        '/main/list': '会议列表'
      };
      return titles[path] || '会议管理系统';
    },
    startStatusUpdateTimer() {
      this.updateMeetingStatus();
      
      this.statusUpdateTimer = setInterval(() => {
        this.updateMeetingStatus();
      }, 60000);
    },
    clearStatusUpdateTimer() {
      if (this.statusUpdateTimer) {
        clearInterval(this.statusUpdateTimer);
        this.statusUpdateTimer = null;
      }
    },
    async updateMeetingStatus() {
      try {
        const response = await apiClient.get('/api/meetinglist/update_meeting_status/');
        if (response.data && response.data.updated_count > 0) {
          console.log('会议状态更新成功:', response.data);
        }
      } catch (error) {
        console.error('会议状态更新失败:', error.response?.data || error);
      }
    }
  }
}
</script>

<style scoped>
.bottom {
  display: flex;
  height: 100vh;
  background-color: #f0f2f5;
}

.b-1 {
  width: 240px;
  background-color: #001529;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  position: relative;
}

.logo {
  height: 64px;
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo h2 {
  color: white;
  margin: 0;
  font-size: 18px;
  font-weight: 500;
}

.nav-menu {
  padding: 16px 0;
  margin: 0;
  flex: 1;
}

li {
  height: 50px;
  list-style-type: none;
  color: rgba(255, 255, 255, 0.65);
  display: flex;
  align-items: center;
  padding: 0 24px;
  margin: 4px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}

li i {
  margin-right: 10px;
  font-size: 18px;
}

li span {
  font-size: 14px;
}

li:hover {
  color: white;
  background-color: rgba(255, 255, 255, 0.1);
}

.active {
  color: white;
  background: #1890ff;
  position: relative;
}

.active::before {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: #1890ff;
}

.b-2 {
  flex: 1;
  background-color: white;
  border-radius: 8px;
  margin: 16px;
  padding: 24px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.nav-footer {
  padding: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.logout-button {
  width: 100%;
  padding: 10px;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  color: rgba(255, 255, 255, 0.65);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.logout-button i {
  margin-right: 8px;
  font-size: 16px;
}

.logout-button:hover {
  color: white;
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.1);
}

/* 添加响应式设计 */
@media screen and (max-width: 768px) {
  .b-1 {
    width: 80px;
  }
  
  .logo h2 {
    display: none;
  }
  
  li span {
    display: none;
  }
  
  li i {
    margin-right: 0;
    font-size: 20px;
  }
  
  .logout-button span {
    display: none;
  }
}

/* 主容器样式 */
.main-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #f0f2f5;
  overflow: hidden;
}

/* 顶部栏样式 */
.header {
  height: 64px;
  background: white;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  position: relative;
  z-index: 10;
}

.header-left h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 500;
  color: #1f2f3d;
}

.header-right {
  display: flex;
  align-items: center;
}

.user-dropdown {
  cursor: pointer;
  padding: 0 12px;
  display: flex;
  align-items: center;
  color: #5a5e66;
  transition: all 0.3s;
}

.user-dropdown:hover {
  color: #409EFF;
}

.user-dropdown i {
  margin-right: 8px;
}

/* 内容区域样式 */
.content-container {
  flex: 1;
  padding: 24px;
  overflow: auto;
}

.content-wrapper {
  background: white;
  border-radius: 4px;
  padding: 24px;
  min-height: 280px;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
}

/* 下拉菜单样式优化 */
:deep(.el-dropdown-menu) {
  padding: 4px 0;
}

:deep(.el-dropdown-menu__item) {
  padding: 8px 20px;
  display: flex;
  align-items: center;
}

:deep(.el-dropdown-menu__item i) {
  margin-right: 10px;
}

/* 响应式调整 */
@media screen and (max-width: 768px) {
  .header {
    padding: 0 12px;
  }

  .header-left h2 {
    font-size: 16px;
  }

  .content-container {
    padding: 12px;
  }

  .content-wrapper {
    padding: 16px;
  }

  .user-dropdown span:not(:first-child) {
    display: none;
  }
}

/* 滚动条美化 */
.content-container::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

.content-container::-webkit-scrollbar-thumb {
  background: #c0c4cc;
  border-radius: 3px;
}

.content-container::-webkit-scrollbar-track {
  background: #f0f2f5;
}
</style>
