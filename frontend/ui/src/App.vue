<template>
  <div>
    <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    <router-link :to="{ name: 'CarsList' }">Cars</router-link>
    <div class="user-actions">
      <!-- Show Sign In or Logout based on user authentication -->
      <router-link v-if="!isAuthenticated" to="/login">Sign In</router-link>
      <button v-if="isAuthenticated" @click="logout">Logout</button>
    </div>
  </nav>
  <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      const expirationTime = localStorage.getItem('tokenExpiration');
      if (expirationTime === null) {
        return false; // Token expiration time not set
      }
      return new Date().getTime() < expirationTime;
    },
  },
  methods: {
    logout() {
      // Clear the access token from localStorage
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('tokenExpiration');
      
      // Update the store's isAuthenticated state on logout
      this.$store.commit('setAuthentication', false);

      // Optionally, you can clear localStorage or perform other actions

      // Redirect to home or login page
      this.$router.push('/');
    },
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  display: flex;
  /* justify-content: space-between; */
  
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

nav a.router-link-exact-active {
  color: white;
  background: crimson;
}

.user-actions {
  display: flex;
  align-items: center;
}

.user-actions button,
.user-actions router-link {
  margin-left: 10px;
  padding: 10px;
  border: none;
  cursor: pointer;
}

.user-actions router-link {
  text-decoration: none;
}

/* Move Sign In/Logout to the top-right */
.user-actions {
  margin-left: auto;
}
</style>
