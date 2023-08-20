<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[1].image1path alt="{{residents[1].header}}"></div>
      <div class="header-container"><strong>{{ residents[1].header }}</strong></div>
      <div class="container-info">{{ residents[1].information }}</div>
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