<template>
  <div id="pagePrincipal">
    <Header :logo="logoCBViagens" />
    <TravelCalculator/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import TravelCalculator from './Pages/TravelCalculator.vue'

export default {
  name: 'App',
  components: {
    Header,
    TravelCalculator
  },
  data(){
    return{
      logoCBViagens: '/imgs/logo.png'
    }
  }
}
</script>

<style>

*{
  font-family: Arial, Helvetica, sans-serif;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

#pagePrincipal{
  display: grid;
  grid-template-columns: 350px 1fr
}

.icon-medium-white{
  font-size: 30px;
  padding-right: 20px;
  color: #FFF;
}

.icon-medium-dark{
  font-size: 30px;
  padding-right: 20px;
  color: #000;
}

.icon-large-white{
  font-size: 40px;
  padding-right: 20px;
  color: #FFF;
}

.icon-large-dark{
  font-size: 40px;
  padding-right: 20px;
  color: #000;
}

.icon-large-blue{
  font-size: 80px;
  /* padding-right: 20px; */
  color: #406C83;
}

</style>
