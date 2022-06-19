<template>

  <div>
    <LimitWidth>
      <h4>Pledges</h4>
<!--      <div style="width: 80%">-->
<!--        <img src="img/net-zero-targets.png" alt="net zero targets">-->
<!--      </div>-->
      <div>
        <div class="text-body1">
          Many countries and regions have announced dates by which they want to be carbon neutral, with many of them
          targeting the year 2050. Some of them have already written the pledge into policy and even laws.
          <br/><br/>
          Not only countries and regions but also companies and organizations are taking active reactions towards
          carbon
          neutrality, including many unicorn corporations.
          <br/><br/>
          Find out more details <a href="https://en.wikipedia.org/wiki/Carbon_neutrality#Pledges">here</a> .
        </div>
      </div>
    </LimitWidth>


    <h4>Reducing emissions</h4>
    <LimitWidth>
      <div class="text-body1">
        This interactive map shows the year-on-year growth rate of CO<sub>2</sub> emissions.
        The value is the difference between the current year and the previous year (e.g. change shown in the year 2020 is the
        difference between emission in 2020 and emission in 2019)
        <br/><br/>
        Considering the sink capacity can not expand in a short temporal period, the world needs large and fast
        reductions in emissions to reach net-zero emissions.
        <br/><br/>
        Towards carbon neutrality, our society not only pledges but also takes actual measures to control carbon
        emissions. In the meantime, more and more people are getting aware of this problem and are starting to reduce their
        carbon footprint. From this map, we can see how much effort have been made in different countries and regions.
      </div>
    </LimitWidth>
    <h5 class="caption">CO<sub>2</sub> emission change in 2001-2020 (minus previous year)</h5>
    <GlobalCO2ChangeMap/>

  </div>

  <h4>More clean (renewable) energy</h4>
  <LimitWidth>
    <div class="text-body1">
      In this industrial age, reducing energy consumption is an almost impossible task. However, we can obtain
      electricity
      and other forms of energy from zero or low carbon energy sources, especially renewable energy,
      such as wind power, nuclear power, hydropower, solar power, and geothermal.
      <br/><br/>
      This interactive map shows the change in renewable energy generation relative to the previous year, measured in
      terawatt-hours.
      This is the sum of energy from hydropower, solar, wind, geothermal, wave and tidal, and bioenergy.
    </div>
  </LimitWidth>
  <h5 class="caption">Renewable energy growth in 2000-2020</h5>
  <GlobalCleanEnergyChange/>


</template>

<script>
import GlobalCO2ChangeMap from "components/maps/GlobalCO2ChangeMap";
import GlobalCleanEnergyChange from "components/maps/GlobalCleanEnergyChange";
import LimitWidth from "components/util/LimitWidth";

export default {
  name: "MakingEfforts",
  components: {
    LimitWidth,
    GlobalCO2ChangeMap,
    GlobalCleanEnergyChange,
  }
}
</script>

<style scoped>
.caption {
  margin-bottom: 0;
}

.text-body1 {
  text-align: left;
}

img {
  max-width: 100%;
}


</style>
