<template>
  <div class="hm-header" @click="handleClick">
    我是HmHeader
  </div>
</template>

<script>
export default {
  methods: {
    handleClick() {
      alert('Header clicked!');
    }
  }
}
</script>

<style>
.hm-header {
  background-color: red; /* 背景颜色 */
  padding: 20px;         /* 内边距 */
  text-align: center;    /* 文本居中 */
  cursor: pointer;       /* 鼠标悬停时显示手型 */
  border: 1px solid #ccc; /* 边框 */
  border-radius: 5px;    /* 圆角 */
  transition: background-color 0.3s; /* 动画效果 */
}

.hm-header:hover {
  background-color: darkred; /* 鼠标悬停时的背景颜色 */
}
</style>
