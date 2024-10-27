<template>
    <div class="homepage">
      <!-- First Section -->
      <section class="first-page">
        <div class="content">
          <h1>Personalized Hotel Recommendation Service</h1>
          <p style="line-height: 2;">
           Based on your needs and preferences,<br>
           our system will recommend the most suitable hotels to help you easily find the ideal place to stay.
          </p>
          <router-link to="/user-signup" class="signup-link">Signup for personalized recommendations !</router-link>
          <div class="scroll-down" @click="scrollToSecondPage">
            <span>↓</span>
          </div>
        </div>
      </section>
  
      <!-- Second Section -->
      <section class="second-page" ref="secondPage">
        <h2>Hotel<br> Recommendation</h2>
        <div class="recommend-list">
          <ul class="list-box">
            <li v-for="item in recommendList" :key="item.id">
              <!-- Left side -->
              <div class="list-left">
                <div class="list-left-img">
                  <img :src="require(`@/assets/${item.img_url}`)" alt="Hotel Image">
                </div>
                <div class="list-left-title">
                  <div class="list-left-titleandtag">
                    <h4>{{item.name}}</h4>
                    <img :src="require(`@/assets/${item.starimg_url}`)" alt="Star Rating" class="star-image">
                  </div>
                  <div class="list-left-transport">
                    <p>{{item.transport}}</p>
                  </div>
                  <div class="list-left-tag">
                    <el-tag type="danger" effect="plain" v-for="(tag, index) in item.tag" :key="index">{{ tag }}</el-tag>
                  </div>
                </div>
              </div>
  
              <!-- Right side -->
              <div class="list-right">
                <div class="list-right-comment">
                  <div class="list-right-describe">
                    <p>{{item.recommendation}}</p>
                    <a href="">{{item.count}}</a>
                  </div>
                  <div class="list-right-score">{{item.score}}</div>
                </div>
                <div class="list-right-price">
                  <p>{{item.price}}</p>
                  <el-button type="primary" @click="goToSignup">View Details</el-button>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        recommendList: [
          {
            id: 1,
            name: 'Carlton Hotel Singapore',
            img_url: 'list-1.jpg',
            starimg_url: 'star2.jpg',
            transport: 'Marina Bay Area | 1.8 km straight line from city center',
            tag: ['Swimming Pool', 'Massage Room', 'Executive Lounge', 'Gym', 'Conference Hall'],
            recommendation: 'Good',
            score: '4.6',
            count: '8384 Reviews',
            price: 'SGD 298',
          },
          {
            id: 2,
            name: 'Fairmont Singapore',
            img_url: 'list-2.jpg',
            starimg_url: 'star2.jpg',
            transport: 'Marina Bay Area | 1.6 km straight line from city center',
            tag: ['Stunning Landscape', 'Hygiene Plus', 'Top Notch Cuisine', 'Sunbathing Spot', 'Sauna Room'],
            recommendation: 'Good',
            score: '4.5',
            count: '7793 Reviews',
            price: 'SGD 501',
          },
          {
            id: 3,
            name: 'Swissotel The Stamford',
            img_url: 'list-3.jpg',
            starimg_url: 'star2.jpg',
            transport: 'Marina Bay Area | 1.5km straight line from city center',
            tag: ['Free Parking', 'Tennis Court', 'Executive Lounge', 'Gym', 'Massage Room'],
            recommendation: 'Good',
            score: '4.7',
            count: '18160 Reviews',
            price: 'SGD 441',
          },
          {
            id: 4,
            name: 'Capella Singapore',
            img_url: 'list-4.jpg',
            starimg_url: 'star2.jpg',
            transport: 'Sentosa Island Area | 4.5 km straight line from the city center',
            tag: ['Free Parking', 'Swimming Pool', 'Executive Lounge', 'Gym', 'Massage Room'],
            recommendation: 'Good',
            score: '4.6',
            count: '2450 Reviews',
            price: 'SGD 854',
          },
        ]
      };
    },
    methods: {
      goToSignup() {
      this.$router.push('/user-signup');
    },  
    scrollToSecondPage() {
      // 使用 scrollIntoView 方法滚动到第二部分
      this.$refs.secondPage.scrollIntoView({ behavior: 'smooth' });
    }
  }
  };
  </script>
  
  <style scoped>
  /* General Page Styles */
  .homepage {
    width: 100%;
    height: 100vh;
    overflow-y: scroll;
    scroll-snap-type: y mandatory;
  }
  
  section {
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    scroll-snap-align: start;
  }
  
  /* First Page */
  .first-page {
    background-image: url('@/assets/background1.jpg'); 
    background-size: cover;
    color: white;
    text-align: center;
  }
  
  .first-page .content h1 {
    font-size: 50px;
    margin-bottom: 60px;
  }
  
  .first-page .content p {
    font-size: 24px;
    margin-bottom: 60px;
  }
  
  /* 在上面的代码中改为signup-button
  .signup-button {
    display: inline-block; 
    padding: 12px 24px; 
    font-size: 22px;
    color: black; 
    background-color: white; 
    border-radius: 100px; 
    text-decoration: none; 
    transition: all 0.3s; 
    cursor: pointer; 
}

.signup-button:hover {
    background-color: #e3e3e3; 
    color: black; 
    border-color: white; 
}*/

  .signup-link {
    font-size: 26px;
    font-weight: bold;
    color: white;
    text-decoration: none;
    transition: all 0.3s;
    cursor: pointer;
  }
  
  .signup-link:hover {
    color: #005eff;
    text-decoration: underline;
    cursor: pointer; 
  }
  
  .scroll-down {
    font-size: 65px;
    color: white;
    margin-top: 50px;
    cursor: pointer;
    animation: bounce 2s infinite;
  }
  
  @keyframes bounce {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(10px);
    }
  }
  
  /* Second Page */
