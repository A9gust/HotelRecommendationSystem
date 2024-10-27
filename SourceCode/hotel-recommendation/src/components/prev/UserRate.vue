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
      // 将勾选框选中的内容发送到后端
      this.$axios.post('http://localhost:5000/saveRates', {
        ratedOptions: ratedOptions
      }, { withCredentials: true })
      .then(response => {
        console.log('Ratings saved:', response);
        // 跳转到下一页
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
.container {
  display: flex;
  flex-direction: column;
  margin: 50px auto; /* Center the border-box within the page */
  max-height: 9000px;
  width: 100%; /* Adjust width as needed */
  align-items: center;
  border: 0px solid transparent;
  box-shadow: 0 0px 0px rgba(222, 121, 6, 0.2);
}

.title-container {
  text-align: center;
  margin-bottom: 0px;
  margin-top: 10px;
  font-size: 20px;
}
h4 {
  font-size: 20px;
}
.border-box {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center content horizontally */
  justify-content: flex-start; /* Align content to the top */
  max-height: 1000px; /* Limit the height to 80% of the viewport */
  overflow-y: auto; /* Add a vertical scrollbar if content exceeds max height */
  width: 100%; /* Adjust width as needed */
  margin: 0px 0px; /* Center the border-box within the page */
  padding: 20px;
  background-color: transparent;
  border: 2px solid transparent;
  border-radius: 10px;
  box-shadow: 0 0px 0px rgba(222, 121, 6, 0.2);
}

.hotel-list {
  display: flex;
  flex-direction: column; /* Arrange hotels vertically */
  align-items: center; /* Center items horizontally */
  gap: 20px; /* Space between items */
  width: 100%; /* Full width to fit within the border-box */
}

.hotel-image {
    width: 400px;
    margin-top: 15px;
    height: auto;
    border-radius: 8px;
}

.rate-item {
  width: 100%; 
  max-width: 1200px; 
  text-align: center;
  background-color: #ffffff;
  padding: 20px; /* Increased padding for more content space */
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
