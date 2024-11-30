<template>
    <div class="hm-main" @click="handleClick">
      我是HmMain
      <!-- 全局组件 -->
      <hm-button></hm-button>
    </div>
  </template>
  
  <script>
import HmButton from './HmButton.vue';
  export default {
  components: { HmButton },
    methods: {
      handleClick() {
        alert('Main clicked!');
      }
    }
  }
  </script>
  
  <style>
  .hm-main {
    background-color: #e0e0e0; /* 背景颜色 */
    padding: 20px;             /* 内边距 */
    text-align: center;        /* 文本居中 */
    cursor: pointer;           /* 鼠标悬停时显示手型 */
    border: 1px solid #ccc;   /* 边框 */
    border-radius: 5px;       /* 圆角 */
    transition: background-color 0.3s; /* 动画效果 */
  }
  
  .hm-main:hover {
    background-color: #d0d0d0; /* 鼠标悬停时的背景颜色 */
  }
  </style>
  