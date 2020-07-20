from flask import Flask, redirect
from flask_restful import reqparse, abort, Api, Resource, request
import pickle
import numpy as np
from model import NLPModel



app = Flask(__name__)
api = Api(app)

model = NLPModel()

clf_path = 'lib/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

vec_path = 'lib/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        userStr = str(user_query)

        # vectorize the user's query and make a prediction
        uq_vectorized = model.vectorizer_transform(np.array([userStr]))
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)

        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'
            
        # round the predict proba value and set to new variable
        confidence = round(pred_proba[0], 3)

        # create JSON object
        return {'prediction': pred_text, 'confidence': confidence}
      
    
# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/statment')


#Display the Pridiction On web
#From EndPoints
@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        query = request.form.get('query')
        return redirect("http://127.0.0.1:5000/statment?query={}".format(query))

    return ''' <h1>Sentiment prediction</h1>
    <form method="POST" >
    Query <input type="text" name="query">
    <input type="submit">
    </form> '''

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

