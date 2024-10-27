<template>
    <div class="border-box">
      <div class="select-title">Based on your ideal vacation you would be most interested in:</div>
      <div class="image-grid">
        <div v-for="(option, index) in vacationOptions" :key="index" class="option-item">
          <img :src="option.imageUrl" alt="Vacation Image" class="vacation-image">
          <div>{{ option.name }}</div>
          <!-- Rating input for each hotel -->
          <el-checkbox v-model="selectedOptions" :label="option.Cluster" class="custom-checkbox"></el-checkbox>
        </div>
      </div>
      <button class="confirm-button" @click="submitSelection">Please confirm your selection</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedOptions: [], 
        vacationOptions: []
    };
  },
  mounted(){
    this.fetchHotelNames();
  },
  methods: {
    fetchHotelNames(){
      this.$axios.get('http://localhost:5000/gethotel')
      .then(response => {
        this.vacationOptions = response.data.map(hotel => ({
            ...hotel,
            rating: 0 // Default rating value
          }));
      })
      .catch(error => {
            console.error('Error fetching hotel names:', error);
          });
    },
    submitSelection() {
      // 将勾选框选中的内容发送到后端
      this.$axios.post('http://localhost:5000/saveSelection', {
        selectedOptions: this.selectedOptions
      }, { withCredentials: true })
      .then(response => {
        console.log('Selection saved:', response);
        // 跳转到下一页
        this.$router.push({ path: '/user-rate', 
        query: { rate: JSON.stringify(response.data) } });
      })
      .catch(error => {
        console.error('Error saving selection:', error);
      });
    }
  }
};
  </script>
  
 
  <style>  
  html, body {  
    height: 100%;  
    margin: 0;  
    display: flex;  
    justify-content: center;  
    align-items: center;  
    background-color: #e3effa;
    min-height: 100vh; 

  }  
  
  .border-box {  
    border: 1px solid #007bff; 
    padding: 20px;  
    border-radius: 10px; 
    width: 90%; 
    max-width: 1500px; 
    height: auto; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    background-color: #ffffff;   
  }  
  
  .select-title {  
    font-family: 'Arial', sans-serif; /* 简化字体设置 */  
    font-size: 32px;  
    font-weight: bold;  
    margin-bottom: 30px;  
    margin-top: 10px;  
    text-align: center;  
    color: #003a78; /* 蓝色标题 */  
  }  
  
  .image-grid {  
    display: grid;  
    grid-template-columns: repeat(3, 1fr);  
    gap: 15px; /* 缩小图片间距 */  
    margin-top: 15px;  
  }  

  .el-checkbox__label {
  visibility: hidden;
}
  .custom-checkbox .el-checkbox__inner {  
  width: 25px;   
  height: 25px; 
}

.custom-checkbox .el-checkbox__inner::after {
  width: 8px;  /* 调整对勾的宽度 */
  height: 8px; /* 调整对勾的高度 */
  border-width: 3px; /* 调整对勾的粗细 */
}
  
  .vacation-image {  
    width: 100%;  
    height: auto;  
    border-radius: 10px; /* 更大的圆角 */  
  }  
  
  .confirm-button {  
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
    white-space: nowrap;
  }  
  
  .confirm-button:hover {  
    background-color: #0056b3; /* 悬停时颜色变深 */  
  }  
</style>

  