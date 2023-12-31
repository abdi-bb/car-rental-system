<template>
    <div>
      <h2>Booking Detail</h2>
      <div v-if="booking">
        <p>Customer: {{ booking.customer.user.username }}</p>
        <p>Car: {{ booking.car.name }}</p>
        <p>Booking Date: {{ booking.start_date }}</p>
        <!-- Add more details as needed -->
      </div>
      <div v-else>
        <p>Booking not found</p>
      </div>
    </div>
  </template>
  
  <script>
  // Import axios library
  import axios from 'axios';
  
  export default {
    data() {
      return {
        booking: null,
      };
    },
    methods: {
      // For testing purposes, use hardcoded data
      fetchBookingData() {
        this.booking = {
          id: 1,
          customer: { user: { username: 'JohnDoe' } },
          car: { name: 'BMW' },
          start_date: '2023-03-01',
          // Add more data as needed
        };
      },
  
      // Uncomment the following lines when using API
      // fetchBookingData() {
      //   axios.get(`/api/bookings/${this.$route.params.id}`)
      //     .then(response => {
      //       this.booking = response.data;
      //     })
      //     .catch(error => {
      //       console.error('Error fetching booking data:', error);
      //       this.booking = null;
      //     });
      // },
    },
    created() {
      this.fetchBookingData();
    },
  };
  </script>
  