<template>
    <button class="generic-button">通用按钮</button>
  </template>
  
  <script>
  export default {
  
  }
  </script>
  
  <style>
  .generic-button {
    background-color: #007bff; /* 背景颜色 */
    color: white;               /* 字体颜色 */
    padding: 10px 20px;        /* 内边距 */
    border: none;               /* 无边框 */
    border-radius: 5px;        /* 圆角 */
    cursor: pointer;            /* 鼠标悬停时显示手型 */
    transition: background-color 0.3s; /* 动画效果 */
  }
  
  .generic-button:hover {
    background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
  }
  </style>
  