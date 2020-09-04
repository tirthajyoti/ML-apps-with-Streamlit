import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("2-D Gaussian heatmap using Seaborn")

code = """
data_density = st.slider("Data density",
                    min_value= 25,
                    max_value=200,
                    value=75,
                    step=25)

sigma = st.slider("Sigma",
                    min_value= 0.1,
                    max_value=2.0,
                    value=1.0,
                    step=0.1)

mu = st.slider("Sigma",
                    min_value= -1.0,
                    max_value=1.0,
                    value=0.0,
                    step=0.1)

x, y = np.meshgrid(np.linspace(-2,2,data_density), np.linspace(-2,2,data_density))
d = np.sqrt(x*x+y*y)
sigma, mu = sigma, mu
g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
sns.heatmap(g)
"""

st.markdown("## Code")
st.code(code)

st.markdown("## Controls")

data_density = st.slider("Data density",
                    min_value= 25,
                    max_value=200,
                    value=75,
                    step=25)

sigma = st.slider("Sigma",
                    min_value= 0.1,
                    max_value=2.0,
                    value=1.0,
                    step=0.1)

mu = st.slider("Sigma",
                    min_value= -1.0,
                    max_value=1.0,
                    value=0.0,
                    step=0.1)

x, y = np.meshgrid(np.linspace(-2,2,data_density), np.linspace(-2,2,data_density))
d = np.sqrt(x*x+y*y)
sigma, mu = sigma, mu
g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
sns.heatmap(g)

st.markdown("## Plot")
st.pyplot()