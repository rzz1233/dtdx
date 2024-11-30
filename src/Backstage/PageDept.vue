<template>
    <div>
      <h1>部门表</h1>
      <table>
        <thead>
          <tr>
            <th>部门 ID</th>
            <th>部门名字</th>
            <th>操作</th>
        
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in meetdatas" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
         
            <td>
              <button class="delete-button" @click="deleteMeeting(item.id)">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button class="add-button" @click="isShow = true">添加</button>
      <AddDept :visible.sync="isShow" @add="fetchData"></AddDept>
    </div>
  </template>
  
  <script>
  import AddDept from '@/components/AddDept.vue';
  // import axios from 'axios';
  import apiClient from '@/view/api';
  export default {
    data() {
      return {
        isShow:false,
        meetdatas: [], // 存储从后端获取的用户数据
      };
    },
    components: {
      AddDept
    },
    created() {
      this.fetchData(); // 调用数据获取方法
    },
    methods: {
      async fetchData() {
        try {
          const response = await apiClient.get('/api/dept/'); // 替换为你的 API 端点
          this.meetdatas = response.data; // 假设返回的数据是用户数组
        } catch (error) {
          console.error('获取数据失败:', error);
        }
      },
      async deleteMeeting(meetingId) {
        if (confirm('确定要删除吗？')) { // 提示确认删除
          try {
            await apiClient.delete(`/api/dept/${meetingId}/`); // 发送删除请求
            this.meetdatas = this.meetdatas.filter(meeting => meeting.id !== meetingId); // 从数组中移除已删除的会议
          } catch (error) {
            console.error('删除失败:', error);
          }
        }
      },
    },
  }
  </script>
  
  <style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
  }
  
  th {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
  }
  
  tbody tr {
    transition: background-color 0.3s;
  }
  
  tbody tr:hover {
    background-color: #f5f5f5; /* 悬停时的背景色 */
  }
  
  .delete-button {
    background-color: #f44336; /* 红色按钮 */
    color: white;
    border: none;
    padding: 8px 12px;
    cursor: pointer;
    border-radius: 4px; /* 圆角 */
    transition: background-color 0.3s;
  }
  
  .delete-button:hover {
    background-color: #d32f2f; /* 悬停时变暗 */
  }
  .add-button {
    background-color: #4CAF50; /* 绿色按钮 */
    color: white;
    border: none;
    padding: 8px 12px;
    cursor: pointer;
    border-radius: 4px; /* 圆角 */
    transition: background-color 0.3s;
    margin-top: 20px; /* 上边距 */
  }
  
  .add-button:hover {
    background-color: #388E3C; /* 悬停时变暗 */
  }
  </style>
  