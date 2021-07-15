<template>
  <div class="section">
    <h3><slot name="title"></slot></h3>
    <p class="desc"><slot name="desc"></slot></p>
    <div><slot></slot></div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.section {
  margin-bottom: 40px;
  padding: 30px 0 0;
}
.desc {
  font-size: 14px;
  color: #5e6d82;
  margin: 20px 0;
}
</style>