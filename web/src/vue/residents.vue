<template>
  <div class="resident">
    <div class="container" v-for="resident in residents" :key="resident.id">
      <div><img :src=resident.image1path alt="{{resident.header}}"></div>
      <div class="header-container"><strong>{{resident.header}}</strong></div>
      <div class="container-info">{{resident.information}}</div>
      <div><button class="container-button" @click="LoadInfoPage(resident.info_page_file)">Подробнее</button></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      residents: [
        {id: 0, image1path: '/images/image1.jpg', header: 'Бар "Куйбышева"', information: 'Танцевальный бар с прекрасной волжской кухней и живыми концертами.', info_page_file: '1'},
        {id: 1, image1path: '/images/image2.jpg', header: 'Монобар "Проходная', information: 'Монобар с говорящим названием, который перенесет тебя совершенно в другое место - проходную советского завода.', info_page_file: '2'},
        {id: 2, image1path: '/images/image3.jpg', header: 'Ulandy Cafe', information: 'Еда на каждый день, которую удобно взять с собой! Наш гравный принцип - супер фреш.', info_page_file: '3'},
        {id: 3, image1path: '/images/image4.jpg', header: 'Бистро "Зозо"', information: 'Современное ретро Битсро с открытой кухней.', info_page_file: '4'}
      ],
    }
  },
  methods: {
    LoadInfoPage(path) {
      window.location.href = path;
    }
  }
}
</script>

<style scoped>
@import "../styles/residents.css";
</style>