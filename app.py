
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# Set the title of the app
st.title("Automated Data Analysis Tool")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show dataframe
    st.subheader("Data Overview")
    st.write(df.head())

    # Show data types and column values
    st.subheader("Column Data Types")
    st.write(df.dtypes)

    # Univariate Analysis
    st.subheader("Univariate Analysis")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in numeric_cols:
        st.write(f"Distribution of {col}:")
        plt.figure(figsize=(10, 5))
        sns.histplot(df[col], kde=True, color='Purple')
        st.pyplot(plt)

    # Bivariate Analysis
    st.subheader("Bivariate Analysis")
    bivariate_col_x = st.selectbox("Select X-axis for Bivariate Analysis", numeric_cols)
    bivariate_col_y = st.selectbox("Select Y-axis for Bivariate Analysis", numeric_cols)
    
    if bivariate_col_x and bivariate_col_y:
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=df, x=bivariate_col_x, y=bivariate_col_y, palette="rainbow")
        st.pyplot(plt)

    

    # Categorical Analysis
    st.subheader("Categorical Analysis")
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    if cat_cols:
        cat_col = st.selectbox("Select a categorical column for analysis", cat_cols)
        if cat_col:
            st.write(df[cat_col].value_counts())
            plt.figure(figsize=(10, 5))
            sns.countplot(y=df[cat_col], palette="rocket")
            st.pyplot(plt)

    # Missing Value Analysis
    st.subheader("Missing Value Analysis")
    st.write("Total Missing Values:")
    st.write(df.isnull().sum())
    
    if st.checkbox("Show Missing Value Heatmap"):
        plt.figure(figsize=(10, 5))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        st.pyplot(plt)

    # Handling Missing Values
    st.subheader("Handle Missing Values")
    missing_value_option = st.selectbox("Choose how to handle missing values", ["Drop rows", "Fill with mean", "Fill with median", "Fill with mode"])
    
    if missing_value_option == "Drop rows":
        df = df.dropna()
        st.write("Rows with missing values dropped.")
    elif missing_value_option == "Fill with mean":
        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)
        st.write("Missing values filled with mean.")
    elif missing_value_option == "Fill with median":
        for col in numeric_cols:
            df[col].fillna(df[col].median(), inplace=True)
        st.write("Missing values filled with median.")
    elif missing_value_option == "Fill with mode":
        for col in cat_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)
        st.write("Missing values filled with mode.")

    # Outlier Detection
    st.subheader("Outlier Detection")
    outlier_col = st.selectbox("Select a column to detect outliers", numeric_cols)
    if outlier_col:
        plt.figure(figsize=(10, 5))
        sns.boxplot(x=df[outlier_col], palette="magma")
        st.pyplot(plt)

    





