<template>
    <div>
      <h2>Reviews for Car {{ $route.params.carId }}</h2>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          <router-link :to="{ name: 'CarReviewDetail', params: { carId: $route.params.carId, reviewId: review.id }}">
            {{ review.customer.user.username }} - Rating: {{ review.rating }}
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
      fetchReviews() {
        this.reviews = [
          { id: 1, customer: { user: { username: 'JohnDoe' } }, rating: 5 },
          { id: 2, customer: { user: { username: 'JaneSmith' } }, rating: 4 },
          // Add more data as needed
        ];
      },
  
      // Uncomment the following lines when using API
      // fetchReviews() {
      //   const carId = this.$route.params.carId;
      //   axios.get(`/api/cars/${carId}/reviews`)
      //     .then(response => {
      //       this.reviews = response.data;
      //     })
      //     .catch(error => {
      //       console.error('Error fetching reviews:', error);
      //     });
      // },
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
    cursor: pointer;
  }
  
  li:hover {
    text-decoration: underline;
  }
  </style>
  