<!-- 推荐很多个，切页。后面需要选择一个然后book -->
<template>
  <div class="container">
    <!-- Wait for loading：if isLoading is true，Display waiting anime -->
    <div v-if="isLoading" class="loading-screen">
      <div class="message" style="font-size: 28px; font-family: 'Times New Roman', Times, serif;">
        Give us a moment,<br> we are finding a suitable recommendation for you...
      </div>
      <div class="hourglass">
        <div class="sand"></div>
      </div>
    </div>

    <div v-else class="recommendation-screen">
      <h2 style="font-size: 30px; font-family: 'Times New Roman', Times, serif;">Your personalized recommendations are ready!</h2>
      <p style="font-size: 24px; font-family: 'Times New Roman', Times, serif; ">We recommend that this hotel for you:</p>

      <div v-if="currentHotel">
        <div class="hotel-info">
          <img :src="currentHotel.imgUrl" alt="Hotel Image" class="hotel-image" />
          <div class="hotel-details">
            <h3>{{ currentHotel.name }}, {{ currentHotel.location }}</h3>
            <ul>
              <li>WiFi: {{ currentHotel['WiFi'] === 1 ? 'Available' : 'Not Available' }}</li>
              <li>Swimming Pool: {{ currentHotel['Swimming Pool'] === 1 ? 'Available' : 'Not Available' }}</li>
              <li>Free Parking: {{ currentHotel['Free Parking'] === 1 ? 'Available' : 'Not Available' }}</li>
              <li>Facilities for Disabled Guests: {{ currentHotel['Disabled Facilities'] === 1 ? 'Available' : 'Not Available' }}</li>
            </ul>
            <!-- <button @click="bookHotel(currentHotel)">Proceed to Book</button> -->
          </div>
        </div>

        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 0">Previous</button>
          <button @click="nextPage" :disabled="currentPage === recommendations.length - 1">Next</button>
        </div>
      </div>
      
      <div class="booking-section">
        <h3 style="font-size: 24px;">If you've decided, book here!</h3>

        <form @submit.prevent="fetchDiscount">
          <label>
            Check-in Date:
            <input type="date" v-model="checkInDate" required />
          </label>
          <label>
            Check-out Date:
            <input type="date" v-model="checkOutDate" required />
          </label>
          <label>
            Number of rooms:
            <input type="number" v-model="numberOfRooms" min="1" required />
          </label>
          
          <button type="submit">Calculate Discount</button>
        </form>

        <!-- Display discount -->
        <div v-if="discount !== null" class="discount-info">
          <p>Discount for your stay: {{ discount }}%</p>
        </div>
      </div>
    </div>
    <div class="bottom-button">
      <button @click="goforRate" :disabled="currentPage === recommendations.length - 1">Rate for our recommend system!</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isLoading: true, // Control loading 
      recommendations: [], // Save the recommend results
      currentPage: 0, // The page number

      // Data about computing discount
      checkInDate: '',
      checkOutDate: '',
      numberOfRooms: 1,
      discount: null, 
    };
  },
  computed: {
    currentHotel() {
      return this.recommendations[this.currentPage];
    }
  },
  methods: {
    async fetchRecommendations() {
      try {
        const response = await axios.get('http://localhost:5000/getrecommendations', { withCredentials: true });  // Flask API 的 URL
        this.recommendations = response.data;
        this.isLoading = false; // Hide loading
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      }
    },
    // Go for system rate
    goforRate() {
      this.$router.push({ path: '/system-rate'});
    },
    prevPage() {
      if (this.currentPage > 0) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.recommendations.length - 1) {
        this.currentPage++;
      }
    },
  
    async fetchDiscount() {
      try {
        const response = await axios.post('http://localhost:5000/getdiscount', {
          checkInDate: this.checkInDate,
          checkOutDate: this.checkOutDate,
          numberOfRooms: this.numberOfRooms
        }, { withCredentials: true });
        this.discount = response.data.discount; 
      } catch (error) {
        console.error('Error fetching discount:', error);
      }
    },
    
  },
  mounted() {
    
    this.fetchRecommendations();
  }
};
</script>

<style>
.container {
  border: 1px solid #000;
  display: flex;
  padding: 20px;
  border-radius: 5px;
  width: 800px;
  height: auto;
  margin: 120px auto;
  padding: 20px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.loading-screen {
  text-align: center;
}

.recommendation-screen {
  text-align: center;
  padding-top: 20px;
}

.hotel-info {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 20px;
  gap: 20px; 
}


.hotel-image {
  width: 300px !important;
  height: 200px !important;
  object-fit: cover !important;
  border-radius: 8px;
  min-width: 300px;
  min-height: 200px;
  max-width: 300px;
  max-height: 200px;
}



.hotel-details {
  text-align: left;
}

.hotel-details ul {
  list-style-type: none;
  padding: 0;
}

.hotel-details li {
  margin-bottom: 5px;
}

.pagination {
  margin-top: 20px;
}

.pagination button {
  margin: 0 10px;
}

.hourglass {
  width: 40px;
  height: 60px;
  border: 4px solid black;
  border-radius: 50%;
  position: relative;
  margin: 20px auto;
  animation: rotate 2s infinite linear;
}

.sand {
  width: 10px;
  height: 10px;
  background: black;
  border-radius: 50%;
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  animation: falling 1.5s infinite ease-in-out;
}

/* Rotate */
@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}


@keyframes falling {
  0% {
    top: 20px;
  }
  50% {
    top: 50px;
  }
  100% {
    top: 20px;
  }
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: 1px solid black;
  background-color: white;
}


.booking-section {
  margin-top: 40px;
  padding: 20px;
  border: none; /* Remove border*/
  border-radius: 8px;
  width: 100%;
}


.booking-section label {
  display: block;
  margin-bottom: 10px;
}

.booking-section input {
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.discount-info {
  margin-top: 20px;
  font-size: 20px;
  color: green;
}

button:hover {
  background-color: #0056b3;
}

</style>