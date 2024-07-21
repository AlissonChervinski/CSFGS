import streamlit as st
import pandas as pd
import os
from PIL import Image

# Função para carregar a tabela
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Função para carregar e exibir imagens em uma grade
def display_images(filtered_ids, image_folder):
    cols = st.columns(4)  # Definir 4 colunas para a grade
    idx = 0
    for img_id in filtered_ids:
        img_path = os.path.join(image_folder, f"{img_id}.png")
        if os.path.exists(img_path):
            img = Image.open(img_path)
            cols[idx % 4].image(img, caption=f"Imagem ID: {img_id}", use_column_width=True)
        #else:
            #cols[idx % 4].write(f"Imagem {img_id}.png não encontrada")
        idx += 1

# Caminho para o arquivo da tabela e para a pasta de imagens
table_file_path = 'tabela_csfgID_Re_kpc_logMstars.csv'  # Substitua pelo caminho do seu arquivo CSV
image_folder = 'png_to_list'  # Substitua pelo caminho da sua pasta de imagens

# Carregar os dados
data = load_data(table_file_path)

# Configurar os sliders na sidebar para cada propriedade
st.sidebar.header("Filtrar parâmetros")

ell_min, ell_max = st.sidebar.slider("Ell", float(data['ell'].min()), float(data['ell'].max()), (float(data['ell'].min()), float(data['ell'].max())))
n_min, n_max = st.sidebar.slider("n", float(data['n'].min()), float(data['n'].max()), (float(data['n'].min()), float(data['n'].max())))
Ie_min, Ie_max = st.sidebar.slider("I_e", float(data['I_e'].min()), float(data['I_e'].max()), (float(data['I_e'].min()), float(data['I_e'].max())))
z_min, z_max = st.sidebar.slider("z", float(data['z'].min()), float(data['z'].max()), (float(data['z'].min()), float(data['z'].max())))
Re_min, Re_max = st.sidebar.slider("R_e_kpc", float(data['R_e_kpc'].min()), float(data['R_e_kpc'].max()), (float(data['R_e_kpc'].min()), float(data['R_e_kpc'].max())))
logMstars_min, logMstars_max = st.sidebar.slider("logMstars", float(data['logMstars'].min()), float(data['logMstars'].max()), (float(data['logMstars'].min()), float(data['logMstars'].max())))

# Filtrar os dados com base nos intervalos selecionados
filtered_data = data[
    (data['ell'] >= ell_min) & (data['ell'] <= ell_max) &
    (data['n'] >= n_min) & (data['n'] <= n_max) &
    (data['I_e'] >= Ie_min) & (data['I_e'] <= Ie_max) &
    (data['z'] >= z_min) & (data['z'] <= z_max) &
    (data['R_e_kpc'] >= Re_min) & (data['R_e_kpc'] <= Re_max) &
    (data['logMstars'] >= logMstars_min) & (data['logMstars'] <= logMstars_max)
]

filtered_ids = filtered_data['csfgID'].tolist()

# Exibir as imagens filtradas
st.header(f"Mostrando {len(filtered_ids)} Imagens")
display_images(filtered_ids, image_folder)
