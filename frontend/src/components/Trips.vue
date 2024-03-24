<template>
  <div id="container" v-if="mostExpensiveTrip && cheapestTrip">
    <div class="infos-trips">
      <div class="text">
        <p>
          Estas são as melhores alternativas de viagem para a data selecionada
        </p>
      </div>
      <div class="info-container">
        <div class="card">
          <div class="trip">
            <i class="material-icons icon-medium-dark">attach_money</i>
            <div class="description">
              <h3>{{ mostExpensiveTrip.name }}</h3>
              <p>Leito: <span>{{mostExpensiveTrip.bed}}(Completo)</span></p>
              <p>Tempo estimado: <span>{{mostExpensiveTrip.duration}}</span></p>
            </div>
          </div>
          <div class="price">
            <h3>Preço</h3>
            <p>{{ mostExpensiveTrip.price_confort }}</p>
          </div>
        </div>
        <div class="card">
          <div class="trip">
            <i class="material-icons icon-medium-dark">schedule</i>
            <div class="description">
              <h3>{{ cheapestTrip.name }}</h3>
              <p>Poltrona: <span>{{cheapestTrip.seat}}(Convercional)</span></p>
              <p>Tempo estimado: <span>{{cheapestTrip.duration}}</span></p>
            </div>
          </div>
          <div class="price">
            <h3>Preço</h3>
            <p>{{cheapestTrip.price_econ}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="btn-container">
      <button class="btn-clear" @click="clearTrips">Limpar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Trips",
  props: {
    mostExpensiveTrip: {
      type: Object,
      default: null,
    },
    cheapestTrip: {
      type: Object,
      default: null,
    },
  },
  methods: {
    clearTrips() {
      this.$emit('clear-trips');
    }
  }
};
</script>

<style scoped>
#container {
  width: 90%;
  height: 100%;
  display: grid;
  grid-template-rows: 1fr 50px;
}

.infos-trips {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.text {
  width: 70%;
}

.text p {
  font-weight: bold;
}

.info-container {
  display: flex;
  flex-direction: column;
}

.card {
  display: grid;
  grid-template-columns: 1fr 150px;
  margin-top: 20px;
}

.trip {
  display: flex;
  align-items: center;
  background-color: #f3f3f3;
  border-radius: 10px;
}

.trip i {
  padding: 30px;
  background-color: #03a8b4;
  color: #fff;
  border-radius: 10px 0 0 10px;
}

.description {
  margin-left: 30px;
  color: #000;
}

.price {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 20px;
  color: #000;
  background-color: #f3f3f3;
  border-radius: 10px;
}

.price p {
  margin: 10px 0px 0px 10px;
}

.btn-container {
  display: flex;
  align-items: center;
  justify-content: end;
}

.btn-clear {
  width: 175px;
  height: 30px;
  margin-top: 40px;
  color: #000;
  border-radius: 5px;
  border: 1px solid transparent;
  background-color: #f3a531;
  cursor: pointer;
  font-weight: bold;
}
</style>