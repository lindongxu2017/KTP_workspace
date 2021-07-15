<template>
  <div class="ktp-color">
    <my-section>
      <template v-slot:title>主色</template>
      <template v-slot:desc>Element 主要品牌颜色是鲜艳、友好的蓝色。</template>
      <div class="el-row" style="margin-left: -6px; margin-right: -6px">
        <div class="el-col el-col-10 el-col-xs-12" style="padding-left: 6px; padding-right: 6px">
          <div class="demo-color-box" style="background: rgb(64, 158, 255)">
            Brand Color
            <div class="value">#409EFF</div>
            <div class="bg-color-sub" style="background: rgb(236, 245, 255)">
              <div class="bg-blue-sub-item" v-for="item in mainColor" :key="item" :style="{background: item}"></div>
            </div>
          </div>
        </div>
      </div>
    </my-section>
    <my-section>
      <template v-slot:title>辅助色</template>
      <template v-slot:desc>除了主色外的场景色，需要在不同的场景中使用（例如危险色表示危险的操作）。</template>
      <div class="el-row" style="margin-left: -6px; margin-right: -6px;"><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box" style="background: rgb(103, 194, 58);">Success<div class="value">#67C23A</div><div class="bg-color-sub"><div class="bg-success-sub-item" style="background: rgb(225, 243, 216);"></div><div class="bg-success-sub-item" style="background: rgb(240, 249, 235);"></div></div></div></div><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box" style="background: rgb(230, 162, 60);">Warning<div class="value">#E6A23C</div><div class="bg-color-sub"><div class="bg-success-sub-item" style="background: rgb(250, 236, 216);"></div><div class="bg-success-sub-item" style="background: rgb(253, 246, 236);"></div></div></div></div><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box" style="background: rgb(245, 108, 108);">Danger<div class="value">#F56C6C</div><div class="bg-color-sub"><div class="bg-success-sub-item" style="background: rgb(253, 226, 226);"></div><div class="bg-success-sub-item" style="background: rgb(254, 240, 240);"></div></div></div></div><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box" style="background: rgb(144, 147, 153);">Info<div class="value">#909399</div><div class="bg-color-sub"><div class="bg-success-sub-item" style="background: rgb(233, 233, 235);"></div><div class="bg-success-sub-item" style="background: rgb(244, 244, 245);"></div></div></div></div></div>
    </my-section>
    <my-section>
      <template v-slot:title>中性色</template>
      <template v-slot:desc>中性色用于文本、背景和边框颜色。通过运用不同的中性色，来表现层次结构。</template>
      <div class="el-row" style="margin-left: -6px; margin-right: -6px;"><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box-group"><div class="demo-color-box demo-color-box-other" style="background: rgb(48, 49, 51);">主要文字<div class="value">#303133</div></div><div class="demo-color-box demo-color-box-other" style="background: rgb(96, 98, 102);">
      常规文字<div class="value">#606266</div></div><div class="demo-color-box demo-color-box-other" style="background: rgb(144, 147, 153);">次要文字<div class="value">#909399</div></div><div class="demo-color-box demo-color-box-other" style="background: rgb(192, 196, 204);">占位文字<div class="value">#C0C4CC</div></div></div></div><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box-group"><div class="demo-color-box demo-color-box-other demo-color-box-lite" style="background: rgb(220, 223, 230);">一级边框<div class="value">#DCDFE6</div></div><div class="demo-color-box demo-color-box-other demo-color-box-lite" style="background: rgb(228, 231, 237);">二级边框<div class="value">#E4E7ED</div></div><div class="demo-color-box demo-color-box-other demo-color-box-lite" style="background: rgb(235, 238, 245);">三级边框<div class="value">#EBEEF5</div></div><div class="demo-color-box demo-color-box-other demo-color-box-lite" style="background: rgb(242, 246, 252);">四级边框<div class="value">#F2F6FC</div></div></div></div><div class="el-col el-col-6 el-col-xs-12" style="padding-left: 6px; padding-right: 6px;"><div class="demo-color-box-group"><div class="demo-color-box demo-color-box-other" style="background: rgb(0, 0, 0);">基础黑色<div class="value">#000000</div></div><div class="demo-color-box demo-color-box-other" style="background: rgb(255, 255, 255); color: rgb(48, 49, 51); border: 1px solid rgb(238, 238, 238);">基础白色<div class="value">#FFFFFF</div></div></div></div></div>
    </my-section>
  </div>
</template>

<script>
export default {
  data () {
    return {
      mainColor: [
        'rgb(83, 168, 255)',
        'rgb(102, 177, 255)',
        'rgb(121, 187, 255)',
        'rgb(140, 197, 255)',
        'rgb(160, 207, 255)',
        'rgb(179, 216, 255)',
        'rgb(198, 226, 255)',
        'rgb(217, 236, 255)'
      ]
    }
  }
};
</script>

<style scoped>
.demo-color-box {
  position: relative;
  border-radius: 4px;
  padding: 20px;
  margin: 5px 0;
  height: 114px;
  box-sizing: border-box;
  color: #fff;
  font-size: 14px;
}
.bg-color-sub {
  width: 100%;
  height: 40px;
  left: 0;
  bottom: 0;
  position: absolute;
}
.bg-blue-sub-item:first-child {
  border-radius: 0 0 0 4px;
}
.bg-blue-sub-item {
  width: 11.1111111%;
  height: 100%;
  display: inline-block;
}
.bg-success-sub-item:first-child {
  border-radius: 0 0 0 4px;
}
.bg-success-sub-item {
  width: 50%;
  height: 100%;
  display: inline-block;
}
.demo-color-box-other {
  height: 74px;
  margin: 10px 0!important;
  border-radius: 4px 4px 4px 4px!important;
  padding: 15px 20px;
}
</style>