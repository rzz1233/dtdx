<template>
    <div v-show="visible" class="overlay" @click.self="close">
        <div class="modal-content">
            <label>添加公司员工</label>
            <input type="text" v-model="name" placeholder="请输入员工姓名" />
            <input type="text" v-model="user" placeholder="请输入用户名" />
            <input type="password" v-model="pwd" placeholder="请输入密码" />
            <div class="form-item">
                <label for="departments">参会部门:</label>
                <select v-model="dept" required>
                    <option value="" disabled>请选择部门</option>
                    <option v-for="item in options" :key="item.id" :value="item.id">
                        {{ item.name }}
                    </option>
                </select>
            </div>
            <button @click="addEmployee" :disabled="loading || !isFormValid">添加</button>
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
            name: "",
            user: "",
            pwd: "",
            dept: "",
            loading: false, // 添加 loading 状态
            options: []
        };
    },
    created() {
        this.fetchData(); // 调用数据获取方法
    },
    computed: {
        isFormValid() {
            return this.name.trim() !== "" && 
                   this.user.trim() !== "" && 
                   this.pwd.trim() !== "" && 
                   this.dept !== "";
        }
    },
    methods: {
        async fetchData() {
            try {
                const response = await apiClient.get('/api/dept/');
                this.options = response.data;
            } catch (error) {
                console.error('获取数据失败:', error);
            }
        },
        async addEmployee() {
            this.loading = true; // 开始加载

            try {
                const response = await apiClient.post('/api/user/', {
                    name: this.name,
                    user: this.user,
                    pwd: this.pwd,
                    dept: this.dept
                });

                console.log("员工添加成功:", response.data);
                this.$emit('add'); // 发出添加成功的事件

            } catch (error) {
                console.error('添加员工失败:', error);

                // 检查后端返回的错误信息
                if (error.response && error.response.data) {
                    alert(error.response.data.error || "添加员工失败，请重试。");
                } else {
                    alert("添加员工失败，请重试。");
                }
            } finally {
                this.loading = false; // 结束加载
                this.close();
            }
        },
        close() {
            // 重置所有输入框
            this.name = "";
            this.user = "";
            this.pwd = "";
            this.dept = "";
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
