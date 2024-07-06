import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados():
    data =  pd.read_csv("PokemonData.csv")
    return data

def home():
    st.title("Bem vindo ao projeto Pokémon Data Visualization")


def grafico_linhas():
    st.title("Gráfico de Linhas")
    data = carregar_dados()
    fig = plt.figure(figsize = (10,10))

    data.groupby("Generation")["HP"].mean().plot(marker="o")
    plt.title("Tendência de HP dos pokémon ao longo das gerações")
    plt.xlabel("Geração")
    plt.ylabel("Média de HP")
    plt.grid(True)
    
    st.pyplot(fig)

    with st.expander("Código para gerar o gráfico"):
        with st.echo():

            fig = plt.figure(figsize = (10,10))
            data.groupby("Generation")["HP"].mean().plot(marker="o")
            plt.title("Tendência de HP dos pokémon ao longo das gerações")
            plt.xlabel("Geração")
            plt.ylabel("Média de HP")
            plt.grid(True)    


def grafico_barras():
    st.title("Gráfico de Barras")
    data = carregar_dados()
    fig = plt.figure(figsize=(10,8))

    type_counts = pd.concat([data["Type1"], data["Type2"]]).value_counts()
    plt.title("Distribuição de pokemón por tipo")
    type_counts.plot(kind = "bar")
    plt.xlabel("Tipo")
    plt.ylabel("Número de pokemón")
    plt.xticks(rotation = 45)
    plt.grid(axis = "y")

    st.pyplot(fig)

    with st.expander("Código para gerar o gráfico"):
        with st.echo():

            fig = plt.figure(figsize=(10,8))
            type_counts = pd.concat([data["Type1"], data["Type2"]]).value_counts()
            plt.title("Distribuição de pokemón por tipo")
            type_counts.plot(kind = "bar")
            plt.xlabel("Tipo")
            plt.ylabel("Número de pokemón")
            plt.xticks(rotation = 45)
            plt.grid(axis = "y")



def grafico_boxplot():
    st.title("Gráfico Boxplot")
    data = carregar_dados()
    fig = plt.figure(figsize = (10,8))

    stats = data[["HP", "Attack" ,"Defense" ,"SpAtk" ,"SpDef", "Speed"]]
    stats.boxplot()
    plt.title("Distribuição das estatísticas dos pokemón")
    plt.ylabel("Valores")
    plt.xticks(rotation = 45)
    plt.grid(axis = "y")

    st.pyplot(fig)

    with st.expander("Código para gerar o gráfico"):
        with st.echo():

            fig = plt.figure(figsize = (10,8))
            stats = data[["HP", "Attack" ,"Defense" ,"SpAtk" ,"SpDef", "Speed"]]
            stats.boxplot()
            plt.title("Distribuição das estatísticas dos pokemón")
            plt.ylabel("Valores")
            plt.xticks(rotation = 45)
            plt.grid(axis = "y")

            
def grafico_pizza():
    st.title("Gráfico de Pizza")
    data = carregar_dados()
    fig = plt.figure(figsize = (10,10))

    legendary_counts = data["Legendary"].value_counts()
    
    plt.title("Proporção de pokemón lendários")
    plt.pie(legendary_counts, labels=["Não lendário", "Lendário"] , autopct = "%1.1f%%", startangle = 140, textprops = {'fontsize' : 17})

    st.pyplot(fig)

    with st.expander("Código para gerar o gráfico"):
        with st.echo():
            
            fig = plt.figure(figsize = (10,10))
            legendary_counts = data["Legendary"].value_counts()
            plt.title("Proporção de pokemón lendários")
            plt.pie(legendary_counts, labels=["Não lendário", "Lendário"] , autopct = "%1.1f%%", startangle = 140, textprops = {'fontsize' : 17})



def main():

    st.sidebar.title("Navegação")

    pages={
        "Página Inicial" : home,
        "Gráfico de Linhas" : grafico_linhas,
        "Gráfico de Barras" : grafico_barras,
        "Gráfico Boxplot" : grafico_boxplot,
        "Gráfico de Pizza" : grafico_pizza,

    }

    selection = st.sidebar.selectbox("Ir para", list(pages.keys()))

    st.sidebar.title("Sobre")
    st.sidebar.write("Projeto com o intuito de demonstrar algumas funcionalidades básicas da biblioteca Matplotlib")

    pages[selection]()

if  __name__ == "__main__":
    main()