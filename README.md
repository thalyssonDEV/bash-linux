# Terminal Linux com Python

**Descrição**  
Este projeto implementa um terminal Linux básico em Python, com funcionalidades semelhantes ao **Bash**. O objetivo é emular um shell de linha de comando, permitindo a execução de comandos do sistema e interação com o sistema operacional.

## Tecnologias Utilizadas

- **Python**: Linguagem utilizada para o desenvolvimento.
- **Bibliotecas**:
  - `os`: Para interação com o sistema operacional (execução de comandos, manipulação de arquivos e processos).
  - `subprocess`: Para executar comandos do sistema e obter seus resultados.
  - `sys`: Para manipulação de caminhos e argumentos da linha de comando, além de controlar a saída do terminal.

## Funcionalidades

- **Execução de Comandos**: O terminal permite que o usuário execute comandos do sistema, como `ls`, `mv`, `echo`, `touch`, `rm`, entre outros.
- **Manipulação de Processos**: É possível iniciar e controlar processos do sistema a partir do terminal Python.
- **Suporte a Comandos Simples**: Implementação de alguns comandos básicos e a simulação de seus comportamentos.
- **Interatividade**: O terminal recebe entrada do usuário e exibe a saída de maneira similar ao terminal Bash.

## Instalação

### Requisitos

- Python instalado no seu sistema.
- Nenhuma dependência externa é necessária, além das bibliotecas padrão do Python.
