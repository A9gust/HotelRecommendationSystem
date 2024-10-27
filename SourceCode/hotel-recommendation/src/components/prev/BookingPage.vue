<template>
    <div class="business-container">
      <h3>Business Rule Page</h3>
  
      <div>
        <label>Check-in Date: {{ checkInDate }}</label>
        <br />
        <label>Check-out Date: {{ checkOutDate }}</label>
        <br />
        <label>Number of People: {{ numberOfPeople }}</label>
        <br />
        <label>Your Price: 
          <input type="text" v-model="price" readonly />
        </label>
        <br />
        <button @click="submitBooking">Book</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        price: '', // 价格
      };
    },
    mounted() {
      this.fetchPrice(); // 页面加载时获取价格
    },
    methods: {
      async fetchPrice() {
        try {
          const { checkInDate, checkOutDate, numberOfPeople } = this.$route.params;
          
          // 向后端发送请求以计算价格
            const response = await axios.post('http://localhost:5000/get-price', {
            checkInDate: checkInDate,
            checkOutDate: checkOutDate,
            numberOfPeople: numberOfPeople,
          });
          
          // 将后端返回的价格赋值给 price 变量
          this.price = response.data.price;
        } catch (error) {
          console.error('Error fetching price:', error);
        }
      },
      async submitBooking() {
        try {
          const { checkInDate, checkOutDate, numberOfPeople } = this.$route.params;
          
          // 向后端发送预订请求
          await axios.post('http://localhost:5000/book-hotel', {
            checkInDate,
            checkOutDate,
            numberOfPeople,
            price: this.price, // 传递价格进行预订
          });
          
          alert('Booking successful!');
        } catch (error) {
          console.error('Error booking hotel:', error);
          alert('Booking failed.');
        }
      },
    },
  };
  </script>
  

<style scoped>
.business-container {
  border: 2px solid #ccc; 
  border-radius: 10px; 
  padding: 20px; 
  width: 800px; 
  height: auto; 
  margin: 50px auto; 
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  font-size: 18px; 
}

h3 {
  font-size: 24px; 
}

label {
  margin-bottom: 10px; 
  line-height: 2;
}

input[type="text"] {
  margin-bottom: 10px; 
  padding: 5px; 
  font-size: 18px; 
}
.booking-form {
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
  }
  
.booking-form form {
    display: flex;
    flex-direction: column;
  }
  

.booking-form label {
    margin-bottom: 10px;
  }
  
.booking-form button {
    margin-top: 10px;
    padding: 5px 10px;
  }
</style>