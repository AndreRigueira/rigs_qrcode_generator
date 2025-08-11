# pip install qrcode
# pip install Pillow
# pip install streamlit

import streamlit as st
import qrcode
from io import BytesIO

st.title('Rigs QRCode Generator')

link = st.text_input('Link:')

if st.button('Gerar QRCode') and link:
    qr = qrcode.make(link)
    
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    
    st.image(buffer.getvalue(), caption='Área de exibição do QR Code gerado', width=300)