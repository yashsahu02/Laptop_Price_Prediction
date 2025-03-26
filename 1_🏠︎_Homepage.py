import streamlit as st 

import numpy as np
import pandas as pd
import pickle

st.set_page_config(
    page_title = "Laptop Price Prediction",
    page_icon="💻"
)

st.title('Laptop Price Prediction')

model = pickle.load(open('models/model.pkl','rb'))
df = pickle.load(open('models/dataframe.pkl','rb'))
cat_col_list = pickle.load(open('models/cat_col_list.pkl','rb'))
preprocessor = pickle.load(open('models/preprocessor.pkl','rb'))


company_list = df['Company'].unique()
selected_company = st.selectbox(
    'Select Company',
    company_list,
)


product_dict = df.groupby('Company')['Product'].unique().to_dict()
product_list = product_dict[selected_company]

selected_product = st.selectbox(
    'Select Product',
    product_list
)

type_dict = df.groupby('Company')['TypeName'].unique().to_dict()
type_list = type_dict[selected_company]

selected_typeName = st.selectbox(
    'Select Type',
    type_list
)

selected_inches = st.selectbox(
    'Screen Size in Inches',
    sorted(list(set(df['Inches'])))
)


selected_ram = st.selectbox(
    'Select RAM Size',
    sorted(list(set(df['Ram'])))
)

os_dict = df.groupby('Company')['OS'].unique().to_dict()
os_list = os_dict[selected_company]
selected_os = st.selectbox(
    'Select OS',
    os_list
)

selected_weight = st.selectbox(
    'Select Weight',
    sorted(list(set(df['Weight'])))
)

selected_screen_type = st.selectbox(
    'Select Screen Type',
    sorted(list(set(df['Screen'])))
)

selected_ScreenW = st.selectbox(
    'Select ScreenW',
    sorted(list(set(df['ScreenW'])))
)

selected_ScreenH = st.selectbox(
    'Select ScreenH',
    sorted(list(set(df['ScreenH'])))
)

selected_Touchscreen = st.selectbox(
    'Touchscreen',
    df['Touchscreen'].unique()
)

selected_IPSpanel = st.selectbox(
    'IPSpanel',
    df['IPSpanel'].unique()
)

selected_RetinaDisplay = st.selectbox(
    'RetinaDisplay',
    df['RetinaDisplay'].unique()
)

CPU_company_dict = df.groupby('Company')['CPU_company'].unique().to_dict()
CPU_company_list = CPU_company_dict[selected_company]
selected_CPU_company = st.selectbox(
    'Select CPU Comapny',
    CPU_company_list
)

selected_CPU_freq = st.selectbox(
    'Select CPU_freq',
    sorted(list(set(df['CPU_freq'])))
)

CPU_model_dict = df.groupby('CPU_company')['CPU_model'].unique().to_dict()
CPU_model_list = CPU_model_dict[selected_CPU_company]
selected_CPU_model = st.selectbox(
    'Select CPU Model',
    CPU_model_list
)

selected_PrimaryStorage = st.selectbox(
    'Select Primary Storage',
    sorted(list(set(df['PrimaryStorage'])))
)

selected_SecondaryStorage = st.selectbox(
    'Select Secondary Storage',
    sorted(list(set(df['SecondaryStorage'])))
)

selected_PrimaryStorageType = st.selectbox(
    'Select Primary Storage Type',
    sorted(list(set(df['PrimaryStorageType'])))
)

selected_SecondaryStorageType = st.selectbox(
    'Select Secondary Storage Type',
    sorted(list(set(df['SecondaryStorageType'])))
)

GPU_company_dict = df.groupby('Company')['GPU_company'].unique().to_dict()
GPU_company_list = GPU_company_dict[selected_company]
selected_GPU_company = st.selectbox(
    'Select GPU Company',
    GPU_company_list
)

GPU_model_dict = df.groupby('GPU_company')['GPU_model'].unique().to_dict()
GPU_model_list = GPU_model_dict[selected_GPU_company]
selected_GPU_model = st.selectbox(
    'Select GPU Model',
    GPU_model_list
)


input = pd.DataFrame([[selected_company,selected_product,selected_typeName,selected_inches,selected_ram,selected_os,selected_weight,selected_screen_type,selected_ScreenW,selected_ScreenH,selected_Touchscreen,selected_IPSpanel,selected_RetinaDisplay,selected_CPU_company,selected_CPU_freq,selected_CPU_model,selected_PrimaryStorage,selected_SecondaryStorage,selected_PrimaryStorageType,selected_SecondaryStorageType,selected_GPU_company,selected_GPU_model]],
                     columns=['Company', 'Product', 'TypeName', 'Inches', 'Ram', 'OS', 'Weight', 'Screen', 'ScreenW', 'ScreenH', 'Touchscreen', 'IPSpanel', 'RetinaDisplay', 'CPU_company', 'CPU_freq', 'CPU_model','PrimaryStorage', 'SecondaryStorage', 'PrimaryStorageType','SecondaryStorageType', 'GPU_company', 'GPU_model'])


# input = pd.get_dummies(input,columns=cat_col_list,drop_first=True,dtype=int)
input = preprocessor.transform(input)


if st.button('Generate Output',on_click=None,type="secondary"):
    output=model.predict(input)
    output = round(output[0], 2)
    output = str(output) + " €"
    st.title(output)
    

app_sidebar = st.sidebar

with app_sidebar:
    st.link_button(
        label="Project Link",
        url="https://github.com/yashsahu02/Laptop_Price_Prediction.git",
        # icon=":material/code_off:",
        use_container_width=True
    )