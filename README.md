# **Who Unfollowed (Quem deixou de seguir)**

Esta ferramenta te mostra uma lista de pessoas que não estão te seguindo de volta, juntamente com umas funcionalidades mixadas

## Uso

Primeiro você precisará de um arquivo JSON ou TXT com um array/lista JSONificado dos seus seguidores. Você pode usar o código do util.js para isso.

Se você quiser ignorar alguns resultados, você pode criar um arquivo TXT e digitar todas as contas que você quer linha por linha e incluir o nome do arquivo como terceiro argumento na CLI. Essas contas não vão aparecer nos resultados.

Na linha de comando, digite:

    python main.py nomearquivo_1 nomearquivo_2 -u

Ou seja, você pode escrever:

    python main.py seguidores.txt seguindo.txt -u

Isso vai retornar uma lista com as contas que não te seguem de volta

Outras flags podem ser usada para retornar diferentes resultados

|Flags| O que ela faz |
|--|--|
| -u | Que não estão te seguindo de volta |
| -b | Que você não está seguindo de volta |

Uso de comandos comuns:

    python main.py seguidores.json seguindo.json -u

    python main.py seguidores.json seguindo.json excluir.txt -u -b

    python main.py seguidores.json seguindo.json -b  
    