import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)
# Create some sample text
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
df=pd.read_csv("result.csv")

comment_words = ''
stopwords = set(STOPWORDS)
 
st.write("wordcloud:")
# iterate through the csv file
for val in df.transcribed_audio:
      
    # typecaste each val to string
    val = str(val)
  
    # split the value
    tokens = val.split()
      
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
      
    comment_words += " ".join(tokens)+" "
  
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
st.pyplot()



import ast 

age=""
dominant_emotion=""
dominant_race=""
gender=""

for i in df.frames_analysis:
#     print(i)
    res = ast.literal_eval(i) 
#     print(res["age"])
#     print(res["dominant_race"])
#     print(res["dominant_emotion"])
#     print(res["gender"])
    
    age=age+" "
    dominant_emotion=dominant_emotion+" "
    dominant_race=dominant_race+" "
    gender=gender+" "
    
    age = age+' '.join([str(elem) for elem in res["age"]]) 
    dominant_emotion = dominant_emotion+' '.join([str(elem) for elem in res["dominant_emotion"]]) 
    dominant_race = dominant_race+' '.join([str(elem) for elem in res["dominant_race"]]) 
    gender = gender+' '.join([str(elem) for elem in res["gender"]])


st.write("age:")
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                min_font_size = 10,include_numbers=True).generate(age)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
st.pyplot()

st.write("emotion:")
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                min_font_size = 10,include_numbers=True).generate(dominant_emotion)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
st.pyplot()


st.write("race:")
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                min_font_size = 10,include_numbers=True).generate(dominant_race)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
st.pyplot()


st.write("gender:")
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                min_font_size = 10,include_numbers=True).generate(gender)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
st.pyplot()