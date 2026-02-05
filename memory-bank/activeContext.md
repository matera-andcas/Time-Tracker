# Contexto Ativo: Time Tracker

**Última Atualização**: 2026-02-03
**Fase Atual**: Refinamento de UI/UX e Harmonização de Tema
**Status**: Estável, Visualmente Aprimorado

## Foco de Trabalho Atual

### Recentemente Completado (2026-02-03)
1. ✅ Harmonização completa do tema dark para diálogos de Time Picker e Calendário
2. ✅ Corrigido problema de truncamento de números no SpinBox
3. ✅ Implementados botões de seta customizados com símbolos Unicode (▲ ▼)
4. ✅ Separador ":" centralizado verticalmente no Time Picker
5. ✅ Aplicada herança de stylesheet do parent aos diálogos
6. ✅ Paleta de cores unificada entre todos os componentes de diálogo

### Tarefas Imediatas
- Monitorar feedback do usuário sobre os novos refinamentos de UI
- Pronto para novas solicitações de recursos ou polimento adicional

### Próximos Passos
- Aguardar direcionamento do usuário para:
  - Aprimoramentos adicionais de UI/UX
  - Novos recursos a implementar
  - Bugs a corrigir
  - Melhorias de performance
  - Otimizações específicas de plataforma

## Mudanças Recentes
- Estrutura do Memory Bank criada com todos os arquivos principais
- Documentação do projeto completa e atualizada
- Instruções customizadas configuradas para persistência de memória

## Decisões e Considerações Ativas

### Decisões Arquiteturais
- **Padrão MVC**: Mantendo separação rigorosa entre camadas
- **PyQt6**: Comprometidos com este framework para o futuro previsível
- **SQLite**: Abordagem local-first, sem planos para sincronização na nuvem

### Decisões de Design
- **Sistema de Temas**: Alternância dark/light suficiente por enquanto
- **Auto-save**: Intervalo de 5 segundos equilibrado entre segurança e performance
- **Precisão do Timer**: Granularidade de 1 segundo atende às necessidades do usuário

### Decisões Técnicas
- **Banco de Dados em Arquivo Único**: Simplifica backup e portabilidade
- **Sem Dependências Externas**: Manter footprint mínimo de dependências
- **Cross-platform Primeiro**: Todos os recursos devem funcionar em Linux e Windows

## Padrões e Preferências Importantes

### Estilo de Código
- **Separação Clara**: Manter camadas MVC distintas
- **Type Hints**: Usar quando útil para clareza
- **Docstrings**: Documentar todos os métodos públicos
- **Comentários**: Explicar o "porquê" não o "o quê"

### Padrões de UI/UX
- **Feedback Imediato**: Todas as ações fornecem resposta visual
- **Sem Estado Oculto**: Usuário sempre sabe o que está acontecendo
- **Espaçamento Consistente**: Usar layouts, não posições codificadas
- **Consistência de Tema**: Todos os widgets customizados suportam ambos os temas
- **Herança de Diálogo**: Diálogos herdam stylesheet do parent para consistência de tema
- **Controles Customizados**: Usar QPushButton para melhor controle sobre ícones/símbolos
- **Harmonia Visual**: Paleta de cores unificada em todos os elementos de UI

### Padrões de Dados
- **Auto-save de Tudo**: Usuário nunca pensa em salvar
- **Preservar Estado**: Aplicação lembra configurações
- **Falhar Graciosamente**: Nunca perder dados do usuário

### Padrões de Desenvolvimento
- **Testar em Ambas Plataformas**: Mudanças devem funcionar em Linux e Windows
- **Build Antes do Release**: Sempre testar executável standalone
- **Documentar Mudanças**: Atualizar arquivos relevantes do memory bank

## Insights e Aprendizados do Projeto

### O Que Funciona Bem
1. **Integração PyQt6**: Sistema de sinais/slots é elegante e confiável
2. **Persistência SQLite**: Banco de dados zero-configuration perfeito para este caso de uso
3. **Implementação do Timer**: QTimer fornece atualizações precisas e de baixo overhead
4. **Sistema de Temas**: Alternância simples atende necessidades do usuário sem complexidade
5. **Auto-save**: Usuários adoram não pensar em salvar

