from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from function import clustering
import pandas as pd
import ast
from function import recommend_nlp, output_rateitems, recommend_cos, recommend_cf
from bus_rule.rule_engine import result
import numpy as np
import random

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Intialize database
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/recommend'  # For MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define a model for a table in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    goldmember = db.Column(db.String(80), nullable=False)
    ideal = db.Column(db.String(255), nullable=True)
    selection = db.Column(db.String(255), nullable=True)
    ratings = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    hotel_name = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Rating {self.username}'


with app.app_context():
    db.create_all()


@app.cli.command()
def create():
    return


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    address = data.get('address')
    country = data.get('country')
    frequency = data.get('holidayFrequency')
    goldmember = data.get('goldMembership')
    session['name'] = name
    new_user = User(name=name, age=age, gender=gender, address=address,
                    country=country, frequency=frequency,
                    goldmember=goldmember)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!",
                    "user": str(new_user)}), 201


@app.route('/saveVacation', methods=['POST'])
def get_idealvacation():
    print(session)
    username = session.get('name')
    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    description = request.json.get('idealVacation')
    if user.ideal:
        user.ideal += description
    else:
        user.ideal = description
    db.session.commit()
    return jsonify({"message": "Successfully upload ideal vacation"}), 200


@app.route('/gethotel', methods=['GET'])
def get_hotel():
    temp = clustering()
    temp['imageUrl'] = ['http://localhost:5000/static/city-hotel.png',
                                'http://localhost:5000/static/mountain-view.png',
                                'http://localhost:5000/static/beach-resort.png',
                                'http://localhost:5000/static/glamping.png',
                                'http://localhost:5000/static/tree-house.png',
                                'http://localhost:5000/static/overwater-bungalow.png']
    # hotels = [
    #     {'name': 'City Hotel', 'imageUrl': 'http://localhost:5000/static/city-hotel.png'},
    #     {'name': 'Mountain View', 'imageUrl': 'http://localhost:5000/static/mountain-view.png'},
    #     {'name': 'Beach Resort', 'imageUrl': 'http://localhost:5000/static/beach-resort.png'},
    #     {'name': 'Glamping', 'imageUrl': 'http://localhost:5000/static/glamping.png'},
    #     {'name': 'Tree House', 'imageUrl': 'http://localhost:5000/static/tree-house.png'},
    #     {'name': 'Overwater Bungalow', 'imageUrl': 'http://localhost:5000/static/overwater-bungalow.png'}
    # ]
    hotels_list = temp.to_dict(orient='records')
    return jsonify(hotels_list)


@app.route('/saveSelection', methods=['POST'])
def get_selection():
    print(request.json)
    username = session.get('name')
    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    selection = str(request.json.get('selectedOptions'))
    user.selection = selection
    db.session.commit()
    return jsonify({"message": "Successfully upload user selections"}), 200


@app.route('/getrateitems', methods=['GET'])
def get_rateitems():
    # username = session.get('name')
    username = 'LLL'
    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    selection = user.selection
    selection = ast.literal_eval(selection)
    hotels = output_rateitems(selection)
    hotels_list = hotels.tolist()

    images = [
        "http://localhost:5000/static/images/image1.jpg",
        "http://localhost:5000/static/images/image2.jpg",
        "http://localhost:5000/static/images/image3.jpg",
        "http://localhost:5000/static/images/image4.jpg",
        "http://localhost:5000/static/images/image5.jpg",
        "http://localhost:5000/static/images/image6.jpg",
        "http://localhost:5000/static/images/image7.jpg",
        "http://localhost:5000/static/images/image8.jpg",
        "http://localhost:5000/static/images/image9.jpg",
        "http://localhost:5000/static/images/image10.jpg",
        "http://localhost:5000/static/images/image11.jpg",
        "http://localhost:5000/static/images/image12.jpg",
        "http://localhost:5000/static/images/image13.jpg",
        "http://localhost:5000/static/images/image14.jpg",
        "http://localhost:5000/static/images/image15.jpg",
        "http://localhost:5000/static/images/image16.jpg",
        "http://localhost:5000/static/images/image17.jpg",
        "http://localhost:5000/static/images/image18.jpg",
        "http://localhost:5000/static/images/image19.jpg",
        "http://localhost:5000/static/images/image20.jpg",
        "http://localhost:5000/static/images/image21.jpg",
        "http://localhost:5000/static/images/image22.jpg",
        "http://localhost:5000/static/images/image23.jpg",
        "http://localhost:5000/static/images/image24.jpg"
    ]

    random.shuffle(images)
    dict_data = []
    for index, value in enumerate(hotels_list):
        if index < len(images):
            dict_data.append({'name': value[0], 'imageUrl': images[index]})

    return jsonify(dict_data)


