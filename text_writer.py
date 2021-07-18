import streamlit as st
if st.button("write"):
	r = open("text.txt", "r").read()
	w = r + "\nHi my name is Prabhupada Pradhan."
	f = open("text.txt", "w").write(w)