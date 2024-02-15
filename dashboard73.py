import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def cleaning_data (df_Data):
    # Copy DataFrame to avoid modifying original data
    data = df_Data.copy()
    
    # Fill missing values with forward fill method
    data.fillna(method='ffill', inplace=True)
    
    # Drop non-numeric columns
    non_numeric_columns = data.select_dtypes(exclude=['number']).columns
    data = data.drop(columns=non_numeric_columns)
    
    return data

def cleaning_data_wd (df_Data):
    # Copy DataFrame to avoid modifying original data
    data_wd = df_Data.copy()
    
    # Fill missing values with forward fill method
    data_wd.fillna(method='ffill', inplace=True)
    
    data_wd['tanggal'] = pd.to_datetime(data_wd[['year', 'month', 'day']], format='%Y-%m-%d')
    
    return data_wd

def pola_CurahHujan (data):
    #Perbandingan per bulan (atau sesuaikan dengan periode waktu yang diinginkan)
    # Buat kolom 'bulan'
    data['bulan'] = data['tanggal'].dt.strftime('%Y-%m')
    # Perbandingan Per Bulan
    monthly_comparison = data.groupby('bulan').mean()
    monthly_comparison
    # Ekstrak bulan dari kolom tanggal
    data['bulan'] = data['tanggal'].dt.month

    #    Perbandingan rata-rata curah hujan per bulan
    monthly_rain_comparison = data1.groupby('bulan')['RAIN'].mean()

    # Visualisasi pola musiman curah hujan
    plt.figure(figsize=(10, 6))
    sns.barplot(x=monthly_rain_comparison.index, y=monthly_rain_comparison)
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Curah Hujan')
    plt.title('Pola Musiman Curah Hujan')
    plt.show()
    
df_Data = load_data("https://github.com/logical030/Uas/blob/main/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
data_clean = cleaning_data (df_Data)
data_clean_wd = cleaning_data_wd (df_Data)

with st.sidebar:
    selected = option_menu('Menu', ['Dashboard'],
                           icons=["easel2", "graph-up"],
                           menu_icon="cast",
                           default_index=0)
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis pola musiman curah hujan")
    tab1, tab2, tab3 = st.tabs(["Pertanyaan 1", "Tab 2", "Tab 3"])

    with tab1:
        st.subheader('Pola Musiman Curah Hujan')
        pola_CurahHujan(data_clean)
    with tab2:
        st.header("Tab 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with tab3:
        st.header("Tab 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")