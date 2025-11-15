# Sistema de Inspeção Industrial

**Gestão de Peças, Qualidade e Armazenamento**

**Autor:** João Henrique Benatti Coimbra  
**Instituição:** UniFECAF  
**Disciplina:** Algoritmos e Lógica de Programação  
**Data:** 15/11/2025

---

## 📋 Descrição

Protótipo funcional de automação digital para inspeção, classificação e armazenamento de peças industriais. O sistema opera com base em critérios de qualidade pré-definidos, validando automaticamente cada peça e organizando as aprovadas em caixas de capacidade limitada.

**Conceitos de Programação Utilizados:**
- Variáveis e tipos de dados básicos (int, float, str, bool)
- Estruturas condicionais (if/elif/else)
- Estruturas de repetição (while, for)
- Listas e dicionários
- Funções simples para modularização de código

---

## 🎯 Funcionalidades

### Menu Principal

1. **Cadastrar nova peça**: Registro individual de peças com validação em tempo real
2. **Listar peças aprovadas/reprovadas**: Visualização completa do inventário
3. **Remover peça cadastrada**: Exclusão de registros por ID
4. **Listar caixas fechadas**: Visualização do armazenamento organizado
5. **Gerar relatório final**: Análise consolidada com indicadores de qualidade
6. **Preenchimento automático (DEMO)**: Cadastro automático de 21 peças para demonstração
0. **Sair do sistema**: Encerramento seguro da aplicação

---

## 📏 Critérios de Qualidade

Uma peça é **APROVADA** quando satisfaz TODOS os seguintes requisitos:

| Parâmetro     | Intervalo Válido    |
|---------------|---------------------|
| Peso          | 95g - 105g          |
| Cor           | azul ou verde       |
| Comprimento   | 10cm - 20cm         |

**Reprovação:** Qualquer desvio desses critérios resulta em reprovação, com registro do motivo específico.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior instalado
- Terminal/Prompt de Comando

### Verificar Instalação do Python

```bash
python --version
```
ou
```bash
python3 --version
```

### Execução do Programa

1. **Navegue até o diretório do arquivo:**

```bash
cd /caminho/para/o/diretorio
```

2. **Execute o programa:**

```bash
python industrial_inspection_system.py
```

ou

```bash
python3 industrial_inspection_system.py
```

3. **No Windows:**

Você também pode executar com duplo clique no arquivo `.py` se Python estiver associado.

---

## 📝 Nomenclatura do Código

**Padrão de Nomenclatura:**
- **Arquivo:** `industrial_inspection_system.py` (inglês)
- **Variáveis:** inglês (ex: `approved_parts`, `rejected_parts`, `current_box`)
- **Funções:** inglês (ex: `validate_part()`, `register_part()`, `generate_report()`)
- **Constantes:** inglês (ex: `MIN_WEIGHT`, `MAX_WEIGHT`, `BOX_CAPACITY`)
- **Comentários e Strings de Saída:** português (trabalho acadêmico brasileiro)

Esta abordagem segue as melhores práticas internacionais de desenvolvimento, mantendo o código legível para colaboração global enquanto preserva a comunicação com o usuário final em português.

---

## 💡 Exemplos de Uso

### Exemplo 1: Cadastro Manual de Peça Aprovada

```
Escolha uma opção: 1

============================================================
           CADASTRO DE NOVA PEÇA
============================================================
ID gerado automaticamente: 1
Digite o peso (g): 100
Digite a cor (azul/verde): azul
Digite o comprimento (cm): 15

✓ PEÇA APROVADA - ID: 1
  Peso: 100.0g | Cor: azul | Comprimento: 15.0cm
```

### Exemplo 2: Cadastro Manual de Peça Reprovada

```
Escolha uma opção: 1

============================================================
           CADASTRO DE NOVA PEÇA
============================================================
ID gerado automaticamente: 2
Digite o peso (g): 110
Digite a cor (azul/verde): verde
Digite o comprimento (cm): 15

✗ PEÇA REPROVADA - ID: 2
  Motivo: Peso fora do intervalo [95g-105g]
```

### Exemplo 3: Fechamento Automático de Caixa

Após cadastrar 10 peças aprovadas:

```
✓ PEÇA APROVADA - ID: 10
  Peso: 98.0g | Cor: verde | Comprimento: 14.0cm

✓✓ CAIXA 1 FECHADA - 10 peças armazenadas
```

