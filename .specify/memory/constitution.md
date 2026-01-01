<!--
Sync Impact Report:
Version: 0.0.0 → 1.0.0
Change Type: Initial constitution creation (MAJOR version bump)
Modified Principles: N/A (initial creation)
Added Sections: All sections added
Removed Sections: None
Templates Status:
  ✅ plan-template.md - Aligned with constitution principles
  ✅ spec-template.md - Aligned with constitution principles
  ✅ tasks-template.md - Aligned with constitution principles
Follow-up TODOs: None
-->

# In-Memory Todo Console App Constitution

## Core Principles

### I. Spec-First Development (NON-NEGOTIABLE)

**MUST**: Every feature begins with a specification before any implementation code is written.

- Specifications MUST be written to `specs/<feature>/spec.md` and approved before implementation
- Implementation work MUST NOT begin until the spec is complete and validated
- Specifications MUST include user scenarios, requirements, and success criteria
- Each feature MUST have clear, testable acceptance criteria documented in the spec

**Rationale**: Spec-first development ensures clear requirements, prevents scope creep, enables independent review, and provides documentation for future reference. This approach prevents wasted implementation effort on misunderstood requirements.

### II. Beginner-Friendly Code Quality

**MUST**: All code MUST be clear, readable, and accessible to beginners learning Python.

- Function and class names MUST be descriptive and self-documenting
- Variable names MUST clearly indicate purpose (avoid single-letter names except in short comprehensions)
- Code MUST use standard Python conventions (PEP 8)
- Complex logic MUST include inline comments explaining the "why", not the "what"
- Avoid advanced Python features (metaclasses, decorators, generators) unless essential and well-documented

**Rationale**: This is an educational project designed for beginners. Code readability and learnability take precedence over clever optimizations or advanced patterns.

### III. Minimal Scope (No Feature Creep)

**MUST**: Implementation MUST strictly match specifications—no additional features unless explicitly requested.

- Do NOT add error handling beyond what is specified
- Do NOT add logging, metrics, or observability unless requested
- Do NOT add configuration options, settings, or extensibility hooks unless specified
- Do NOT refactor or "improve" code outside the current feature scope
- Each feature MUST be independently deliverable without dependencies on unspecified features

**Rationale**: Minimalism keeps the codebase simple, maintainable, and aligned with learning objectives. Feature creep adds complexity that obscures core concepts for beginners.

### IV. In-Memory Storage Only

**MUST**: All data MUST be stored in-memory using native Python data structures.

- No databases (SQL, NoSQL, or embedded)
- No file persistence (JSON, pickle, CSV, etc.)
- No external storage services or caching systems
- All data resets when the program terminates
- Use Python lists, dictionaries, or dataclasses for data storage

**Rationale**: In-memory storage eliminates external dependencies, simplifies deployment, and focuses learning on core programming concepts rather than database operations.

### V. Console-Only Interface

**MUST**: All user interaction MUST occur through the command-line interface.

- Use Python's `input()` for user prompts
- Use `print()` for output (formatted clearly and consistently)
- No graphical user interfaces (GUI)
- No web interfaces or REST APIs
- Clear, user-friendly console menus and prompts
- Error messages MUST be displayed clearly in the console

**Rationale**: Console interfaces are universal, require no additional frameworks, and teach fundamental input/output concepts without the complexity of UI frameworks.

### VI. Test-Driven Development (Optional, User-Requested Only)

**CONDITIONAL**: Tests are written ONLY if explicitly requested in the feature specification.

- When tests are requested: TDD workflow MUST be followed (write tests → tests fail → implement → tests pass)
- Test files MUST be organized in a `tests/` directory
- Use Python's built-in `unittest` or `pytest` framework
- Tests MUST be runnable independently
- If no tests are requested in the spec, DO NOT create test files

**Rationale**: While testing is a best practice, this educational project prioritizes simplicity. Testing is taught when explicitly requested rather than imposed universally.

## Data Model Standards

### Task Entity Requirements

**MUST**: All Task entities MUST have these exact attributes:

- **ID** (integer): Auto-generated, unique, sequential starting from 1
- **Title** (string): Required, non-empty, maximum 100 characters
- **Description** (string): Optional, maximum 500 characters
- **Status** (enum/string): Either "Pending" or "Completed" (case-sensitive)

**MUST NOT**: Add additional attributes unless explicitly specified in a feature spec.

**Rationale**: Standardized data models ensure consistency across features and prevent confusion for users learning the codebase.

## Core Features

### Required Feature Set

The application MUST support these five core operations:

