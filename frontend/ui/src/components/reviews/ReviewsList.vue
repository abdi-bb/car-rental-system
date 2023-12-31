<template>
    <div>
      <h2>Reviews List</h2>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          <router-link :to="{ name: 'ReviewDetail', params: { id: review.id }}">
            {{ review.customer.username }} - {{ review.car.name }} - Rating: {{ review.rating }}
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        reviews: [],
      };
    },
    methods: {
      // For testing purposes, use hardcoded data
      // fetchReviews() {
      //   this.reviews = [
      //     { id: 1, customer: { user: { username: 'JohnDoe' } }, car: { name: 'BMW' }, rating: 5 },
      //     { id: 2, customer: { user: { username: 'JaneSmith' } }, car: { name: 'Nissan' }, rating: 4 },
      //     // Add more data as needed
      //   ];
      // },
  
      // Uncomment the following lines when using API
      fetchReviews() {
        axios.get(`http://127.0.0.1:8000/api/v1/cars/${this.$route.params.carId}/reviews`)
          .then(response => {
            this.reviews = response.data;
          })
          .catch(error => {
            console.error('Error fetching reviews:', error);
          });
      },
    },
    created() {
      this.fetchReviews();
    },
  };
  </script>
  
  <style>
  /* Add your styles here if needed */
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
    padding: 10px;
    background-color: #f4f4f4;
    border-radius: 8px;
    cursor: pointer;
  }
  
  li:hover {
    background-color: #ddd;
  }
  
  router-link {
    text-decoration: none;
    color: #333;
  }
  </style>
  