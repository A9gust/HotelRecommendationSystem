<!--注册页面，改了-->
//这个右半边的图片signup-image.png我没找到太好的。后续可以换一下。
<template>
  <div class="user-signup">
    <div class="register-container">
      <div class="register-form">
        <h1>User Signup</h1>

    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="Name :">
        <el-input v-model="form.name" placeholder="Please enter your name"></el-input>
      </el-form-item>

      <el-form-item label="Age :">
        <el-input v-model="form.age" type="number" placeholder="Please enter your age"></el-input>
      </el-form-item>

      <el-form-item label="Gender :">
        <el-select v-model="form.gender" placeholder="Select Gender">
          <el-option label="Male" value="Male"></el-option>
          <el-option label="Female" value="Female"></el-option>
          <el-option label="Other" value="Other"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="Address :">
        <el-input v-model="form.address" placeholder="Please enter your address"></el-input>
      </el-form-item>

      <el-form-item label="Country :">
        <el-input v-model="form.country" placeholder="Please enter your country"></el-input>
      </el-form-item>

      <el-form-item label="Holiday Frequency :">
        <el-input v-model="form.holidayFrequency" type="number" placeholder="How often do you go for holiday in a year?"></el-input>
      </el-form-item>

      <el-form-item label="Do you want to sign up for Gold Membership? :" label-width="380px">
        <el-radio-group v-model="form.goldMembership">
          <el-radio label="Yes">Yes</el-radio>
          <el-radio label="No">No</el-radio>
        </el-radio-group>
      </el-form-item>

      <div class="form-group submit-group">
        <el-button type="primary" @click="submitForm">Submit</el-button>
      </div>
    </el-form>
  </div>

  <div class="register-image">
        <img src="@/assets/signup-image.png" alt="Registration Illustration" />
      </div>
    </div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        age: '',
        gender: '',
        address: '',
        country: '',
        holidayFrequency: '',
        goldMembership: '',
      },
    };
  },
  methods: {
    submitForm() {
      this.$axios.post('http://localhost:5000/signup', this.form, { withCredentials: true })
      .then(response => {
          console.log('User info submitted', response);
          if (this.$route.path !== '/ideal-vacation') {
            this.$router.push('/ideal-vacation');
          }
        })
        .catch(error => {
          console.error('Error submitting form', error);
        });
    },
  },
};
</script>

<style>

.user-signup {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #BED3E9;
}


.register-container {
  display: flex;
  justify-content: space-between;
  width: 80%; 
  height: 90vh; 
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* 左侧注册表单 */
.register-form {
  width: 50%;
  padding: 40px;
  box-sizing: border-box;
}
.el-input{
  width: 80%;
}
.el-form-item {
  margin-bottom: 40px; 
}
.el-form-item__label {
    text-align: right;
    vertical-align: middle;
    float: left;
    font-size: 16px;
    line-height: 40px;
    padding: 0 12px 0 0;
    box-sizing: border-box;
    white-space: nowrap !important; 
    width: 160px !important; 
}
.el-input__inner{
  font-size: 15px;
  border: 2px solid; /*输入框边框的粗细*/
}
h1 {
  text-align: center;
  font-size: 28px;
  color: #333;
  margin-top: 30px;
  margin-bottom: 50px;
}

.el-radio__label{
  font-size: 16px;
}

.submit-group {
  text-align: center;
}


.el-button{
  margin-left: 0px !important;
  background-color: #0b74de;
  color: white;
}

/* 右侧图片部分 */
.register-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0 10px 10px 0;
}
</style>

