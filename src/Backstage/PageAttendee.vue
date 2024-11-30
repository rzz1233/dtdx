<template>
  <div>
    <h1>签到表</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>会议名称</th>
          <th>参会人员</th>
          <th>会议日期</th>
          <th>会议时间</th>
          <th>签到状态</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in meetdatas" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.meetname }}</td>
          <td>{{ item.user }}</td>
          <td>{{ item.meetdate }}</td>
          <td>{{ item.check_time }}</td>
          <td>{{ item.status }}</td>
          <td>
            <button class="delete-button" @click="deleteMeeting(item.id)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="pagination">
      <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1">上一页</button>
      <span>第 {{ currentPage }} 页 / {{ totalPages }} 页</span>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">下一页</button>
    </div>
  </div>
</template>

<script>
import apiClient from '@/view/api';
export default {
  data() {
    return {
      meetdatas: [], // 存储从后端获取的用户数据
      currentPage: 1, // 当前页数
      pageSize: 6,    // 每页记录数
      totalPages: 1,  // 总页数
    };
  },
  created() {
    this.fetchData(); // 调用数据获取方法
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get(`/api/attendeepro/?page=${this.currentPage}&page_size=${this.pageSize}`); // 替换为你的 API 端点
        this.meetdatas = response.data.results; // 假设返回的数据在 results 数组中
        this.totalPages = Math.ceil(response.data.count / this.pageSize); // 更新总页数
      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    async deleteMeeting(meetingId) {
      if (confirm('确定要删除吗？')) { // 提示确认删除
        try {
          await apiClient.delete(`/api/attendee/${meetingId}/`); // 发送删除请求
          this.meetdatas = this.meetdatas.filter(meeting => meeting.id !== meetingId); // 从数组中移除已删除的会议
        } catch (error) {
          console.error('删除失败:', error);
        }
      }
    },
    changePage(page) {
      if (page < 1 || page > this.totalPages) return; // 确保页码合法
      this.currentPage = page; // 更新当前页码
      this.fetchData(); // 重新获取数据
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

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.pagination button {
  margin: 0 10px;
  padding: 8px 12px;
  cursor: pointer;
}
</style>
