<template>
  <div class="ktp-button">
    <my-section>
      <template v-slot:title>防止重复操作</template>
      <template v-slot:desc>点击按钮后进行数据加载操作，在按钮上显示加载状态，防止重复操作。</template>
      <el-button class="button" type="primary" :loading="loading" @click="btnClick">{{value}}</el-button>
      <!-- <el-input class="input" placeholder="请输入" v-model="value"></el-input> -->
      <p class="tip">点击成功次数 {{count}}</p>
    </my-section>
    
  </div>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      value: '加载中',
      count: 0
    }
  },
  methods: {
    btnClick () {
      if (!this.loading) {
        this.loading = true
        this.count++
        setTimeout(() => {
          this.loading = false
        }, 1000);
      }
    }
  }
}
</script>

<style scoped>
  .ktp-button {
    word-wrap: break-word;
    word-break: break-all;
  }
</style>