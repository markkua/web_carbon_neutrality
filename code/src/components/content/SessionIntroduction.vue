<template>
  <SessionBanner
    img-url="./img/pexels-scott-webb-1048033.jpg"
    title="Introduction"
    subtitle=""/>
  <!--    TODO: change cover  -->


  <h3>Impact of green house gasses</h3>
  <div>
    [Text]
  </div>
  <div>
    [Photo]
  </div>
  <div>
    <div>
      [Line chart] Temperature anomaly
    </div>
    [Text]
  </div>
  <!--  TODO: -->

  <h3>What is carbon neutralization</h3>
  <div>
    [Text]
  </div>

  <h3>How to achieve carbon neutralization</h3>
  <div class=" row wrap justify-center items-start content-start">
    <div style="max-width: 48vw; min-width: 20vw">
      <h5>Reducing emissions</h5>
      <!--     TODO -->
    </div>
    <div style="max-width: 48vw; min-width: 20vw">
      <h5>Carbon offsetting</h5>
      <!--      TODO -->
    </div>
  </div>


</template>


<script>

import SessionBanner from "components/util/SessionBanner";

export default {
  name: "SessionIntroduction",
  components: {
    SessionBanner
  }
}
</script>


<style scoped>

</style>
