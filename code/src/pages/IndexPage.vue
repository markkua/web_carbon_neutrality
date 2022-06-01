<template>

  <div id="scroll" style="height: 100%">

    <SessionIntroduction/>

    <RecentSituation/>

    <WhereAreWe/>

    <WhatCanWeDo/>

    <SessionSource/>

  </div>

</template>

<script>
import { defineComponent } from 'vue'
import SessionIntroduction from "components/content/SessionIntroduction";
import RecentSituation from "components/content/RecentSituation";
import WhereAreWe from "components/content/WhereAreWe";
import WhatCanWeDo from "components/content/WhatCanWeDo";
import SessionSource from "components/content/SessionSource";


export default defineComponent({
  name: 'IndexPage',

  components: {
    SessionIntroduction,
    RecentSituation,
    WhereAreWe,
    WhatCanWeDo,
    SessionSource
  },
})
</script>
