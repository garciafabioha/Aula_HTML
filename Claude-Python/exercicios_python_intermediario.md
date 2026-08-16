# Exercícios Intermediários de Python

Um exercício de cada "tipo" de trabalho comum, pensado pra quem já sabe o básico e quer aplicar em scripts do dia a dia.

---

## 1. Manipulação de arquivos

**Organizador de arquivos por extensão**

Escreva um script que:
- Recebe um caminho de pasta.
- Lista todos os arquivos dentro dela.
- Move cada arquivo para uma subpasta com o nome da sua extensão (ex: `.csv` vai para `csv/`, `.pdf` vai para `pdf/`).
- Se a subpasta não existir, cria automaticamente.
- No final, imprime um resumo: quantos arquivos foram movidos por tipo.

*Módulos sugeridos:* `os`, `shutil`, `pathlib`

---

## 2. Tratamento de erros / exceções

**Validador de dados de entrada**

Escreva uma função `processar_registro(dado)` que recebe um dicionário como `{"nome": "João", "idade": "30"}` e:
- Converte `idade` para inteiro, tratando `ValueError` se não for possível.
- Lança uma exceção customizada `CampoObrigatorioError` se faltar a chave `"nome"`.
- Usa `try/except/else/finally` para logar se o processamento deu certo ou não.
- Testa a função com pelo menos 3 registros diferentes (um válido, um com idade inválida, um sem nome).

---

## 3. Programação orientada a objetos (POO)

**Sistema simples de controle de estoque**

Crie uma classe `Produto` com atributos `nome`, `preco`, `quantidade`, e uma classe `Estoque` que:
- Armazena uma lista de produtos.
- Tem métodos `adicionar_produto`, `remover_produto`, `atualizar_quantidade`.
- Tem um método `valor_total()` que retorna o valor total do estoque (soma de preço × quantidade).
- Lança uma exceção se tentar remover mais itens do que existem em estoque.

*Bônus:* implemente `__str__` na classe `Produto` para exibição amigável.

---

## 4. Automação de tarefas

**Renomeador em lote com regras**

Escreva um script que:
- Percorre uma pasta de arquivos `.txt`.
- Renomeia cada um seguindo o padrão `AAAA-MM-DD_nome-original.txt`, usando a data de modificação do arquivo.
- Registra as renomeações em um arquivo de log (`log.txt`), uma linha por arquivo.
- Permite rodar em modo "simulação" (mostra o que faria sem renomear de fato).

---

## 5. Trabalhando com APIs (requisições HTTP)

**Consulta de CEP**

Usando a biblioteca `requests`, escreva um script que:
- Recebe um CEP do usuário.
- Consulta uma API pública de CEP (ex: ViaCEP: `https://viacep.com.br/ws/{cep}/json/`).
- Trata erros de conexão e CEP inválido.
- Formata e imprime o endereço de forma legível.
- Bônus: aceita uma lista de CEPs e consulta todos, mostrando o resultado em formato de tabela.

---

## 6. Estruturas de dados e list/dict comprehension

**Análise de vendas**

Dada uma lista de dicionários representando vendas:

```python
vendas = [
    {"produto": "Caneta", "categoria": "Papelaria", "valor": 2.5, "qtd": 10},
    {"produto": "Caderno", "categoria": "Papelaria", "valor": 15.0, "qtd": 3},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 45.0, "qtd": 2},
]
```

- Use *list/dict comprehension* para calcular o total (`valor * qtd`) de cada venda.
- Agrupe o total vendido por categoria (dicionário `{categoria: total}`).
- Encontre o produto mais vendido em valor total, sem usar loops explícitos (use `max()` com `key`).

---

## 7. Funções avançadas e decorators

**Cronômetro e cache de funções**

- Escreva um decorator `@cronometro` que imprime quanto tempo uma função levou para rodar.
- Escreva um decorator `@cache_simples` que guarda em memória o resultado de chamadas já feitas (evita recalcular para os mesmos argumentos).
- Aplique os dois decorators numa função que simula um cálculo pesado (ex: uma função recursiva de Fibonacci sem otimização).
- Compare o tempo de execução com e sem o cache.

---

## 8. Expressões regulares (regex)

**Extrator de dados de log**

Dado um arquivo de log com linhas como:

```
2026-08-14 10:32:11 ERROR Falha ao conectar no banco: timeout
2026-08-14 10:33:02 INFO Conexão restabelecida
```

- Use `re` para extrair data, hora, nível (`ERROR`, `INFO`, etc.) e mensagem de cada linha.
- Organize os resultados em uma lista de dicionários.
- Filtre e imprima apenas as linhas de nível `ERROR`.
- Bônus: conte quantos erros ocorreram por hora.

---

## Como usar esta lista

- Resolva na ordem que fizer mais sentido pro seu momento — não precisa ser sequencial.
- Se travar, tente primeiro sem consultar documentação, depois valide.
- Me manda o código que você fizer que eu reviso e sugiro melhorias.
