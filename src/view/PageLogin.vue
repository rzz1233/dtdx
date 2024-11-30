<template>
  <div id="app" class="login-container">
    <div class="login-box">
      <div class="login-header">
        <h2>会议管理系统</h2>
        <p>欢迎登录</p>
      </div>
      <div class="form-container">
        <div class="input-group">
          <i class="el-icon-user"></i>
          <input type="text" v-model="username" placeholder="请输入用户名" class="input-field" />
        </div>
        <div class="input-group">
          <i class="el-icon-lock"></i>
          <input type="password" v-model="password" placeholder="请输入密码" class="input-field" />
        </div>
        <button @click="login" class="login-button" :disabled="loading">
          {{ loading ? '登录中...' : '登录' }}
        </button>
        <div class="register-link">
          还没有账号？ <router-link to="/register">立即注册</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import apiClient from './api';

export default {
  data() {  
    return {
      username: '',
      password: '',
      loading: false,
    };
  },

  methods: {
    async login() {
      if (!this.username || !this.password) {
        alert('请输入用户名和密码');
        return;
      }

      this.loading = true;
      try {
        const response = await apiClient.post('/api/login1/', {
          username: this.username,
          password: this.password,
        });

        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        localStorage.setItem('is_superuser', response.data.is_superuser);

        if (response.data.is_superuser) {
          this.$router.push('/backstageview');
        } else {
          this.$router.push('/main');
        }
      } catch (error) {
        console.error('登录失败:', error);
        if (error.response) {
          if (error.response.status === 400) {
            alert('用户名或密码错误');
          } else {
            alert('登录失败，请重试');
          }
        } else {
          alert('网络错误，请检查连接');
        }
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #1890ff 0%, #001529 100%);
}

.login-box {
  width: 400px;
  padding: 40px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.login-header {
  text-align: center;
  margin-bottom: 40px;
}

.login-header h2 {
  margin: 0;
  color: #1f2f3d;
  font-size: 28px;
  font-weight: 500;
}

.login-header p {
  margin: 10px 0 0;
  color: #909399;
  font-size: 16px;
}

.form-container {
  margin-top: 20px;
}

.input-group {
  position: relative;
  margin-bottom: 20px;
}

.input-group i {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #909399;
  font-size: 18px;
}

.input-field {
  width: 100%;
  height: 45px;
  padding: 0 15px 0 40px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  color: #606266;
  transition: all 0.3s;
  box-sizing: border-box;
}

.input-field:focus {
  border-color: #409EFF;
  box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.2);
  outline: none;
}

.login-button {
  width: 100%;
  height: 45px;
  background: #409EFF;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 10px;
}

.login-button:hover {
  background: #66b1ff;
}

.login-button:disabled {
  background: #a0cfff;
  cursor: not-allowed;
}

.register-link {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #606266;
}

.register-link a {
  color: #409EFF;
  text-decoration: none;
  margin-left: 5px;
}

.register-link a:hover {
  color: #66b1ff;
}

/* 添加动画效果 */
.login-box {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 响应式设计 */
@media screen and (max-width: 480px) {
  .login-box {
    width: 90%;
    padding: 20px;
  }

  .login-header h2 {
    font-size: 24px;
  }
}
</style>
