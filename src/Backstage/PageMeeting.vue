<template>
  <div>
    <h1>会议表</h1>
    <table>
      <thead>
        <tr>
          <th>会议主题</th>
          <th>会议日期</th>
          <th>会议开始时间</th>
          <th>会议结束时间</th>
          <th>参会部门</th>
          <th>外部人员</th>
          <th>会议状态</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="meeting in meetdatas" :key="meeting.id">
          <td>{{ meeting.title }}</td>
          <td>{{ meeting.date }}</td>
          <td>{{ meeting.starttime }}</td>
          <td>{{ meeting.endtime }}</td>
          <td>{{ meeting.dept_info.name }}</td>
          <td>{{ meeting.outpeople }}</td>
          <td>{{ meeting.status }}</td>
          <td>
            <button class="delete-button" @click="deleteMeeting(meeting.id)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 添加分页按钮 -->
    <div class="pagination">
      <button @click="goToPrevPage" :disabled="!prevPage">上一页</button>
      <span>当前页: {{ currentPage }}</span>
      <button @click="goToNextPage" :disabled="!nextPage">下一页</button>
    </div>

    <button class="add-button" @click="isShow = true">添加</button>
    <AddMeeting :visible.sync="isShow" @add="fetchData"></AddMeeting>
  </div>
</template>

<script>
import apiClient from '@/view/api';
import AddMeeting from '../components/AddMeeting.vue';

export default {
  data() {
    return {
      isShow: false,
      meetdatas: [],       // 保存会议数据
      currentPage: 1,      // 当前页数
      pageSize: 2,         // 每页显示的记录数
      nextPage: null,      // 下一页链接
      prevPage: null       // 上一页链接
    };
  },
  components: {
    AddMeeting
  },
  created() {
    this.fetchData(this.currentPage); // 调用数据获取方法
  },
  methods: {
    // 获取分页数据
    async fetchData(page) {
      try {
        const response = await apiClient.get(`/api/meetinglist1/?page=${page}&page_size=${this.pageSize}`);
        this.meetdatas = response.data.results; // 处理返回的分页数据
        console.log(this.meetdatas)
        this.currentPage = page; // 更新当前页数

        // // 按日期和时间降序排序
        // this.meetdatas.sort((a, b) => {
        //   const dateA = new Date(`${a.date}T${a.starttime}`);
        //   const dateB = new Date(`${b.date}T${b.starttime}`);
        //   return dateB - dateA; // 按时间降序排列
        // });

        // 保存 `next` 和 `previous` 信息，用于控制分页按钮
        this.nextPage = response.data.next;
        this.prevPage = response.data.previous;

      } catch (error) {
        console.error('获取数据失败:', error);
      }
    },
    // 删除会议
    async deleteMeeting(meetingId) {
      if (confirm('确定要删除这个会议吗？')) { // 提示确认删除
        try {
          await apiClient.delete(`/api/meetinglist/${meetingId}/`); // 发送删除请求
          this.fetchData(this.currentPage); // 删除后重新获取当前页数据
        } catch (error) {
          console.error('删除会议失败:', error);
        }
      }
    },
    // 跳转到下一页
    goToNextPage() {
      if (this.nextPage) {
        this.fetchData(this.currentPage + 1);
      }
    },
    // 跳转到上一页
    goToPrevPage() {
      if (this.prevPage) {
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

/* 分页按钮样式 */
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
