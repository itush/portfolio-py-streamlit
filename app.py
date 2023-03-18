import requests
import streamlit as st
from streamlit_lottie import st_lottie

# basic page config:
st.set_page_config(page_title ="Tushar Biswas", page_icon=":tada:")

# Error handling function
def img_url(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

# Header
with st.container():    
    st.subheader("Namaste! 🙏 my name is Tushar Biswas,")
    st.write("I'm a Frontend web developer from India 🇮🇳 I build modern websites with 100% money back guarantee for my clients. I feel, Programing is Painful yet Perky😀 So if you need help with your project or simply have some questions, please feel free to contact me!")


# ---- LOAD ASSETS ----
hero_img = img_url("https://assets7.lottiefiles.com/packages/lf20_iv4dsx3q.json")

st_lottie(hero_img, width=300, key="coding")