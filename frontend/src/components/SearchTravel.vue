<template>
  <div class="travelSearch-container">
    <div class="title">
      <i class="material-icons icon-medium-dark">attach_money</i>
      <p>Calcule o Valor da Viagem</p>
    </div>
    <form @submit="postSearchTravel($event)">
      <div class="form-group">
        <label for="destiny">Destino</label>
        <select name="destiny" id="destiny" v-model="city">
          <option :value="null" disabled selected>Selecione o destino</option>
          <option v-for="city in listCity" :key="city" :value="city">
            {{ city }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="">Data</label>
        <flat-pickr
          v-model="date"
          :config="config"
          placeholder="Selecione uma data"
          class="custom-flatpickr"
        ></flat-pickr>
      </div>
      <div class="input-container">
        <input class="btn-submit" type="submit" value="Buscar" />
      </div>
    </form>
    <div v-if="modalOpen" class="modal">
      <div class="modal-content">
        <i class="material-icons icon-large-blue">info</i>
        <p>Insira os valores para realizar a cotação.</p>

        <button @click="closeModal" class="btn-close">Fechar</button>
      </div>
    </div>
  </div>
</template>

<script>
import FlatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Portuguese } from "flatpickr/dist/l10n/pt";

export default {
  name: "SearchTravel",
  props: ["clearForm"],
  components: {
    FlatPickr,
  },
  data() {
    return {
      config: {
        dateFormat: "d/m/Y",
        locale: Portuguese,
      },
      listCity: null,
      date: null,
      city: null,
      mostExpensiveTrip: null,
      cheapestTrip: null,
      modalOpen: false,
    };
  },
  methods: {
    async getCities() {
      try {
        const req = await fetch("http://localhost:3000/cidades");
        const response = await req.json();
        this.listCity = response.cidades;
      } catch (error) {
        console.error("Erro ao buscar cidades:", error);
        this.listCity = [];
      }
    },
    async postSearchTravel(e) {
      e.preventDefault();

      if (this.city == null) {
        this.openModal();
        return;
      }

      if (this.date == null) {
        this.openModal();
        return;
      }

      try {
        const req = await fetch(`http://localhost:3000/viagens/${this.city}`);
        const response = await req.json();
        this.mostExpensiveTrip = response.viagem_mais_cara;
        this.cheapestTrip = response.viagem_mais_barata;

        this.$emit("updateMostExpensiveTrip", this.mostExpensiveTrip);
        this.$emit("updateCheapestTrip", this.cheapestTrip);
      } catch (error) {
        console.error("Erro ao buscar cidades:", error);
        this.listCity = [];
      }
    },
    openModal() {
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
  },
  created() {
    this.getCities();
  },
  watch: {
    clearForm(newVal) {
      if (newVal) {
        this.city = null;
        this.date = null;
      }
    },
  },
};
</script>

<style scoped>
.travelSearch-container {
  background-color: #f3f3f3;
  height: 100%;
  width: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
}

.travelSearch-container .title {
  display: flex;
  align-items: center;
}

.travelSearch-container .title p {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: 1px;
}

.travelSearch-container .title i {
  padding-right: 0;
}

.travelSearch-container form div {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  width: 300px;
}

.travelSearch-container form div label {
  font-weight: bold;
  font-size: small;
  margin-bottom: 10px;
}

.travelSearch-container form div select {
  width: 100%;
  height: 35px;
  border-radius: 5px;
  border: 1px solid #bfbfbf;
  padding-left: 15px;
  color: #575757;
  font-size: medium;
  font-weight: 500;
  cursor: pointer;
}

.travelSearch-container form div .custom-flatpickr {
  width: 100%;
  height: 35px;
  border-radius: 5px;
  border: 1px solid #bfbfbf;
  padding-left: 15px;
  color: #575757;
  font-size: medium;
  font-weight: 500;
}

.input-container {
  display: flex;
  align-items: center;
}

.btn-submit {
  width: 175px;
  height: 30px;
  margin-top: 40px;
  color: #000;
  border-radius: 5px;
  border: 1px solid transparent;
  background-color: #03a8b4;
  cursor: pointer;
  font-weight: bold;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  width: 40vw;
  height: 30vh;
  padding: 20px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.modal-content p {
  font-size: 25px;
  font-weight: 500;
}

.btn-close {
  width: 175px;
  height: 30px;
  margin-top: 40px;
  color: #000;
  border-radius: 5px;
  border: 1px solid transparent;
  background-color: #03a8b4;
  cursor: pointer;
  font-weight: bold;
}
</style>