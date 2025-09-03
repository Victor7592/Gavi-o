import streamlit as st
import pandas as pd
# python -m streamlit run app.py

# ------------------------------------------------- sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Gaviões Da Fiel')



jogador = ['Yuri Alberto', 'Romero', 'Memphis Depay', 'André Carrillo', 'Talles Magno']

opcao = st.sidebar.selectbox('Escolha o Jogador eleito o Melhor da Partida de Hoje', jogador)


#===============================================

st.title('Corinthians - Gaviôes')

st.image(f'{opcao}.png')
st.markdown(f'## Você Escolheu o Jogador: {opcao}')
st.markdown('---')


###### INFORMAÇÕES DOS JOGADORES 

yuri_alberto_stats = {
    'temporada': '2024',
    'jogos': 58,
    'gols': 31,
    'assistencias': 8
}

romero_stats = {
    'temporada': '2024',
    'jogos': 43,
    'gols': 8,
    'assistencias': 3
}

memphis_depay_stats = {
    'time': 'Atlético de Madrid',
    'temporada': '2024/2025',
    'jogos': 27,
    'gols': 7,
    'assistencias': 2
}

andre_carrillo_stats = {
    'time': 'Al-Qadsiah',
    'temporada': '2023/2024',
    'jogos': 29,
    'gols': 2,
    'assistencias': 6
}

talles_magno_stats = {
    'time': 'New York City FC',
    'temporada': '2024',
    'jogos': 15,
    'gols': 1,
    'assistencias': 2
}


#-------------------------------------------------------------------------------------------








# gols = st.text_input(f'Quantos Gols o {opcao} Fez na partida?')
# assistencias = st.text_input(f'Quantas assistencias ele deu no jogo? {opcao}')


if opcao == 'Yuri Alberto':
    st.markdown(
    f"""
    ### **Estatísticas de Yuri Alberto na Temporada {yuri_alberto_stats['temporada']}**

    * **Jogos:** {yuri_alberto_stats['jogos']}
    * **Gols:** {yuri_alberto_stats['gols']}
    * **Assistências:** {yuri_alberto_stats['assistencias']}
    
    _Fonte: Dados de pesquisa online, referentes ao ano de 2024._
    """
)

if opcao == 'Romero':
    st.markdown(
    f"""
    ### **Estatísticas de Romero na Temporada {romero_stats['temporada']}**

    * **Jogos:** {romero_stats['jogos']}
    * **Gols:** {romero_stats['gols']}
    * **Assistências:** {romero_stats['assistencias']}
    
    _Fonte: Dados de pesquisa online, referentes ao ano de 2024._
    """
)

if opcao == 'Memphis Depay':
    st.markdown(
    f"""
    ### **Estatísticas de Memphis Depay na Temporada {memphis_depay_stats['temporada']}**

    * **Clube:** {memphis_depay_stats['time']}
    * **Jogos:** {memphis_depay_stats['jogos']}
    * **Gols:** {memphis_depay_stats['gols']}
    * **Assistências:** {memphis_depay_stats['assistencias']}
    
    _Fonte: Dados de pesquisa online, referentes ao ano de 2024/2025._
    """
)



if opcao == 'André Carrillo':
    st.markdown(
    f"""
    ### **Estatísticas de André Carrillo na Temporada {andre_carrillo_stats['temporada']}**

    * **Clube:** {andre_carrillo_stats['time']}
    * **Jogos:** {andre_carrillo_stats['jogos']}
    * **Gols:** {andre_carrillo_stats['gols']}
    * **Assistências:** {andre_carrillo_stats['assistencias']}
    
    _Fonte: Dados de pesquisa online, referentes ao ano de 2024._
    """
)
    


if opcao == 'Talles Magno':
    st.markdown(
    f"""
    ### **Estatísticas de Talles Magno na Temporada {talles_magno_stats['temporada']}**

    * **Clube:** {talles_magno_stats['time']}
    * **Jogos:** {talles_magno_stats['jogos']}
    * **Gols:** {talles_magno_stats['gols']}
    * **Assistências:** {talles_magno_stats['assistencias']}
    
    _Fonte: Dados de pesquisa online, referentes ao ano de 2024._
    """
)


# if st.button('Calcular'):
#     gols = int(gols)
#     assistencias = float(assistencias)

#     total_gol = gols * gols
#     total_assistencias = assistencias * 0.15
#     total = total_gol+total_assistencias

#     st.warning(f'Você escolheu o jogador {opcao} e o total de gols dele foi de {gols} e fez um total de assistencias de {assistencias}o valor da aposta a ser pago e de R${total:.2f}')
