<template>
  <div class="app">
    <div class="resident">
      <div class="container" v-for="resident in residents" :key="resident.id">
        <div><img :src=resident.image1path alt="{{resident.header}}"></div>
        <div class="header-container"><strong>{{resident.header}}</strong></div>
        <div class="container-info">{{resident.information}}</div>
        <div><button class="container-button" @click="LoadInfoPage(resident.info_page_file)">Подробнее</button></div>
      </div>
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
      console.log(path)
    }
  }
}

</script>


<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.resident {
  padding-top: 20px;
}

.container {
  width: 75vw;
  max-width: 100%;
  margin: 0 auto;
  padding-bottom: 50px;
}

.container img {
  width: 100%;
  height: auto;
}

.header-container {
  padding-top: 10px;
  text-align: center;
  text-decoration: underline;
  text-decoration-color: red;
  color: black;
  font-size: 24px;
  padding-bottom: 10px;
}

.container-info {
  text-align: center;
  font-size: 18px;
  padding-bottom: 10px;
}

.container-button {
  border: none;
  background-color: transparent;
  text-decoration: underline;
  text-decoration-color: red;
  color: black;
  cursor: pointer;
  font-size: 18px;
  display: block;
  margin: 0 auto;
}

.container-button:hover {
  background-color: #934c50;
  color: black;
}

</style>