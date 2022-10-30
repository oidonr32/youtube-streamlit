import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']    
# )
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# if st.checkbox('Show Image'):
#     img = Image.open('./Pictures/DSC_0206_.jpg')
#     st.image(img, caption='Running Shoes', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# option = st.sidebar.text_input('あなたの趣味は？')
# condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)

# 'あなたの趣味は、', option, 'です。'
# 'コンディション：', condition
