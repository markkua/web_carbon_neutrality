<template>
  <SessionBanner
    img-url="https://ourworldindata.org/uploads/2021/01/data_explorer-featured-768x404.png"
    title="Recent Situation"
    subtitle=""/>

  <div>
    <h4>[MAP] Green house gas emission (per capita)</h4>
  </div>

  <div>
    <h4>[multi line chart] Emission type</h4>
  </div>


</template>


<script>

import SessionBanner from "components/util/SessionBanner";

export default {
  name: "RecentSituation",
  components: {
    SessionBanner
  }
}
</script>


<style scoped>

</style>
