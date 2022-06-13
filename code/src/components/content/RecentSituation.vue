<template>

  <LimitWidth>
  <div>
    <h3>Global CO<sub>2</sub> emission and carbon sinks</h3>
    <img src="img/essd2021_Global_Sources_and_Sinks.png" width="50vw" alt="essd2021_Global_Sources_and_Sinks.png">
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
import GlobalGHGMap from "components/maps/GlobalGHGMap";
import LimitWidth from "components/util/LimitWidth";

export default {
  name: "RecentSituation",
  components: {
    GlobalGHGMap,
    LimitWidth,
  }
}
</script>


<style scoped>
h4 {
  margin-bottom: 0;
}
</style>
