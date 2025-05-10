import streamlit as st
import pandas as pd
import json 
import os from datetime import datetime
import time
import random
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

#set_page_config
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

#custom css for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .sub_header {
        font-size: 1.8rem !important;
        color: 3B82F6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    .success-message {
        padding: 1rem;
        background-color: #ECFDF5;
        border-left: 5px solid #10B981;
        border-radius: 0.375rem;
    }
    
    .warning-message {
        padding: 1rem;
        background-color: #FEF3C7;
        border-left: 5px solid F59E0B;
        border-radius: 0.375rem;
    }
    
    .book-card {
        background-color: #F3F4F6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 5px solid #3B82F6;
        transition: transform 0.3s ease;
        }
        
    .book-card-hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        }
        
        """)
