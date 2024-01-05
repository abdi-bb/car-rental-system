<template>
    <div>
      <h2>User Registration</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="userData.username" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="userData.email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="userData.password" required />
        </div>
        <div>
          <label for="firstName">First Name:</label>
          <input type="text" id="firstName" v-model="userData.firstName" required />
        </div>
        <div>
          <label for="lastName">Last Name:</label>
          <input type="text" id="lastName" v-model="userData.lastName" required />
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      <p v-if="registrationMessage">{{ registrationMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userData: {
          username: '',
          email: '',
          password: '',
          firstName: '',
          lastName: '',
        },
        registrationMessage: '',
      };
    },
    methods: {
      async submitForm() {
        try {
          // Replace this URL with your actual backend API endpoint for user registration
          const response = await fetch('http://127.0.0.1:8000/api/v1/auth/users/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.userData),
          });
  
          if (!response.ok) {
            throw new Error('Failed to register user');
          }


          // Update registration message and redirect to login page
          this.registrationMessage = 'User registered successfully';
          this.$router.push('/login');
        } catch (error) {
          console.error('Error registering user:', error);
          this.registrationMessage = 'Error registering user. Please try again.';
        }
      },
    },
  };
  </script>
  
  <style>
  /* Add your styles here if needed */
  form {
    max-width: 400px;
    margin: auto;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 16px;
  }
  
  button {
    padding: 8px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  