# Python

## Estrutura Básica

O Python é composto por dois modos básicos: **o interativo e o de scripts**. O modo _interativo_ serve basicamente para fazer testes rápidos e executar os programas. Enquanto, o modo _de scripts_ tem como principal função a crição de programas (_scripts_) maiores.

## Primeiros Comandos

***

### Comando de Saida de Dados

Em Python, o comando de saída de dados é função `print()`, nela a mensagem deve ser colocada entre aspas simples ou duplas, exceto se forem números ou variáveis.

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

**Obs**: Note que o operador `+` realiza a concatenação de strings em Python.

### Atribuição

A atribuição é feita com o operador `=`.

```Python
>> nome = 'Marcos'
>> idade = 21
>> peso = 69.5
>> print(nome, 'tem', idade, 'anos e pesa', peso, 'kg')
>> Marcos tem 21 anos e pesa 69.5 kg
```

### Comando de Entrada de Dados

Em Python, o comando de entrada de dados é a função `input()`, nela a mensagem a ser exibida ao usuário deve ser colocada entre aspas simples ou duplas.

```Python
>> nome = input('Qual o seu nome?')
>> idade = input('Qual a sua idade?')
>> peso = input('Qual o seu peso?')
```

**Obs**: Note que a função `input` sempre retorna um objeto do tipo `str`, que é uma string. Então para converter a string para outros tipos de variáveis, como inteiros ou pontos flutuantes, é preciso utilizar outras funções em conjunto com o `input`. Por exemplo:

```Python
>> idade = int(input('Qual a sua idade?'))
>> peso = float(input('Qual o seu peso?'))
```

### Variáveis

Para o Python, **toda variável é um objeto**. Dessa forma, cada variável possui atributos e métodos associados a si.

## Tipos Primitivos

***

Em Python, tem-se 4 tipos primitos básicos para as variáves, são eles:  
> **int**: representa os números inteiros, como: *1, 2, -5, -9*;  
> **float**: representa os números com ponto flutuante, como: *1.4, 2.0, -5.1, -9.457*;  
> **str**: representa as strings, que são variáveis definidas entres aspas simples ou duplas, como: *'Marcos', "3", "false", 'Henrique'*;  
> **boolean**: representa os valores lógicos verdadeiro (*True*) e falso (*False*).

**Observação**: Para indicar o tipo primitivo em Python basta apenas definir a atirbuição da variável, como mostra abaixo:

```Python
>> nome = 'Marcos Henrique'  # Str
>> idade = 21  # Int
>> peso = 68.9  # Float
>> casado = False  # Boolean  
```

## Saída Formatada

***

Devido ao fato das variáveis serem objetos em Python, principalmente as *strings* possuem métodos especiais que ajudam na hora de programar. Um desses métodos é o `.format()` que permite a formatação de uma string por meio de chaves **{}**.

**Exemplo**: A ordem dos parâmetros segue a mesma sequência das chaves.

```Python
>> print('Meu nome é {} e tenho {} anos'.format(nome,idade))
>> Meu nome é Marcos Henrique e tenho 21 anos.
```

**Exemplo**: A ordem de exibição dos parâmetros pode ser indicada por números entre as chaves.

```Python
>> p1 = 'José'
>> p2 = 'Maria'
>> print('{0} e {1} foram ao shopping, porém {0} esqueceu de comprar algo importante'.format(p1,p2))
>> José e Maria foram ao shopping, porém José esqueceu de comprar algo importante
```

## Alguns Métodos da Classe Str

***

As strings além do método `.format()` possui outros métodos importantes, que ajudam o programador. São alguns deles:

> `.isnumeric()`: indica se a string é composta apenas por números;  
> `.isalpha()`: indica se a string é composta apenas por letras;  
> `.isalnum()`: indica se a string é composta apenas por números ou letras;  
> `.istitle()`: indica se a string é capitalizada;  
> `.islower()`: indica se a string é composta apenas letras minúsculas;  
> `.isupper()`: indica se a string é composta apenas letras maiúsculas;  
