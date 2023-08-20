<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[2].image alt="{{residents[2].title}}"></div>
      <div class="header-container"><strong>{{ residents[2].title }}</strong></div>
      <div class="container-info">{{ residents[2].info }}</div>
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