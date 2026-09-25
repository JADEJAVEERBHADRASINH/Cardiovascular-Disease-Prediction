"""
Cached dataset loader for cardio_train.csv.
Uses @st.cache_data for instant interactive chart filtering without re-reading disk.
"""
import os
import streamlit as st
import pandas as pd

@st.cache_data(show_spinner=False)
def load_cardio_dataset():
    """
    Loads cardio_train.csv with cached optimization.
    Computes age_years and bmi for fast interactive chart filtering.
    """
    # Check current directory, then parent directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        "cardio_train.csv",
        os.path.join(base_dir, "cardio_train.csv"),
        os.path.join("..", "cardio_train.csv")
    ]
    
    file_path = None
    for p in candidates:
        if os.path.exists(p):
            file_path = p
            break
            
    if file_path is None:
        return None
    
    df = pd.read_csv(file_path, sep=";")
    df["age_years"] = (df["age"] / 365.0).round(1)
    df["height_m"] = df["height"] / 100.0
    df["bmi"] = (df["weight"] / (df["height_m"] ** 2)).round(1)
    
    # Human-readable labels for plotting
    df["target_label"] = df["cardio"].map({0: "Healthy (No CVD)", 1: "Cardiovascular Disease"})
    df["gender_label"] = df["gender"].map({1: "Female", 2: "Male"})
    df["chol_label"] = df["cholesterol"].map({1: "Normal", 2: "Above Normal", 3: "High"})
    df["gluc_label"] = df["gluc"].map({1: "Normal", 2: "Above Normal", 3: "High"})
    df["smoke_label"] = df["smoke"].map({0: "Non-Smoker", 1: "Smoker"})
    df["alco_label"] = df["alco"].map({0: "No Alcohol", 1: "Alcohol Consumer"})
    df["active_label"] = df["active"].map({0: "Inactive", 1: "Active"})
    
    return df
