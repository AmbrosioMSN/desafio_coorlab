<template>
  <div id="header-container">
    <img :src="logo" alt="" class="logo" />
    <div id="header-nav">
      <i class="material-icons icon-medium-white">calculate</i>
      <p>Calculadora de Viagem</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: ["logo"],
};
</script>

<style scoped>
#header-container {
  display: flex;
  flex-direction: column;
  background-color: #2a3041;
  height: 100vh;
  color: #fff;
}

#header-container img{
  cursor: pointer;
}

#header-nav{
  margin-top: 30px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  padding: 20px;
  transition: .2s;
}

#header-nav:hover{
  background-color: #717070;
}

#header-nav p{
    font-size: 20px;
    font-weight: 500;
    letter-spacing: 1.3px;
}

.icon-large{
    font-size: 30px;
    padding-right: 20px;
}

.logo {
  width: 200px;
  height: 30px;
  margin: 30px;
}
</style>