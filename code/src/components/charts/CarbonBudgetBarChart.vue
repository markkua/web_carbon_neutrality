<template>
  <div id="carbon_budget_bar_chart" style="height: 600px"></div>
</template>

<script>
import * as echarts from "echarts";
import loaded_data from "../../../public/data/carbon_budget_2000-2020.json"

export default {
  name: "CarbonBudgetBarChart",
  data: function () {
    return {
      years: [],
      carbon_data: {},
      series: [],
      legends: []
    };
  },
  methods: {
    processData() {
      this.years = loaded_data.year;
      this.carbon_data = loaded_data.carbon_budget;
      // construct series data
      for (let key in this.carbon_data) {
        this.series.push({
          name: key,
          displayName: key,
          data: this.carbon_data[key]['data'],
          type: 'bar',
          stack: 'x',
          color: this.carbon_data[key]['color'],
          tooltip: {
            valueFormatter: value => value + ' GtC'
          },
        });
        this.legends.push(key);
      }
      // atmospheric_growth
      const Atmospheric_Growth = "Atmospheric Growth"
      this.series.push({
        name: 'Atmospheric Growth',
        data: loaded_data[Atmospheric_Growth]['data'],
        type: 'line',
        color: loaded_data[Atmospheric_Growth]['color'],
        tooltip: {
          valueFormatter: value => value + ' GtC'
        },
      })
      this.legends.push(Atmospheric_Growth)
    },
  },
  mounted() {
    console.log(loaded_data);
    this.processData();

    var myChart = echarts.init(document.getElementById("carbon_budget_bar_chart"));
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

      yAxis: [
        {
          type: 'value',
          name: 'Carbon Budget',
          alignTicks: true,
        },
        {
          type: 'value',
          name: 'Atmospheric Growth'
        }
      ],

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

</style>
