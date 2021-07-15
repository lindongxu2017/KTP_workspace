<template>
  <div class="custom-map">
    <div id="map"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
// import geo from "../../public/china.json"
import geo from "../../public/yangjiang.json";

export default {
  data() {
    return {

    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      echarts.registerMap("YJ", geo);
      var myChart = echarts.init(document.getElementById("map"));

      myChart.setOption({
        title: {
          text: "阳江市",
          subtext: "subtitle",
          sublink: "",
        },
        tooltip: {
          trigger: "item",
          formatter: "{b}<br/>{c} (人 / Km2)",
        },
        series: [
          {
            name: "阳春市人口密度",
            type: "map",
            map: "YJ", // 自定义扩展图表类型
            label: {
              show: true,
            },
            data: [
              { name: "阳春市", value: 20057.34 },
              { name: "阳东县", value: 15477.48 },
              { name: "阳西县", value: 31686.1 },
              { name: "江城区", value: 6992.6 },
              { name: "青海省", value: 6992.6 }
            ],
          },
        ],
      });
    },
  },
};
</script>

<style scoped>
#map {
  width: 1000px;
  height: 600px;
  margin: 0 auto;
  border: 1px solid #eee;
}
</style>