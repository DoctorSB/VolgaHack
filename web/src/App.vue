<template>
  <div class="app">
    <form @submit.prevent>
      <h4>Cоздание кластера</h4>
      <input v-bind:value="title"
             @input="title = $event.target.value"
             class="input"
             type="text"
             placeholder="Название">
      <input v-bind:value="body"
             @input="body = $event.target.value"
             class="input"
             type="text"
             placeholder="Описание">
      <button class="button"
              @click="createCluster">Создать
      </button>
    </form>

    <div class="post" v-for="post in posts" :key="post.id">
      <div><strong>Название</strong> {{post.title}}</div>
      <div><strong>Описание</strong> {{post.body}}</div>
    </div>

  </div>
</template>

<script>

export default {
  data() {
    return {
      posts: [],
      title: '',
      body: ''
    }
  },
  methods: {
    createCluster() {
      const newPost = {
        id: Date.now(),
        title: this.title,
        body: this.body
      }
      this.posts.push(newPost)
      this.title = ''
      this.body = ''
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

.app {
  padding: 20px;
}

.post {
  padding: 15px;
  border: 2px solid seagreen;
  margin-top: 15px;
}

form {
  display: flex;
  flex-direction: column;
}

.button {
  margin-top: 15px;
  align-self: flex-end;
  padding: 10px 15px;
  border: 2px solid seagreen;
  background: none;
}

.input {
  width: 100%;
  border: 2px solid seagreen;
  padding: 10px 15px;
  margin-top: 15px;
}
</style>