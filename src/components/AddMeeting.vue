<template>
  <!-- 模态窗口 -->
  <div v-show="visible" class="overlay">
    <div class="meeting-form">
      <!-- 关闭窗口按钮 -->
      <span class="close-button" @click="closeWindow">✖</span>
      <!-- 表单标题 -->
      <h2 class="form-title">会议预约</h2>

      <!-- 会议预约表单 -->
      <form @submit.prevent="submitForm">

        <!-- 选择会议日期 -->
        <div class="form-item">
          <label for="date">选择日期:</label>
          <input type="date" id="date" v-model="value1" required />
        </div>

        <!-- 会议开始时间 -->
        <div class="form-item">
          <label for="startTime">开始时间:</label>
          <input type="time" id="startTime" v-model="form.startTime" required />
        </div>

        <!-- 会议结束时间 -->
        <div class="form-item">
          <label for="endTime">结束时间:</label>
          <input type="time" id="endTime" v-model="form.endTime" required />
        </div>

        <!-- 会议主题 -->
        <div class="form-item">
          <label for="topic">会议主题:</label>
          <input type="text" id="topic" v-model="form.topic" placeholder="请输入会议主题" required />
        </div>

        <!-- 参会部门（单选） -->
        <div class="form-item">
          <label for="departments">参会部门:</label>
          <select v-model="form.department" id="departments" required>
            <option value="" disabled>请选择部门</option>
            <option v-for="item in options" :key="item.id" :value="item.id">
              {{ item.name }}
            </option>
          </select>
        </div>

        <!-- 外部人员输入框 -->
        <div class="form-item">
          <label for="externalAttendee">外部人员:</label>
          <input type="text" id="externalAttendee" v-model="newExternalAttendee" placeholder="请输入外部人员" />
          <button type="button" @click="addExternalAttendee">添加</button>
          <ul v-if="form.externalAttendees.length">
            <li v-for="(attendee, index) in form.externalAttendees" :key="index">
              {{ attendee }} <button type="button" @click="removeExternalAttendee(index)">删除</button>
            </li>
          </ul>
        </div>

        <!-- 提交和重置按钮 -->
        <div class="form-item">
          <button type="button" @click="resetForm" class="cancel-button">取消</button>
          <button type="submit" class="submit-button">预约</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
import apiClient from '@/view/api';

export default {
  props: {
    visible: Boolean,
  },
  data() {
    return {
      form: {
        startTime: '',
        endTime: '',
        topic: '',
        department: '',
        externalAttendees: [],
      },
      newExternalAttendee: '',
      options: [],
      value1: '', // 会议日期
    };
  },
  created() {
    this.fetchData(); // 调用数据获取方法
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get('/api/dept/');
        this.options = response.data;
      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    closeWindow() {
      this.$emit('update:visible', false);
    },
    resetForm() {
      this.form.startTime = '';
      this.form.endTime = '';
      this.form.topic = '';
      this.form.department = '';
      this.newExternalAttendee = '';
      this.form.externalAttendees = [];
    },
    async checkTimeConflict() {
      try {
        const response = await apiClient.get('/api/meetinglist/check_time_conflict/', {
          params: {
            date: this.value1,
            starttime: this.form.startTime,
            endtime: this.form.endTime,
          },
        });
        return response.data.conflict; // 假设后端返回的数据包含 conflict 字段
      } catch (error) {
        console.error('检查时间冲突失败:', error);
        return false; // 出现错误时假设没有冲突
      }
    },
    async submitForm() {
      // 基本验证
      if (!this.value1 || !this.form.startTime || !this.form.endTime || !this.form.topic) {
        alert('请填写完整信息');
        return;
      }

      // 获取当前时间
      const now = new Date();
      const currentDate = now.toISOString().split('T')[0]; // 获取当前日期 YYYY-MM-DD
      const currentTime = now.toTimeString().slice(0, 8); // 获取当前时间 HH:mm:ss

      // 检查日期是否是过去的日期
      if (this.value1 < currentDate) {
        alert('不能预约过去的日期');
        return;
      }

      // 如果是当天，检查时间是否是过去的时间
      if (this.value1 === currentDate && this.form.startTime < currentTime) {
        alert('不能预约过去的时间');
        return;
      }

      // 检查结束时间是否晚于开始时间
      if (this.form.endTime <= this.form.startTime) {
        alert('结束时间必须晚于开始时间');
        return;
      }

      // 检查时间冲突
      const hasConflict = await this.checkTimeConflict();
      if (hasConflict) {
        alert('所选时间与已有会议冲突，请选择其他时间。');
        return;
      }

      try {
        const response = await apiClient.post('/api/meetinglist/', {
          date: this.value1,
          starttime: this.form.startTime,
          endtime: this.form.endTime,
          title: this.form.topic,
          dept: this.form.department,
          outpeople: this.form.externalAttendees.join(','),
          status: '未开始',
        });

        console.log('响应数据:', response.data);
        this.$emit('add');
        alert('会议预约成功');
        this.resetForm();
        this.closeWindow();
      } catch (error) {
        console.error('提交表单失败:', error);
        alert('预约失败，请稍后重试');
      }
    },
    addExternalAttendee() {
      if (this.newExternalAttendee) {
        if (!this.form.externalAttendees.includes(this.newExternalAttendee)) {
          this.form.externalAttendees.push(this.newExternalAttendee);
          alert(`外部人员 ${this.newExternalAttendee} 已添加`);
          this.newExternalAttendee = '';
        } else {
          alert('该外部人员已存在');
        }
      } else {
        alert('请输入外部人员');
      }
    },
    removeExternalAttendee(index) {
      this.form.externalAttendees.splice(index, 1);
    },
  },
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
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* 会议表单样式 */
.meeting-form {
  width: 450px;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  position: relative;
}

/* 关闭按钮样式 */
.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 24px;
  color: #999;
  cursor: pointer;
}

.close-button:hover {
  color: #ff4d4f;
}

/* 表单标题样式 */
.form-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

/* 输入框和选择框样式 */
input[type="text"],
input[type="date"],
input[type="time"],
select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 按钮样式 */
.submit-button,
.cancel-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button {
  background-color: #007bff;
  color: #fff;
}

.submit-button:hover {
  background-color: #0056b3;
}

.cancel-button {
  background-color: #f0f0f0;
  color: #333;
}

.cancel-button:hover {
  background-color: #e0e0e0;
}

/* 外部人员列表样式 */
ul {
  padding-left: 20px;
  list-style-type: disc;
}

ul li {
  margin: 5px 0;
}

ul li button {
  background: transparent;
  border: none;
  color: red;
  cursor: pointer;
}

ul li button:hover {
  text-decoration: underline;
}
</style>
