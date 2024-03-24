# Resultado - Desáfio CoorLab

<!-- Front End -->
Toda a parte de front-end foi desenvolvida utilizando exclusivamente HTML, CSS e JavaScript. Não utilizei outras bibliotecas além das especificadas, optando por criar tudo do zero. Também incorporei algumas funcionalidades do Vue.js, como a biblioteca "FlatPickr", utilizada na seção de pesquisa de viagens (SearchTravel).

Adicionei algumas funcionalidades que não estavam presentes no protótipo, como tratamento de erros para casos em que os campos de inserção de dados não são preenchidos (caso o usuário não selecione o destino ou a data). Além disso, implementei um botão de limpar, que aparece logo após a busca ser realizada, para limpar os resultados.

Com base no entendimento do que foi solicitado, desenvolvi duas opções que deveriam ser retornadas: a viagem mais barata e a mais cara. Para isso, criei um endpoint que, a partir do nome do destino, retorna um array com a viagem mais barata e outro com a viagem mais cara, permitindo assim a separação dessas opções no front-end.

<!-- Back End -->
No back-end, optei por criar dois endpoints:

1 - Endpoint que realiza a busca de todas as cidades de destino presentes no arquivo data.json. Ao obter todas as cidades, as transforma em um array acessível, sendo utilizado para preencher o campo de seleção de destino no front-end.

2 - Este endpoint recebe a cidade que o usuário solicitou para buscar. Em seguida, realiza uma iteração sobre todas as viagens para essa cidade, selecionando as viagens com o maior valor (viagem confortável) e o menor valor (viagem econômica). Essas informações são então utilizadas no componente "Trips" para configurar os valores correspondentes em forma de cards.