<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[0].image alt="{{residents[0].title}}"></div>
      <div class="header-container"><strong>{{ residents[0].title }}</strong></div>
      <div class="container-info">{{ residents[0].info }}</div>
    </div>
  </div>
</template>

<script>
import residents from "@/scripts/residents";

export default {
  mixins: [residents]
}

</script>

<style scoped>
@import "@/styles/style.css";
</style>