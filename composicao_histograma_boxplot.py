import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def composicao_histograma_boxplot(dataframe, coluna, intervalos="auto", titulo="Título do Gráfico", nome_arquivo="distribuicao.png", salvar=False):
    # Definir o caminho para a pasta 'images'
    pasta_imagens = os.path.join(os.getcwd(), "images")
    
    # Garantir que a pasta seja criada apenas se necessário
    if salvar:
        if not os.path.exists(pasta_imagens):
            try:
                os.makedirs(pasta_imagens)
                print(f"Pasta criada em: {pasta_imagens}")
            except Exception as e:
                print(f"Erro ao criar a pasta {pasta_imagens}: {e}")
                return  # Interromper a execução se houver erro na criação da pasta
    
    # Criação dos gráficos
    fig, (ax1, ax2) = plt.subplots(
        nrows=2, 
        ncols=1, 
        sharex=True,
        gridspec_kw={
            "height_ratios": (0.15, 0.85), # proporção (tamanho) dos gráficos
            "hspace": 0.02 # espaço entre os gráficos
        }
    )

    sns.boxplot(
        data=dataframe, 
        x=coluna, 
        showmeans=True,  
        meanline=True, # traço da média no boxplot
        meanprops={"color": "C1", "linewidth": 1.5, "linestyle": "--"}, # propriedades do traço da média no boxplot
        medianprops={"color": "C2", "linewidth": 1.5, "linestyle": "-"}, # propriedades do traço da mediana no boxplot
        ax=ax1,
    )

    sns.histplot(data=dataframe, x=coluna, kde=True, bins=intervalos, ax=ax2)

    for ax in (ax1, ax2):
        ax.grid(True, linestyle="--", color="gray", alpha=0.5)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xlabel("")
        ax.set_ylabel("")

    ax2.axvline(dataframe[coluna].mean(), color="C1", linestyle="--", label="Média")
    ax2.axvline(dataframe[coluna].median(), color="C2", linestyle="--", label="Mediana")
    ax2.axvline(dataframe[coluna].mode()[0], color="C3", linestyle="--", label="Moda") # A moda pede o índice

    ax2.legend()
    
    fig.suptitle(titulo, fontsize=14, fontweight="bold", color="Gray")
    
    # Salvar o gráfico se 'salvar' for True
    if salvar:
        caminho_arquivo = os.path.join(pasta_imagens, nome_arquivo)
        try:
            plt.savefig(caminho_arquivo, dpi=300, bbox_inches="tight")
            print(f"Gráfico salvo em: {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo {caminho_arquivo}: {e}")

    plt.show()

import numpy as np
from scipy.stats import mode, skew, kurtosis

# Função para calcular as estatísticas
def calcular_estatisticas(amostra):
    moda_result = mode(amostra, keepdims=True)  # Garantir que a moda é retornada como array
    estatisticas = {
        "Média": np.mean(amostra),
        "Mediana": np.median(amostra),
        "Moda": moda_result.mode[0] if len(moda_result.mode) > 0 else np.nan,
        "Variância": np.var(amostra, ddof=1),
        "Desvio Padrão": np.std(amostra, ddof=1),
        "Assimetria": skew(amostra),
        "Curtose": kurtosis(amostra, fisher=False),  # fisher=False retorna a curtose de momento
        "1º Quartil": np.percentile(amostra, 25),
        "2º Quartil (Mediana)": np.percentile(amostra, 50),
        "3º Quartil": np.percentile(amostra, 75)
    }
    return estatisticas