.second-page {
  background-image: url('@/assets/background2.jpg');
  background-size: cover;
  color: black;
  padding: 2rem;
}

.second-page h2 {
  padding-top: 5px;
  margin: 0;
  font-size: 30px;
  margin-bottom: 2rem;
  text-align: center; 
  /*width: 100%; */
  padding: 20px;  
}

/* Hotel List */
.recommend-list .list-box {
  list-style-type: none;
  padding: 0;
}

.star-image {
  max-width: 15%; /* 图片宽度不会超过父容器 */
  height: auto; /* 高度根据宽度自动调整，保持比例 */
  display: block; /* 防止默认行内元素带来的间隙 */
}


.recommend-list .list-box li {
  display: flex;
  background-color: #FFF;
  margin-bottom: 5px;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  height: 170px;
}

/* Left Section */
.list-left {
  flex: 2;
  display: flex;
  height: 170px;
}
.list-right {
        flex: 1;
        border-left: 1px solid hsla(0, 34%, 67%, 0.395);
        text-align: right;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

.list-left-img {
  flex: 1;
}

.list-left-img img {
  width: 100%;
  height: 100%;
  
}

.list-left-title {
  margin-left: 20px;
  flex: 3;
}

.list-left-titleandtag {
    font-size: 18px;
        line-height: 24px;
        display: flex;
        margin-bottom: 8px;
        align-items: center;
}

.list-left-titleandtag h4 {
  margin-right: 18px;
  margin: 0;
}

.list-left-transport {
  margin-bottom: 10px;
}
.list-left-titleandtag img {
    height: 18px;
    width: auto;
    margin-left: 15px;
}

.list-left-tag .el-tag {
  margin-right: 5px;
}

/* Right Section */
/*.list-right {
  flex: 1;
  text-align: right;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}*/

.list-right-comment {
    display: flex;
    justify-content: flex-end;
}
.list-right-describe p {
  font-size: 16px;
  color: rgb(54, 163, 253);
  font-weight: bold;
}

.list-right-describe a {
  font-size: 14px;
  color: #7a7979;
  text-decoration: none;
}

.list-right-score {
  background-color: rgb(54, 163, 253);
  height: 25px;
  color: white;
  padding: 5px;
  margin: 5px 5px;
  font-size: 18px;
  font-weight: bold;
  border-radius: 5px;
}

.list-right-price p {
  font-size: 18px;
  font-weight: bold;
  color: rgb(54, 163, 253);
}

.el-button {

  background-color: rgb(54, 163, 253);
  border-color: rgb(54, 163, 253);
  color: white;
}

.el-button:hover {
   
  background-color: rgb(33, 123, 212);
  border-color: rgb(33, 123, 212);
}
</style>