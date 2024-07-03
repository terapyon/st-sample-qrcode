from io import BytesIO
import streamlit as st
import qrcode


st.title("QRコード生成アプリ・改造")
text = st.text_input("QRコードに変換したい文字列を入力してください")
if text and st.button("QRコードを生成する"):
    with BytesIO() as output:
        qrcode.make(text).save(output)
        img = output.getvalue()
    st.image(img, caption="QRコード")
