# 🧮 Calculadora Simples em Python

Uma calculadora simples desenvolvida em Python que realiza as quatro operações matemáticas básicas:

- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão

O projeto também conta com:

- Tratamento de erros para entradas inválidas
- Proteção contra divisão por zero
- Loop para realizar múltiplas operações sem reiniciar o programa

---

## 📚 Tecnologias Utilizadas

- Python

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/AdeventeeH/calculadora-python.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd calculadora-python
```

### 3️⃣ Execute o arquivo Python

```bash
python calculadora.py
```

---

## 💻 Exemplo de Uso

```bash
Calculadora Simples
--------------------

Digite o primeiro número: 10
Digite a operação (+, -, *, /): *
Digite o segundo número: 5

Resultado: 50.0

Deseja realizar outra operação? (s/n): s
```

---

## ⚙️ Funcionalidades

### ✅ Entrada segura de números

O sistema utiliza `try/except` para impedir erros caso o usuário digite caracteres inválidos.

### ✅ Validação de operações

Somente as seguintes operações são aceitas:

```python
+, -, *, /
```

### ✅ Proteção contra divisão por zero

Caso o usuário tente dividir um número por zero, a calculadora retorna uma mensagem de erro amigável.

### ✅ Execução contínua

Após finalizar uma operação, o usuário pode escolher continuar utilizando a calculadora sem precisar reiniciar o programa.

---

## 🧠 Estrutura do Código

| Função | Descrição |
|---|---|
| `obter_numero_1()` | Solicita o primeiro número |
| `obter_operacao()` | Solicita a operação matemática |
| `obter_numero_2()` | Solicita o segundo número |
| `calcular()` | Realiza o cálculo |
| `continuar()` | Pergunta se o usuário deseja continuar |
| `main()` | Controla a execução principal do programa |

---

## 📌 Conceitos Praticados

Este projeto foi desenvolvido para praticar conceitos fundamentais de programação com Python:

- Funções
- Estruturas de repetição (`while`)
- Estruturas condicionais (`if/elif/else`)
- Tratamento de exceções (`try/except`)
- Entrada e saída de dados
- Organização de código

---

## 📷 Resultado Esperado

```bash
Calculadora Simples
--------------------
Digite o primeiro número: 25
Digite a operação (+, -, *, /): /
Digite o segundo número: 5

Resultado: 5.0
```

---

## 📄 Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para utilizar, estudar e modificar o código.

---

## 👨‍💻 Autor

Desenvolvido por [Lucas Adevente](https://github.com/AdeventeeH) 🚀