### Descobertas Chave
1. **Detecção de URL**: Usuários frequentemente colam URLs de issues como nomes de cards
2. **Múltiplos Cards**: Usuários frequentemente rastreiam 3-5 tarefas simultaneamente
3. **Preferência de Tema**: Seleção de tema persistente é altamente valorizada
4. **Ações de Um Clique**: Minimizar cliques melhora satisfação do usuário
5. **Feedback Visual**: Estados de hover e animações de botões importam

### Aprendizados Técnicos
1. **Confiabilidade do QTimer**: Mais confiável que threading.Timer do Python
2. **SQLite Row Factory**: Usar Row factory simplifica acesso a dados
3. **Peculiaridades do PyInstaller**: Arquivo spec necessário para ícone e metadados
4. **Caminhos Cross-platform**: Sempre usar os.path.join ou pathlib
5. **Ambientes Virtuais**: Essenciais para builds consistentes
6. **Estilização de QDialog**: Diálogos não herdam automaticamente stylesheets, deve aplicar parent.styleSheet()
7. **Botões Customizados no SpinBox**: Triângulos CSS não confiáveis, usar QPushButton com símbolos Unicode
8. **Alinhamento de Widgets**: Usar layouts de container com spacing ao invés de alinhamento direto
9. **Harmonização de Tema**: Cores de fundo unificadas criam coesão visual

### Preferências do Usuário (Inferidas)
- UI minimalista preferida
- Tema dark é a escolha primária
- Velocidade importa mais que recursos
- Confiabilidade é crítica
- Sem configuração desejada

## Problemas Conhecidos e Considerações

### Limitações Atuais
1. Sem sincronização na nuvem (por design)
2. Sem funcionalidade de exportação ainda
3. Sem relatórios/analytics
4. Sem atalhos de teclado
5. Sem funcionalidade de desfazer

### Ideias de Aprimoramento Futuro
1. Exportar dados de tempo para CSV
2. Atalhos de teclado para ações comuns
3. Dashboard de estatísticas/relatórios
4. Categorias ou tags de cards
5. Rastreamento de metas de tempo
6. Notificação em marcos de timer

### Considerações Específicas de Plataforma
- **Linux**: Integração com arquivo .desktop funciona bem
- **Windows**: Builds de EXE limpamente com PyInstaller
- **Ambos**: Diferenças de renderização de fonte aceitáveis

## Estado do Ambiente de Desenvolvimento

### Setup Atual
- Ambiente virtual com PyQt6 6.6.0+
- Python 3.8+ (testado no 3.10+)
- PyInstaller 6.0.0+ para builds
- Todas as dependências em requirements.txt

### Status do Build
- Scripts de build funcionais para ambas plataformas
- Executável testado e funcionando
- Integração de ícone bem-sucedida

### Estado do Banco de Dados
- Schema estável
- Sem migrações necessárias atualmente
- Persistência de dados confiável

## Padrões de Comunicação

### Com Usuários
- Manter jargão técnico mínimo
- Focar em funcionalidade, não implementação
- Fornecer feedback claro e acionável
- Documentar workarounds quando necessário

### No Código
- Código auto-documentado preferido
- Comentários apenas para lógica complexa
- Docstrings para todas as APIs públicas
- Nomes de variáveis claros

## Contexto para Sessões Futuras

### Referência Rápida
- **Entrada Principal**: `main.py`
- **Controller**: `src/application/controller.py`
- **UI**: `src/ui/main_window.py`
- **Database**: `src/infrastructure/database.py`
- **Models**: `src/domain/models.py`

### Tarefas Comuns
1. **Adicionar Recurso**: Começar no controller, adicionar UI em main_window, atualizar models/database conforme necessário
2. **Corrigir Bug**: Identificar camada (UI/Controller/Database), isolar problema, corrigir e testar
3. **Atualizar UI**: Modificar `main_window.py` e `styles.py`, garantir suporte a tema
4. **Mudança de Schema**: Atualizar `database.py`, adicionar lógica de migração, testar completamente

### Arquivos Chave para Referência
- `README.md`: Documentação do usuário
- `requirements.txt`: Dependências
- `TimeTracker.spec`: Configuração de build
- Arquivos do Memory Bank: Contexto e decisões do projeto

## Pronto para Próxima Tarefa
A aplicação está estável e funcional. Memory Bank está completo e pronto para guiar desenvolvimento futuro. Aguardando input do usuário para próximo aprimoramento ou correção.
