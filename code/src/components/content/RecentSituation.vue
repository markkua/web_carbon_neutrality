<template>

  <LimitWidth>
    <div>
      <h4>Global emissions have not yet peaked</h4>
      <div class="text-body1">
        As explained above, there are 2 method to reach carbon net-zero: reducing emissions and offsetting.
        The goal is to stabilize (or even reduce) concentrations of CO2 in the atmosphere.
        <br/><br/>

        The interactive figure below shows the combined components of the global carbon budget, including main source of
        emissions (fossil emission and land-use change emissions) and carbon sinks(cement, ocean, and land).
        The remaining part then goes into the atmosphere sink.
        <br/><br/>

        Although we can find the emission growth gradually slows down, the global emissions keep growing and have not
        yet peaked.
        Considering the sink capacity can not expand in a short temporal period, the world need large and fast
        reductions in emissions
        to reach reach net-zero emissions.
      </div>

      <h5 class="caption">Global carbon emission and carbon sinks in 2000-2020</h5>
      <CarbonBudgetBarChart/>
    </div>
  </LimitWidth>


  <LimitWidth>
    <h4>Who are the "big players" of carbon emissions</h4>
    <div>
      <div style="float: right">
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ipVxxxqwBQw"
                title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
      </div>

      <div class="text-body1">
        The world’s largest <b>per capita</b> carbon dioxide emitters are the major oil producing countries; this is particularly true for those with relatively low population size.
        However more populous countries with some of the highest per capita emissions therefore have high total emissions.
        <br/><br/>

        Many of the world’s <b>largest emitters today</b> are in Asia. Asia is by far the largest emitter, accounting for 53% of global emissions.
        However, as it is home to 60% of the world’s population this means that per capita emissions in Asia are slightly lower than the world average.
        And Asia’s rapid rise in emissions has only occurred in very recent decades.
        <br/><br/>

        <b>Historically</b>, since 1751 the world has emitted over 1.5 trillion tonnes of CO<sub>2</sub>. To reach our climate goal of
        limiting average temperature rise to 2°C, the world needs to urgently reduce emissions.
        One common argument is that those countries which have added most to the green house gasses in our atmosphere –
        contributing most to the problem today – should take on the greatest responsibility in tackling it.

      </div>
    </div>

  </LimitWidth>

  <h5 class="caption">Green house gas emission in 2000-2020</h5>
  <GlobalGHGMap/>



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
.caption {
  margin-bottom: 0;
}

.text-body1 {
  text-align: left;
}

.half_card {
  max-width: max(500px, 50%);
  min-width: 20vw;
  padding: 20px;
}
</style>
