<template>
    <div>
      <h2>Bookings List</h2>
      <ul>
        <li v-for="booking in bookings" :key="booking.id">
          <router-link :to="{ name: 'BookingDetail', params: { id: booking.id }}">
            {{ booking.customer.user.username }} - {{ booking.car.name }} - {{ booking.start_date }}
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  // Import axios library
  import axios from 'axios';
  
  export default {
    data() {
      return {
        bookings: [],
      };
    },
    methods: {
      // For testing purposes, use hardcoded data
      fetchData() {
        this.bookings = [
          {
            id: 1,
            customer: { user: { username: 'JohnDoe' } },
            car: { name: 'BMW' },
            start_date: '2023-03-01',
          },
          {
            id: 2,
            customer: { user: { username: 'JaneSmith' } },
            car: { name: 'Nissan' },
            start_date: '2023-03-15',
          },
          // Add more data as needed
        ];
      },
  
      // Uncomment the following lines when using API
      // fetchData() {
      //   axios.get('/api/bookings')
      //     .then(response => {
      //       this.bookings = response.data;
      //     })
      //     .catch(error => {
      //       console.error('Error fetching data:', error);
      //     });
      // },
    },
    created() {
      this.fetchData();
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
  