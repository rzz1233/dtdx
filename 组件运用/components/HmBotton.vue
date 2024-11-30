<template>
    <div class="hm-botton" @click="handleClick">
      我是HmBotton
      <hm-button></hm-button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      handleClick() {
        alert('Botton clicked!'); // 更新提示内容
      }
    }
  }
  </script>
  
  <style>
  .hm-botton {
    background-color: #007bff; /* 背景颜色 */
    color: white;              /* 字体颜色 */
    padding: 15px;             /* 内边距 */
    text-align: center;        /* 文本居中 */
    cursor: pointer;           /* 鼠标悬停时显示手型 */
    border: none;              /* 无边框 */
    border-radius: 5px;       /* 圆角 */
    transition: background-color 0.3s; /* 动画效果 */
  }
  
  .hm-botton:hover {
    background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
  }
  </style>
  