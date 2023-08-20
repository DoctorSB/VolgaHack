<template>
  <div>
    <div class="resident">
      <div class="container" v-for="resident in residents" :key="resident.id">
        <div><img :src=resident.image alt="{{resident.title}}"></div>
        <div class="header-container"><strong>{{ resident.title }}</strong></div>
        <div class="container-info">{{ resident.info }}</div>
        <div><button class="container-button" @click="LoadInfoPage(resident.push_path)">Подробнее</button></div>
      </div>
    </div>
  </div>
</template>

<script>
import residents from "@/scripts/residents.js";

export default {
  mixins: [residents]
}
</script>

<style scoped>
@import "@/styles/style.css";
</style>