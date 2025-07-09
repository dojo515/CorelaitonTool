# Streamlit-based Interactive Correlation Explorer

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import pearsonr

st.set_page_config(page_title="Correl-o-scope", layout="wide")
st.title("🔍 Correl-o-scope: Explore Correlation with Your Eyes!")

# Sidebar controls
st.sidebar.header("🎛️ Customize the Dataset")
n_points = st.sidebar.slider("Number of data points", min_value=10, max_value=500, value=100, step=10)
noise = st.sidebar.slider("Noise level", min_value=0.0, max_value=2.0, value=0.5, step=0.1)
nonlinear_pct = st.sidebar.slider("Nonlinear pattern (%)", min_value=0, max_value=100, value=0, step=1)
show_fit = st.sidebar.checkbox("Show trend lines", value=True)

# Generate data
np.random.seed(42)
x = np.linspace(-5, 5, n_points)
y_linear = x + np.random.normal(scale=noise, size=n_points)
y_nonlinear = np.sin(x) * (nonlinear_pct / 100)
y_mix = (1 - nonlinear_pct / 100) * y_linear + y_nonlinear
r, _ = pearsonr(x, y_mix)

# Linear & Nonlinear fits
linear_fit = np.poly1d(np.polyfit(x, y_mix, 1))(x)
nonlinear_fit = np.poly1d(np.polyfit(x, y_mix, 3))(x)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y_mix, mode='markers', name='Data', marker=dict(color='cornflowerblue')))
if show_fit:
    fig.add_trace(go.Scatter(x=x, y=linear_fit, mode='lines', name='Linear Fit', line=dict(dash='dash', color='red')))
    fig.add_trace(go.Scatter(x=x, y=nonlinear_fit, mode='lines', name='Nonlinear Fit', line=dict(dash='dot', color='green')))

fig.update_layout(title=f"📊 Correlation Explorer (Pearson r = {r:.2f})",
                  xaxis_title="X", yaxis_title="Y",
                  height=500, legend=dict(x=0, y=1))

st.plotly_chart(fig, use_container_width=True)

# Interpretation
st.subheader("🧠 Interpretation")
if abs(r) > 0.85:
    st.info("**Strong correlation detected.** But is it linear or nonlinear?")
elif abs(r) > 0.5:
    st.warning("**Moderate correlation.** Patterns exist, but might not be linear.")
elif abs(r) > 0.2:
    st.warning("**Weak correlation.** There might be hidden structure or noise.")
else:
    st.error("**No strong linear correlation.** Could still be nonlinear or due to outliers.")

# Quick quiz block
st.markdown("---")
st.subheader("🤔 Quick Check: Would a linear model be appropriate here?")
with st.expander("💡 Click to reveal answer"):
    if nonlinear_pct > 60 and abs(r) < 0.3:
        st.write("Probably not. The data shows a nonlinear shape and low r.")
    elif abs(r) > 0.8:
        st.write("Yes, a linear model might perform decently—but check the fit visually.")
    else:
        st.write("Unclear. Consider inspecting both linear and nonlinear fits.")

st.markdown("---")
st.caption("Correlation ≠ Causation. Use visuals, intuition, and context together!")
