<template>
  <div id="scroll" style="height: 100%">
<!--    <SessionBanner img-url="./img/pexels-scott-webb-1048033.jpg" title="Global warming and carbon neutrality" subtitle=""/>-->

    <CoverPage />

    <LimitWidth>
      <SessionIntroduction/>
    </LimitWidth>

    <SessionBanner img-url="img/unsplash-chimney.jpg"
                   title="Recent Situation" subtitle=""/>
    <!--    <div class="my-content">-->
    <RecentSituation/>
    <!--    </div>-->

    <SessionBanner img-url="img/unsplash-solar_panel.jpg"
                   title="We are making efforts" subtitle=""/>
    <!--    <div class="my-content">-->
    <MakingEfforts/>
    <!--    </div>-->

    <SessionBanner img-url="img/pixabay-trees.jpg"
                   title="What else can we do?" subtitle=""/>
    <!--    <div class="my-content">-->
    <WhatCanWeDo/>
    <!--    </div>-->

    <SessionSource/>
  </div>

</template>

<script>
import {defineComponent} from 'vue'
import CoverPage from "components/util/CoverPage";
import SessionBanner from "components/util/SessionBanner";
import SessionIntroduction from "components/content/SessionIntroduction";
import RecentSituation from "components/content/RecentSituation";
import MakingEfforts from "components/content/MakingEfforts";
import WhatCanWeDo from "components/content/WhatCanWeDo";
import SessionSource from "components/content/SessionSource";
import LimitWidth from "components/util/LimitWidth";

export default defineComponent({
  name: 'IndexPage',

  components: {
    SessionBanner,
    LimitWidth,
    CoverPage,
    SessionIntroduction,
    RecentSituation,
    MakingEfforts,
    WhatCanWeDo,
    SessionSource
  },
})
</script>

<style>

</style>
