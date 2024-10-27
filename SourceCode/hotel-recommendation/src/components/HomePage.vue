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
        <router-link to="/user-signup" class="signup-link">Signup for personalized recommendations!</router-link>
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
      this.$refs.secondPage.scrollIntoView({ behavior: 'smooth' });
    }
  }
};
</script>

<style scoped>
/* General Page Styles */
.homepage {
  width: 100%;
  height: auto;
  overflow-x: hidden; /* Hide horizontal scroll bars */
}

/* First Page */
.first-page {
  background-image: url('@/assets/background1.jpg');
  background-size: cover;  /* Fit itself */
  background-position: center;  /* Midlle Center */
  background-repeat: no-repeat;  /* Avoid repeat */
  color: white;
  text-align: center;
  height: 100vh;  
  width: 100vw;  
  display: flex;
  justify-content: center;
  align-items: center;
}


.first-page .content h1 {
  font-size: 50px;
  margin-bottom: 30px;
}

.first-page .content p {
  font-size: 24px;
  margin-bottom: 30px;
}

.signup-link {
  font-size: 26px;
  font-weight: bold;
  color: white;
  text-decoration: none;
  transition: all 0.3s;
}

.signup-link:hover {
  color: #005eff;
  text-decoration: underline;
}

.scroll-down {
  font-size: 50px;
  color: white;
  margin-top: 20px;
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
  padding: 2rem;
}

.second-page h2 {
  padding-top: 5px;
  font-size: 30px;
  margin-bottom: 2rem;
  text-align: center;
}

/* Hotel List */
.recommend-list .list-box {
  list-style-type: none;
  padding: 0;
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

.star-image {
  height: 18px;
  width: auto;
  margin-left: 15px;
}

.list-left-tag .el-tag {
  margin-right: 5px;
}

/* Right Section */
.list-right {
  flex: 1;
  border-left: 1px solid hsla(0, 34%, 67%, 0.395);
  text-align: right;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

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
