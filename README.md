# 🧾 Sistema de Cadastro de Pessoas / People Registration System

## Português / Portuguese

Este é um exercício de prática com **dicionários** e **listas** em Python, que simula um sistema simples de cadastro de pessoas. A cada novo cadastro, os dados são armazenados de forma organizada e estruturada, permitindo análise posterior dos registros.

## English

This is a practice exercise using **dictionaries** and **lists** in Python, simulating a simple people registration system. With each new entry, the data is stored in an organized and structured way, allowing for subsequent analysis of the records.

---

## 💡 Funcionalidades / Features

### Português / Portuguese

- Cadastro de nome, sexo e idade.
- Validação de entrada para sexo e idade.
- Armazenamento de múltiplas pessoas usando dicionários copiados dentro de uma lista.
- Cálculo da **média de idade** do grupo.
- Listagem de:
  - Total de pessoas cadastradas.
  - Nomes das mulheres cadastradas.
  - Pessoas com idade acima da média.

### English

- Registration of name, gender, and age.
- Input validation for gender and age.
- Storing multiple people using copied dictionaries within a list.
- Calculating the **average age** of the group.
- Listing:
  - Total number of registered people.
  - Names of registered women.
  - People with age above average.

---

## 📌 Como funciona / How It Works

### Português / Portuguese

O programa roda em um loop que coleta os dados de cada pessoa. Cada registro é salvo usando uma cópia do dicionário `cadastros`, para garantir que as informações não sejam sobrescritas. Após o encerramento do cadastro, o programa realiza os cálculos e exibe os resultados.

### English

The program runs in a loop that collects data from each person. Each entry is saved using a copy of the `record` dictionary to ensure the information is not overwritten. After the registration process ends, the program calculates and displays the results.

---

## 🧠 Conceitos usados / Concepts Used

### Português / Portuguese

- `while True` com `break` para controle de loop.
- Validação de dados com `while` e `in`.
- Uso de `.copy()` para duplicar dicionários de forma independente.
- F-strings para formatação de saída.
- List comprehension para filtrar dados.

### English

- `while True` with `break` for loop control.
- Data validation with `while` and `in`.
- Using `.copy()` to duplicate dictionaries independently.
- F-strings for output formatting.
- List comprehension to filter data.

---

## 🚀 Exemplo de saída / Sample Output

### Português / Portuguese

```bash
Nome: Ana
Sexo: F
Idade: 28
Quer continuar? [S/N] S
Nome: Lucas
Sexo: M
Idade: 34
Quer continuar? [S/N] N

Foram cadastradas 2 pessoas.
A média de idade do grupo é 31.0 anos.
Mulheres cadastradas: Ana.
As pessoas com idade acima da média são: Lucas com 34 anos.



Name: Ana
Gender: F
Age: 28
Do you want to continue? [Y/N] Y
Name: Lucas
Gender: M
Age: 34
Do you want to continue? [Y/N] N

2 people were registered.
The average age of the group is 31.0 years.
Registered women: Ana.
People above average age: Lucas (34 years).