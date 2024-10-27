<template>
  <div class="user-signup">
    <div class="register-container">
      <div class="register-form">
        <h1>User Signup</h1>

        <el-form ref="form" :model="form" label-width="120px" label-position="top">
          <el-form-item label="Name :" class="inline-item">
            <el-input v-model="form.name" placeholder="Please enter your name"></el-input>
          </el-form-item>

          <el-form-item label="Age :" class="inline-item">
            <el-input v-model="form.age" type="number" placeholder="Please enter your age"></el-input>
          </el-form-item>

          <el-form-item label="Gender :" class="inline-item">
            <el-select v-model="form.gender" placeholder="Select Gender">
              <el-option label="Male" value="Male"></el-option>
              <el-option label="Female" value="Female"></el-option>
              <el-option label="Other" value="Other"></el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="Address :" class="inline-item">
            <el-input v-model="form.address" placeholder="Please enter your address"></el-input>
          </el-form-item>

          <el-form-item label="Country :" class="inline-item">
            <el-input v-model="form.country" placeholder="Please enter your country"></el-input>
          </el-form-item>

          <el-form-item label="Holiday Frequency :" class="inline-item">
            <el-input v-model="form.holidayFrequency" type="number" placeholder="How often do you go for holiday in a year?"></el-input>
          </el-form-item>

          <el-form-item label="Gold Membership :" class="inline-item">
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
  min-height: 90vh;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.register-form {
  width: 50%;
  padding: 40px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.inline-item {
  display: flex;
  align-items: center;
}

.inline-item .el-form-item__label {
  width: 120px;
  text-align: left;
  margin-right: 10px;
}

.el-input,
.el-select,
.el-radio-group {
  width: 80%; 
}

.el-form-item {
  margin-bottom: 15px;
}

h1 {
  text-align: center;
  font-size: 28px;
  color: #333;
  margin-top: 30px;
  margin-bottom: 30px;
}

.submit-group {
  text-align: center;
  margin-top: 20px;
}

.el-button {
  background-color: #0b74de;
  color: white;
  border-radius: 5px;
}

.register-image {
  width: 50%;
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
