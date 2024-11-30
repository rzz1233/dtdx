<template>
  <div id="app" class="app-background">
    <div class="container">
      <h1>
        {{ title }} <span class="current-date">{{ currentDate }}</span>
      </h1>
      <div class="button-group">
        <!-- 根据会议状态动态改变按钮文本和样式 -->
        <button class="large-button" :class="{'in-use': isMeetingInProgress}" @click="goToOrder">
          {{ isMeetingInProgress ? '正在使用中' : '空闲中' }}
        </button>
      </div>

      <div class="reservation-buttons">
        <button @click="isShow = true">预约会议</button>
        <button @click="viewMoreReservations">更多预约</button>
      </div>

      <!-- 登录框组件 -->
      <LoginFrom :visible.sync="isShow" @login-success="showMeetingForm" />

      <!-- 预约会议组件 -->
      <AddMeeting :visible.sync="isShowMeetingForm" />

      <!-- 下一预约列表 -->
      <div class="next-appointments">
        <h2>下一预约</h2>
        <ul>
          <li v-if="nextAppointments.length === 0">今日暂无预约</li>
          <li v-for="item in nextAppointments" :key="item.id">
            <i class="el-icon-time"></i> {{ item.date }} - {{ item.starttime }} - {{ item.endtime }} --- 
            <i class="el-icon-suitcase"></i> {{ item.title }} --- 
            <i class="el-icon-user-solid"></i> {{ item.dept_info.name }} --- 
            <i class="el-icon-success"></i> {{ item.status }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/icon.css';
import apiClient from './api';
import LoginFrom from '../components/LoginFrom.vue';
import AddMeeting from '../components/AddMeeting.vue';

export default {
  data() {
    return {
      title: '会议室',
      isShow: false,              // 登录框显示状态
      isShowMeetingForm: false,   // 会议预约窗口显示状态
      nextAppointments: [],       // 下一预约的示例数据
      currentDate: '',            // 当前日期
      currentTime: '',            // 当前时间
      isMeetingInProgress: false  // 判断是否有正在进行中的会议
    };
  },
  components: {
    LoginFrom,
    AddMeeting,
  },
  created() {
    this.fetchData(); // 调用数据获取方法
    this.setCurrentDate(); // 设置当前日期
    this.setCurrentTime(); // 设置当前时间
    this.checkMeetingStatus(); // 检查是否有进行中的会议
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get('/api/meetinglist/'); // 替换为你的 API 端点
        const allAppointments = response.data;
        console.log(allAppointments)

        // 过滤出与当前日期相同且 starttime 在当前时间之后的预约
        this.nextAppointments = allAppointments.filter(item => {
          const appointmentDate = item.date;
          const appointmentStartTime = item.starttime;
          return (
            appointmentDate === this.currentDate && // 日期相同
            appointmentStartTime > this.currentTime // 开始时间在当前时间之后
          );
        });
      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    setCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
    },
    setCurrentTime() {
      const date = new Date();
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      this.currentTime = `${hours}:${minutes}`;
    },
    async checkMeetingStatus() {
      try {
        const response = await apiClient.get('/api/meetinglist/');
        const allAppointments = response.data;

        // 添加数据验证
        if (!Array.isArray(allAppointments)) {
          console.warn('返回的数据不是数组格式:', allAppointments);
          this.isMeetingInProgress = false;
          return;
        }

        // 检查是否有 status 为 "进行中" 的会议
        this.isMeetingInProgress = allAppointments.some(item => 
          item && 
          item.status === '进行中' && 
          item.date === this.currentDate
        );
      } catch (error) {
        console.error('检查会议状态失败:', error);
        this.isMeetingInProgress = false;
      }
    },
    goToOrder() {
      this.$router.push('/main/order'); // 跳转到详情页面
    },
    showMeetingForm() {
      this.isShowMeetingForm = true; // 显示会议预约窗口
    },
    viewMoreReservations() {
      this.$router.push('/main/list'); // 跳转到会议列表页面
    }
  }
};
</script>

<style scoped>
/* 背景样式 */
.app-background {
  background: linear-gradient(135deg, #e0f7fa, #80deea);
  height: 90vh;
}

/* 主容器样式 */
.container {
  background-image: url('../images/tu2.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 85%;
  height: 75vh;
  margin: 50px auto;
  padding: 30px;
  border: 2px solid #1abc9c;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  position: relative;
}

/* 按钮组样式 */
.button-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

/* 预约按钮样式 */
.reservation-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

/* 标题样式 */
h1 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
  font-size: 40px;
}

/* 当前日期样式 */
.current-date {
  margin-left: 10px;
  font-size: 24px;
}

/* 下一预约样式 */
.next-appointments {
  margin-top: 30px;
}

.next-appointments h2 {
  text-align: center;
  color: #333;
  font-size: 24px;
  margin-bottom: 10px;
}

ul {
  padding: 0;
  list-style-type: none;
}

li {
  padding: 10px;
  background-color: #f1f1f1;
  margin-bottom: 10px;
  border-radius: 5px;
}

/* 按钮样式 */
button {
  padding: 12px 24px;
  background-color: blue;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
}

/* "空闲中"按钮变大、加醒目样式 */
.large-button {
  padding: 20px 40px;
  background-color: #1abc9c;
  font-size: 18px;
  font-weight: bold;
}

.large-button.in-use {
  background-color: red; /* 使用中的按钮背景色 */
}

/* 按钮悬停效果 */
button:hover {
  background-color: #16a085;
  transform: scale(1.05);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
</style>
