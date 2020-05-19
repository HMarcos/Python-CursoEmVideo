# Python

## Estrutura Básica

> O Python é composto por dois modos básicos: **o interativo e o de scripts**. O modo _interativo_ serve basicamente para fazer testes rápidos e executar os programas. Enquanto, o modo _de scripts_ tem como principal função a crição de programas (_scripts_) maiores.

## Primeiros Comandos

***

### Comando de Saida de Dados

> No Python, o comando de saída de dados é função `print()`, nela a mensagem deve ser colocada entre aspas simples ou duplas, exceto se forem números ou variáveis.

```Python
>> print('Olá, Mundo!')
>> Olá, Mundo!
>> print(7 + 4)
>> 11
>> print('7' + '5')
>> 75
>> print('Igual a ', 5)
>> Igual a 5
```

> **Obs**: Note que o operador `+` realiza a concatenação de strings em Python.

### Atribuição

> A atribuição é feita com o operador `=`.

```Python
>> nome = 'Marcos'
>> idade = 21
>> peso = 69.5
>> print(nome, 'tem', idade, 'anos e pesa', peso, 'kg')
>> Marcos tem 21 anos e pesa 69.5 kg
```

### Comando de Entrada de Dados

> No Python, o comando de entrada de dados é a função `input()`, nela a mensagem a ser exibida ao usuário deve ser colocada entre aspas simples ou duplas.

```Python
>> nome = input('Qual o seu nome?')
>> idade = input('Qual a sua idade?')
>> peso = input('Qual o seu peso?')
```

> **Obs**: Note que a função `input` sempre retorna um objeto do tipo `str`, que é uma string. Então para converter a string para outros tipos de variáveis, como inteiros ou pontos flutuantes, é preciso utilizar outras funções em conjunto com o `input`. Por exemplo:

```Python
>> idade = int((input('Qual a sua idade?')))
>> peso = float((input('Qual o seu peso?')))
```

### Variáveis

> Para o Python, **toda variável é um objeto**. Dessa forma, cada variável possui atributos e métodos associados a si.
