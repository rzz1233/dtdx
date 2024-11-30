<template>
  <div id="app" class="app-background">
    <div class="container">
      <h1>{{ title }} </h1>

      <!-- 日期选择 -->
      <div class="date-picker">
        <input type="date" v-model="selectedDate" @change="fetchData" />
      </div>

      <!-- 会议列表 -->
      <div class="meeting-list">
        <h2>会议列表</h2>
        <table>
          <thead>
            <tr>
              <th>时间</th>
              <th>主题</th>
              <th>状态</th>
            </tr>
          </thead>
          <tbody>
            <template v-if="meetings.length > 0">
              <tr v-for="item in meetings" :key="item.id">
                <td>{{item.date}} - {{ item.starttime }} - {{ item.endtime }}</td>
                <td>{{ item.title }}</td>
                <td :class="item.status">{{ item.status }}</td>
              </tr>
            </template>
            <template v-else>
              <tr>
                <td colspan="3" class="no-meetings">暂无会议</td>
              </tr>
            </template>
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
      title: '会议列表',
      currentDate: '',
      selectedDate: '',
      meetings: []
    };
  },
  created() {
    this.getCurrentDate();
    this.selectedDate = this.currentDate;
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get('/api/meetinglist/');
        
        // 过滤选择日期的会议
        this.meetings = response.data.filter(item => {
          const meetingDate = item.date;
          return meetingDate === this.selectedDate;
        });

        // 按开始时间排序
        this.meetings.sort((a, b) => {
          const aStartTime = new Date(`${a.date} ${a.starttime}`);
          const bStartTime = new Date(`${b.date} ${b.starttime}`);
          return aStartTime - bStartTime;
        });

      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    getCurrentDate() {
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const day = String(today.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
    }
  }
};
</script>

<style scoped>
/* 背景样式 */
.app-background {
  background: linear-gradient(135deg, #e0f7fa, #80deea); /* 渐变背景 */
  height: 100vh; /* 使背景占满整个视口 */
}

/* 主容器样式 */
.container {
  background-image: url('../images/tu3.jpg'); /* 替换为您的背景图路径 */
  background-size: cover; /* 使背景图像覆盖整个容器 */
  background-position: center; /* 背景图像居中 */
  background-repeat: no-repeat; /* 不重复背景图像 */
  width: 85%; /* 宽度占据页面的 85% */
  height: 75vh; /* 高度占据页面的 75% */
  margin: 50px auto; /* 垂直居中 */
  padding: 30px; /* 内边距 */
  border: 2px solid #1abc9c; /* 边框颜色 */
  border-radius: 12px; /* 圆角边框 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* 增加阴影效果 */
  background-color: #ffffff; /* 背景颜色 */
  position: relative; /* 为伪元素提供定位 */
}

/* 标题样式 */
h1 {
  text-align: center;
  color: wheat;
  margin-bottom: 20px; /* 底部间距 */
  font-size: 28px; /* 增加字体大小 */
}

.date {
  font-size: 16px;
  color: white;
  margin-left: 10px;
}

/* 日期选择样式 */
.date-picker {
  text-align: center;
  margin: 20px 0; /* 上下间距 */
}

input[type="date"] {
  padding: 10px;
  font-size: 16px; /* 增加字体大小 */
}

/* 会议列表样式 */
.meeting-list {
  margin-top: 30px; /* 顶部间距 */
}

.meeting-list h2 {
  text-align: center;
  color: whitesmoke;
  font-size: 24px; /* 标题字体大小 */
  margin-bottom: 20px; /* 底部间距 */
}

/* 表格样式 */
table {
  width: 100%;
  border-collapse: collapse; /* 去掉表格的空隙 */
  margin-bottom: 20px;
}

thead th {
  background-color: #1abc9c;
  color: white;
  padding: 10px;
  text-align: left;
}

tbody td {
  padding: 10px;
  border-bottom: 1px solid #ddd; /* 下边框 */
}

tbody tr {
  background-color: #f9f9f9; /* 奇偶行的不同背景色 */
}

/* 状态样式 */
.ongoing {
  color: #e74c3c; /* 红色进行中 */
}

.upcoming {
  color: #f39c12; /* 橙色即将开始 */
}

.finished {
  color: #2ecc71; /* 绿色已结束 */
}

/* 暂无会议样式 */
.no-meetings {
  text-align: center; /* 内容居中 */
  color: #777; /* 灰色文本 */
  font-style: italic; /* 斜体 */
  padding: 20px; /* 内边距 */
}
</style>
