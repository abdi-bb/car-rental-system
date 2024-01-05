<template>
    <div>
      <h2>Customers List</h2>
      <ul>
        <li v-for="customer in customers" :key="customer.id">
          <router-link :to="{ name: 'CustomerDetail', params: { id: customer.id }}">
            {{ customer.username }} - {{ customer.phone_number || 'Phone Number N/A'}}
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
        customers: [],
      };
    },
    methods: {
      // For testing purposes, use hardcoded data
      // fetchData() {
      //   this.customers = [
      //     { id: 1, user: { username: 'JohnDoe' }, phone_number: '123-456-7890' },
      //     { id: 2, user: { username: 'JaneSmith' }, phone_number: '987-654-3210' },
      //     // Add more data as needed
      //   ];
      // },
  
      // Uncomment the following lines when using API
      fetchData() {
        // Retrieve the access token from localStorage
        const accessToken = localStorage.getItem('accessToken');

        // Set the Authorization header
        const headers = {
          'Authorization': `JWT ${accessToken}`,
        };

        axios.get('http://127.0.0.1:8000/api/v1/customers', { headers })
          .then(response => {
            this.customers = response.data;
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      },
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
  