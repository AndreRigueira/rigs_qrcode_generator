# 🤖 Rigs QRCode Generator  

Um aplicativo web simples e fácil de usar para gerar QR Codes a partir de qualquer link, construído com Python e Streamlit.

## 🌟 Sobre o Projeto  

Este é um projeto simples, mas poderoso, que demonstra como transformar um script Python em uma interface web interativa em minutos. Com o Rigs QRCode Generator, você pode rapidamente criar QR Codes para seus links, sites ou qualquer URL que precisar.

Ele é perfeito para quem está começando com Python e quer ver o potencial da biblioteca Streamlit para criar aplicativos web sem a necessidade de conhecimento em HTML, CSS ou JavaScript.

## 🚀 Como Usar  

Pré-requisitos
Certifique-se de que você tem o Python instalado em sua máquina. Em seguida, instale as bibliotecas necessárias com o seguinte comando:

`pip install streamlit qrcode`  


### Rodando o Aplicativo  
1- Clone este repositório para a sua máquina local (ou crie um arquivo com o código-fonte).  
2- Abra o terminal na pasta do projeto.  
3- Execute o seguinte comando:  

`streamlit run app.py`  

4- Uma nova aba no seu navegador será aberta automaticamente com o aplicativo rodando!


## ⚙️ Código-Fonte  
Este é o coração do projeto. O código é simples e bem comentado para facilitar o entendimento:

Python

```import streamlit as st
import qrcode
from io import BytesIO

st.title('Rigs QRCode Generator')

link = st.text_input('Link:')

if st.button('Gerar QRCode') and link:
    # Gera o QR Code a partir do link fornecido
    qr = qrcode.make(link)
    
    # Salva o QR Code em um buffer de memória
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    
    # Exibe a imagem no Streamlit
    st.image(buffer.getvalue(), caption='Área de exibição do QR Code gerado', width=300)
```

## 🤝 Contribuições  
Contribuições são sempre bem-vindas! Se você tiver alguma ideia de melhoria, como adicionar opções para cores, tamanhos ou outros formatos, sinta-se à vontade para abrir uma issue ou um pull request.

## 📄 Licença  
Este projeto é de código aberto e está disponível sob a licença MIT.
