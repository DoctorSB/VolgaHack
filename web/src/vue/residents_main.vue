<template>
  <div>
    <div class="resident">
      <div class="container" v-for="resident in residents" :key="resident.id">
        <div><img :src=resident.image1path alt="{{resident.header}}"></div>
        <div class="header-container"><strong>{{ resident.header }}</strong></div>
        <div class="container-info">{{ resident.information }}</div>
        <div><button class="container-button" @click="LoadInfoPage(resident.info_page_file)">Подробнее</button></div>
      </div>
    </div>
  </div>
</template>

<script>
import residents from "../js/residents.js";

export default {
  mixins: [residents]
}
</script>

<style scoped>
@import "../styles/residents.css";
</style>