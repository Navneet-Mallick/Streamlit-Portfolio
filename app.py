import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Page Config
st.set_page_config(page_title="Navneet Mallick | Portfolio", page_icon="💻", layout="wide")

# Custom CSS for the "Awesome" look
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SIDEBAR / NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Skills", "Contact"],
        icons=["house", "code-slash", "brain", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#0f111a"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "orange"},
        }
    )

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.image("nm.jpeg", width=250)
    with col2:
        st.title("Navneet Mallick")
        st.subheader("Software Developer & ML Enthusiast")
        st.write("""
        Engineering student at IOE Purwanchal Campus. 
        I build intelligent systems and beautiful web interfaces. 
       
        """)
        if st.button("Download CV"):
            st.write("Generating Download Link...")

# --- PROJECTS SECTION ---
if selected == "Projects":
    st.header("My Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://img.freepik.com/premium-vector/movie-theater-signboard-blue_34230-295.jpg")
        st.subheader("Movie Recommender")
        st.write("Content-based filtering system built with Streamlit.")
        st.markdown("[View App](https://movie-recommender-navneet.streamlit.app/)")

    with col2:
        st.image("https://storage.googleapis.com/kaggle-datasets-images/4210881/7265027/dataset-cover.jpg")
        st.subheader("Car Price Predictor")
        st.write("Linear Regression model to predict resale value.")
        st.markdown("[View App](https://carpredictor-navneet.streamlit.app/)")

# --- SKILLS SECTION ---
if selected == "Skills":
    st.header("Technical Toolbox")
    
    # Using columns for the "Sectional" look you wanted
    tab1, tab2, tab3 = st.tabs(["Web Dev", "ML & AI", "Tools"])
    
    with tab1:
        st.write("HTML/CSS")
        st.progress(95)
        st.write("JavaScript")
        st.progress(90)
        st.write("Node.js")
        st.progress(85)

    with tab2:
        st.write("Python")
        st.progress(90)
        st.write("Machine Learning")
        st.progress(75)
        st.write("Data Science")
        st.progress(65)

    with tab3:
        st.write("SQL")
        st.progress(85)
        st.write("Django")
        st.progress(50)

# --- CONTACT SECTION ---
if selected == "Contact":
    st.header("Get In Touch")
    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)