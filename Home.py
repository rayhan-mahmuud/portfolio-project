import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([0.2, 0.8])

with col1:
    st.image("images/my_image.jpg", width=230)

with col2:
    st.title("Rayhan Mahmud")
    content = """Hi, I'm Rayhan Mahmud. I graduated in 2022 with a BSc in Electrical & Electronic Engineering. Coding 
    and problem solving have always been my passions, and I'm currently focused on learning Python.

Welcome to my portfolio website, where I showcase my Python projects. Here, you'll find a collection of my work that 
highlights my journey in mastering Python and applying it to solve various challenges. I enjoy developing innovative 
solutions and continuously pushing myself to improve my skills.

Feel free to explore my projects and see how I've combined my engineering background with my love for coding. Thank 
you for visiting!"""

    st.write(content)
st.write("---")

df = pd.read_csv("data.csv")

col3,  col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}", width=400)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")
        st.write("---")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}", width=400)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")
        st.write("---")


