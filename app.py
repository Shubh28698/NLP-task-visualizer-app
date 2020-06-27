import pandas as pd
import numpy as np 
import streamlit as st
from nltk.tokenize import word_tokenize
import os
import re
from translate import Translator
import nltk


@st.cache
def tokenize(msg):
	text=msg
	nltk_tokens = word_tokenize(text)
	return(nltk_tokens)


@st.cache
def extract_email(msg):
	text=msg
	emails=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
	return(emails)

@st.cache
def translate(msg):
	text=msg
	translator=Translator(to_lang="German")
	translation = translator.translate(msg)
	return(translation)

@st.cache
def count(msg):
	text=msg
	nltk_tokens = nltk.word_tokenize(text)
	print(nltk_tokens)
	print("\n")
	return("Number of Words: " , len(nltk_tokens))


		


		
def main():
	st.title("Visual NLP Tasks application")
	st.subheader("Welcome to the application !!!! Visualize NLP tasks in one click")



	if st.sidebar.checkbox("Show tokenization"):
		st.subheader("tokenize your text data")
		msg=st.text_area("Enter your text","Type here")
		if st.button("Tokenize"):
			final_result=tokenize(msg)
			st.write(final_result)


	if st.sidebar.checkbox("Show extracted e-mails"):
		st.subheader("Extract emails from  your text data")
		msg=st.text_area("Enter your text for extracting e-mails","Type here")
		if st.button("Extract e-mails"):
			final_result=extract_email(msg)
			st.write(final_result)


	if st.sidebar.checkbox("Show translation into german"):
		st.subheader("Translate your text data into german")
		msg=st.text_area("Enter your text for translation","Type here")
		if st.button("translate"):
			final_result=translate(msg)
			st.write(final_result)

	if st.sidebar.checkbox("Calculate no. of words"):
		st.subheader("calculate no. of words from text data")
		msg=st.text_area("Enter your text for word counting","Type here")
		if st.button("calculate"):
			final_result=count(msg)
			st.write(final_result)



st.markdown("""
<style>
body {
    color: #fff;
    background-color: #001f3f;
    etc. 
}
</style>
    """, unsafe_allow_html=True)
    




st.sidebar.subheader("About App")
st.sidebar.info("This app can help you visualize NLP tasks on your text")

    

    

if __name__ == '__main__':
	main()