1. **Add Task**: Create a new task with title and optional description
2. **View Tasks**: Display all tasks with their full details
3. **Update Task**: Modify title or description of an existing task
4. **Delete Task**: Remove a task by ID
5. **Mark Complete/Incomplete**: Toggle task status between Pending and Completed

Each feature MUST be independently specifiable and implementable.

## Development Workflow

### Feature Development Lifecycle

**MUST** follow this sequence for every feature:

1. **Specification Phase** (`/sp.specify`):
   - Write `specs/<feature>/spec.md` with user scenarios and requirements
   - Get user approval before proceeding

2. **Planning Phase** (`/sp.plan`):
   - Create `specs/<feature>/plan.md` with technical approach
   - Document architecture decisions if significant

3. **Task Breakdown** (`/sp.tasks`):
   - Generate `specs/<feature>/tasks.md` with granular, testable tasks
   - Ensure tasks are ordered by dependencies

4. **Implementation Phase** (`/sp.implement`):
   - Implement tasks in dependency order
   - Create Prompt History Records (PHR) for each implementation session
   - Mark tasks complete only when fully working

5. **Commit Phase** (`/sp.git.commit_pr`):
   - Commit completed features with clear messages
   - Create pull requests when appropriate

### Prompt History Records (PHR)

**MUST**: Create a PHR after every user prompt that results in implementation work, planning, or specification changes.

**PHR Routing** (all under `history/prompts/`):
- Constitution-related → `history/prompts/constitution/`
- Feature-specific → `history/prompts/<feature-name>/`
- General → `history/prompts/general/`

**PHR Content Requirements**:
- MUST capture full user input verbatim (no truncation)
- MUST include representative response snapshot
- MUST record all modified files
- MUST include stage, date, model, and surface metadata
- MUST follow template at `.specify/templates/phr-template.prompt.md`

**Rationale**: PHRs provide traceability, enable learning from past sessions, and document decision-making context.

### Architecture Decision Records (ADR)

**Conditional**: ADRs are created ONLY when all three conditions are met:

1. **Impact**: The decision has long-term architectural consequences
2. **Alternatives**: Multiple viable approaches were considered
3. **Scope**: The decision is cross-cutting and affects system design

**Process**:
- When a significant decision is detected, SUGGEST (do NOT auto-create):
  - "📋 Architectural decision detected: <brief> — Document reasoning and tradeoffs? Run `/sp.adr <decision-title>`"
- Wait for user consent before creating ADR
- ADRs MUST be stored in `history/adr/`
- ADRs MUST follow template at `.specify/templates/adr-template.md`

**Rationale**: ADRs document important decisions without creating overhead for routine choices.

## Code Standards

### Python-Specific Requirements

**MUST**:
- Use Python 3.8+ features (type hints encouraged but not required)
- Follow PEP 8 style guidelines
- Use meaningful variable names: `task_id` not `tid`, `user_input` not `ui`
- Avoid global variables except for the in-memory task store
- Use docstrings for functions and classes (Google or NumPy style)

**MUST NOT**:
- Use deprecated Python features
- Mix tabs and spaces (use 4 spaces per indentation level)
- Leave commented-out code in production
- Use wildcard imports (`from module import *`)

### Error Handling

**MUST**:
- Validate user inputs (e.g., non-empty titles, valid task IDs)
- Display clear, actionable error messages to users
- Handle expected errors gracefully (e.g., invalid menu choice)
- Use `try/except` only for genuinely exceptional cases, not control flow

**MUST NOT**:
- Crash the application on invalid user input
- Display technical stack traces to end users
- Silently ignore errors

### Security Considerations

**MUST**:
- Validate all user inputs for type and format
- Prevent extremely long inputs that could exhaust memory
- Sanitize displayed output (though low risk in console apps)

**MUST NOT**:
- Execute user input as code (e.g., `eval()`, `exec()`)
- Allow arbitrary file system access (not applicable given in-memory constraint)

## Governance

### Amendment Process

This constitution MUST be amended through the `/sp.constitution` command only.

**Version Semantic**:
- **MAJOR**: Backward-incompatible changes (e.g., removing principles, changing core requirements)
- **MINOR**: Adding new principles or sections (backward-compatible)
- **PATCH**: Clarifications, typos, wording improvements

### Compliance

**MUST**: All specifications, plans, and implementation work MUST verify compliance with this constitution.

- Specs MUST reference applicable principles in "Constitution Check" section
- Plans MUST justify any violations in "Complexity Tracking" table
- Code reviews MUST verify adherence to code standards

### Living Document

This constitution evolves with the project. When principles conflict with practical needs:
1. Surface the conflict to the user immediately
2. Propose amendment with clear rationale
3. Get explicit approval before violating existing principles
4. Update constitution via `/sp.constitution` command

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
