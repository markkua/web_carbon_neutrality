<template>
  <div id="scroll" style="height: 100%">
    <SessionBanner img-url="./img/pexels-scott-webb-1048033.jpg" title="Introduction" subtitle=""/>
    <div class="my-content">
      <SessionIntroduction/>
    </div>

    <SessionBanner img-url="https://ourworldindata.org/uploads/2021/01/data_explorer-featured-768x404.png"
                   title="Recent Situation" subtitle=""/>
    <div class="my-content">
      <RecentSituation/>
    </div>

    <SessionBanner img-url="https://ourworldindata.org/uploads/2021/01/data_explorer-featured-768x404.png"
                   title="We are making efforts" subtitle=""/>
    <div class="my-content">
      <MakingEfforts/>
    </div>

    <SessionBanner img-url="https://ourworldindata.org/uploads/2021/01/data_explorer-featured-768x404.png"
                   title="What can we do" subtitle=""/>
    <div class="my-content">
      <WhatCanWeDo/>
    </div>

    <SessionSource/>
  </div>

</template>

<script>
import {defineComponent} from 'vue'
import SessionBanner from "components/util/SessionBanner";
import SessionIntroduction from "components/content/SessionIntroduction";
import RecentSituation from "components/content/RecentSituation";
import MakingEfforts from "components/content/MakingEfforts";
import WhatCanWeDo from "components/content/WhatCanWeDo";
import SessionSource from "components/content/SessionSource";

export default defineComponent({
  name: 'IndexPage',

  components: {
    SessionBanner,

    SessionIntroduction,
    RecentSituation,
    MakingEfforts,
    WhatCanWeDo,
    SessionSource
  },
})
</script>

<style>
.my-content {
  align-items: center;
  align-content: center;
  align-self: center;
  margin: auto;
  text-align: center;
}

@media (max-width: 699px) {
  .my-content {
    /*height: 100%;*/
    width: 100vw;
    /*max-width: 700px*/
  }
}

@media (min-width: 700px) and (max-width: 999px) {
  .my-content {
    /*height: 100%;*/
    width: 95vw;
    /*max-width: 700px*/
  }
}

/* Limit width on wide screen */
@media (min-width: 1000px) and (max-width: 1199px) {
  .my-content {
    /*height: 100%;*/
    width: 90vw;
    max-width: 900px
  }
}

@media (min-width: 1200px) and (max-width: 1499px) {
  .my-content {
    /*height: 100%;*/
    width: 90vw;
    max-width: 1000px
  }
}

@media (min-width: 1500px) {
  .my-content {
    /*height: 100%;*/
    width: 90vw;
    max-width: 1200px
  }
}

</style>
