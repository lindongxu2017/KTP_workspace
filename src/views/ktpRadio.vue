<template>
  <div class="ktp-button">
    <my-section>
      <template v-slot:title>基础</template>
      <template v-slot:desc>由于选项默认可见，不宜过多，若选项过多，建议使用 Select 选择器。</template>
      <el-radio v-model="radio" :label="item.label" v-for="item in dataRadio" :key="item.label">{{item.name}}</el-radio>
      <p class="tip">当前选择： {{radio}}</p>
    </my-section>
    
  </div>
</template>

<script>
export default {
  data () {
    return {
      radio: '1',
      dataRadio: [
        {label: '1', name: '选项一'},
        {label: '2', name: '选项二'},
        {label: '3', name: '选项三'},
        {label: '4', name: '选项四'},
        {label: '5', name: '选项五'}
      ]
    }
  }
}
</script>

<style scoped>

</style>