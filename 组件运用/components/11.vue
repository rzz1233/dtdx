<template>
    <div v-show="visible" class="overlay">
      <div class="meeting-form">
        <span class="close-button" @click="closeWindow">✖</span>
        <h2 class="form-title">会议预约</h2>
        <el-form ref="form" :model="form" label-width="100px" label-position="right">
          <!-- 会议开始和结束时间 -->
          <el-form-item label="会议时间" prop="startTime">
            <div class="meeting-time">
              <el-time-picker
                v-model="form.startTime"
                placeholder="请选择开始时间（HH:mm）"
                format="HH:mm"
                style="width: 130px; margin-right: 10px;"
                clearable
                class="time-picker"
                :picker-options="timePickerOptions"
              ></el-time-picker>
              <span class="time-separator">-</span>
              <el-time-picker
                v-model="form.endTime"
                placeholder="请选择结束时间（HH:mm）"
                format="HH:mm"
                style="width: 130px; margin-left: 10px;"
                clearable
                class="time-picker"
                :picker-options="timePickerOptions"
              ></el-time-picker>
            </div>
          </el-form-item>
  
          <!-- 会议主题 -->
          <el-form-item label="会议主题" prop="topic">
            <el-input v-model="form.topic" placeholder="请输入会议主题" class="input-field"></el-input>
          </el-form-item>
  
          <!-- 参会人员 -->
          <el-form-item label="参会人员">
            <el-select v-model="form.attendees" placeholder="请选择" multiple style="width: 100%" class="attendee-select">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
  
          <!-- 外部人员 -->
          <el-form-item label="外部人员">
            <el-input v-model="newExternalAttendee" placeholder="请输入外部人员" class="input-field"></el-input>
            <el-button icon="el-icon-plus" circle @click="addExternalAttendee"></el-button>
          </el-form-item>
  
          <!-- 按钮 -->
          <el-form-item>
            <el-button @click="resetForm" plain class="cancel-button">取消</el-button>
            <el-button type="primary" @click="submitForm" class="submit-button">预约</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: Boolean
    },
    data() {
      return {
        form: {
          startTime: '',
          endTime: '',
          topic: '',
          attendees: [],
          externalAttendees: []
        },
        newExternalAttendee: '',
        options: [
          { value: '张三', label: '张三' },
          { value: '李四', label: '李四' },
          { value: '王五', label: '王五' }
        ],
        timePickerOptions: {
          selectableRange: '00:00:00 - 23:59:59' // 设置可选择的时间范围
        }
      };
    },
    methods: {
      closeWindow() {
        this.$emit('update:visible', false);
      },
      resetForm() {
        this.$refs.form.resetFields();
        this.newExternalAttendee = '';
        this.form.externalAttendees = []; // 清空外部人员
      },
      submitForm() {
        if (!this.validateTimeFormat(this.form.startTime) || !this.validateTimeFormat(this.form.endTime)) {
          this.$message.warning('请确保时间格式为 HH:mm');
          return;
        }
        console.log('提交的表单数据:', this.form);
        this.$message.success('会议预约成功');
        this.closeWindow(); // 预约成功后关闭窗口
      },
      addExternalAttendee() {
        if (this.newExternalAttendee) {
          if (!this.form.externalAttendees.includes(this.newExternalAttendee)) {
            this.form.externalAttendees.push(this.newExternalAttendee);
            this.$message.success(`外部人员 ${this.newExternalAttendee} 已添加`);
            this.newExternalAttendee = ''; // 清空输入框
          } else {
            this.$message.warning('该外部人员已存在');
          }
        } else {
          this.$message.warning('请输入外部人员');
        }
      },
      validateTimeFormat(time) {
        const timeFormat = /^([01]\d|2[0-3]):([0-5]\d)$/; // 正则表达式
        return timeFormat.test(time);
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
  
  /* 增加组件阴影效果 */
  .meeting-form:hover {
    box-shadow: 0 6px 30px rgba(0, 0, 0, 0.3);
  }
  
  /* 输入框和选择框样式 */
  .input-field, .time-picker, .attendee-select {
    border-radius: 4px; /* 圆角边框 */
    transition: border-color 0.3s; /* 输入框的过渡效果 */
  }
  
  /* 输入框获得焦点时的样式 */
  .input-field:focus, .time-picker:focus, .attendee-select:focus {
    border-color: #007bff; /* 聚焦时边框颜色 */
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* 聚焦时阴影效果 */
  }
  
  /* 时间选择器分隔符样式 */
  .time-separator {
    font-size: 18px; /* 字体大小 */
    margin: 0 10px; /* 左右间距 */
    color: #666; /* 字体颜色 */
  }
  
  /* 提交按钮样式 */
  .submit-button {
    background-color: #007bff; /* 主色调 */
    color: #fff; /* 字体颜色 */
  }
  
  .submit-button:hover {
    background-color: #0056b3; /* 悬停时颜色 */
  }
  
  /* 取消按钮样式 */
  .cancel-button {
    color: #333; /* 字体颜色 */
  }
  
  .cancel-button:hover {
    background-color: #f0f0f0; /* 悬停时颜色 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 悬停时阴影效果 */
  }
  
  /* 参会人员选择样式 */
  .attendee-select {
    border-radius: 4px; /* 圆角边框 */
  }
  </style>
  