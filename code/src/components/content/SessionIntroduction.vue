<template>
  <div>
    <!--    <h3>Global warming</h3>-->
    <div class="text-body2" style=" text-align: left; padding: 20px">
      Impact of global warming: xxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxx xxxxxx xxxxx xxxxxxxxxxx xxxx xxxxxxxx xxxxxxxxxxx
      xxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxx xxxxxx xxxxx xxxxxxxxxxx xxxx xxxxxxxx xxxxxxxxxxx xxxxxxx xxxxx xxxxxx xxxxx
      xxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxx xxxxxx xxxxx xxxxxxxxxxx xxxx xxxxxxxx xxxxxxxxxxx xxxxxxx xxxxx xxxxxx xxxxx
    </div>
    <div class="row wrap justify-center items-start content-start">
      <div class="image_card">
        <img src="img/pexels-andrea-schettino-3923277.jpg" width="100%" alt="global warming">
      </div>
      <div class="image_card">
        <img src="img/pexels-andrea-schettino-3923277.jpg" width="100%" alt="global warming">
      </div>
    </div>

    <h4>Main cause: green house gasses</h4>
    <div class=" row wrap justify-center">
      [Line chart] Temperature anomaly
      <!--        <img src="img/anomaly.png" width="100%">-->
      What is temperature anomaly.

      <TempAnomalyLineChart/>

    </div>


    <h3>What is carbon neutralization</h3>
    <div>
      [Text]
      <img src="img/carbon_cycle_schematic.png" width="100%">
    </div>

    <h3>How to achieve carbon neutralization</h3>
    <div class=" row wrap justify-center items-start content-start">
      <div class="half_card">
        <h5>Reducing emissions</h5>
        <div class="text-body2">
          Reducing carbon emissions can be done by moving towards energy sources and industry processes that produce
          less
          greenhouse gases,
          thereby transitioning to a low-carbon economy. Shifting towards the use of renewable energy such as wind,
          geothermal, and solar power, as well as nuclear power reduces greenhouse gas emissions.
          Although both renewable and non-renewable energy production produce carbon emissions in some form, renewable
          sources produce negligible to almost zero carbon emissions. Transitioning to a low-carbon economy would also
          mean
          making changes to current industrial and agricultural processes to reduce carbon emissions, for example, diet
          changes to livestock such as cattle can potentially reduce methane production by 40%. Carbon projects and
          emissions trading are often used to reduce carbon emissions, and carbon dioxide can even sometimes be
          prevented
          from entering the atmosphere entirely (such as by carbon scrubbing).
          <!--     TODO -->
        </div>
      </div>
      <div class="half_card">
        <h5>Carbon offsetting</h5>
        <div class="text-body2">
          Balancing carbon dioxide emissions with carbon offsets — the process of reducing or avoiding greenhouse gas
          emissions
          or removing carbon dioxide from the atmosphere to make up for emissions elsewhere.
          If the total greenhouse gases emitted is equal to the total amount avoided or removed, then the two effects
          cancel
          each other out and the net emissions are 'neutral'.
          <!--      TODO -->
          Carbon sinks:
          Carbon sinks are vast ecosystems that absorb CO2. They regulate the climate and stop global warming. As they
          are
          exploited, many are releasing their carbon stores.
          Check <a
          href="https://edition.cnn.com/videos/world/2020/12/17/carbon-sinks-explained-c2e-intl-lon-orig.cnn/video/playlists/call-to-earth/">
          this video</a> for more details
        </div>
      </div>
    </div>
  </div>


</template>


<script>
import TempAnomalyLineChart from "components/charts/TempAnomalyLineChart";

export default {
  name: "SessionIntroduction",
  components: {
    TempAnomalyLineChart,
  }
}
</script>


<style scoped>

.half_card {
  max-width: 500px;
  min-width: 20vw;
  padding: 20px;
}

.image_card {
  width: 50%;
  min-width: 300px;
  max-width: 800px;
  padding: 20px;
}

.text-body2 {
  text-align: left;
}


</style>
