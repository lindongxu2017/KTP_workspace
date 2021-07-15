<template>
  <div class="ktp-aisde">
    <div class="link-wrapper">
      <div :class="['link-item', activePath == item.path ? 'active' : '']" v-for="item in routers" :key="item.name" v-text="item.title" @click="router(item.name)"></div>
    </div>
  </div>
</template>

<script>
import * as routers from '@/router/route.json'
export default {
  data () {
    return {
      routers: routers.default
    }
  },
  methods: {
    router (name) {
      this.$router.push({name})
    }
  },
  computed: {
    activePath: function () {
      return this.$route.path
    }
  }
}
</script>

<style scoped>
  .ktp-aisde {
    padding-bottom: 100px;
  }
  .link-item {
    font-size: 14px;
    line-height: 40px;
    cursor: pointer;
    user-select: none;
  }
  .link-item:hover, .link-item.active {
    color: #409eff;
  }
</style>