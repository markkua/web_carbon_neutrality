<template>
  <div class="cover">
    <div class="callout">
      <!-- <h1>Global trade</h1> -->
      <h3>Carbon neutrality -- where are we on the way to it?</h3>


    </div>
  </div>
</template>

<script>
export default {
  name: "CoverPage"
}
</script>

<style scoped>
.cover {
  background-image: url("../../../public/img/unsplash-windmill.jpg");
  background-repeat: no-repeat;
  background-size: 100vw;
  background-attachment: fixed;
  /*background-size: cover;*/

  height: 500px;
  width: 100vw;
}

.callout {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100%;
  text-align: center;
  position: relative;
  z-index: 10;
  width: 70%;
  margin: auto;
/*@media (max-width: 767px) {*/
/*  width: 90%;*/
/*}*/
}

h3 {
  text-align: center;
  font-weight: bold;
  color: #4db6ac;
  /* width: 50%; */
  min-width: 375px;
  margin: auto;
}

</style>
