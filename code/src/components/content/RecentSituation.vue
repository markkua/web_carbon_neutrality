<template>

  <LimitWidth>
  <div>
    <h3>Global carbon emission and carbon sinks</h3>

    <CarbonBudgetBarChart />

<!--    <img src="img/essd2021_Global_Sources_and_Sinks.png" width="50vw" alt="essd2021_Global_Sources_and_Sinks.png">-->
    (measuring or estimating carbon sink is still a research topic)
  </div>
  </LimitWidth>

  <div>
    <h3>Green house gas emission</h3>

    <h4>Green house gas emission from 2000-2020</h4>

    <GlobalGHGMap/>

  </div>

  <div>
    <h3>Emission types</h3>
    <h4>[multi line chart] Emission types</h4>
  </div>


</template>


<script>
import LimitWidth from "components/util/LimitWidth";
import GlobalGHGMap from "components/maps/GlobalGHGMap";
import CarbonBudgetBarChart from "components/charts/CarbonBudgetBarChart";

export default {
  name: "RecentSituation",
  components: {
    GlobalGHGMap,
    LimitWidth,
    CarbonBudgetBarChart,
  }
}
</script>


<style scoped>
h4 {
  margin-bottom: 0;
}
</style>
