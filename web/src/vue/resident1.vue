<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[0].image1path alt="{{residents[0].header}}"></div>
      <div class="header-container"><strong>{{ residents[0].header }}</strong></div>
      <div class="container-info">{{ residents[0].information }}</div>
    </div>
  </div>
</template>

<script>
import residents from "../js/residents";

export default {
  mixins: [residents]
}

</script>

<style scoped>
@import "../styles/residents.css";
</style>