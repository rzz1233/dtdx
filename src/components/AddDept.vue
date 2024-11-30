<template>
    <div v-show="visible" class="overlay" @click.self="close">
        <div class="modal-content">
            <label>添加部门</label>
            <input type="text" v-model="deptname" placeholder="请输入部门名称" />
            <button @click="addDepartment" :disabled="loading">添加</button>
            <button @click="close">关闭</button>
            <div v-if="loading">正在添加...</div>
        </div>
    </div>
</template>

<script>
import apiClient from '@/view/api';

export default {
    props: {
        visible: Boolean,
    },
    data() {
        return {
            deptname: "",
            loading: false, // 添加 loading 状态
        };
    },
    methods: {
        async addDepartment() {
            if (this.deptname.trim() === "") {
                alert("部门名称不能为空！");
                return;
            }

            this.loading = true; // 开始加载

            try {
                const response = await apiClient.post('/api/dept/', {
                    name: this.deptname
                });

                console.log("部门添加成功:", response.data);
                this.$emit('add'); // 发出添加成功的事件
                // 你可以在这里处理成功后的逻辑，比如更新部门列表

            } catch (error) {
                console.error('添加部门失败:', error);
                alert("添加部门失败，请重试。");
            } finally {
                this.loading = false; // 结束加载
                this.close()
            }
        },
        close() {
            this.deptname = "";
            this.$emit('update:visible', false);
        }
    }
}
</script>

<style scoped>
/* 模态窗口的遮罩层 */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

/* 模态框内容样式 */
.modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

input {
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 5px;
    width: 100%;
}

button {
    margin-right: 10px;
}

</style>
