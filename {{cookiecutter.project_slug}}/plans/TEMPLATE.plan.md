# Implementation Plan

**Spec:** `spec-vX.Y`
**Plan Version:** X.Y.Z
**Status:** Draft | Ready for Implementation

---

## Spec Reference

- **Spec file:** `specs/FEATURE.spec.md`
- **Spec version:** `spec-vX.Y`
- **Spec status:** Ready for Implementation

---

## Spec Gaps & Blockers

Before proceeding, resolve these issues:

| Gap | Severity | Status | Notes |
|-----|----------|--------|-------|
| [Missing info] | BLOCKER / Warning | Open / Resolved | [Details] |

If any BLOCKERS are Open, do NOT proceed with implementation.

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Low/Medium/High | Low/Medium/High | [How to mitigate] |
| [Risk 2] | ... | ... | ... |

---

## Tasks

### Task 1: [Task Name]

**Files:** `path/to/file.ext`

**References:**
- `knowledge/file.md` for [what info]
- `specs/FEATURE.spec.md` section X for [what info]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Dependencies:** None

---

### Task 2: [Task Name]

**Files:** `path/to/file.ext`

**References:**
- [Reference 1]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Dependencies:** Task 1

---

### Task 3: [Output/Export Task]

**Files:** `path/to/output/`

**References:**
- `specs/FEATURE.spec.md` section "Deliverable"

**Acceptance Criteria:**
- [ ] Output matches spec format
- [ ] Output written to correct location
- [ ] Output passes verification queries

**Dependencies:** Task 1, Task 2

---

## Dependency Graph

```
Task 1 ─────┬──────► Task 3
Task 2 ─────┘
```

---

## Testing Requirements

**Plan agents own testing strategy.** If verify agent finds basic failures, that's a plan gap.

### Test Categories

| Category | Tests Required |
|----------|----------------|
| Schema | [Which fields are unique/not_null?] |
| Referential integrity | [Which FKs must be valid?] |
| Business rules | [What equations/thresholds/constraints?] |
| Spec scenarios | [Each acceptance scenario from spec] |
| Edge cases | [Known edge cases to handle] |

### Specific Tests

| Test | Logic | Expected Result |
|------|-------|-----------------|
| [Test 1] | [What's being tested] | [Pass condition] |
| [Test 2] | [What's being tested] | [Pass condition] |
| [Test 3] | [What's being tested] | [Pass condition] |

### Testing Boundary

- **Impl Agent:** Implements all tests above + any discovered during implementation
- **Verify Agent:** Tests for things NO ONE thought of (true edge cases)

---

## Notes for Impl Agent

### Setup
- Run `./scripts/sdd preflight` before starting
- [Any additional setup steps]

### Gotchas
- [Known issue 1]
- [Known issue 2]

---

## Checklist Before Publishing

- [ ] Spec gaps identified (or marked as blockers)
- [ ] All knowledge files read and referenced
- [ ] Deliverable has explicit task
- [ ] Risks section completed
- [ ] Consistent task granularity
- [ ] Dependencies are explicit
- [ ] Testing section complete with specific tests
- [ ] Each spec scenario has a corresponding test
- [ ] Edge cases documented with tests
- [ ] At least 10 tests specified (more for complex features)
