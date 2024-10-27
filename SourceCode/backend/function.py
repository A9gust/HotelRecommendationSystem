import os
os.environ["OMP_NUM_THREADS"] = '3'
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import random
import matplotlib.pyplot as plt
import spacy
import pickle

from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

file_path = r'la0730.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

nlp = spacy.load('en_core_web_sm')
facilities_keywords = {
    'Cleanliness': ['cleanliness', 'clean', 'hygiene'],
    'Comfort': ['comfort', 'comfortable', 'relax', 'cozy'],
    'Facilities': ['facilities', 'amenities', 'service'],
    'Swimming Pool': ['swimming pool', 'pool'],
    'Free WiFi': ['wifi', 'internet', 'free wifi'],
    'Restaurant': ['restaurant', 'dining', 'food', 'meal'],
    'Fitness Center': ['fitness', 'gym', 'exercise'],
    'Private Beach Area': ['beach', 'private beach']
}


def cluster():
    clustering_data = data[['Cleanliness', 'Comfort', 'Facilities', 'Staff', 'Value for money', 'Free WiFi']]
    clustering_data_cleaned = clustering_data.dropna()
    data_cleaned = data.loc[clustering_data_cleaned.index]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(clustering_data_cleaned)

    kmeans = KMeans(n_clusters=6, random_state=42)
    data_cleaned['Cluster'] = kmeans.fit_predict(scaled_data)
    data_cleaned.to_csv('results.csv', index=False)
    return


def clustering():
    data_cleaned = pd.read_csv('results.csv')
# Step 1: keep one hotel from the cluster
    random_hotels = data_cleaned.groupby('Cluster')[['name', 'Cluster']].apply(lambda x: x.sample(n=1)).reset_index(drop=True)
    # random_hotels['name'] = ['City Hotel', 'Mountain View', 'Beach Resort',
    #                          'Glamping', 'Tree House', 'Overwater Bungalow']
    random_hotels['image'] = ['http://localhost:5000/static/city-hotel.png',
                                'http://localhost:5000/static/mountain-view.png',
                                'http://localhost:5000/static/beach-resort.png',
                                'http://localhost:5000/static/glamping.png',
                                'http://localhost:5000/static/tree-house.png',
                                'http://localhost:5000/static/overwater-bungalow.png']
    temp = random_hotels[['name', 'Cluster']]
    return temp


def output_rateitems(selected_clusters):
    df = pd.read_csv('results.csv')
    random_hotels = pd.DataFrame()

    # Loop through the specified clusters and sample 5 hotels from each cluster
    for cluster_id in selected_clusters:
        cluster_data = df[df['Cluster'] == cluster_id]
        sampled_hotels = cluster_data.sample(n=5, random_state=42)
        random_hotels = pd.concat([random_hotels, sampled_hotels])
    random_hotels = random_hotels[['name']].values
# Display the randomly sampled hotels from the specified clusters
    return random_hotels


# Preprocess the user input
def extract_facilities_from_input(user_input):
    user_input_doc = nlp(user_input.lower())
    extracted_facilities = set()
    for token in user_input_doc:
        for facility, keywords in facilities_keywords.items():
            if token.lemma_ in keywords:
                extracted_facilities.add(facility)
    return list(extracted_facilities)


def calculate_hotel_scores(user_facilities, hotel_data):
    if not user_facilities:
        return pd.Series([0] * len(hotel_data))

    scores = hotel_data[user_facilities].mean(axis=1)
    return scores


def recommend_cos(user_ratings, hotels_list, selected_cluster):
    data_cleaned = pd.read_csv('results.csv')
    hotels_in_selected_cluster = pd.DataFrame()
    selected_hotels = data_cleaned.groupby('Cluster').apply(lambda x: x.sample(n=15)).reset_index(drop=True)
    for i in selected_cluster:
        hotels_in_current_cluster = selected_hotels[selected_hotels['Cluster'] == i]
        hotels_in_selected_cluster = pd.concat([hotels_in_selected_cluster, hotels_in_current_cluster], ignore_index=True)
    best_rated_hotel_index = np.argmax(user_ratings)
    best_rated_hotel = hotels_list.iloc[best_rated_hotel_index]
    hotel_features = hotels_in_selected_cluster[['Cleanliness', 'Comfort', 'Facilities', 'Staff', 'Value for money', 'Free WiFi']].dropna()
    similarity_matrix = cosine_similarity(hotel_features)
    best_hotel_index = hotel_features.index.get_loc(best_rated_hotel.name)
    similarities = similarity_matrix[best_hotel_index]
    most_similar_indices = np.argsort(similarities)[-2:][::-1] 
    recommended_hotels = hotels_in_selected_cluster.iloc[most_similar_indices]
    return recommended_hotels['name'].values


def recommend_nlp(user_input):
    user_facilities = extract_facilities_from_input(user_input)
    data['user_specific_score'] = calculate_hotel_scores(user_facilities, data)
    top_hotels = data.nlargest(5, 'user_specific_score')
    return list(top_hotels['name'])


def recommend_cf(best_rated_hotel):
    df = pd.read_csv('trainset.csv')
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)
    trainset = data.build_full_trainset()

    with open('knn_model.pkl', 'rb') as f:
        loaded_algo = pickle.load(f)
    similar_items = loaded_algo.get_neighbors(trainset.to_inner_iid(best_rated_hotel), k=5)
    similar_hotels = [trainset.to_raw_iid(inner_id) for inner_id in similar_items]

    return similar_hotels


if __name__ == '__main__':
    df = pd.read_csv('results.csv')
    print(df.head)
