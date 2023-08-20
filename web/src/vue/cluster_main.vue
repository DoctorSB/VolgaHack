<template>
  <div class="cluster">
      <div class="container" v-for="cluster in clusters" :key="cluster.id">
        <div class="header-container"><strong>{{ cluster.title }}</strong></div>
        <div><img :src=cluster.image alt="{{cluster.title}}"></div>
        <div class="container-info">{{ cluster.info }}</div>
        <div class="container-info"> Типо график </div>
        <div><button class="container-button" @click="LoadInfoPage(cluster.resident_path)">Подробнее</button></div>

      </div>
    </div>
</template>

<script>
import cluster from "@/scripts/cluster";

export default {
  mixins: [cluster]
}
</script>

<style>
@import "@/styles/style.css";
</style>