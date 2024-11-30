import axios from 'axios';

// 定义基础 URL
const base_url = 'http://127.0.0.1:8000/';

// 创建 axios 实例
const apiClient = axios.create({
  baseURL: base_url,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 添加请求拦截器
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// // 添加响应拦截器
apiClient.interceptors.response.use(
  response => response, // 如果响应正常，直接返回响应
  async (error) => {
    const originalRequest = error.config;

    // 检查是否是401未授权错误
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true; // 标记请求为重试
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const response = await axios.post(`${base_url}api/token/refresh/`, { refresh: refreshToken });
        const newAccessToken = response.data.access;

        // 存储新的访问令牌
        localStorage.setItem('access_token', newAccessToken);
        
        // 更新请求头并重试请求
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
        return apiClient(originalRequest);
      } catch (refreshError) {
        console.error('刷新令牌失败:', refreshError);
        // 刷新令牌失败，处理错误或登出
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        // 重定向到登录页面
        window.location.href = '/login'; // 根据你的路由设置调整
      }
    }
    
    return Promise.reject(error);
  }
);

// 导出 apiClient 以便其他文件使用
export default apiClient;
