<template>
  <div>
    <h1>Cars</h1>
    <div v-for="car in cars" :key="car.id" class="car">
      <router-link :to="{ name: 'CarDetail', params: { id: car.id }}">
        <h2>{{ car.name }}</h2>
      </router-link>
      <router-link :to="{ name: 'CarReviewsList', params: { carId: car.id }}">
        <p>View Reviews</p>
      </router-link>
    </div>
  </div>
</template>

<script>
// Import axios library
import axios from 'axios';

export default {
  name: 'CarsList',
  components: {},
  data() {
    return {
      cars: [],
    };
  },
  // Use the created lifecycle hook to fetch data when the component is created
  created() {
    // Uncomment the following lines when using API
    // Replace 'your-api-endpoint' with the actual endpoint
    axios.get('http://127.0.0.1:8000/api/v1/cars/')
      .then(response => {
        // Update the 'cars' data with the received data
        this.cars = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    // For testing and development, you can keep the hardcoded data
    // this.cars = [
    //   { name: 'BMW', model: '2024', id: 1, desc: 'description' },
    //   { name: 'Nissan', model: '2024', id: 2, desc: 'description' },
    //   { name: 'Suzuki', model: '2024', id: 3, desc: 'description' },
    //   { name: 'Tucson', model: '2024', id: 4, desc: 'description' },
    // ];
  },
};
</script>

<style>
.car h2 {
  background: #f4f4f4;
  padding: 20px;
  border-radius: 10px;
  margin: 10px auto;
  max-width: 600px;
  cursor: pointer;
  color: #444;
}

.car h2:hover {
  background: #ddd;
}

.car a {
  text-decoration: none;
}
</style>
