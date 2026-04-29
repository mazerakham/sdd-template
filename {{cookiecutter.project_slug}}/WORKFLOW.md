# SDD Workflow

This document defines how agents collaborate on spec-driven development.

---

## Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. EXPLORE: Validate assumptions                  [Explore Agent]│
│    - Query real data to validate assumptions                    │
│    - Document findings in knowledge/                            │
│    - Flag gaps before spec is written                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. SPEC: Define success criteria                    [Spec Agent]│
│    - Write specs/*.spec.md with validated assumptions           │
│    - Include Data Validation section with query results         │
│    - Tag: spec-v{X.Y}                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. PLAN: Create implementation plan                 [Plan Agent]│
│    - Branch: plan-v{X.Y.Z} from spec-v{X.Y}                     │
│    - Write plans/*.plan.md with tasks                           │
│    - Identify spec gaps as blockers                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. IMPL: Build the solution                         [Impl Agent]│
│    - Worktree: impl-v{X.Y.Z}-{agent}                            │
│    - Run ./scripts/sdd preflight first                          │
│    - Document ambiguities in AMBIGUITIES.md                     │
│    - Write SPEC_FEEDBACK.md with issues found                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. VERIFY: Independent verification               [Verify Agent]│
│    - Run ./scripts/sdd verify independently                     │
│    - Sample records and trace end-to-end                        │
│    - Write VERIFY_REPORT.md                                     │
│    - APPROVE or REJECT                                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. SHIP: Merge to main                                  [Human] │
│    - Review VERIFY_REPORT.md                                    │
│    - Merge approved impl to main                                │
│    - Clean up worktrees                                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Branch Model

```
main (spec-controlled)
│
├── tag: spec-v1.0 ◄── defines what to build
│   │
│   └── branch: plan-v1.0.1 ◄── implementation plan
│       │
│       ├── worktree: impl-v1.0.1-alice ◄── Alice's implementation
│       │   └── verified, approved → merge to main
│       │
│       └── worktree: impl-v1.0.1-bob ◄── Bob's parallel attempt
│
└── tag: spec-v1.1 ◄── next spec version
    └── ...
```

---

## Agent Roles

### Explore Agent
- **Reads:** External data sources, existing documentation
- **Writes:** `knowledge/*.md`
- **Rules:**
  - Validate assumptions with real queries
  - Document findings with query results
  - Flag gaps before spec is written

### Spec Agent
- **Reads:** Knowledge files, user requirements
- **Writes:** `specs/*.spec.md`, `knowledge/*.md`
- **Creates:** Spec version tags on `main`
- **Before starting:** Read `knowledge/EXPLORATION_GUIDE.md`
- **Rules:**
  - Never write implementation code
  - All assumptions must be validated with data
  - Include "Data Validation" section with query results
  - Include "NOT in scope" section
  - Spec changes require new version tag

### Plan Agent
- **Reads:** Spec, knowledge, **`knowledge/PLANNING_GUIDE.md`**
- **Writes:** `plans/*.plan.md` (includes tasks)
- **Creates:** Plan branches off spec tags
- **Before starting:** Read `knowledge/PLANNING_GUIDE.md` for best practices
- **Rules:**
  - Never modify spec or knowledge (flag issues for Spec Agent)
  - Plan must reference spec version
  - Tasks must be atomic and testable
  - **Must identify spec gaps** - mark missing info as blockers
  - **Must assess risks** - especially spec stability
  - **Must specify testing requirements** - not just "add tests" but what tests, what they check, what passing means
  - **Owns testing strategy** - verify agent should find surprises, not obvious gaps

### Impl Agent
- **Reads:** Spec, knowledge, plan
- **Writes:** Implementation code, AMBIGUITIES.md, SPEC_FEEDBACK.md
- **Creates:** Commits on impl worktree
- **Rules:**
  - Run `./scripts/sdd preflight` before any work
  - Work ONLY in assigned worktree
  - Never modify spec, knowledge, or plan
  - Document ambiguities in `AMBIGUITIES.md`
  - Write `SPEC_FEEDBACK.md` with issues encountered
  - All code must trace to plan tasks
  - **Implement all tests specified in plan** - do not hand off until all pass
  - **Add tests discovered during implementation** - if you find an edge case, test it

### Verify Agent
- **Reads:** Spec, knowledge, plan, implementation output
- **Writes:** `VERIFY_REPORT.md`
- **Creates:** Verification results, approval/rejection
- **Rules:**
  - Never modify implementation code
  - Start with direct data queries, not build tools
  - Verify spec assumptions first
  - Sample records and trace end-to-end
  - Have fallback when build tools fail
  - Independent from impl agent (different context/session)
  - **Can reject implementation** if verification fails
  - **Focus on unspecified scenarios** - your job is to find what plan/impl missed
  - **Flag plan gaps** - if you find basic failures (duplicates, nulls, broken FKs), note that plan should have specified these tests

---

## Testing Boundary

Clear separation of testing responsibilities:

| Agent | Tests For |
|-------|-----------|
| **Plan Agent** | Specifies all known test requirements with pass criteria |
| **Impl Agent** | Implements specified tests + any discovered during impl |
| **Verify Agent** | Tests for things NO ONE thought of (true edge cases, integration issues) |

**Key principle:** If verify agent finds a basic failure (duplicates, nulls, broken FKs, balance equations), that's a plan/impl failure, not a verify discovery.

---

## Commands

### Environment
```bash
./scripts/sdd preflight              # Check environment (REQUIRED)
./scripts/sdd validate               # Check SDD discipline
```

### Spec Agent Commands
```bash
./scripts/sdd spec-release v1.0      # Create spec version tag
```

### Plan Agent Commands
```bash
./scripts/sdd plan-create v1.0 1     # Creates plan-v1.0.1
```

### Impl Agent Commands
```bash
./scripts/sdd impl-start plan-v1.0.1 alice    # Create worktree
./scripts/sdd impl-rebase                      # Rebase onto upstream
./scripts/sdd impl-submit                      # Mark ready for review
```

### Verify Agent Commands
```bash
./scripts/sdd verify-start impl-v1.0.1-alice  # Start verification
./scripts/sdd verify                           # Run verification
./scripts/sdd verify-approve impl-v1.0.1-alice
./scripts/sdd verify-reject impl-v1.0.1-alice "reason"
```

---

## File Ownership

| Path | Explore | Spec | Plan | Impl | Verify |
|------|:-------:|:----:|:----:|:----:|:------:|
| `knowledge/` | ✅ | ✅ | ❌ | ❌ | ❌ |
| `specs/` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `plans/` | ❌ | ❌ | ✅ | ❌ | ❌ |
| impl code | ❌ | ❌ | ❌ | ✅ | ❌ |
| `AMBIGUITIES.md` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `SPEC_FEEDBACK.md` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `VERIFY_REPORT.md` | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Feedback Loop

Every impl agent must produce `SPEC_FEEDBACK.md` documenting:
1. **Schema gaps** - Missing/incorrect info in knowledge docs
2. **Setup gaps** - Environment issues not documented
3. **Spec gaps** - Requirements that were unclear or missing
4. **Classification** - Was it a spec issue or implementer mistake?

This feedback feeds into the next spec version.

---

## Cascade Rules

When upstream changes, downstream must rebase:

| Change | Action Required |
|--------|-----------------|
| Knowledge updated | Spec may need revision |
| Spec updated | All plans rebase, then all impls rebase |
| Plan updated | All impls on that plan rebase |

**Rebase command:**
```bash
./scripts/sdd cascade-rebase
```
