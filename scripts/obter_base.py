from pathlib import Path
from urllib.request import urlretrieve
import hashlib


# Define a pasta principal do projeto
ROOT = Path(__file__).resolve().parents[1]

# Define o diretório e o arquivo da base
DATA_DIR = ROOT / 'data'
DATA_PATH = DATA_DIR / 'ckd_uci.csv'

# Endereço da base armazenada no GitHub
SOURCE_URL = (
    'https://raw.githubusercontent.com/'
    'joaoemanuelpl/Doenca-Renal-Cronica/'
    'main/data/ckd_uci.csv.csv'
)

# Hash SHA-256 da cópia utilizada no projeto
EXPECTED_SHA256 = (
    'dbc44321265b9d447280a126c6188b5feb'
    '0d856ce722baf9c0431e33477dbcdb'
)


def calcular_sha256(caminho):
    """Calcula o hash SHA-256 de um arquivo."""
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def obter_base():
    """Obtém a base e verifica sua integridade."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if DATA_PATH.exists():
        print('Base já disponível. Verificando integridade...')
        actual_sha256 = calcular_sha256(DATA_PATH)

    else:
        print('Baixando a base do repositório GitHub...')

        temp_path = DATA_PATH.with_name(DATA_PATH.name + '.part')

        try:
            urlretrieve(SOURCE_URL, temp_path)
            actual_sha256 = calcular_sha256(temp_path)

            if actual_sha256 != EXPECTED_SHA256:
                raise ValueError(
                    'O hash da base não corresponde ao esperado.'
                )

            temp_path.replace(DATA_PATH)

        finally:
            if temp_path.exists():
                temp_path.unlink()

    if actual_sha256 != EXPECTED_SHA256:
        raise ValueError(
            'A integridade da base não foi confirmada.'
        )

    print('Base disponível e integridade verificada!')
    print('Arquivo:', DATA_PATH)


if __name__ == '__main__':
    try:
        obter_base()
    except Exception as erro:
        raise SystemExit(f'Erro ao obter a base: {erro}')
