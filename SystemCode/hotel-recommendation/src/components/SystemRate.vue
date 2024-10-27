<template>
    <div class="rating-container">
      <h2 class="title">Rate Our System</h2>
      <div class="stars">
        <span
          v-for="star in stars"
          :key="star"
          class="star"
          @click="rate(star)"
          :class="{ filled: star <= rating }"
        >
          ★
        </span>
      </div>
      <div v-if="rating > 0" class="submit-button">
        <button @click="submitRating">Submit Rating</button>
      </div>
      <div v-if="submitted" class="thank-you-message">
        <h2>Thank You for Your Rating!</h2>
        <p>Your feedback helps us improve our service.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        stars: [1, 2, 3, 4, 5],
        rating: 0,
        submitted: false,
      };
    },
    methods: {
      rate(star) {
        this.rating = star; // Set the rating based on the clicked star
      },
      submitRating() {
        // You can send the rating to your server here if needed
        this.submitted = true; // Show thank you message
        this.resetRating(); // Reset rating after submission
      },
      resetRating() {
        this.rating = 0; // Reset the rating
      }
    },
  };
  </script>
  
  <style scoped>
  .rating-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 50px;
  }
  
  .title {
    font-size: 40px; /* Adjust the size as needed */
    font-weight: bold; /* Make it bold */
  }
  
  .stars {
    font-size: 40px;
  }
  
  .star {
    cursor: pointer;
    color: lightgray;
  }
  
  .star.filled {
    color: gold;
  }
  
  .submit-button {
    margin-top: 20px;
  }
  
  .thank-you-message {
    margin-top: 20px;
    font-size: 24px;
    color: green;
    text-align: center;
  }
  </style>
  