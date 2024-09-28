from flask import Flask, render_template, request
import joblib,os

app = Flask(__name__) #

@app.route('/',methods=['GET'])  
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])  
def training():
    os.system("python main.py")
    return "Training Successful!"



model = joblib.load('artifacts/model_train/model.joblib') 
vectorizer = joblib.load('artifacts/model_train/vector.joblib')


def preprocess(content):
    
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
