<template>
  <div
    class="q-pa-md items-center"
    style="
      background-color: #e0e0e0;
      height: 60px;
      display: flex;
      justify-content: center;
    "
  >
    <q-btn
      @click="scroll"
      flat
      align="around"
      label="Source"
      icon="article"
      style="margin: auto; display: block"
    />
  </div>

  <div class="row" style="background-color: #e0e0e0" v-if="show" id="source">
    <div class="column">
      <span style="color: #505050; font-size: 120%">Data Source:</span>
      <div class="text-body2">
        <a href="https://essd.copernicus.org/articles/14/1917/2022/essd-14-1917-2022.pdf"
        >Global Carbon Budget 2021</a
        >
      </div>
<!--      <div class="text-body2">-->
<!--        <a-->
<!--          href="https://unctadstat.unctad.org/wds/ReportFolders/reportFolders.aspx"-->
<!--        >UNCTAD STAT</a-->
<!--        >-->
<!--      </div>-->
<!--      <div class="text-body2">-->
<!--        <a-->
<!--          href="https://marketplace.officialstatistics.org/ais-weekly-port-calls"-->
<!--        >AIS: Weekly Port Calls</a-->
<!--        >-->
<!--      </div>-->
<!--      <div class="text-body2">-->
<!--        <a href="https://comtrade.un.org/data">UN Comtrade Database</a>-->
<!--      </div>-->
<!--      <div class="text-body2">-->
<!--        <a-->
<!--          href="https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/export/"-->
<!--        >OPENDATASOFT</a-->
<!--        >-->
<!--      </div>-->
    </div>
    <q-separator vertical inset color="white" />
    <div class="column">
      <span style="color: #505050; font-size: 120%">Software:</span>
<!--      <div class="text-body2">-->
<!--        Data Processing: <a href="https://pandas.pydata.org/">Pandas</a>,-->
<!--        <a href="https://geopandas.org/">GeoPandas</a>,-->
<!--        <a herf="https://www.qgis.org/en/site/">QGIS</a>-->
<!--      </div>-->
<!--      <div class="text-body2">-->
<!--        Front-end design and development:-->
<!--        <a href="https://v3.vuejs.org/">Vue</a>,-->
<!--        <a href="https://quasar.dev/">Quasar</a>,-->
<!--        <a href="https://animejs.com/">animejs</a>-->
<!--      </div>-->
<!--      <div class="text-body2">-->
<!--        Visualization:-->
<!--        <a href="https://docs.mapbox.com/mapbox-gl-js/api/">Mapbox</a>,-->
<!--        <a href="https://globe.gl/">Globe.GL</a>,-->
<!--        <a href="https://d3js.org/">D3.js</a>,-->
<!--        <a href="https://echarts.apache.org/zh/index.html">Apache ECharts</a>,-->
<!--        <a href="https://flourish.studio/">Flourish</a>-->
<!--      </div>-->
    </div>
    <q-separator vertical inset color="white" />
    <div class="column">
      <span style="color: #505050; font-size: 120%">Graphic: </span>
      <div class="text-body2">
        Images:
<!--        <a href="https://www.flaticon.com/">Flaticon</a>,-->
        <a href="https://www.pexels.com/">Pexels</a>,
        <a href="https://unsplash.com/">Unsplash</a>
      </div>
      <div class="text-body2">
        Icons:
        <a href="https://www.flaticon.com/free-icons/carbon-neutral" title="https://www.flaticon.com/free-icons/carbon-neutral">Freepik - Flaticon</a>
      </div>
<!--      <div class="text-body2">-->
<!--        Videos:-->
<!--        <a href="https://www.pexels.com/">Pexels</a>,-->
<!--        <a href="https://www.oecd.org/economic-outlook/">OECD</a>-->
<!--      </div>-->
    </div>

    <q-space class="q-ma-md" />
  </div>


  <div class="text-body2 q-pl-lg q-pr-lg q-pb-sm">
    &copy; 2022 Bingxin Ke. All rights reserved.
  </div>


</template>

<script>
export default {
  name: "SessionSource",

  data() {
    return {
      show: true,
    };
  },
  methods: {
    scroll() {
      if (this.show == true) {
        this.show = false;
      } else {
        this.show = true;
        setTimeout(() => {
          const element = document.getElementById("source");
          element.scrollIntoView({ behavior: "smooth" });
        }, 100);
      }
    },
  },

}
</script>

<style scoped>
.column {
  float: left;
  width: 33%;
  padding-left: 2%;
}
.row:after {
  content: "";
  display: table;
  clear: both;
}
.no_underline {
  text-decoration: none;
}
p {
  font-size: 90%;
}
a {
  color: #505050;
  text-decoration: underline;
  font-size: 80%;
}
html {
  scroll-behavior: smooth;
}
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}
</style>

