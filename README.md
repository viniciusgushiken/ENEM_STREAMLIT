# ENEM_STREAMLIT
Autores: Jessica, Jonas, Leonardo, Lucas e Vinicius 

Aplicativo web para descobrir sua nota do ENEM. Confira o modelo em produção no link abaixo.
https://descubrasuanota.herokuapp.com/

## Sobre

Trabalho final do curso de Data Science da Digital House, turma do 1º semestre de 2020. O projeto requer a criação de um modelo de machine learning com dados reais e fazer o deploy do modelo, colocando-o em produção na forma de um produto. O produto deve atender uma necessidade de mercado e conter as técnicas aprendidas ao longo do semestre.

Nosso produto fornece a nota do ENEM predita pelo modelo Random Forest. O modelo possui um MAE de 52 pontos e um R2 de 90%. O aplicativo web foi desenvolvido com o framework Streamlit.

Os dados são os Microdados do ENEM de 2018, que podem ser encontrados no site do INEP (http://inep.gov.br/microdados). O dataset contem mais de 5 milhões de linhas e 137 colunas. Contendo informações socioecomicas sobre cada participante, alem de informações sobre suas notas em cada prova do ENEM.

O modelo escolhido foi o Random Forest, sua vantagem é o ensemble learning do qual consegue realizar uma predição baseada em diversas predições. Além disso, o modelo permite realizar predições regressoras, que convém com a nota do ENEM que varia de 0 a 1000. O modelo está compactado, para rodar localmente é necessario descompacta-lo.

O aplicativo web foi desenvolvoido interiramente no framework Streamlit, a vantagem do mesmo é que ele foi desenvolvido especificamente para Data Apps, além disso, todo o desenvolvimetno é feito em python.

O produto é um aplicativo que pode ser acessado por qualquer usuário com acesso à internet. Os usuários podem ter uma boa noção de sua nota baseada na sua posição socioeconomica brasileira.
