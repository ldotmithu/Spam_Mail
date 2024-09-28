import streamlit as st
import re,joblib
from nltk.stem import PorterStemmer

poter =PorterStemmer() 
from sklearn.feature_extraction.text import TfidfVectorizer
model=joblib.load('artifacts/model_train/model.joblib')
tfidf=joblib.load('artifacts/model_train/vector.joblib')
st.title('Spam Mail Detection')

def nlp_preprocess(content):
    st_content= re.sub(r'\W', ' ', content)
    st_content=re.sub(r'\s+', ' ', st_content)
    st_content= st_content.lower()
    st_content=st_content.split()
    st_content=[poter.stem(word) for word in st_content]
    return ' '.join(st_content)

email_text = st.text_area('Enter the email text : ')

if st.button('Predict'):
    try:
        email_cleaned = nlp_preprocess(email_text)
        email_vectorized = tfidf.transform([email_cleaned])
        prediction = model.predict(email_vectorized)
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        st.write('prediction', result)
    except Exception as e:
        raise e