<template>
  <div class="container">
    <div class="title-container">
      <h3 class="title-text">For the selection of <span>{{ selectedOption }}</span></h3>
    </div>
  <div class="border-box">
    <div class="hotel-list">
      <div v-for="(option, index) in recommendations" :key="index" class="rate-item">
        <img :src="option.imageUrl" alt="Hotel Image" class="hotel-image">
        <div>
          <h4>{{ option.name }}</h4>
          <p>{{ option.details }}</p>
          <el-rate v-model="option.rating" :max="5"></el-rate>
        </div>
      </div>
    </div>
    <button class="next-button" @click="submitRatings">Next</button>
  </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      selectedOption: '', // User-selected option
      recommendations: [
        // // Static hotel information
        // {
        //   name: 'Hotel Sunshine',
        //   imageUrl: 'http://localhost:5000/static/city-hotel.png',
        //   details: 'A beautiful hotel located near the beach.',
        //   rating: 4
        // },
        // {
        //   name: 'Mountain Retreat',
        //   imageUrl: 'http://localhost:5000/static/city-hotel.png',
        //   details: 'A quiet retreat in the mountains.',
        //   rating: 5
        // },
        // {
        //   name: 'Mountain Retreat',
        //   imageUrl: 'http://localhost:5000/static/city-hotel.png',
        //   details: 'A quiet retreat in the mountains.',
        //   rating: 5
        // },
        // {
        //   name: 'Mountain Retreat',
        //   imageUrl: 'http://localhost:5000/static/city-hotel.png',
        //   details: 'A quiet retreat in the mountains.',
        //   rating: 5
        // }
        // // Add more static hotels here if needed
      ]
    };
  },
  mounted() {
    this.fetchHotelNames();
  },
  methods: {
    fetchHotelNames(){
      this.$axios.get('http://localhost:5000/getrateitems')
      .then(response => {
        this.recommendations = response.data.map(hotel => ({
            ...hotel,
            rating: 0 // Default rating value
          }));
      })
      .catch(error => {
            console.error('Error fetching hotel names:', error);
          });
    },
    submitRatings() {
      const ratedOptions = this.recommendations.filter(option => option.rating > 0)
      .map(option => ({
      name: option.name,
      rating: option.rating
      }));
      // POst to backend
      this.$axios.post('http://localhost:5000/saveRates', {
        ratedOptions: ratedOptions
      }, { withCredentials: true })
      .then(response => {
        console.log('Ratings saved:', response);
        // Turn to next page
        this.$router.push({ path: '/recommend-result', 
        query: { rate: JSON.stringify(response.data) } });
      })
      .catch(error => {
        console.error('Error saving selection:', error);
      });
    },
    goToNextPage() {
      this.$router.push('/finalpage'); // Navigate to the next page
    }
  }
};
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #e3effa;
  min-height: 100vh;
  overflow-x: hidden; 
}

.container {
  display: flex;
  flex-direction: column;
  margin: 50px auto;
  width: 100%;
  max-width: 100%; 
  align-items: center;
  overflow-y: auto;
  overflow-x: hidden;
  border: none; 
  box-shadow: none; 
}

.border-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  padding: 20px;
  background-color: transparent;
  border: 2px solid transparent;
  border-radius: 10px;
}

.hotel-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr); 
  gap: 20px; 
  width: 100%; 
}

.rate-item {
  width: 320px; 
  max-width: none; 
  text-align: center;
  background-color: #ffffff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 10px auto;
}


.hotel-image {
  width: 100%; 
  height: auto;
  border: none; 
  box-shadow: none; 
  border-radius: 8px;
}


.next-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
  display: block;
  width: auto;
  margin-left: auto;
  margin-right: auto;
}

.next-button:hover {
  background-color: #0056b3;
}


</style>
