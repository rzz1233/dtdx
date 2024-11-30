<template>
  <div>
    <h1>公司员工表</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>姓名</th>
          <th>用户名</th>
          <th>密码</th>
          <th>部门</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in meetdatas.results" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.user }}</td>
          <td>{{ item.pwd }}</td>
          <td>{{ item.dept_info.name }}</td>
          <td>
            <button class="delete-button" @click="deleteMeeting(item.id)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 添加分页按钮 -->
    <div class="pagination">
      <button @click="goToPrevPage" :disabled="!meetdatas.previous">上一页</button>
      <span>当前页: {{ currentPage }}</span>
      <button @click="goToNextPage" :disabled="!meetdatas.next">下一页</button>
    </div>

    <button class="add-button" @click="isShow = true">添加</button>
    <AddUser :visible.sync="isShow" @add="fetchData"></AddUser>
  </div>
</template>

<script>
import AddUser from '@/components/AddUser.vue';
import apiClient from '@/view/api';

export default {
  data() {
    return {
      meetdatas: { results: [] }, // 存储从后端获取的分页用户数据
      isShow: false,
      currentPage: 1, // 当前页数
      pageSize: 6, // 每页显示的记录数
    };
  },
  components: {
    AddUser
  },
  created() {
    this.fetchData(this.currentPage); // 调用数据获取方法
  },
  methods: {
    // 获取分页数据
    async fetchData(page = 1) {
      try {
        const response = await apiClient.get(`/api/user/?page=${page}&page_size=${this.pageSize}`);
        this.meetdatas = response.data; // 处理返回的分页数据
        this.currentPage = page; // 更新当前页数
      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    // 删除用户
    async deleteMeeting(meetingId) {
      if (confirm('确定要删除吗？')) { // 提示确认删除
        try {
          await apiClient.delete(`/api/user/${meetingId}/`);
          this.fetchData(this.currentPage); // 删除后重新获取当前页数据
        } catch (error) {
          console.error('删除失败:', error);
        }
      }
    },
    // 跳转到下一页
    goToNextPage() {
      if (this.meetdatas.next) {
        this.fetchData(this.currentPage + 1);
      }
    },
    // 跳转到上一页
    goToPrevPage() {
      if (this.meetdatas.previous) {
        this.fetchData(this.currentPage - 1);
      }
    }
  }
};
</script>

<style>
/* 样式保持不变 */

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
  background-color: #f5f5f5;
}

.delete-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.delete-button:hover {
  background-color: #d32f2f;
}

.add-button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
  margin-top: 20px;
}

.add-button:hover {
  background-color: #388E3C;
}

/* 分页按钮 */
.pagination {
  margin-top: 20px;
}

.pagination button {
  padding: 10px 20px;
  margin: 0 5px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.pagination button:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}
</style>
