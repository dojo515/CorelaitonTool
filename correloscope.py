# Streamlit-based Interactive Correlation Explorer with Anscombe's Quartet and Quiz Tab

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import pearsonr

st.set_page_config(page_title="Correl-o-scope", layout="wide")

# Tabs
main_tab, anscombe_tab, quiz_tab = st.tabs(["🔍 Correlation Explorer", "📊 Anscombe’s Quartet", "📝 Quiz Zone"])

with main_tab:
    # (Content unchanged from previous main tab)
    ...

with anscombe_tab:
    # (Content unchanged from previous anscombe tab)
    ...

with quiz_tab:
    st.title("📝 Quiz Zone: Test Your Correlation IQ")
    st.markdown("Try these 5 conceptual questions based on what you've explored so far:")

    quiz_score = 0

    q1 = st.radio("1. What does Pearson's correlation coefficient (r) measure?", [
        "The strength of any kind of relationship",
        "The linear relationship between two variables",
        "The average distance from the mean"
    ], key='quiz_q1')
    if q1:
        if q1 == "The linear relationship between two variables":
            st.success("Correct! Pearson’s r measures linear association.")
            quiz_score += 1
        else:
            st.error("Incorrect. r only captures linear relationships.")

    q2 = st.radio("2. If two variables have r = 0, what does it mean?", [
        "There’s absolutely no relationship",
        "They have no linear relationship",
        "One causes the other"
    ], key='quiz_q2')
    if q2:
        if q2 == "They have no linear relationship":
            st.success("Right! But there could still be a nonlinear one.")
            quiz_score += 1
        else:
            st.error("Not quite. Zero correlation only means no **linear** link.")

    q3 = st.radio("3. Why is it risky to rely only on correlation value?", [
        "Because r ignores units",
        "Because r can hide nonlinear or outlier effects",
        "Because it's hard to calculate"
    ], key='quiz_q3')
    if q3:
        if q3 == "Because r can hide nonlinear or outlier effects":
            st.success("Exactly! Always visualize your data.")
            quiz_score += 1
        else:
            st.error("Incorrect. Visualization reveals what r may miss.")

    q4 = st.radio("4. What is special about Anscombe’s Quartet?", [
        "Each dataset has a different correlation",
        "They all have the same mean",
        "They have the same correlation but look very different"
    ], key='quiz_q4')
    if q4:
        if q4 == "They have the same correlation but look very different":
            st.success("Spot on! That’s the magic of Anscombe’s Quartet.")
            quiz_score += 1
        else:
            st.error("Try again. It’s about the visual difference.")

    q5 = st.radio("5. Which of these is most likely to inflate the value of r?", [
        "Outliers",
        "Having too many points",
        "Measuring in percentages"
    ], key='quiz_q5')
    if q5:
        if q5 == "Outliers":
            st.success("Correct! Outliers can distort correlation heavily.")
            quiz_score += 1
        else:
            st.error("Nope. Outliers have the biggest impact on r.")

    # Final Score
    if all([q1, q2, q3, q4, q5]):
        st.markdown("---")
        st.subheader("🎯 Your Quiz Zone Score:")
        st.markdown(f"You scored **{quiz_score}/5**. Well done!")
        if quiz_score == 5:
            st.balloons()
        elif quiz_score >= 3:
            st.info("Good job! Review your weak spots and try again.")
        else:
            st.warning("Keep going! Revisit the visual and narrative feedback to improve.")
