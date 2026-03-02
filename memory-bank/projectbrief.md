# Resumo do Projeto: Time Tracker

## Visão Geral do Projeto
Time Tracker é uma aplicação desktop leve e multi-plataforma para rastrear tempo gasto em múltiplos cards/tarefas simultaneamente. Construída com Python e PyQt6, oferece uma interface moderna, rápida e intuitiva para desenvolvedores gerenciarem tempo entre diferentes issues, tickets ou projetos.

## Objetivos Principais
1. **Leve e Rápido**: Aplicação desktop nativa com uso mínimo de recursos
2. **Gerenciamento Multi-card**: Rastrear múltiplas tarefas simultaneamente com timers independentes
3. **Multi-plataforma**: Suporte para ambientes Linux e Windows
4. **Persistência Automática**: Todos os dados salvos automaticamente no banco SQLite
5. **Amigável**: Interface simples e intuitiva com suporte a tema claro/escuro

## Requisitos Chave

### Requisitos Funcionais
- Adicionar cards com nomes customizados ou URLs
- Controles Play/Pause independentes para cada card
- Display preciso de timer (formato HH:MM:SS)
- Gravação automática de hora de início/fim
- Seleção e exclusão em massa
- Edição de nome de card
- Detecção de URL e links clicáveis
- Alternância de tema Escuro/Claro com persistência de preferência
- Atribuição automática de data para cada card

### Requisitos Técnicos
- Python 3.8+
- PyQt6 6.6.0+ para UI
- SQLite para persistência de dados
- Compatibilidade multi-plataforma (Linux/Windows)
- Funcionalidade de auto-save (a cada 5 segundos)
- Distribuível como executável standalone

## Escopo do Projeto
- **No Escopo**: Rastreamento de tempo desktop, persistência SQLite, operações CRUD básicas, suporte a temas
- **Fora do Escopo**: Versão web, apps mobile, recursos de colaboração em equipe, sincronização na nuvem

## Usuários Alvo
Desenvolvedores, freelancers e profissionais que precisam rastrear tempo em múltiplas tarefas ou projetos simultaneamente.

## Critérios de Sucesso
- Aplicação roda suavemente em Linux e Windows
- Timers são precisos e confiáveis
- Dados persistem entre sessões
- Interface é responsiva e intuitiva
- Executável constrói com sucesso para distribuição

## Restrições do Projeto
- Deve usar Python e PyQt6
- Deve ser leve (dependências mínimas)
- Deve suportar operação offline
- Não deve requerer serviços externos
