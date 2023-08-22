<template>
  <div class="resident">
    <div class="container">
      <div><img :src=residents[3].image alt="{{residents[3].title}}" class="resident-image"></div>
      <div class="header-container-resident"><strong>{{ residents[3].title }}</strong></div>
      <div class="container-info">{{ residents[3].info }}</div>

      <div class="container-hashtag">
        <span class="hashtag">#вкуснаяеда</span>
        <span class="hashtag">#классныеконцерты</span>
        <span class="hashtag">#приятнаямузыка</span>
      </div>

      <div class="resident-info show">
        <div class="resident-info-title"><strong>Информация</strong></div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Площадь:</div>
          <div class="resident-info-stats-number">130м²</div>
        </div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Количество сидячих мест:</div>
          <div class="resident-info-stats-number">60</div>
        </div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Средний чек:</div>
          <div class="resident-info-stats-number">1500р</div>
        </div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Время работы:</div>
          <div class="resident-info-stats-number">08:00 - 20:00</div>
        </div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Email</div>
          <div class="resident-info-stats-number"><a href="https://google.com">resident@gmail.com</a></div>
        </div>

        <div class="resident-info-block">
          <div class="resident-info-stats">Telegram</div>
          <div class="resident-info-stats-number"><a href="https://google.com">t.me/resident</a></div>
        </div>
      </div>

      <div><img :src="residents[3].showimage" alt="Image" class="resident-image"></div>

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