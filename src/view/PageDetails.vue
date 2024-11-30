<template>
    <div id="app" class="app-background">
      <div class="container">
          <h1>{{ title }} <span class="date">{{ currentDate }}</span></h1>
          <button class="refresh-button" @click="addDate">请点击刷新会议详情</button>

          <!-- 会议详情列表 -->
          <div class="meeting-details">
              <h2>会议详情</h2>
              <template v-if="attendeelist.length > 0">
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
                          <tr v-for="item in attendeelist" :key="item.id">
                              <td>{{ item.meetname }}</td>
                              <td>{{ item.user }}</td>
                              <td>{{ item.meetdate }}</td>
                              <td>{{ item.check_time }}</td>
                              <td>
                                  <button 
                                      :class="item.status === '签到' ? 'absent' : 'checked-in'" 
                                      @click="checkIn(item)" 
                                      :disabled="item.status !== '签到'">
                                      {{ item.status }}
                                  </button>
                              </td>
                          </tr>
                      </tbody>
                  </table>
              </template>
              <p v-else class="no-meetings">请点击刷新会议详情</p>
          </div>
      </div>
      <LoginFrom1 :visible.sync="isShow" @loginSuccess="handleLoginSuccess"></LoginFrom1>
  </div>
</template>

<script>
import apiClient from './api';
import LoginFrom1 from '@/components/LoginFrom-1.vue';

export default {
  data() {
      return {
          title: '会议详情', // 组件标题
          currentDate: '', // 当前日期
          meetingdata: [], 
          users: [], // 用户列表
          attendeelist: [], // 签到列表
          isShow:false,
          isLoggedIn:false,
      };
  },
  components: {
    LoginFrom1,
   
  },
  created() {
      // 组件创建时调用的方法
      this.getCurrentDate(); // 获取当前日期
      this.fetchData(); // 获取会议数据
      this.deptData(); // 获取用户数据
      this.attendeeData(); // 获取签到记录
  },
  methods: {
      async fetchData() {
          try {
              //获取会议信息
              const response = await apiClient.get('/api/meetinglist/');
              this.meetingdata = response.data; 
          } catch (error) {
              console.error('获取数据失败:', error); // 错误处理
          }
      },
      async deptData() {
          try {
              // 获取用户数据
              const response = await apiClient.get('/api/user/');
              this.users = response.data.results; // 保存用户数据
          } catch (error) {
              console.error('获取数据失败:', error); // 错误处理
          }
      },

      async addDate() {
          try {
              // 获取当前已签到用户的信息
              const existingAttendees = this.attendeelist.filter(item => item.status === '已签到');

              // 删除所有签到记录
              await apiClient.delete('/api/attendee/all/');

              // 重新添加签到记录
              for (const meeting of this.meetingdata) {
                  const usersInDept = this.getFilteredUsers(meeting.dept_info.name);
                  for (const user of usersInDept) {
                      // 检查该用户是否已经签到
                      const alreadyCheckedIn = existingAttendees.some(item => item.user === user.name && item.meetname === meeting.title);
                      if (!alreadyCheckedIn) {
                          // 如果未签到，添加新记录
                          try {
                              await apiClient.post('/api/attendee/', {
                                  meetname: meeting.title, // 会议名称
                                  user: user.name, // 用户名称
                                  meetdate: meeting.date, // 会议日期
                                  check_time: meeting.starttime, // 签到时间
                                  status: "签到" // 初始签到状态
                              });
                          } catch (error) {
                              console.error('添加失败:', error); // 错误处理
                          }
                      } else {
                          // 如果该用户已经签到，保持其原有状态
                          const existingAttendee = existingAttendees.find(item => item.user === user.name && item.meetname === meeting.title);
                          await apiClient.post('/api/attendee/', {
                              meetname: existingAttendee.meetname,
                              user: existingAttendee.user,
                              meetdate: existingAttendee.meetdate,
                              check_time: existingAttendee.check_time,
                              status: existingAttendee.status // 保持原有状态
                          });
                      }
                  }
              }

              // 重新获取签到记录以更新attendeelist
              await this.attendeeData(); // 确保更新视图
          } catch (error) {
              console.error('操作失败:', error); // 错误处理
          }
      },

      async attendeeData() {
        try {
            // 获取签到记录
            const response = await apiClient.get('/api/attendee/');
            const allAttendees = response.data; // 获取所有签到记录

            // 筛选出会议日期为当前日期的签到记录
            this.attendeelist = allAttendees.filter(item => item.meetdate === this.currentDate);

            // 对attendeelist按签到时间排序
            this.attendeelist.sort((a, b) => {
                const dateA = new Date(`${a.meetdate}T${a.check_time}`); // 创建日期对象
                const dateB = new Date(`${b.meetdate}T${b.check_time}`); // 创建日期对象
                return dateA - dateB; // 从近到远排序
            });
        } catch (error) {
            console.error('获取数据失败:', error); // 错误处理
        }
    },
    handleLoginSuccess() {
        this.isShow = false; // 隐藏登录窗口
        this.isLoggedIn = true; // 设置登录状态为已登录
    },


    async checkIn(item) {
    if (!this.isLoggedIn) { // 如果用户未登录
        this.isShow = true; // 显示登录窗口
        return; // 暂停签到操作
    }
    try {
        // 用户已经登录，更新签到状态为“已签到”
        const response = await apiClient.put(`/api/attendee/${item.id}/`, {
            ...item, // 保留其他信息
            status: "已签到" // 更新签到状态
        });
        console.log('签到成功:', response);
        // 更新本地数据
        item.status = '已签到'; // 更新状态
    } catch (error) {
        console.error('签到失败:', error); // 错误处理
    }
},


      getCurrentDate() {
          // 获取当前日期并格式化为YYYY-MM-DD
          const today = new Date();
          const year = today.getFullYear();
          const month = String(today.getMonth() + 1).padStart(2, '0');
          const day = String(today.getDate()).padStart(2, '0');
          this.currentDate = `${year}-${month}-${day}`; // 更新当前日期
      },

      getFilteredUsers(dept) {
          // 根据部门过滤用户
          return this.users.filter(user => user.dept_info.name === dept);
      }
  }
};
</script>

