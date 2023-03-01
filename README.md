
# homeassistant-futebol

Este script Python usa a biblioteca Requests e BeautifulSoup, fazendo Webscrapping no site placardefutebol.com.br para obter informações dos próximos jogos do Palmeiras. Ele salva as informações em um dicionário Python e as printa na console. 


## Configuração no Homeassistant

Insira os valores contidos na seção sensor do arquivo configuration.yaml de exemplo, na chave sensor da configuração do seu Home Assistant. Essa configuração cria um sensor que lê o retorno do script Python, mapeando todos os elementos do retorno do array como atributos deste sensor. Deste modo, podemos utilizar as informações no frontend Lovelace, como no exemplo abaixo:


<br />
<p align="center">
  <a href="https://github.com/thiagobucca/homeassistant-futebol">
    <img src="images/screenshots.png" alt="Logo" width="480" height="600">
  </a>
</p>

## Dependências

`requests`    
`bs4`     
`homeassistant`     


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshots.png
