<template>
  <div class="user-management">
    <h1>用户注册表</h1>
    <table class="user-table">
      <thead>
        <tr>
          <th>用户名</th>
          <th>身份</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in users" :key="item.id">
          <td>{{ item.username }}</td>
          <td>{{ item.is_superuser ? '管理员' : '普通用户' }}</td>
          <td>
            <button class="delete-button" @click="deleteUser(item.id)">删除</button>
            <button class="update-button" @click="openUpdateModal(item)">修改</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 分页控制按钮 -->
    <div class="pagination-controls">
      <button @click="goToPrevPage" :disabled="!prevPage">上一页</button>
      <button @click="goToNextPage" :disabled="!nextPage">下一页</button>
    </div>

    <!-- 用户更新模态框 -->
    <UpdateAdmin :visible.sync="isModalVisible">
      <h2>修改用户信息</h2>
      <label>身份：</label>
      <select v-model="selectedUser.is_superuser" class="identity-select">
        <option :value="true">管理员</option>
        <option :value="false">普通用户</option>
      </select>
      <button @click="updateUser" class="save-button">保存修改</button>
    </UpdateAdmin>
  </div>
</template>

<script>
import apiClient from '@/view/api';  // 导入API客户端
import UpdateAdmin from '@/components/UpdateAdmin.vue'; // 引入模态窗口组件

export default {
  components: {
    UpdateAdmin
  },
  data() {
    return {
      isModalVisible: false,
      selectedUser: {},
      users: [],  // 用来存储用户数据
      nextPage: null,  // 下一页的URL
      prevPage: null,  // 上一页的URL
      currentPage: 1,  // 当前页数
      pageSize: 6,     // 每页显示的记录数
    };
  },
  created() {
    this.fetchData(this.currentPage); // 默认加载第一页数据
  },
  methods: {
    // 获取用户数据并处理分页信息
    async fetchData(page) {
      try {
        const response = await apiClient.get(`/api/users/?page=${page}&page_size=${this.pageSize}`);
        this.users = response.data.results;  // 获取用户数据
        this.nextPage = response.data.next;  // 下一页链接
        this.prevPage = response.data.previous;  // 上一页链接
        this.currentPage = page;  // 更新当前页码
      } catch (error) {
        console.error('获取数据失败:', error);
        alert('获取用户数据失败，请检查网络或联系管理员。');
      }
    },

    // 删除用户
    async deleteUser(userId) {
      if (confirm('确定要删除该用户吗？')) {
        try {
          await apiClient.delete(`/api/users/${userId}/`);
          this.users = this.users.filter(user => user.id !== userId);  // 移除已删除的用户
          alert('用户删除成功！');
        } catch (error) {
          console.error('删除失败:', error);
          alert('删除失败，请重试。');
        }
      }
    },

    // 打开更新模态框
    openUpdateModal(user) {
      this.selectedUser = { ...user };  // 复制用户数据
      this.isModalVisible = true;  // 显示模态框
    },

    // 更新用户信息
    async updateUser() {
      try {
        await apiClient.put(`/api/users/${this.selectedUser.id}/`, {
          is_superuser: this.selectedUser.is_superuser  // 更新用户身份
        });
        alert('用户信息更新成功！');
        this.fetchData(this.currentPage);  // 更新数据
        this.isModalVisible = false;  // 关闭模态框
      } catch (error) {
        console.error('更新失败:', error);
        alert('更新失败，请重试。');
      }
    },

    // 切换到下一页
    goToNextPage() {
      if (this.nextPage) {
        const nextPageNumber = new URL(this.nextPage).searchParams.get('page');
        this.fetchData(nextPageNumber);  // 加载下一页
      }
    },

    // 切换到上一页
    goToPrevPage() {
      if (this.prevPage) {
        const prevPageNumber = new URL(this.prevPage).searchParams.get('page');
        this.fetchData(prevPageNumber);  // 加载上一页
      }
    }
  }
};
</script>

<style scoped>
/* 用户管理页面样式 */
.user-management {
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

.user-table {
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

td {
  font-size: 14px;
}

.delete-button, .update-button, .save-button {
  padding: 8px 16px;
  border-radius: 4px;
  border: none;
  color: white;
  cursor: pointer;
}

.delete-button {
  background-color: #f44336;
}

.update-button {
  background-color: #2196F3;
}

.save-button {
  background-color: #4CAF50;
}

.delete-button:hover, .update-button:hover, .save-button:hover {
  opacity: 0.8;
}

.pagination-controls {
  margin-top: 20px;
  text-align: center;
}

.pagination-controls button {
  padding: 10px 20px;
  margin: 5px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.identity-select {
  padding: 6px;
  margin-top: 10px;
  font-size: 14px;
  border-radius: 4px;
  border: 1px solid #ccc;
  width: 200px;
}
</style>
