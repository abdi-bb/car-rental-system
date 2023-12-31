<template>
  <div class="home">
    <h1>Welcome to Car Rental System</h1>
    <p>Explore our wide range of high-quality cars for rent. Whether you need a sedan for a business trip or an SUV for a family vacation, we have the perfect vehicle for you.</p>
    
    <div class="featured-cars">
      <h2>Featured Cars</h2>
      <div v-for="car in featuredCars" :key="car.id" class="car">
        <img :src="car.image" :alt="car.name" />
        <h3>{{ car.name }}</h3>
        <p>{{ car.description }}</p>
      </div>
    </div>
    
    <p>Ready to hit the road? Rent a car with us today!</p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      featuredCars: [
        { id: 1, name: 'Luxury Sedan', description: 'Smooth and elegant. Perfect for business trips.', image: '/images/luxury_sedan.jpg' },
        { id: 2, name: 'Family SUV', description: 'Spacious and comfortable. Ideal for family vacations.', image: '/images/family_suv.jpg' },
        { id: 3, name: 'Sport Convertible', description: 'Experience the thrill. Perfect for a weekend getaway.', image: '/images/sport_convertible.jpg' },
      ],
    };
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

.home {
  padding: 20px;
}

.featured-cars {
  margin-top: 20px;
}

.car {
  margin-bottom: 20px;
}

.car img {
  max-width: 100%;
  border-radius: 8px;
}
</style>
