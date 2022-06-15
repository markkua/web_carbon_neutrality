<template>
    <div id="temperature_line_chart" class="echarts"></div>
</template>

<script>
import * as echarts from "echarts";
import loaded_data from "../../../public/data/temperature_anomaly_1990-2019.json";

export default {
  name: "TempAnomalyLineChart",
  components: {
  },

  data: function () {
    return {
      years: [],
      temperature: {},
      series: [],
      legends: []
    };
  },
  methods: {
    processData() {
      this.years = loaded_data.year;
      this.temperature = loaded_data.temperature;
      // construct series data
      for (let key in this.temperature) {
        this.series.push({
          name: key,
          displayName: key,
          data: this.temperature[key]['data'],
          type: 'line',
          color: this.temperature[key]['color'],
          tooltip: {
            valueFormatter: value => value + '°C'
          },
        });
        this.legends.push(key);
      }
    },
  },
  mounted() {
    console.log(loaded_data);
    this.processData();

    var myChart = echarts.init(document.getElementById("temperature_line_chart"));
    myChart.setOption({
      tooltip: {
        trigger: 'axis'
      },

      xAxis: [{
        data: this.years,
        type: 'category',
        axisPointer: {
          type: 'shadow'
        }
      }],

      yAxis: [{
        type: 'value',
        name: 'Temperature',
        axisLabel: {
          formatter: '{value} °C'
        }
      }],

      series: this.series,

      legend: {
        data: this.legends
      },

    });

    window.addEventListener("resize", function () {
      //resize the bar chart according to the screen size
      myChart.resize();
    });

  },

}
</script>

<style scoped>
.echarts {
  height: 500px;
  width: 100%;
  position: relative;
  margin: auto;
}

</style>
