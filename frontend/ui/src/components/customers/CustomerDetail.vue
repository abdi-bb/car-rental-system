<template>
    <div>
      <h2>Customer Detail</h2>
      <div v-if="customer">
        <p>Name: {{ customer.name }}</p>
        <p>Email: {{ customer.email }}</p>
        <!-- Add more details as needed -->
      </div>
      <div v-else>
        <p>Customer not found</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        customer: null, // Assuming you fetch customer details from an API or elsewhere
      };
    },
    methods: {
      fetchCustomerData() {

        // Retrieve the access token from localStorage
        const accessToken = localStorage.getItem('accessToken');

        // Set the Authorization header
        const headers = {
          'Authorization': `JWT ${accessToken}`,
        };
        // Fetch customer details from your API based on the route parameter 'id'
        axios.get(`http://127.0.0.1:8000/api/v1/customers/${this.$route.params.id}`, { headers }).then(response => this.customer = response.data);
      },
    },
    created() {
      this.fetchCustomerData();
    },
  };
  </script>
  