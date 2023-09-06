import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
from PIL import Image
import time


tokyo_lat = 35.69
tokyo_lon = 139.69

option_check = st.checkbox('DataFrameの表示')

df_tokyo = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[tokyo_lat, tokyo_lon],
    columns=['lat','lon']
)

if option_check == True:
    st.write(df_tokyo)

option_select = st.selectbox(
    'どれか一つ選択してください',
    ('A', 'B', 'C')
)
st.write('あなたが選んだのは：', option_select)




option_radio = st.radio(
    "好きな果物を選んでください",
    ('りんご', 'バナナ', 'オレンジ', 'その他')
)
st.write('あなたが選んだ果物は : ', option_radio)


option_button = st.button('ボタン')
if option_button == True:
    st.write('ボタンが押されました')
else:
    st.write('ボタンを押してください')


image =Image.open('01.jpg')
st.image(image, caption='サンプル１', use_column_width=True)





view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

hexagon_layer = pdk.Layer('HexagonLayer',
                          data=df_tokyo,
                          get_position = ['lon','lat'],
                          elevation_scale=3,
                          radius=200,
                          extruded=True
                          )

layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)

st.pydeck_chart(layer_map)

