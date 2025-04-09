<template>
    <div id="app" class="app-background">
      <div class="container">
          <h1>会议详情 <span class="date">{{ currentDate }}</span></h1>
          
          <!-- 会议详情列表 -->
          <div class="meeting-details">
              <h2>会议详情</h2>
              <table>
                  <thead>
                      <tr>
                          <th>会议名称</th>
                          <th>参会人员</th>
                          <th>会议日期</th>
                          <th>会议时间</th>
                          <th>签到状态</th>
                      </tr>
                  </thead>
                  <tbody>
                      <tr v-if="qiandaoList.length === 0">
                          <td colspan="5">
                              <p class="loading-text">加载会议数据中...</p>
                          </td>
                      </tr>
                      <tr v-for="(item, index) in qiandaoList" :key="index">
                          <td>{{ item.meetname }}</td>
                          <td>{{ item.user }}</td>
                          <td>{{ item.meetdate }}</td>
                          <td>{{ item.check_time }}</td>
                          <td>
                              <button 
                                  :class="{'checked-in': item.status === '已签到'}"
                                  :disabled="item.status === '未签到'"
                                  @click="handleCheckIn(item)">
                                  {{ item.status }}
                              </button>
                          </td>
                      </tr>
                  </tbody>
              </table>
          </div>
      </div>
  </div>
</template>

<script>
import apiClient from './api';

export default {
  data() {
      return {
          currentDate: '',
          qiandaoList: [] // 新增签到数据列表
      };
  },
  created() {
      this.getCurrentDate();
      this.fetchQiandaoData(); // 新增数据获取
  },
  methods: {
      getCurrentDate() {
          const today = new Date();
          const year = today.getFullYear();
          const month = String(today.getMonth() + 1).padStart(2, '0');
          const day = String(today.getDate()).padStart(2, '0');
          this.currentDate = `${year}-${month}-${day}`;
      },
      // 新增数据获取方法
      async fetchQiandaoData() {
          try {
              const response = await apiClient.get('/api/qiandao/', {
                  params: {
                      date: this.currentDate
                  }
              });
              this.qiandaoList = response.data;
          } catch (error) {
              console.error('获取签到数据失败:', error);
          }
      },
      // 修改后的签到处理方法
      handleCheckIn(item) {
          // 直接更新本地数据状态
          this.qiandaoList = this.qiandaoList.map(i => {
              if (i.meetname === item.meetname && i.user === item.user) {
                  return { ...i, status: "已签到" };
              }
              return i;
          });
      }
  }
};
</script>

<style scoped>
/* 优化后的背景样式 */
.app-background {
  background: linear-gradient(135deg, #e3f2fd, #bbdefb);
  min-height: 100vh;
}

/* 增强容器视觉效果 */
.container {
  background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.98)), 
                    url('../images/tu4.jpg');
  backdrop-filter: blur(2px);
  box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
}

/* 优化标题样式 */
h1 {
  font-size: 2.2rem;
  color: #2c3e50;
  text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
  padding: 15px 0;
  border-bottom: 2px solid #1abc9c;
}

.date {
  font-size: 1.1rem;
  color: #7f8c8d;
  margin-left: 10px;
}

/* 增强表格视觉效果 */
table {
  border: 1px solid #ecf0f1;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

thead th {
  background: linear-gradient(145deg, #1abc9c, #16a085);
  font-weight: 600;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:nth-child(even) {
  background-color: #f8f9fa;
}

tbody tr:hover {
  background-color: #f1f8ff;
}

/* 优化按钮样式 */
button {
  min-width: 80px;
  padding: 8px 16px;
  border-radius: 20px;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

button.checked-in {
  background: linear-gradient(145deg, #2ecc71, #27ae60);
}

button:not(.checked-in) {
  background: linear-gradient(145deg, #e74c3c, #c0392b);
}

button:disabled {
  background: linear-gradient(145deg, #95a5a6, #7f8c8d) !important;
  cursor: not-allowed;
  opacity: 0.7;
}

button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* 新增加载状态样式 */
.loading-text {
  text-align: center;
  color: #7f8c8d;
  font-size: 1.1rem;
  padding: 20px;
}
</style>
