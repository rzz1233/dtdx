<template>
  <div id="app" class="app-background">
    <div class="container">
      <div class="header">
        <span class="current-date">{{ currentDate }}</span> 
        <h1>{{ title }}</h1>
        
      </div>
      <div class="button-group">
        <button class="large-button" @click="goToOrder">即将开始</button>
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
        <ul v-if="nextAppointments.length > 0">
          <li v-for="item in nextAppointments" :key="item.id">
            <i class="el-icon-time"></i>  {{item.date}} - {{ item.starttime }} - {{ item.endtime }} --- <i class="el-icon-suitcase"></i> {{ item.title }} --- <i class="el-icon-user-solid"></i> {{ item.dept_info.name }} --- <i class="el-icon-success"></i>{{ item.status }}
          </li>
          </ul>
        <ul v-else>
          <li>今日暂无预约</li>
        </ul> 
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from './api';
import LoginFrom from '../components/LoginFrom.vue';
import AddMeeting from '../components/AddMeeting.vue';

export default {
  data() {
    return {
      title: '会议室',
      isShow: false,             // 登录框显示状态
      isShowMeetingForm: false,  // 会议预约窗口显示状态
      nextAppointments: [],       // 下一预约的示例数据
      currentDate: '',            // 当前日期
      currentTime: '',            // 当前时间
      currentMeetingTitle: ''      // 当前会议的标题
    };
  },
  components: {
    LoginFrom,
    AddMeeting
  },
  created() {
    this.fetchData(); // 调用数据获取方法
    this.setCurrentDate(); // 设置当前日期
    this.setCurrentTime(); // 设置当前时间
  },
  methods: {
    async fetchData() {
    try {
      const response = await apiClient.get('/api/meetinglist/'); // 替换为你的 API 端点
      const allAppointments = response.data; // 假设返回的数据是预约列表

      // 过滤出与当前日期相同且在当前时间之后的预约
      this.nextAppointments = allAppointments.filter(item => {
        const appointmentDate = item.date; // 预约日期
        const appointmentStartTime = item.starttime; // 预约开始时间
        return (
          appointmentDate === this.currentDate && // 日期相同
          appointmentStartTime > this.currentTime // 开始时间在当前时间之后
        );
      });

      // 按开始时间排序
      this.nextAppointments.sort((a, b) => {
        const startA = new Date(`${a.date}T${a.starttime}`); // 预约 A 的开始时间
        const startB = new Date(`${b.date}T${b.starttime}`); // 预约 B 的开始时间
        return startA - startB; // 从小到大排序
      });

      // 设置标题为下一预约的第一个会议的标题
      if (this.nextAppointments.length > 0) {
        this.title = this.nextAppointments[0].title;
      } else {
        this.title = '暂无预约';
      }

    } catch (error) {
      console.error('获取数据失败:', error);
    }
  },
    setCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份从 0 开始，所以加 1
      const day = String(date.getDate()).padStart(2, '0'); // 确保日数是两位数
      this.currentDate = `${year}-${month}-${day}`; // 设置当前日期为 YYYY-MM-DD 格式
    },
    setCurrentTime() {
      const date = new Date();
      const hours = String(date.getHours()).padStart(2, '0'); // 确保小时是两位数
      const minutes = String(date.getMinutes()).padStart(2, '0'); // 确保分钟是两位数
      this.currentTime = `${hours}:${minutes}`; // 设置当前时间为 HH:MM 格式
    },
    goToOrder() {
      this.$router.push('/main/page2'); // 跳转到详情页面
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
  background: linear-gradient(135deg, #e0f7fa, #80deea); /* 渐变背景 */
  height: 100vh; /* 使背景占满整个视口 */
}

/* 主容器样式 */
.container {
  background-image: url('../images/tu2.jpg'); /* 替换为您的背景图路径 */
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

/* 头部样式 */
.header {
  display: flex;
  flex-direction: column; /* 使标题和日期垂直排列 */
  align-items: center; /* 水平居中 */
  margin-bottom: 20px;
}

/* 标题样式 */
h1 {
  text-align: center; /* 水平居中 */
  color: #333;
  font-size: 40px; /* 增加字体大小 */
  margin: 0; /* 去掉默认的外边距 */
}

/* 当前日期样式 */
.current-date {
  font-size: 24px; /* 调整字体大小 */
  margin-top: 10px; /* 给日期和标题增加间距 */
}

/* 按钮组样式 */
.button-group {
  display: flex; /* 使用 flex 布局 */
  justify-content: center; /* 按钮居中 */
  margin-bottom: 20px; /* 底部间距 */
}

/* 预约按钮样式 */
.reservation-buttons {
  display: flex; /* 使用 flex 布局 */
  justify-content: center; /* 按钮居中 */
  gap: 20px; /* 按钮之间的间隔 */
}

/* 下一预约样式 */
.next-appointments {
  margin-top: 30px; /* 顶部间距 */
}

.next-appointments h2 {
  text-align: center;
  color: #333;
  font-size: 24px; /* 标题字体大小 */
  margin-bottom: 10px; /* 底部间距 */
}

ul {
  padding: 0;
  list-style-type: none; /* 去掉默认样式 */
}

li {
  padding: 10px;
  background-color: #f1f1f1; /* 背景颜色 */
  margin-bottom: 10px; /* 底部间距 */
  border-radius: 5px; /* 圆角 */
}

/* 按钮样式 */
button {
  padding: 12px 24px; /* 增加内边距 */
  background-color: blue;
  color: white;
  border: none;
  border-radius: 6px; /* 圆角 */
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease; /* 添加过渡效果 */
}

/* 大按钮样式 */
.large-button {
  padding: 20px 40px; /* 增加尺寸 */
  background-color: orange; /* 显眼的颜色 */
  font-size: 18px; /* 增加字体大小 */
  font-weight: bold;
}

/* 按钮悬停效果 */
button:hover {
  background-color: #16a085;
  transform: scale(1.05); /* 悬停时的放大效果 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* 增加悬停时的阴影效果 */
}

/* 添加边框内部的背景效果 */
.container::before {
  content: ""; /* 必须添加内容才能显示伪元素 */
  position: absolute; /* 绝对定位 */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  /* background: rgba(245, 245, 245, 0.8); 背景颜色和透明度 */
  border-radius: 10px; /* 圆角 */
  z-index: 0; /* 确保在内容下面 */
}

h1, .button-group, .reservation-buttons, .next-appointments {
  position: relative; /* 确保标题和按钮组位于伪元素之上 */
  z-index: 1; /* 提升 z-index 使其在背景上方 */
}
</style>
