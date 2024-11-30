<template>
    <div class="app">
        <!-- <HmHeader></HmHeader> -->
        <HmMain></HmMain>
        <HmBotton></HmBotton>
        <!-- 全局组件 -->
        <hm-button></hm-button>
    </div>
  
</template>

<script>
// import HmHeader from './components/HmHeader.vue';
import HmMain from './components/HmMain.vue';
import HmBotton from './components/HmBotton.vue';
import HmButton from './components/HmButton.vue';
export default {
    components:{
        //组件名：组件对象
        // HmHeader,
        HmMain,
        HmBotton,
        HmButton
    }

}
</script>

<style>

</style>
