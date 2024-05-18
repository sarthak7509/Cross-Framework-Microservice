from django.shortcuts import render
from rest_framework.views import APIView
import os
import pickle
import pandas as pd
from rest_framework.response import Response
# Create your views here.
COSINE_PATH = os.path.join("media","cosine.pkl")
FORMATTED_PATH = os.path.join("media","formatted.csv")
INDICES_PATH = os.path.join("media","indices.pkl")

class MovieRecommadation(APIView):
    # Function that takes in movie title as input and outputs most similar movies
    def get_recommendations(self,title:str):
        with open(COSINE_PATH,'rb') as f:
            cosine_sim = pickle.load(f)

        df2 = pd.read_csv(FORMATTED_PATH)

        indices = pd.read_pickle(INDICES_PATH)

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return df2['title'].iloc[movie_indices]
    

    def post(self,request,*args,**kwargs):
        title = request.data['title']
        return Response(self.get_recommendations(title))
    
    def get(self,request,*args,**kwargs):
        df2 = pd.read_csv(FORMATTED_PATH)
        return Response(df2['title'])