@app.route('/saveRates', methods=['GET', 'POST'])
def save_rate():
    username = session.get('name')
    temp = request.json
    new_data = [{'name': item['name'], 'rating': item['rating']}
                for item in temp['ratedOptions']]
    with app.app_context():
        for item in new_data:
            new_entry = Rating(username=username, hotel_name=item['name'], rating=item['rating'])
            db.session.add(new_entry)
        db.session.commit()
    return jsonify(request.json)


@app.route('/getrecommendations', methods=['GET'])
def get_recommendations():
    username = session.get('name')
    ratings = Rating.query.filter_by(username=username).all()
    rate_hotel_list = []
    rate_value = []
    for entry in ratings:
        rate_hotel_list.append(entry.hotel_name)
        rate_value.append(entry.rating)

    user = User.query.filter_by(name=username).first()
    selected_cluster = ast.literal_eval(user.selection)
    user_input = user.ideal
    best_rated_hotel_index = np.argmax(rate_value)
    best_rated_hotel = rate_hotel_list[best_rated_hotel_index]
    name_list = []

    df = pd.DataFrame(rate_hotel_list, columns=['name'])
    result_cos = recommend_cos(rate_value, df, selected_cluster)
    dict_data = [{'name': value} for value in result_cos]
    for value in result_cos:
        name_list.append(value)

    result_nlp = recommend_nlp(user_input)
    dict_data1 = [{'name': value} for value in result_nlp]
    for value in result_nlp:
        name_list.append(value)

    result_cf = recommend_cf(best_rated_hotel)
    dict_data2 = [{'name': value} for value in result_cf]
    for value in result_cf:
        name_list.append(value)

    name_list = list(set(name_list))
    # result = dict_data + dict_data1 + dict_data2

    columns_to_keep = ['name', 'WiFi', 'Free Parking', 'Swimming Pool', 'Facilities for Disabled Guests']
    df = pd.read_csv('results.csv', usecols=columns_to_keep)
    hotel_information = df[df['name'].isin(name_list)]
    hotel_information.rename(columns={'Facilities for Disabled Guests': 'Disabled Facilities'}, inplace=True)

    images = [
        "http://localhost:5000/static/images/image1.jpg",
        "http://localhost:5000/static/images/image2.jpg",
        "http://localhost:5000/static/images/image3.jpg",
        "http://localhost:5000/static/images/image4.jpg",
        "http://localhost:5000/static/images/image5.jpg",
        "http://localhost:5000/static/images/image6.jpg",
        "http://localhost:5000/static/images/image7.jpg",
        "http://localhost:5000/static/images/image8.jpg",
        "http://localhost:5000/static/images/image9.jpg",
        "http://localhost:5000/static/images/image10.jpg",
        "http://localhost:5000/static/images/image11.jpg",
        "http://localhost:5000/static/images/image12.jpg",
        "http://localhost:5000/static/images/image13.jpg",
        "http://localhost:5000/static/images/image14.jpg",
        "http://localhost:5000/static/images/image15.jpg",
        "http://localhost:5000/static/images/image16.jpg",
        "http://localhost:5000/static/images/image17.jpg",
        "http://localhost:5000/static/images/image18.jpg",
        "http://localhost:5000/static/images/image19.jpg",
        "http://localhost:5000/static/images/image20.jpg",
        "http://localhost:5000/static/images/image21.jpg",
        "http://localhost:5000/static/images/image22.jpg",
        "http://localhost:5000/static/images/image23.jpg",
        "http://localhost:5000/static/images/image24.jpg"
    ]

    random.shuffle(images)
    imglist = []
    for index, value in enumerate(list(hotel_information['name'].values)):
        if index < len(images):
            imglist.append(images[index])
    hotel_information['imgUrl'] = imglist  
    recommend_info = hotel_information.to_dict(orient='records')

    return jsonify(recommend_info)


@app.route('/getdiscount', methods=['GET', 'POST'])
def get_discount():
    username = session.get('name')
    print(username)
    user = User.query.filter_by(name=username).first()
    member = 'standard'
    if (user.goldmember == 'Yes'):
        member = 'gold'
    else:
        member = 'silver'
    data = request.json
    order = []
    order.append(str(data['checkInDate']))
    order.append(str(data['checkOutDate']))
    order.append(str(data['numberOfRooms']))
    order.append(member)
    with open("./bus_rule/order.txt", "w") as file:
        file.write(", ".join(order))
    rate = str(round(result() * 100))
    return jsonify({"message": "Successfully upload user selections", "discount": rate})


@app.route('/get-price', methods=['GET'])
def get_price():
    test_rule()
    return jsonify({"message": "Success"}), 200


@app.route('/test', methods=['POST', 'GET'])
def test():
    print(session)
    return jsonify(session), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Port 5000
