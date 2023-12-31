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
  export default {
    data() {
      return {
        customer: null, // Assuming you fetch customer details from an API or elsewhere
      };
    },
    methods: {
      fetchCustomerData() {
        // Fetch customer details from your API based on the route parameter 'id'
        // axios.get(`/api/customers/${this.$route.params.id}`).then(response => this.customer = response.data);
      },
    },
    created() {
      this.fetchCustomerData();
    },
  };
  </script>
  