from pathlib import Path
from urllib.request import urlretrieve
import hashlib


# Define a pasta principal do projeto
ROOT = Path(__file__).resolve().parents[1]

# Define o diretório e o arquivo da base
DATA_DIR = ROOT / 'data'
DATA_PATH = DATA_DIR / 'ckd_uci.csv'

# Fonte oficial da base de dados
SOURCE_URL = 'https://archive.ics.uci.edu/static/public/336/data.csv'

# Hash SHA-256 esperado para verificar a integridade
EXPECTED_SHA256 = (
    '0eeea8d17f5ad8792d854999d6ddf1602'
    'ec4e116616f6ccdfdaef0ba8109e694'
)


def calcular_sha256(caminho):
    """Calcula o hash SHA-256 de um arquivo."""
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def obter_base():
    """Baixa a base CKD e verifica sua integridade."""

    # Cria a pasta de dados caso ela não exista
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if DATA_PATH.exists():
        print('Base já disponível. Verificando integridade...')
        actual_sha256 = calcular_sha256(DATA_PATH)

    else:
        print('Realizando download da base de dados...')

        # Utiliza um arquivo temporário durante o download
        temp_path = DATA_PATH.with_name(DATA_PATH.name + '.part')

        try:
            urlretrieve(SOURCE_URL, temp_path)
            actual_sha256 = calcular_sha256(temp_path)

            if actual_sha256 != EXPECTED_SHA256:
                raise ValueError(
                    'A integridade da base não foi confirmada.'
                )

            # Move o arquivo para o diretório definitivo
            temp_path.replace(DATA_PATH)

        finally:
            if temp_path.exists():
                temp_path.unlink()

    # Confere a integridade do arquivo
    if actual_sha256 != EXPECTED_SHA256:
        raise ValueError(
            'A base apresenta divergência em relação à versão verificada.'
        )

    print('Base disponível e integridade verificada com sucesso!')
    print('Arquivo:', DATA_PATH)


if __name__ == '__main__':
    try:
        obter_base()
    except Exception as erro:
        raise SystemExit(f'Erro ao obter a base: {erro}')