### Exemplo 4: Uso do Preenchimento Automático (DEMO)

```
Escolha uma opção: 6

============================================================
      PREENCHIMENTO AUTOMÁTICO - MODO DEMONSTRAÇÃO
============================================================

Cadastrando peças de exemplo...

✓ ID 001: APROVADA | 100.0g | azul | 15.0cm
✓ ID 002: APROVADA | 98.5g | verde | 12.5cm
✓ ID 003: APROVADA | 102.0g | azul | 18.0cm
...
✓ ID 010: APROVADA | 100.5g | verde | 15.5cm
  >> CAIXA 1 FECHADA!
✓ ID 011: APROVADA | 98.0g | azul | 12.0cm
...
✗ ID 014: REPROVADA | Peso fora do intervalo [95g-105g]
✗ ID 016: REPROVADA | Cor não conforme [azul/verde]
...

============================================================
✓ Preenchimento automático concluído!
  • 13 peças aprovadas cadastradas
  • 8 peças reprovadas cadastradas
  • 1 caixa(s) fechada(s)
  • 3 peça(s) na caixa em andamento
============================================================
```

### Exemplo 5: Relatório Consolidado

```
Escolha uma opção: 5

============================================================
      RELATÓRIO CONSOLIDADO DE PRODUÇÃO
============================================================

📊 INDICADORES GERAIS:
  • Total de peças processadas: 21
  • Peças aprovadas: 13
  • Peças reprovadas: 8
  • Taxa de aprovação: 61.90%

📦 ARMAZENAMENTO:
  • Caixas fechadas: 1
  • Peças na caixa atual: 3/10

------------------------------------------------------------
❌ DETALHAMENTO DE REPROVAÇÕES:

  Reprovações por motivo:
    • Peso fora do intervalo [95g-105g]: 2 (25.0%)
    • Cor não conforme [azul/verde]: 2 (25.0%)
    • Comprimento fora do intervalo [10cm-20cm]: 4 (50.0%)

  Lista completa de peças reprovadas:
    • ID 014: Peso fora do intervalo [95g-105g]
    • ID 015: Peso fora do intervalo [95g-105g]
    • ID 016: Cor não conforme [azul/verde]
    • ID 017: Cor não conforme [azul/verde]
    • ID 018: Comprimento fora do intervalo [10cm-20cm]
    • ID 019: Comprimento fora do intervalo [10cm-20cm]
============================================================
```

---

## 📊 Estrutura de Dados

### Dicionário de Peça Aprovada
```python
{
    "id": 1,
    "peso": 100.0,
    "cor": "azul",
    "comprimento": 15.0
}
```

### Dicionário de Peça Reprovada
```python
{
    "id": 2,
    "peso": 110.0,
    "cor": "verde",
    "comprimento": 15.0,
    "motivo": "Peso fora do intervalo [95g-105g]"
}
```

### Estrutura de Caixa
```python
[
    {"id": 1, "peso": 100.0, "cor": "azul", "comprimento": 15.0},
    {"id": 2, "peso": 98.5, "cor": "verde", "comprimento": 12.5},
    # ... até 10 peças
]
```

---

## 🎬 Demonstração em Vídeo

Para gravação do **vídeo pitch de 4 minutos**, recomenda-se o seguinte roteiro:

1. **[0:00-0:30]** Introdução ao problema industrial
2. **[0:30-1:00]** Apresentação da solução e critérios de qualidade
3. **[1:00-2:30]** Demonstração prática usando **Opção 6** (Preenchimento Automático)
   - Mostrar cadastro automático
   - Navegar pelas opções de listagem (2 e 4)
   - Gerar relatório (opção 5)
4. **[2:30-3:30]** Cadastro manual de 1 peça aprovada e 1 reprovada (opção 1)
5. **[3:30-4:00]** Conclusão e perspectivas futuras

**Vantagem do Preenchimento Automático:** Economiza tempo de digitação e demonstra rapidamente todos os cenários do sistema (aprovação, reprovação por diferentes motivos, fechamento de caixas).

---

## 🧪 Casos de Teste

### Caso 1: Peça no Limite Inferior (Aprovada)
```
Peso: 95.0g
Cor: verde
Comprimento: 10.0cm
Resultado: ✓ APROVADA
```

### Caso 2: Peça no Limite Superior (Aprovada)
```
Peso: 105.0g
Cor: azul
Comprimento: 20.0cm
Resultado: ✓ APROVADA
```

