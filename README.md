

## SECTION 1 : PROJECT TITLE
## Hotel Recommender System

<img src="SystemCode/clips/static/hdb-bto.png"
     style="float: left; margin-right: 0px;" />

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
In the modern travel industry, online booking platforms have greatly facilitated travelers' accommodation choices. However, in the face of the vast amount of hotel resources, it is often difficult for users to make the most appropriate choice based on their own preferences. Traditional hotel search methods often rely on basic filters such as price, location, star rating, and so on. However, these approaches tend to ignore more personalized factors such as a user's historical choices or preferences for certain hotel amenities (e.g. gym, swimming pool, etc.). 

To solve this problem, hotel recommender systems have become an important means of providing personalized advice, able to make customized recommendations based on the user's needs. By leveraging data on both hotel facility characteristics and user preferences, the system can offer more accurate and targeted recommendations, ultimately simplifying the decision-making process and enhancing the user experience. With the increasing demand for personalized recommendations from travelers, the design of an efficient hotel recommendation system has become a key research direction to enhance the overall customer travel experience.

Our hotel recommender system is built with a Vue.js frontend that allows users to input preferences and view personalized recommendations through an intuitive interface. The backend, developed in Flask, manages data processing, user interactions, and serves as the core API. MySQL is used to store and organize hotel data, user profiles, and recommendation-related metrics. At the core of the recommendation logic is a collaborative filtering (CF) algorithm, leveraging cosine similarity to match users with relevant hotels based on historical preferences. To further enhance user experience, the system integrates a Python-based business rule engine that refines recommendations with rule-based adjustments, ensuring recommendations are both accurate and tailored to individual user needs. This combination of CF with business rules creates a well-rounded and highly adaptable hotel recommendation experience.

Our team is enthusiastically working on this hotel recommendation project, with the hope that users will engage with it and provide valuable feedback to improve the system further. We see potential for expanding the system’s reach internationally by enriching the database with diverse hotel options. By capturing variations across a broader range of hotels, we aim to provide users with even more accurate and personalized recommendations.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Desmond Chua | A1234567A | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567A@nus.edu.sg |
| Chang Ye Han | A1234567B | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567B@gmail.com |
| Chee Jia Wei | A1234567C | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567C@outlook.com |
| Ganesh Kumar | A1234567D | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567D@yahoo.com |
| Jeanette Lim | A1234567E | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567E@qq.com |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Sudoku AI Solver](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Sudoku AI Solver")

Note: It is not mandatory for every project member to appear in video presentation; Presentation by one project member is acceptable. 
More reference video presentations [here](https://telescopeuser.wordpress.com/2018/03/31/master-of-technology-solution-know-how-video-index-2/ "video presentations")

---

## SECTION 5 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

### [ 1 ] Environment Requirement

> pip install requirements


### [ 2 ] To run the system in local machine:

> open terminal in our local fold file

> $ git clone https://github.com/A9gust/HotelRecommendationSystem.git

> $ cd HotelRecommendationSystem/backend

> $ python app.py

> $ cd HotelRecommendationSystem/hotel-recommendation

> $ npm run serve

> **Go to URL using web browser http://0.0.0.0:8080 or http://127.0.0.1:8080

---
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

**Recommended Sections for Project Report / Paper:**
1. Introduction	
2. Market Research	
2.1 Industry Overview	
2.2 Current Trends in Hotel Recommend Systems	
2.3 Competitive Landscape	
2.4 Opportunities for Differentiation	
3. Business Value	
4. Objectives of Project	
5. Overview of Dataset	
5.1 Data type and source identification	
5.2 Dataset Structure	
6. System Design	
- 6.1 System Architecture	
6.2 Technology Stack	
6.3 System Components	
6.4 System Workflow	
7. System Development & Implementation	
7.1 Development Process	
7.2 Implementation Details	
7.3 System Integration & Testing	
8. Findings and Discussion	
8.1 High Matrix Sparsity
8.2 Collaborative Filtering Outcomes	
8.3 Prediction Accuracy	
8.4 Discussion	
Appendix 1: Project Proposal	
Appendix 2: Mapped System Functionalities Against Knowledge	
Appendix 3: Installation & User Guide	


---
## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

### HDB_BTO_SURVEY.xlsx
* Results of survey
* Insights derived, which were subsequently used in our system

---

### <<<<<<<<<<<<<<<<<<<< End of Template >>>>>>>>>>>>>>>>>>>>

---

**This [Machine Reasoning (MR)](https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning "Machine Reasoning") course is part of the Analytics and Intelligent Systems and Graduate Certificate in [Intelligent Reasoning Systems (IRS)](https://www.iss.nus.edu.sg/stackable-certificate-programmes/intelligent-systems "Intelligent Reasoning Systems") series offered by [NUS-ISS](https://www.iss.nus.edu.sg "Institute of Systems Science, National University of Singapore").**

**Lecturer: [GU Zhan (Sam)](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan "GU Zhan (Sam)")**

[![alt text](https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png "Let's check Sam' profile page")](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan)

**zhan.gu@nus.edu.sg**
