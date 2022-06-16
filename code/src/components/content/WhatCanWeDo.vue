<template>


  <div>
    <LimitWidth>
      <h4>Working together as a whole</h4>
      <div class="text-body1">
        Climate change is a global problem, and no country alone can fix it. Working out who is responsible is not as
        simple
        as it seems, and it's a draft question. Plaguing this question in the international politics no longer helps
        solving the problem.
        <br/><br/>
        We don't have much time left. Everybody needs to do their best, from <b>today</b> instead of tomorrow.
      </div>

      <h4>What can we do as individuals</h4>

      <div class="text-body1">
        <div style="float: right; width: 40%">
          <img src="img/transport_emission.png" alt="transport emission">
        </div>

        <b>On the Road, in the Sky.</b>
        According to 2017 <a href="http://iopscience.iop.org/article/10.1088/1748-9326/aa7541/pdf">study</a>
        from researchers at Lund University and the University of British Columbia,
        going carless for a year could save about 2.6 tons of carbon dioxide. So, <b>try taking a train, bus or better yet, ride a bike.</b>
        One may argue that driving electric cars has no emission. However, the emission doesn't disappear, it's shifted to
        the power station. Considering the percentage of clean energy we are using, saving energy by driving less is still a better option.
        <br/><br/>

        <b>On Your Plate.</b>
        Firstly, <b>don't waste food</b>. Food production accounts for one quarter - 26% - of global green house gas emission.
        Food waste is responsible for 6% of global greenhouse gas emissions
        <small>(<a href="https://ourworldindata.org/environmental-impacts-of-food#food-waste-is-responsible-for-6-of-global-greenhouse-gas-emissions">source</a>)</small>.

        Secondly, <b>reduce meet consumption</b>.
        Overall, eating low down the food chain as often as you can is a probably a good way to reduce your carbon footprint and stay healthy.
        Check <a href="http://studymaps.ethz.ch/sustainability-atlas/meat-consumption">this atlas</a> for more details.
        <br/><br/>

        <b>In Your Home.</b>
        You can <b>save much energy</b> in your daily life by simple actions, such as turning down the heat,
        turning off lights when you leave, replacing with LED lights, replacing old fridges.
        On the other hand, <b>recycling as much as possible</b> not only saves materials, but also reduces carbon emissions
        of the factory.
        <br/><br/>

        <b>What You Do.</b>
        In addition to changing your day-to-day habits, exercising your rights as a customer or a citizen is one of
        the most significant things you can do to help the planet, for example, supporting sustainable products, environment-friendly business and politics.

        <br/><br/>
        Try to calculate your carbon footprint using this
        <a href="https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/?redirect=https-301">calculator</a>.
      </div>


      <h6>
        For a more detailed explanation of carbon neutrality, please check this video:
      </h6>
      <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9pPsso2acew"
              title="YouTube video player" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen></iframe>

    </LimitWidth>
  </div>

</template>

<script>
import LimitWidth from "components/util/LimitWidth";

export default {
  name: "WhatCanWeDo",
  components: {LimitWidth}
}
</script>

<style scoped>
.text-body1 {
  text-align: left;
}

img {
  max-width: 100%;
}
</style>
