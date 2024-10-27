<template>
  <div class="ideal-vacation">
    <div class="chat-content">
      <div class="chat-window">
        <h2 class="chat-title">
          <img src="@/assets/chat-icon.png" alt="Chat Icon" class="chat-icon" />
          Chat Window
        </h2>
        <div class="messages">
          <div
            v-for="message in messages"
            :key="message.id"
            :class="['message', message.type === 'sent' ? 'user-message' : 'ai-message']"
          >
            <div class="message-bubble" v-if="!message.photo">{{ message.text }}</div>
          </div>  
        </div>

        <!-- 标签部分：点击插入预设文本 -->
        <div class="tags">
          <button @click="insertText('I would like a hotel with a swimming pool.')">Swimming Pool</button>
          <button @click="insertText('I prefer hotels with free parking.')">Free Parking</button>
          <button @click="insertText('I need a hotel that serves free breakfast.')">Free Breakfast</button>
        </div>

        <div class="input-container">
          <input
            type="text"
            v-model="message"
            placeholder="Type your message..."
            @keydown.enter="sendMessage"
          />
          <button @click="sendMessage" class="send-button">
            <i class="send-icon"></i>
          </button>
          <button @click="Confirm">Confirm</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000';

export default {
  name: 'IdealVacation',
  data() {
    return {
      messages: [
        { id: 1, text: 'Hello! Tell us about your ideal vacation!', type: 'received' },
      ],
      message: '', // 存储当前输入
    };
  },
  methods: {
    // 点击标签时插入文本
    insertText(text) {
      this.message = text;
    },

    // 发送用户消息到后端并获取回复
    async sendMessage() {
      if (this.message.trim()) {
        // 显示用户输入的消息
        this.messages.push({ id: Date.now(), text: this.message, type: 'sent' });

        const userMessage = this.message;
        this.message = ''; // 清空输入框

        try {
          // 发送用户输入的消息到后端
          await axios.post('http://localhost:5000/saveVacation', { idealVacation: userMessage }, { withCredentials: true });

          // 自动回复
          const autoReply = 'We have received a description of your ideal hotel and will make a recommendation based on it.';
          this.messages.push({ id: Date.now(), text: autoReply, type: 'received' });
        } catch (error) {
          console.error('Error sending message:', error);
          this.messages.push({ id: Date.now(), text: 'Error processing your message.', type: 'received' });
        }
      }
    },

    Confirm() {
      this.$router.push('/user-selection');
    },
  },
};
</script>

<style scoped>
.ideal-vacation {
  display: flex;
  justify-content: center;
  width: 100vw; 
  height: 100vh; 
  background: linear-gradient(to right, #f0f4f8, #ffffff);
  padding: 10px;
  box-sizing: border-box;
}

.chat-title {
  font-size: 30px; 
  margin-top: 0;
}
.chat-icon {
  width: 60px; 
  height: 60px; 
  margin-right: 20px; 
  margin-left: 20px;
}
.chat-content {
  display: flex;
  height: 95%;
  width: 95%;
  justify-content: center;
  align-items: center;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.chat-window {
  flex: 1;
  display: flex;
  flex-direction: column;
  max-width: 2000px;
  height: 90%;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
  background: url('../assets/logo2.jpg') no-repeat center center;
  background-size: cover;
}
.messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}
.message {
  margin-bottom: 10px;
  display: flex;
}
.user-message {
  justify-content: flex-end;
}
.ai-message {
  justify-content: flex-start;
}
.message-bubble {
  margin-top: 15px;
  max-width: 60%;
  font-size: 22px;
  padding: 10px;
  border-radius: 15px;
  background-color: #e3f2fd;
}
.user-message .message-bubble {
  margin-right: 20px;
  background-color: #5ec962;
  color: #ffffff;
}
.ai-message .message-bubble {
  background-color: #1e88e5;
  color: #ffffff;
  margin-left: 20px;
}
.input-container {
  display: flex;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  height: 100px;
  padding: 5px;
}
input {
  flex: 1;
  font-size: 22px;
  border: none;
  outline: none;
  padding: 10px;
  border-radius: 5px;
}
button {
  margin-left: 12px;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-right: 5px;
  background-color: #509ee1;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
}
button:hover {
  background-color: #1e88e5;
}
.send-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}
.send-button:hover {
  background-color: rgba(255, 87, 34, 0.1); 
  border-radius: 50%; 
}
.send-icon {
  display: inline-block;
  background-image: url('../assets/send-icon.png');
  width: 65px; 
  height: 65px; 
  background-size: cover;
}

/* 标签样式 */
.tags {
  margin-bottom: 15px;
}

.tags button {
  margin-right: 10px;
  padding: 8px 12px;
  background-color: #509ee1;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.tags button:hover {
  background-color: #357ae8;
}
</style>