<style scoped>
/* 背景样式 */
.app-background {
  background: linear-gradient(135deg, #e0f7fa, #80deea);
  height: 100vh; /* 高度设置为视口高度 */
}

/* 主容器样式 */
.container {
  background-image: url('../images/tu4.jpg');
  background-size: cover; /* 背景图像覆盖容器 */
  background-position: center; /* 背景图像居中 */
  background-repeat: no-repeat; /* 不重复背景图像 */
  width: 85%; /* 容器宽度 */
  height: 75vh; /* 容器高度 */
  margin: 50px auto; /* 垂直居中 */
  padding: 20px; /* 内边距 */
  border: 2px solid #1abc9c; /* 边框样式 */
  border-radius: 12px; /* 圆角 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  background-color: rgba(255, 255, 255, 0.9); /* 背景颜色 */
  display: flex; /* 使用弹性布局 */
  flex-direction: column; /* 垂直方向布局 */
  justify-content: space-between; /* 子元素均匀分布 */
}

/* 标题样式 */
h1 {
  text-align: center; /* 标题居中 */
  color: wheat; /* 标题颜色 */
  margin-bottom: 10px; /* 下外边距 */
  font-size: 28px; /* 字体大小 */
}

.date {
  font-size: 16px; /* 日期字体大小 */
  color: white; /* 日期颜色 */
}

/* 刷新按钮样式 */
.refresh-button {
  font-size: 14px; /* 调整字体大小 */
  padding: 5px 10px; /* 调整内边距 */
  background-color: #1abc9c; /* 背景颜色 */
  color: white; /* 文字颜色 */
  border: none; /* 去掉边框 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标指针样式 */
  margin-bottom: 10px; /* 增加底部间距 */
  transition: background-color 0.3s ease; /* 添加过渡效果 */
}

.refresh-button:hover {
  background-color: #16a085; /* 悬停时颜色变化 */
}

/* 会议详情列表样式 */
.meeting-details {
  margin-top: 10px; /* 上外边距 */
  flex-grow: 1; /* 允许扩展以填充容器 */
  overflow-y: auto; /* 允许垂直滚动 */
}

.meeting-details h2 {
  text-align: center; /* 标题居中 */
  color: whitesmoke; /* 标题颜色 */
  font-size: 24px; /* 字体大小 */
  margin-bottom: 20px; /* 下外边距 */
}

/* 表格样式 */
table {
  width: 100%; /* 表格宽度 */
  border-collapse: collapse; /* 合并边框 */
  margin-bottom: 20px; /* 下外边距 */
}

thead th {
  background-color: #1abc9c; /* 表头背景颜色 */
  color: white; /* 表头文字颜色 */
  padding: 10px; /* 内边距 */
  text-align: left; /* 左对齐 */
}

tbody td {
  padding: 10px; /* 内边距 */
  border-bottom: 1px solid #ddd; /* 下边框 */
}

tbody tr {
  background-color: #f9f9f9; /* 行背景颜色 */
}

/* 签到状态按钮样式 */
button {
  padding: 10px 20px; /* 增加内边距 */
  border: none; /* 去掉边框 */
  border-radius: 8px; /* 增加圆角 */
  cursor: pointer; /* 鼠标指针样式 */
  color: white; /* 文字颜色设置为白色 */
  font-weight: bold; /* 加粗文字 */
  transition: background-color 0.3s ease, transform 0.2s ease; /* 添加平滑过渡效果 */
}

/* 已签到状态 */
.checked-in {
  background-color: #2ecc71; /* 绿色已签到 */
}

.checked-in:hover {
  background-color: #27ae60; /* 悬停时稍微加深绿色 */
  transform: scale(1.05); /* 悬停时放大 */
}

/* 未签到状态 */
.absent {
  background-color: #e74c3c; /* 红色未签到 */
}

.absent:hover {
  background-color: #c0392b; /* 悬停时稍微加深红色 */
  transform: scale(1.05); /* 悬停时放大 */
}

/* 按钮的禁用状态 */
button:disabled {
  background-color: #95a5a6; /* 灰色禁用状态 */
  cursor: not-allowed; /* 鼠标指针样式为不可用 */
}

.no-meetings {
  text-align: center;
  color: #e74c3c;
  font-size: 18px;
  margin-top: 20px;
}
</style>
