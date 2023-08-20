<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[2].image1path alt="{{residents[2].header}}"></div>
      <div class="header-container"><strong>{{ residents[2].header }}</strong></div>
      <div class="container-info">{{ residents[2].information }}</div>
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