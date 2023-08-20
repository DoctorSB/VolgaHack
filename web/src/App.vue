<template>
  <div class="app"></div>
  <header>
    <div class="logo"><strong>Cluster+</strong></div>
    <input type="checkbox" id="toggle">
    <label for="toggle" class="burger-menu">&#9776;</label>
  </header>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;700&family=Roboto+Mono&display=swap" rel="stylesheet">
  <router-view></router-view>
</template>


<script>
export default {}
</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

header {
  width: 100vw;
  background-color: #333;
  color: #fff;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Roboto Mono', monospace;
}

nav ul li {
  display: inline-block;
  margin-right: 10px;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

.burger-menu {
  display: none;
  font-size: 24px;
  cursor: pointer;
}

@media (max-width: 768px) {
  .logo {
    font-size: 30px;
  }

  nav ul {
    display: none;
  }

  .burger-menu {
    display: block;
  }

  #toggle {
    display: none;
  }

  #toggle:checked ~ nav ul {
    display: block;
  }
}
</style>