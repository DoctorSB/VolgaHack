<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[3].image alt="{{residents[3].title}}"></div>
      <div class="header-container"><strong>{{ residents[3].title }}</strong></div>
      <div class="container-info">{{ residents[3].info }}</div>
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