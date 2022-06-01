<template>
  <SessionBanner
    img-url="https://ourworldindata.org/uploads/2021/01/data_explorer-featured-768x404.png"
    title="Where are we on the way"
    subtitle=""/>
  <!--  TODO: change image -->

  <div>
    <h3>Emission reduction</h3>
    [Map] emission change from 2015 to 2020: by country per capita
    <div>
      <h4>Clean energy percentage change</h4>
      [Map]
      [Line chart]

    </div>
  </div>

  <div>

  </div>


</template>

<script>

import SessionBanner from "components/util/SessionBanner";


export default {
  name: "WhereAreWe",
  components: {
    SessionBanner
  }
}
</script>

<style scoped>

</style>
