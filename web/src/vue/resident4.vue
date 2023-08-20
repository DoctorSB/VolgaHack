<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[3].image1path alt="{{residents[3].header}}"></div>
      <div class="header-container"><strong>{{ residents[3].header }}</strong></div>
      <div class="container-info">{{ residents[3].information }}</div>
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