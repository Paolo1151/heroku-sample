import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 4: Adding plots to Streamlit

df = pd.read_csv("data/2016-2019-voter-data.csv")

# 5: Adding interactive options: checkbox

if st.checkbox('Show data', value=True):
    st.subheader('Data')
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.markdown('Loading data...**done!**')


st.title("Data")
# Add section header
st.header("data/2016-2019 Philippine Voter Dataset")

# Add any text
data_load_state = st.text('Loading data...')
df = pd.read_csv("data/2016-2019-voter-data.csv")
st.write(df.head(20))

# Customize texts using markdown
st.markdown('Loading data...**done!**')

region_voter = df.groupby("Region")["2019-Registered_Voters"].sum()

#Copy paste your code from Jupyter but assign plt.figure to variable

fig = plt.figure(figsize=(8,6)) 

# the main code to create the graph
plt.bar(region_voter.index, region_voter.values) 

# additional elements that can be customzed
plt.title("Number of Registered Voters by Region", fontsize=16)
plt.ylabel("Number of Registered Voters", fontsize=12)
plt.xlabel("Region", fontsize=12)
plt.xticks(rotation=45)

# display graph
plt.show()

# display graph by plotting figure variable
st.pyplot(fig=fig)

# 6: Adding interactive options: selectbox

#Create selectbox
option = st.selectbox('Please Select an Option: ', df['Region'].unique())

'You selected: ', option

# Filter the entry in the plot
province_level = df[df['Region']==option].groupby("Province")["2019-Registered_Voters"].sum()

# store figure in fig variable
fig = plt.figure(figsize=(8,6)) 

plt.bar(province_level.index, province_level.values) 

plt.title("Registered Voters by Province", fontsize=16)
plt.ylabel("Number of Registered Voters", fontsize=12)
plt.xlabel("Province", fontsize=12)
plt.xticks(rotation=45)

# display graph
st.pyplot(fig)