# Memory Bank: Time Tracker

Este diretório contém o Memory Bank do projeto Time Tracker - um sistema abrangente de documentação projetado para preservar o contexto do projeto através das sessões de desenvolvimento.

## Propósito

O Memory Bank serve como a única fonte de verdade para:
- Objetivos e requisitos do projeto
- Arquitetura e padrões do sistema
- Decisões técnicas e restrições
- Status de trabalho atual e progresso
- Insights e aprendizados de desenvolvimento

## Arquivos Principais

### 📋 [projectbrief.md](./projectbrief.md)
**Documento fundamental** - Define requisitos essenciais, objetivos, escopo e critérios de sucesso do projeto Time Tracker. Esta é a fonte de verdade que molda toda a documentação.

### 🎯 [productContext.md](./productContext.md)
**Visão do produto** - Explica por que o Time Tracker existe, quais problemas resolve e como deve funcionar da perspectiva do usuário. Define objetivos de UX e padrões de qualidade.

### 🏗️ [systemPatterns.md](./systemPatterns.md)
**Arquitetura técnica** - Documenta a arquitetura MVC, padrões de design, relacionamentos de componentes e caminhos críticos de implementação. Essencial para entender a estrutura do código.

### 🔧 [techContext.md](./techContext.md)
**Detalhes tecnológicos** - Cobre toda a stack tecnológica (Python, PyQt6, SQLite), configuração de desenvolvimento, ferramentas e considerações específicas de plataforma.

### 📍 [activeContext.md](./activeContext.md)
**Estado atual** - Rastreia o foco de trabalho imediato, mudanças recentes, decisões ativas, padrões importantes e aprendizados. Atualizado frequentemente para refletir o status atual de desenvolvimento.

### 📊 [progress.md](./progress.md)
**Status do projeto** - Documenta o que funciona, o que falta construir, problemas conhecidos, histórico de versões e evolução das decisões do projeto.

## Relacionamento entre Arquivos

```
projectbrief.md (fundação)
    ├── productContext.md (visão do produto)
    ├── systemPatterns.md (arquitetura)
    └── techContext.md (tecnologia)
            ↓
    activeContext.md (trabalho atual)
            ↓
    progress.md (rastreamento de status)
```

## Quando Atualizar

### Sempre Atualizar Quando:
1. 🎯 Iniciar uma nova funcionalidade ou tarefa importante
2. ✅ Completar trabalho significativo
3. 💡 Descobrir padrões ou insights importantes
4. 🔄 Fazer decisões arquiteturais ou técnicas
5. 📢 Usuário solicitar com "**atualizar memory bank**"

### Arquivos para Atualizar com Mais Frequência:
- **activeContext.md**: Trabalho atual, mudanças recentes, decisões ativas
- **progress.md**: Trabalho completado, problemas conhecidos, atualizações de status

### Arquivos para Atualizar Ocasionalmente:
- **systemPatterns.md**: Novos padrões ou mudanças arquiteturais
- **techContext.md**: Mudanças na stack tecnológica ou novas ferramentas
- **productContext.md**: Insights de UX ou clarificações de comportamento

### Raramente Alterados:
- **projectbrief.md**: Definição central do projeto (atualizar apenas se o escopo mudar)

## Como Usar

### Iniciando uma Nova Sessão
1. Leia `projectbrief.md` para entender a fundação do projeto
2. Revise `activeContext.md` para status do trabalho atual
3. Verifique `progress.md` para trabalho completado e problemas conhecidos
4. Referencie `systemPatterns.md` e `techContext.md` conforme necessário

### Durante o Desenvolvimento
1. Anote descobertas e padrões importantes
2. Documente decisões conforme são tomadas
3. Acompanhe o progresso nas tarefas atuais

### Após Trabalho Importante
1. Atualize `activeContext.md` com mudanças e aprendizados
2. Atualize `progress.md` com marcos completados
3. Atualize outros arquivos se padrões ou arquitetura mudaram

### Quando Usuário Diz "Atualizar Memory Bank"
1. Revise **TODOS** os arquivos do memory bank
2. Atualize estado atual e progresso
3. Documente insights e padrões descobertos
4. Clarifique próximos passos e considerações

## Diretrizes

### Estilo de Escrita
- **Claro e conciso**: Linguagem direta, sem enrolação
- **Específico e acionável**: Detalhes concretos, não descrições vagas
- **Rico em contexto**: Explique o "porquê" por trás das decisões
- **Orientado ao futuro**: Escreva para alguém pegando o projeto do zero

### Princípios de Conteúdo
- **Precisão**: Informação deve ser correta e atualizada
- **Completude**: Incluir todo contexto essencial
- **Consistência**: Usar terminologia consistente entre arquivos
- **Relevância**: Focar no que importa para o desenvolvimento

### Manutenção
- Manter arquivos com menos de 500 linhas quando possível
- Arquivar informação antiga se se tornar irrelevante
- Criar arquivos de contexto adicionais para tópicos complexos
- Revisão regular para garantir precisão

## Arquivos de Contexto Adicionais

Conforme o projeto cresce, criar arquivos adicionais para:
- Documentação específica de funcionalidades
- Especificações de integração
- Documentação de API
- Estratégias de teste
- Procedimentos de deploy

Colocá-los no diretório `memory-bank/` com nomes claros e descritivos.

## Benefícios

✅ **Consistência**: Manter entendimento do projeto entre sessões
✅ **Eficiência**: Rápida adaptação para novo trabalho
✅ **Qualidade**: Melhores decisões com contexto completo
✅ **Colaboração**: Documentação clara para membros da equipe
✅ **Continuidade**: Nenhum contexto perdido entre sessões

---

**Nota**: O Memory Bank é um sistema de documentação vivo. Deve evoluir com o projeto, sempre refletindo o estado atual e fornecendo contexto acionável para trabalho futuro.
