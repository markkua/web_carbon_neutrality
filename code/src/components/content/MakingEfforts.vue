<template>

  <div>
    <h3>Less green house gas emissions</h3>
    <h4>CO<sub>2</sub> emission change from 2001 to 2020 (minus previous year)</h4>
    <GlobalCO2ChangeMap />

  </div>

  <h3>More clean energy</h3>
  <h4>Clean energy growth</h4>
  <GlobalCleanEnergyChange />

  <h3>Less deforestation</h3>
  <h4>[Line chart] deforestation and reforestation (copy from deforestation project)</h4>


</template>

<script>
import GlobalCO2ChangeMap from "components/maps/GlobalCO2ChangeMap";
import GlobalCleanEnergyChange from "components/maps/GlobalCleanEnergyChange";

export default {
  name: "MakingEfforts",
  components: {
    GlobalCO2ChangeMap,
    GlobalCleanEnergyChange,
  }
}
</script>

<style scoped>
h4 {
  margin-bottom: 0;
}

</style>
