# carregar os dados
dados = [
        {"nome": "Hermano", "cidade": "Uberlândia"},
        {"nome": "Dayane", "cidade": "Monte Carmelo"}
]


# processar 
template = """\
    <html>
    <body>
        <ul>
            <li> Nome: {dados[nome]} </li>
            <li> Cidade: {dados[cidade]} </li>
        </ul>
    </body>
    </html>
"""

# renderizar

for item in dados:
    print(template.format(dados=item))
