<template>
  <div class="home">
    <Map />
  </div>
</template>

<script>
import Map from '../components/MyMap.vue'
import { computed } from 'vue'
export default {
  name: 'home',
  components: {
    Map
  },
  data () {
    return {
      todolist: []
    }
  },
  // 父组件不需要知道哪些子组件使用它 provide 的 property
  // 子组件不需要知道 inject 的 property 来自哪里
  provide () {
    return {
      cur: computed(() => this.todolist.length)
    }
  },
  mounted () {
    this.getdata()
  },
  methods: {
    getdata () {
      setTimeout(() => {
        this.mapData = {
          name: '阳江市12'
        }
      }, 1000);
    },
    inc () {
      this.todolist.push(Math.random())
    }
  }
}
</script>

<style>

</style>