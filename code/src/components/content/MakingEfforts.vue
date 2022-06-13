<template>

  <div>
    <h3>Less green house gas emissions</h3>
    <h4>CO<sub>2</sub> emission change from 2001 to 2020 (minus previous year)</h4>
    <GlobalCO2ChangeMap />

  </div>

  <h3>More clean energy</h3>
  <h4>[map]  Clean energy change (in percentage) of countries and regions</h4>

  <h3>Less deforestation</h3>
  <h4>[Line chart] deforestation and reforestation (copy from deforestation project)</h4>


</template>

<script>
import GlobalCO2ChangeMap from "components/maps/GlobalCO2ChangeMap";

export default {
  name: "MakingEfforts",
  components: {
    GlobalCO2ChangeMap,
  }
}
</script>

<style scoped>
h4 {
  margin-bottom: 0;
}

</style>
