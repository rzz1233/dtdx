<template>
  <div v-show="visible" class="overlay">
    <div class="login-box">
      <h1>登录</h1>
      <input type="text" v-model="username" placeholder="请输入用户名" class="input-field">
      <input 
        v-model="password" 
        :type="passwordVisible ? 'text' : 'password'" 
        placeholder="请输入密码" 
        class="input-field">
      <button class="toggle-password" @click="togglePasswordVisibility">{{ passwordVisible ? '隐藏' : '显示' }}密码</button>
      <button class="login-button" @click="login">登录</button>
      <button class="cancel-button" @click="close">取消</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import apiClient from '@/view/api';
export default {
  props: {
    visible: Boolean
  },
  data() {
    return {
      username: '',
      password: '',
      passwordVisible: false, // 控制密码可见性
      errorMessage: '' ,// 错误信息
      datas:[],
      isLoggedIn: false,
    }
  },
  created() {
    this.fetchData(); // 调用数据获取方法
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get('/api/user/'); // 替换为你的 API 端点
        // console.log(response.data); // 检查返回的数据结构
        this.datas = response.data.results; // 假设返回的数据是用户数组
      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    close() {
      this.username = ''; // 清空用户名
      this.password = ''; // 清空密码
      this.errorMessage = ''; // 清空错误信息
      this.$emit('update:visible', false);
    },
    login() {
    if (this.username && this.password) {
      // 检查用户输入的用户名和密码是否在后端返回的用户数据中
      const data = this.datas.find(
        (d) => d.user === this.username && d.pwd === this.password
      );

      if (data) {
        // 如果找到了用户，则表示登录成功
        this.$emit('login-success'); // 触发登录成功事件
        this.close(); // 登录成功后关闭登录框
      } else {
        alert('用户名或密码错误'); // 错误提示
      }
    } else {
      alert('请输入用户名和密码'); // 输入检查
    }
  },
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    }
  }
};
</script>

<style scoped>
/* 模态窗口的遮罩层 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5); /* 半透明背景 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* 登录框样式 */
.login-box {
  background-color: #fff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* 阴影效果 */
  width: 400px;
  text-align: center;
  position: relative;
  z-index: 1001;
}

.login-box h1 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

.input-field {
  width: 100%;
  padding: 12px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.login-button, .cancel-button {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: 10px;
}

.login-button {
  background-color: #007bff;
}

.login-button:hover {
  background-color: #0056b3;
}

.cancel-button {
  background-color: #e57373;
}

.cancel-button:hover {
  background-color: #ef5350;
}

/* 错误信息样式 */
.error-message {
  color: red;
  margin-top: 10px;
}

/* 切换密码可见性按钮样式 */
.toggle-password {
  background: none;
  border: none;
  color: #007bff;
  cursor: pointer;
  margin-bottom: 10px;
}
</style>
