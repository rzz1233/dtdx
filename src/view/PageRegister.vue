<template>
  <div id="app" class="register-container">
    <div class="register-box">
      <div class="register-header">
        <h2>会议管理系统</h2>
        <p>用户注册</p>
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
        <div class="input-group">
          <i class="el-icon-lock"></i>
          <input type="password" v-model="confirmPassword" placeholder="请确认密码" class="input-field" />
        </div>
        <button @click="register" class="register-button" :disabled="loading">
          {{ loading ? '注册中...' : '注册' }}
        </button>
        <div class="login-link">
          已有账号？ <router-link to="/login">立即登录</router-link>
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
      username: '',
      password: '',
      confirmPassword: '',
      loading: false,
    };
  },
  methods: {
    async register() {
      if (!this.username || !this.password || !this.confirmPassword) {
        alert('请填写所有字段');
        return;
      }
      if (this.password !== this.confirmPassword) {
        alert('两次输入的密码不匹配');
        return;
      }

      this.loading = true;
      try {
        const response = await apiClient.post('/api/register1/', {
          username: this.username,
          password: this.password,
        });
        console.log(response.data);
        alert('注册成功，请登录');
        this.$router.push('/login');
      } catch (error) {
        if (error.response && error.response.status === 400) {
          alert(error.response.data.error);
        } else {
          alert('注册失败，请重试');
        }
        console.error('注册失败:', error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #1890ff 0%, #001529 100%);
}

.register-box {
  width: 400px;
  padding: 40px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.register-header {
  text-align: center;
  margin-bottom: 40px;
}

.register-header h2 {
  margin: 0;
  color: #1f2f3d;
  font-size: 28px;
  font-weight: 500;
}

.register-header p {
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

.register-button {
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

.register-button:hover {
  background: #66b1ff;
}

.register-button:disabled {
  background: #a0cfff;
  cursor: not-allowed;
}

.login-link {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #606266;
}

.login-link a {
  color: #409EFF;
  text-decoration: none;
  margin-left: 5px;
}

.login-link a:hover {
  color: #66b1ff;
}

/* 添加动画效果 */
.register-box {
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
  .register-box {
    width: 90%;
    padding: 20px;
  }

  .register-header h2 {
    font-size: 24px;
  }
}
</style>
