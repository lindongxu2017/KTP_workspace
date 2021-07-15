<template>
  <div class="main-container">
    <el-scrollbar style="height: 100%">
      <div class="home-layout">
        <div class="aside">
          <el-scrollbar style="height: 100%">
            <ktpAside />
          </el-scrollbar>
        </div>
        <div class="main">
          <div class="view-title">
            <h2>{{ activePathTitle }}</h2>
            <p>{{ activePathDesc }}</p>
          </div>
          <router-view v-slot="{ Component }">
            <transition name="el-fade-in" mode="out-in" :duration="{ enter: 300, leave: 150 }">
              <keep-alive>
                <component :is="Component" />
              </keep-alive>
            </transition>
          </router-view>
        </div>
      </div>
    </el-scrollbar>
  </div>
</template>

<script>
import ktpAside from "com/aside.vue";
export default {
  components: {
    ktpAside,
  },
  computed: {
    activePathTitle: function () {
      return this.$route.meta.title;
    },
    activePathDesc: function () {
      return this.$route.meta.desc;
    },
  },
};
</script>

<style scoped>
.main-container {
  height: 100%;
}
.home-layout {
  width: 1140px;
  height: 100%;
  box-sizing: border-box;
  margin: 0 auto;
  padding-top: 80px;
}
.aside {
  width: 240px;
  position: fixed;
  top: 0;
  bottom: 0;
  margin-top: 80px;
}
.main {
  padding-left: 270px;
  box-sizing: border-box;
}
.view-title p {
  font-size: 14px;
  color: #5e6d82;
}
</style>