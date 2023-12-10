
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_files(base_url, save_path):
    # Certifique-se de que a pasta de destino existe
    os.makedirs(save_path, exist_ok=True)

    # Faça a requisição GET para a página HTML
    response = requests.get(base_url)

    # Verifique se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Analise o conteúdo HTML com BeautifulSoup para obter os links dos arquivos .grib
        soup = BeautifulSoup(response.text, 'html.parser')
        grib_links = [urljoin(base_url, link['href']) for link in soup.find_all('a') if link['href'].endswith('.grib2')]

        # Baixe cada arquivo .grib
        for grib_link in grib_links:
            file_name = os.path.join(save_path, os.path.basename(grib_link))
            with open(file_name, 'wb') as grib_file:
                grib_data = requests.get(grib_link).content
                grib_file.write(grib_data)
            print(f'Arquivo {file_name} baixado com sucesso.')
    else:
        print(f'Falha na requisição. Código de status: {response.status_code}')

# Substitua a URL base pela URL real que contém os links para os arquivos .grib
base_url = 'http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/HOURLY/2023/01/01/'
# Substitua o caminho para a pasta onde deseja salvar os arquivos .grib
save_path = 'Saida/desafio01'

download_files(base_url, save_path)
