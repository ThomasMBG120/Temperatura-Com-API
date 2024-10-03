**Requisitos**
**Bibliotecas** **Necessárias**
O projeto faz uso da biblioteca requests, que é uma dependência externa. Para instalar a biblioteca, execute o comando abaixo no terminal:


pip install requests


**Conta na WeatherAPI**
É necessário ter uma conta na WeatherAPI para obter uma chave de API. Você pode se cadastrar gratuitamente em: https://www.weatherapi.com.

**Ambiente de Execução**:
Python 3.x
Acesso à internet para fazer as requisições de API.

**Funcionamento do Script**

O script é dividido em três partes principais:

**Obtenção do Endereço IP Público**:

O script utiliza a API pública da ipify para obter o endereço IP do usuário.
Consulta de Informações do Tempo: Utilizando o IP obtido, o script faz uma requisição à WeatherAPI para obter as condições meteorológicas atuais.
Atualização Automática a Cada 30 Segundos: O script repete o processo de consulta e exibição dos dados meteorológicos a cada 30 segundos.
Configuração do Projeto

**Passo 1: Clonar o Projeto**
Clone ou copie o script Python para seu ambiente de trabalho.

**Passo 2: Instalar Dependências**
Instale a biblioteca requests (se não estiver instalada) com o comando:

pip install requests

**Passo 3**: **Inserir a Chave de API da WeatherAPI**
 Substitua a string 'sua_chave_da_weatherapi' pela sua chave da WeatherAPI no script:
API_KEY = 'sua_chave_da_weatherapi'

**Passo 4: Executar o Script**
Execute o script utilizando Python:

python WeatherAPI.py

**Exemplo de Saída**
O script exibirá algo parecido com o seguinte, atualizado a cada 30 segundos:

Localização: Porto Alegre, Rio Grande do Sul, Brazil
Condição atual: Ensolarado
Temperatura: 25°C
----------------------------------------
Localização: Porto Alegre, Rio Grande do Sul, Brazil
Condição atual: Ensolarado
Temperatura: 25°C
----------------------------------------
