<template>
  <div id="main-container">
    <div class="top-container"></div>
    <div class="content-container">
      <div class="card-container">
        <div class="card-header">
          <i class="material-icons icon-large-white">local_shipping</i>
          <p>Calculadora de Viagem</p>
        </div>
        <div class="card-main">
          <SearchTravel :clearForm="clearForm" @updateMostExpensiveTrip="updateMostExpensiveTrip" @updateCheapestTrip="updateCheapestTrip"/>
          <div id="trips-container">
            <Trips :mostExpensiveTrip="mostExpensiveTrip" :cheapestTrip="cheapestTrip" @clear-trips="clearTrips"/>
            <h3 v-if="mostExpensiveTrip === null && cheapestTrip === null">Nenhum dado selecionado.</h3>
        </div>
    </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchTravel from "../components/SearchTravel.vue";
import Trips from "../components/Trips.vue"

export default {
  name: "TravelCalculator",
  components: {
    SearchTravel,
    Trips
  },
  data() {
    return {
      mostExpensiveTrip: null,
      cheapestTrip: null,
      clearForm: false
    };
  },
  methods: {
    updateMostExpensiveTrip(mostExpensiveTrip) {
      this.mostExpensiveTrip = mostExpensiveTrip;
    },
    updateCheapestTrip(cheapestTrip) {
      this.cheapestTrip = cheapestTrip;
    },
    clearTrips() {
      this.mostExpensiveTrip = null;
      this.cheapestTrip = null;
      this.clearForm = true;
      setTimeout(() => this.clearForm = false, 1000)
    }
  }
};
</script>

<style scoped>
#main-container {
  width: 100%;
  height: 100vh;
  display: flex;
  background-color: #f3f3f3;
  display: grid;
  grid-template-rows: 100px 1fr;
}

.top-container {
  top: 0;
  width: 100%;
  background-color: #fff;
  border-bottom: 6px solid #bfbfbf;
}

.content-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-container {
  width: 70vw;
  height: 65vh;
  background-color: #fff;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
}

.card-header {
  width: 100%;
  height: 15%;
  border-radius: 5px 5px 0 0;
  background-color: #2a3041;
  color: #fff;
  display: flex;
  align-items: center;
}

.card-header i {
  margin-left: 50px;
}

.card-header p {
  font-size: 23px;
  font-weight: bold;
  letter-spacing: 1.1px;
}

.card-main {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  padding: 40px 0 20px 20px;
  align-items: center;
  height: 100%;
  width: 100%;
}

#trips-container{
  height: 100%;
  width: 60%;
  color: #575757;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.select-none{
    display: none;
}
</style>