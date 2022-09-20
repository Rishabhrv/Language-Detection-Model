import pickle
import streamlit as st
import pandas as pd
from PIL import Image

lang = pickle.load(open(r'C:\Users\pc\ML\Projects\Language Detection\\lang.pkl','rb'))
cv = pickle.load(open(r'C:\Users\pc\ML\Projects\Language Detection\\cv.pkl','rb'))
le = pickle.load(open(r'C:\Users\pc\ML\Projects\Language Detection\\lable_encoder.pkl','rb'))
df = pd.read_csv(r'C:\Users\pc\ML\Projects\Language Detection\\language.csv',index_col=False)

image = Image.open(r'C:\Users\pc\ML\Projects\Recc Movie\myimage.jpg')

def predict(text):
    x = cv.transform([text]).toarray() # converting text to bag of words model (Vector)
    lan = lang.predict(x) # predicting the language
    lan = le.inverse_transform(lan) # finding the language corresponding the the predicted value
    #print("The langauge is in",lan[0]) # printing the language
    return lan


st.title('Language Detection')

st.sidebar.write('Built By -')
st.sidebar.title('Rishabh Vyas')
st.sidebar.image(image,caption='Machine Learning Engineer',width=160)
st.sidebar.write('E-mail - rishabhvyas472@gmail.com')

text = st.text_area(max_chars=100,label='Enter your Text Here')

if st.button('Detect'):
    pred = predict(text)
    st.header('The langauge is '+pred[0])
    
    
if st.button('Languages we support'):
    st.table(df)
    #lang = df.Language.uniqueg()
    #for i in lang:
        #st.write(i)