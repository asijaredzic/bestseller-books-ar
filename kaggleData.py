import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling Books from 2009 to 2022.")

# Sidebar: Add New Data
st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0, 0.5) # min and max values for sliders
    new_reviews = st.number_input("Reviews", min_value=0.0, step=0.1)
    new_price = st.number_input("Price", min_value=0.0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())

st.subheader("Summary Statistics")
total_books = books_df.shape[0] # (3, 2)
unique_titles = books_df['Name']. nunique()
average_rating = books_df["User Rating"].mean()
average_price = books_df["Price"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

# Dataset Preview
st.subheader("Dataset Preview")
st.write(books_df.head())

# Book Title Distribution and Author Distribution
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_author = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_author)

# Genre Distribution
st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title="Most Liked Genre (2009-2022)", color="G", color_discrete_sequence=px.colors.sequential)

st.plotly_chart(fig)

# Interactivity: filter Data By Genre
st.subheader("Filter Data by Genre")
genre_filter = st.selectbox("Select Genre", books_df["Genre"].unique())
filtered_df = books_df[books_df["Genre"] == genre_filter]
st.write(filtered_df)

