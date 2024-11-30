<template>
  <div id="app">
    <div class="bottom">
      <div class="b-1">
        <ul>
          <li @click="topage('pagemeeting')">会议表</li>
          <li @click="topage('pageuser')">用户表</li>
          <li @click="topage('pagedept')">部门表</li>
          <li @click="topage('pageattendee')">签到表</li>
          <li @click="topage('pagelogin1')">登录注册表</li>
        </ul>
      </div>
      <div class="b-2">
        <button class="back-button" @click="back">返回主页</button>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    topage(path) {
      this.$router.push('/backstageview/' + path);
    },
    back() {
      this.$router.push('/main/page1');
    }
  }
}
</script>

<style scoped>
.bottom {
  display: flex;
  height: 100vh;
}

.b-1 {
  width: 15%;
  background-color: #2c3e50;
  padding: 20px;
}

li {
  height: 42px;
  list-style-type: none;
  margin-bottom: 12px;
  border-radius: 4px;
  color: white;
  line-height: 42px;
  padding-left: 15px;
  cursor: pointer;
}

li:hover {
  background-color: #1abc9c;
}

.b-2 {
  background-color: #ecf0f1;
  width: 85%;
  padding: 20px;
  position: relative;
}

.back-button {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 15px;
  cursor: pointer;
  position: absolute;
  top: 20px;
  right: 20px;
}

.back-button:hover {
  background-color: #2980b9;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #ecf0f1;
}

ul {
  padding: 0;
}
</style>

  