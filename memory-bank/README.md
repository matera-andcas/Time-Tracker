# Memory Bank: Time Tracker

This directory contains the Memory Bank for the Time Tracker project - a comprehensive documentation system designed to preserve project context across development sessions.

## Purpose

The Memory Bank serves as the single source of truth for:
- Project goals and requirements
- System architecture and patterns
- Technical decisions and constraints
- Current work status and progress
- Development insights and learnings

## Core Files

### 📋 [projectbrief.md](./projectbrief.md)
**Foundation document** - Defines core requirements, goals, scope, and success criteria for the Time Tracker project. This is the source of truth that shapes all other documentation.

### 🎯 [productContext.md](./productContext.md)
**Product vision** - Explains why Time Tracker exists, what problems it solves, and how it should work from a user perspective. Defines UX goals and quality standards.

### 🏗️ [systemPatterns.md](./systemPatterns.md)
**Technical architecture** - Documents the MVC architecture, design patterns, component relationships, and critical implementation paths. Essential for understanding code structure.

### 🔧 [techContext.md](./techContext.md)
**Technology details** - Covers the full technology stack (Python, PyQt6, SQLite), development setup, tools, and platform-specific considerations.

### 📍 [activeContext.md](./activeContext.md)
**Current state** - Tracks immediate work focus, recent changes, active decisions, important patterns, and learnings. Updated frequently to reflect current development status.

### 📊 [progress.md](./progress.md)
**Project status** - Documents what works, what's left to build, known issues, version history, and evolution of project decisions.

## File Relationships

```
projectbrief.md (foundation)
    ├── productContext.md (product vision)
    ├── systemPatterns.md (architecture)
    └── techContext.md (technology)
            ↓
    activeContext.md (current work)
            ↓
    progress.md (status tracking)
```

## When to Update

### Always Update When:
1. 🎯 Starting a new feature or major task
2. ✅ Completing significant work
3. 💡 Discovering important patterns or insights
4. 🔄 Making architectural or technical decisions
5. 📢 User requests with "**update memory bank**"

### Files to Update Most Frequently:
- **activeContext.md**: Current work, recent changes, active decisions
- **progress.md**: Completed work, known issues, status updates

### Files to Update Occasionally:
- **systemPatterns.md**: New patterns or architectural changes
- **techContext.md**: Technology stack changes or new tools
- **productContext.md**: UX insights or behavior clarifications

### Rarely Changed:
- **projectbrief.md**: Core project definition (only update if scope changes)

## How to Use

### Starting a New Session
1. Read `projectbrief.md` to understand project foundation
2. Review `activeContext.md` for current work status
3. Check `progress.md` for completed work and known issues
4. Reference `systemPatterns.md` and `techContext.md` as needed

### During Development
1. Note important discoveries and patterns
2. Document decisions as they're made
3. Track progress on current tasks

### After Major Work
1. Update `activeContext.md` with changes and learnings
2. Update `progress.md` with completed milestones
3. Update other files if patterns or architecture changed

### When User Says "Update Memory Bank"
1. Review **ALL** memory bank files
2. Update current state and progress
3. Document insights and patterns discovered
4. Clarify next steps and considerations

## Guidelines

### Writing Style
- **Clear and concise**: Direct language, no fluff
- **Specific and actionable**: Concrete details, not vague descriptions
- **Context-rich**: Explain "why" behind decisions
- **Future-oriented**: Write for someone picking up the project fresh

### Content Principles
- **Accuracy**: Information must be correct and up-to-date
- **Completeness**: Include all essential context
- **Consistency**: Use consistent terminology across files
- **Relevance**: Focus on what matters for development

### Maintenance
- Keep files under 500 lines when possible
- Archive old information if it becomes irrelevant
- Create additional context files for complex topics
- Regular review to ensure accuracy

## Additional Context Files

As the project grows, create additional files for:
- Feature-specific documentation
- Integration specifications
- API documentation
- Testing strategies
- Deployment procedures

Place them in the `memory-bank/` directory with clear, descriptive names.

## Benefits

✅ **Consistency**: Maintain project understanding across sessions
✅ **Efficiency**: Quick onboarding for new work
✅ **Quality**: Better decisions with full context
✅ **Collaboration**: Clear documentation for team members
✅ **Continuity**: No lost context between sessions

---

**Note**: The Memory Bank is a living documentation system. It should evolve with the project, always reflecting the current state and providing actionable context for future work.
