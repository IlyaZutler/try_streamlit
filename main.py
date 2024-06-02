import streamlit as st
import pandas as pd
import seaborn as sns

st.write("""
# My first app
Hello *world!*
""")

da_ta = st.date_input('wounderfull day')
df = sns.load_dataset('dowjones')

df.set_index('Date', inplace = True)
print(df)

st.line_chart(df)
st.write(da_ta)