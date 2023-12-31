<template>
  <div class="about">
    <h1>About Car Rental System</h1>
    <img src="/images/about.jpg" alt="About Car Rental" class="about-image" />
    <p>Welcome to Car Rental System, your go-to platform for hassle-free car rentals. Whether you're planning a road trip, a family vacation, or need a reliable vehicle for your business travels, we've got you covered.</p>
    <p>At Car Rental System, we offer a diverse fleet of high-quality cars, from luxurious sedans to spacious SUVs. Our mission is to provide you with a seamless and enjoyable car rental experience, ensuring that you can focus on what matters most – your journey.</p>
    <p>Explore our user-friendly website to discover our range of vehicles, check availability, and make reservations with ease. Our dedicated team is committed to delivering excellent customer service, making sure your rental experience exceeds your expectations.</p>
    <p>Thank you for choosing Car Rental System. We look forward to being a part of your travel adventures.</p>
  </div>
</template>

<script>
export default {
  name: 'About',
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

.about {
  padding: 20px;
}

.about-image {
  width: 100%;
  max-width: 800px;
  border-radius: 8px;
  margin: 20px 0;
}

.about p {
  margin-bottom: 15px;
}
</style>
