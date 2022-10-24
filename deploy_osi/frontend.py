import streamlit as st
import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt

def run():
    #Set page_title and title
    st.title ('Exploratory Data Analysis')

    # Make Sub  Header
    st.subheader('EDA of Online Shopper Intention Analysis')

    # Make Description
    st.write('Afifah Rahma - Batch-015-RMT')

    # Make a line
    st.markdown('-----------')

    # Make brief explanation
    st.write("Below are some of the simple exploratory data analysis of online shopper. The dataset are taken from kaggle.com.")
    st.write("[Access Dataset >](https://www.kaggle.com/datasets/henrysue/online-shoppers-intention)")

    lottie_pic ="https://assets7.lottiefiles.com/packages/lf20_9aaqrsgf.json"

    st.markdown("-----------")


    # Show DataFrame
    st.write('### Online Shopper Intention Dataset')
    df = pd.read_csv('https://raw.githubusercontent.com/afifahrahma/learning_data/main/online_shoppers_intention.csv')

    st.dataframe(df)

    # Membuat pie-chart
    st.write('#### Percentage of Revenue')
    fig = plt.figure(figsize=(3,3))
    df.Revenue.value_counts().plot(kind='pie', figsize=(3,3), autopct='%1.1f%%')
    plt.title('Percentage of Revenue', fontsize= 5)
    st.pyplot(fig)


    # Show Histogram of features
    st.write('#### Histogram based on User Input')
    opt = st.selectbox('Choose column: ', ['BounceRates', 'ExitRates', 'ProductRelated', 'ProductRelated_Duration', "Administrative", "Informational", "ProductRelated_Duration", "ExitRates", "PageValues", "SpecialDay"], index=1)
    fig=plt.figure(figsize=(15,5))
    sns.histplot(df[opt], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Barplot
    st.write('#### Barplot based on User Input')
    opt = st.selectbox('Choose column: ', ['OperatingSystems', 'Browser', 'Region', 'VisitorType', 'Weekend', 'Month'])
    fig= plt.figure(figsize = (10,5))
    sns.countplot(x = opt,
                data = df,
                order = df[opt].value_counts().index)
    st.pyplot(fig)

if __name__ == '__main__':
    run()