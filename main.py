from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model components
cv = joblib.load('cv_model.pkl')
similarity = joblib.load('similarity_matrix.pkl')
new = joblib.load('movies_data.pkl')

def recommendation(movie_title):
    # Check if the movie exists in the dataset
    if movie_title not in new['title'].values:
        return "Movie not found in the dataset."
    
    # Find the index of the movie
    index = new[new['title'] == movie_title].index[0]
    
    # Calculate the similarity scores
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Get the top 5 recommendations
    recommendations = []
    for i in distance[1:6]:  # Exclude the first item as it is the input movie itself
        recommendations.append(new.iloc[i[0]].title)
    
    return recommendations

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit1', methods=['POST'])
def submit1():
    movie_name = request.form.get('reco')
    
    if movie_name:
        re = recommendation(movie_name)
        return render_template('result.html', movie_name=movie_name, recommendations=re)
    return "No movie name provided."


if __name__ == '__main__':
    app.run(host = "0.0.0.0",port=3456, debug=True)
#http://127.0.0.1:3456/recommend?title=Spectre