### Caso 3: Peso Abaixo do Limite (Reprovada)
```
Peso: 94.9g
Cor: azul
Comprimento: 15.0cm
Resultado: ✗ REPROVADA - Peso fora do intervalo
```

### Caso 4: Cor Inválida (Reprovada)
```
Peso: 100.0g
Cor: vermelho
Comprimento: 15.0cm
Resultado: ✗ REPROVADA - Cor não conforme
```

### Caso 5: Comprimento Acima do Limite (Reprovada)
```
Peso: 100.0g
Cor: verde
Comprimento: 20.1cm
Resultado: ✗ REPROVADA - Comprimento fora do intervalo
```

---

## 🔧 Tratamento de Erros

O sistema implementa validação de entrada para prevenir erros:

- **Entrada não-numérica para peso/comprimento:** Mensagem de erro e cancelamento do cadastro
- **ID inexistente na remoção:** Notificação de que o ID não foi encontrado
- **Opção de menu inválida:** Solicitação de nova entrada

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────┐
│         INTERFACE DO USUÁRIO            │
│            (Menu Interativo)            │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      CAMADA DE PROCESSAMENTO            │
│  ┌────────────────────────────────┐     │
│  │   validar_peca()               │     │
│  │   cadastrar_peca()             │     │
│  │   remover_peca()               │     │
│  │   gerar_relatorio()            │     │
│  └────────────────────────────────┘     │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│        CAMADA DE DADOS                  │
│  ┌────────────────────────────────┐     │
│  │  pecas_aprovadas: []           │     │
│  │  pecas_reprovadas: []          │     │
│  │  caixas_fechadas: []           │     │
│  │  caixa_atual: []               │     │
│  └────────────────────────────────┘     │
└─────────────────────────────────────────┘
```

---

## 📈 Métricas do Sistema

Após execução do preenchimento automático, o sistema gera:

- **13 peças aprovadas** (61.90% de taxa de aprovação)
- **8 peças reprovadas** divididas por:
  - 25% por peso inadequado
  - 25% por cor não conforme
  - 50% por comprimento incorreto
- **1 caixa completa fechada** (10 peças)
- **1 caixa em andamento** (3 peças)

---

## 🔄 Fluxo de Validação

```
Entrada de Dados
       ↓
Validação de Peso (95-105g)
       ↓ [APROVADO]
Validação de Cor (azul/verde)
       ↓ [APROVADO]
Validação de Comprimento (10-20cm)
       ↓ [APROVADO]
Armazenamento em Caixa
       ↓
Verificação de Capacidade (10 peças)
       ↓ [CAIXA CHEIA]
Fechamento e Nova Caixa
```

---

## 🎓 Conceitos Pedagógicos Aplicados

Este projeto demonstra a aplicação prática de:

1. **Modularização**: Separação de responsabilidades em funções específicas
2. **Estruturas de Dados**: Uso eficiente de listas e dicionários
3. **Lógica Condicional**: Validações em cascata com early return
4. **Controle de Fluxo**: Loops while para menu e for para iterações
5. **Gestão de Estado**: Variáveis globais controladas por funções
6. **Feedback ao Usuário**: Mensagens claras e formatação visual

---

## 🚀 Perspectivas de Evolução

### Curto Prazo (Manter Escopo Introdutório)
- Persistência de dados em arquivo JSON
- Interface com cores usando biblioteca colorama

### Médio Prazo (Conceitos Intermediários)
- Refatoração para Orientação a Objetos (classes Peca, Caixa, Sistema)
- Testes unitários com pytest
- Interface gráfica com Tkinter

### Longo Prazo (Integração Industrial)
- Integração com sensores IoT (peso, cor via visão computacional)
- Dashboard web com Flask/FastAPI
- Machine Learning para detecção avançada de defeitos
- Integração com sistemas MES/ERP

---

## 📝 Licença e Uso Acadêmico

Este código foi desenvolvido exclusivamente para fins educacionais como trabalho acadêmico da disciplina de Algoritmos e Lógica de Programação. Livre para uso educacional com devida atribuição.

---

## 📞 Suporte

Para dúvidas ou sugestões relacionadas ao projeto:
- **Autor:** João Henrique Benatti Coimbra
- **Instituição:** UniFECAF
- **Disciplina:** Algoritmos e Lógica de Programação

---

**Versão:** 1.0  
**Última Atualização:** 15/11/2025