<template>
    <div>
      <h2>Review Detail</h2>
      <div v-if="review">
        <p>Customer: {{ review.customer.user.username }}</p>
        <p>Car: {{ review.car.name }}</p>
        <p>Rating: {{ review.rating }}</p>
        <p>Description: {{ review.description }}</p>
        <!-- Add more details as needed -->
      </div>
      <div v-else>
        <p>Review not found</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        review: null,
      };
    },
    methods: {
      // For testing purposes, use hardcoded data
      // fetchReviewData() {
      //   this.review = {
      //     id: 1,
      //     customer: { user: { username: 'JohnDoe' } },
      //     car: { name: 'BMW' },
      //     rating: 5,
      //     description: 'Great car!',
      //     // Add more data as needed
      //   };
      // },
  
      // Uncomment the following lines when using API
      fetchReviewData() {
        const carId = this.$route.params.carId;
        const reviewId = this.$route.params.reviewId;
        axios.get(`http://127.0.0.1:8000/api/v1/cars/${carId}/reviews/${reviewId}`)
          .then(response => {
            this.review = response.data;
          })
          .catch(error => {
            console.error('Error fetching review data:', error);
            this.review = null;
          });
      },
    },
    created() {
      this.fetchReviewData();
    },
  };
  </script>
  
  <style>
  /* Add your styles here if needed */
  </style>
  