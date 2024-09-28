from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('arti/spam_model.pkl')  # Adjust the path as necessary
vectorizer = joblib.load('model/vectorizer.pkl')

# Preprocessing function (you may want to include the one you use for training)
def preprocess(content):
    # Basic preprocessing, similar to the one used during training
    import re
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    
    st_content = re.sub(r'\W', ' ', content)
    st_content = re.sub(r'\s+', ' ', st_content)
    st_content = st_content.lower()
    st_content = st_content.split()
    st_content = [stemmer.stem(word) for word in st_content]
    
    return ' '.join(st_content)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        processed_message = preprocess(message)
        vect_message = vectorizer.transform([processed_message])
        prediction = model.predict(vect_message)

        if prediction[0] == 1:
            result = "Spam"
        else:
            result = "Not Spam"

        return render_template('index.html', prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
