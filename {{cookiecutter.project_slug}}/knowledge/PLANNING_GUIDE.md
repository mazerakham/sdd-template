# Planning Guide

**Purpose:** Best practices for Plan Agents creating implementation plans.
**Read this before:** Creating any `plans/*.plan.md` file.

---

## Before You Start

### Assess Spec Stability

| Spec Indicator | Risk Level | Action |
|----------------|------------|--------|
| X.0 version (major) | High | Keep plan flexible, expect changes |
| Open questions section | Medium | Plan may need revision |
| Status: Draft | High | Do NOT plan yet |
| Status: Ready | Low | Safe to plan |

### Check for Spec Gaps

The spec MUST define these. If missing, mark as **BLOCKER**:

- [ ] **Deliverable format** (CSV, JSON, API response, etc.)
- [ ] **Output location** (file path, endpoint, database)
- [ ] **Testable success criteria** (not aspirational)
- [ ] **Scope boundaries** (what's explicitly excluded)
- [ ] **Data validation section** (assumptions verified with queries)

> **If any are missing:** Flag to Spec Agent. Do not proceed with planning.

---

## Required Plan Sections

Every plan must include:

1. **Spec Reference** - Version being implemented
2. **Spec Gaps & Blockers** - What's missing or unclear
3. **Risks** - What might go wrong? What's volatile?
4. **Tasks** - With files, acceptance criteria, references
5. **Dependencies** - What can parallelize?
6. **Notes for Impl Agent** - Practical tips

---

## Task Granularity

Each task should be:

| Criterion | Good | Bad |
|-----------|------|-----|
| **Size** | Completable in one session | Multi-day effort |
| **Scope** | Single responsibility | "Implement the feature" |
| **Verifiable** | Has acceptance criteria | "Make it work" |
| **Dependencies** | Explicit references | Implicit ordering |

### Example Good Task

```markdown
### Task 3: Create user validation

**Files:** `src/validators/user.ts`

**References:**
- `knowledge/user-schema.md` for field definitions
- `specs/USER-API.spec.md` section 3.2 for validation rules

**Acceptance Criteria:**
- [ ] Email format validation
- [ ] Required fields checked
- [ ] Returns typed error objects
- [ ] Unit tests pass

**Dependencies:** Task 1, Task 2
```

### Example Bad Task

```markdown
### Task: Build the API
Build all the API endpoints we need.
```

---

## Testing Requirements

**Plans must specify tests, not just say "add tests."** If verify agent finds basic failures (duplicates, nulls, broken FKs), that's a plan gap.

### Required Test Categories

| Category | Plan Must Specify | Impl Agent Writes |
|----------|-------------------|-------------------|
| Schema tests | Which fields are unique/not_null | schema.yml entries |
| Referential integrity | Which FKs must be valid | Relationship tests |
| Business rules | Equations, thresholds, constraints | Custom tests |
| Spec scenarios | Each acceptance scenario from spec | Scenario tests |
| Edge cases | Known edge cases to handle | Edge case tests |

### Test Specification Format

For each test, specify:
- **What** is being tested
- **Expected result** (pass condition)
- **Failure meaning** (what's broken if it fails)

Example:

| Test | Logic | Expected |
|------|-------|----------|
| Balance equation | items + taxes - refunds = subtotal | Variance < $0.01 |
| No duplicate keys | COUNT(DISTINCT id) = COUNT(*) | 0 duplicates |
| Valid FKs | All customer_id values exist in customers | 0 orphans |

### Testing Boundary

| Agent | Tests For |
|-------|-----------|
| **Plan Agent** | Specifies all known test requirements |
| **Impl Agent** | Implements specified tests + any discovered during impl |
| **Verify Agent** | Tests for things NO ONE thought of (true edge cases) |

**If verify agent finds a basic failure, that's a plan/impl failure, not a verify discovery.**

---

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| No deliverable task | Impl done but no output | Always include export/output task |
| Spec gap pass-through | Impl asks "what format?" | Plan agent must catch gaps spec missed |
| No risk assessment | Impl invalidated by spec change | Add Risks section |
| Stub tasks for future work | "TBD" tasks | Either fully spec or mark as "placeholder" |
| Inconsistent granularity | Some tasks 1hr, some 2 days | Break large tasks down |
| Minimal test spec | "Add tests" with no detail | Specify each test with pass criteria |
| Verify finds basics | Duplicates, nulls, broken FKs | Plan should have specified these tests |

---

## Risk Assessment Template

```markdown
## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Spec changes before impl done | Medium | High | Keep tasks modular |
| External API unavailable | Low | High | Mock for development |
| Performance requirements unclear | Medium | Medium | Add profiling task |
```

---

## Checklist Before Publishing

Run through this before marking plan ready:

- [ ] **Spec gaps identified** - or marked as blockers
- [ ] **All knowledge files read** - referenced in tasks
- [ ] **Deliverable has a task** - output/export explicit
- [ ] **Risks section completed** - especially spec stability
- [ ] **Consistent task granularity** - all tasks ~same size
- [ ] **Dependencies explicit** - what blocks what
- [ ] **Testing section complete** - all test categories covered
- [ ] **Each spec scenario has a test** - acceptance criteria are tested
- [ ] **Edge cases documented** - known edge cases have tests

---

## When to Flag Issues

Plan agents cannot modify specs, but **must** flag issues:

| Issue Type | Action |
|------------|--------|
| Missing deliverable format | BLOCKER - flag to Spec Agent |
| Contradictory statements | Flag specific locations |
| Unclear scope boundary | Ask for clarification |
| Unrealistic success criteria | Suggest alternatives |
| Unvalidated assumptions | Flag - explore first |

Create an entry in your plan's "Spec Gaps" section for each issue.

---

## Lessons Learned

| Mistake | Lesson |
|---------|--------|
| No export task | Deliverables need explicit tasks |
| Didn't assess spec stability | Early specs need risk section |
| Missed output format constraints | Validate deliverable requirements |
| Vague future tasks | Expand or mark as placeholders |
