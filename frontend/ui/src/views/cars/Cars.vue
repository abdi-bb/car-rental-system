<template>
    <h1>Cars</h1>
    <div v-for="car in cars" :key="car.id" class="car">
      <router-link :to="{ name: 'CarDetail', params: { id: car.id }}">
      <h2>{{ car.name }}</h2>
      </router-link>
    </div>  
  </template>
  
  <script>
  
  export default {
    name: 'Cars',
  components: {  },
    data() {
        return {
            cars: [
                { name: 'BMW', model: '2024', id: 1, desc: 'description' },
                { name: 'BMW', model: '2024', id: 2, desc: 'description' },
                { name: 'BMW', model: '2024', id: 3, desc: 'description' },
                { name: 'BMW', model: '2024', id: 4, desc: 'description' }

            ]
        }
    }
  }
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
  