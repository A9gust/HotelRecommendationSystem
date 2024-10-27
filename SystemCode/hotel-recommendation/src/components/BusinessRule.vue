<template>
    <div class="business-container">
      <h3 style="font-size: 26px; font-family: 'Times New Roman', Times, serif;">{{ hotel.name }}, {{ hotel.location }}</h3>
      <form @submit.prevent="submitBooking">
        <label>
          Your price:
          <input type="text" :value="price" readonly class="price-output" />
        </label>
        <button type="book">Book</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['hotel', 'numberOfPeople', 'checkInDate', 'checkOutDate'], // params from router
    data() {
      return {
        price: null, // Save price from business rule
      };
    },
    mounted() {
      if (this.hotel && this.hotel.id) {
        this.fetchPrice(); // Get price info
      } else {
        console.error("Hotel data is missing or undefined.");
      }
    },
    methods: {
      async fetchPrice() {
        try {
          const response = await axios.post('http://localhost:5000/get-price', {
            hotelId: this.hotel.id,
            numberOfPeople: this.numberOfPeople,
            checkInDate: this.checkInDate,
            checkOutDate: this.checkOutDate
          });
          this.price = response.data.price; // Get price from backend
        } catch (error) {
          console.error('Error fetching price:', error);
        }
      },
      submitBusinessRule() {
        // Turn to book page
        this.$router.push({ 
          name: 'booking', 
          params: { 
            hotel: this.hotel, 
            numberOfPeople: this.numberOfPeople,
            checkInDate: this.checkInDate,
            checkOutDate: this.checkOutDate,
            price: this.price 
          }
        });
      }
    }
  };
  </script>

<style>
.business-container {
    border: 1px solid black;
    display: flex;
    padding: 20px;
    border-radius: 5px;
    width: 800px;
    height: 600px;
    margin: 120px auto;
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    justify-content: center;
    font-family: 'Times New Roman', Times, serif;
  }
  
.price-output {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid black;
  background-color: #f9f9f9;
  width: 150px;
  text-align: right;
}  

button {
    margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: 1px solid black;
  background-color: white;
}

</style>