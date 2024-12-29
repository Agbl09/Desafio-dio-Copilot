# Desafio de IA e Codespace - Curso DIO

Este repositório contém um conjunto de códigos criados como parte de um desafio do curso da DIO. O objetivo do desafio foi implementar funções que solicitam entradas do usuário, realizam operações simples e exibem resultados. Além disso, o código foi ampliado para incluir o uso de valores absolutos, repetições de strings e mais.

A proposta do desafio envolveu três tarefas principais:

1. Exibir informações personalizadas: Solicitar o nome e a profissão do usuário e exibir uma mensagem personalizada.

2. Repetir strings: Solicitar uma string e um número de repetições e exibir a string repetida separada por um caractere específico.

3. Operações matemáticas: Realizar operações simples (adição, subtração, multiplicação, divisão, etc) entre dois números informados pelo usuário, tratando de forma especial a subtração e a divisão por zero.

## Funcionalidades Implementadas

1. Entrada de Nome e Profissão:

   O código solicita ao usuário o nome e a profissão e imprime uma mensagem personalizada, como: "João é programador".

2. Repetição de String:

   O usuário digita uma string e um número de repetições, e o programa exibe a string repetida o número de vezes desejado, separando as repetições por um " - ".

3. Operações Matemáticas:

   O código permite ao usuário realizar operações matemáticas simples (adição, subtração, multiplicação ,divisão, etc). Ele também lida com a subtração, mostrando sempre o valor absoluto da diferença entre os números, e com a divisão, evitando a divisão por zero.

## Como Funciona

- O código solicita entradas do usuário para o nome, profissão, string e números para as operações matemáticas.
- Em seguida, realiza as operações com base nas entradas e exibe os resultados.
- Para operações matemáticas, a subtração sempre exibe o valor absoluto da diferença, e a divisão verifica se o divisor é zero para evitar erro.

**Exemplo de Execução**

Entrada:
```yaml
Digite seu nome: João
Digite sua profissão: programador
João é programador

Digite qualquer string: Python
Digite o número de repetições: 3
Python - Python - Python

Digite o 1° número: 10
Digite o 2° número: 5
Escolha a operação:
1 - Adição (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
Digite o número da operação desejada: 2
O resultado de 10 - 5 é: 5
```

Saída:
```yaml
João é programador
Python - Python - Python
O resultado de 10 - 5 é: 5
```

## Objetivo

O principal objetivo deste desafio foi melhorar meus conhecimentos em Python, praticando conceitos de entrada e saída de dados, estruturas condicionais e manipulação de strings. Através deste desafio, quero expandir minhas habilidades de programação e explorar mais funcionalidades do Python para implementações futuras.

## Tecnologias Utilizadas

- Python 3.x
- GitHub Codespace
- ChatGPT(Seguindo a proposta do desafio)