# SDD for Humans

This guide explains Spec-Driven Development for humans working on or managing SDD projects.

---

## What is SDD?

Spec-Driven Development is a workflow where:

1. **Requirements are documented as specs** before implementation
2. **Assumptions are validated** against real data
3. **Implementation follows the spec** exactly
4. **Verification checks** against spec criteria, not developer intent

The goal: Reduce rework by catching mistakes early.

---

## When to Use SDD

**Good fit:**
- Multi-step features
- Data transformations
- Work that will be verified independently
- Anything touching external systems
- Projects with multiple contributors (human or AI)

**Overkill:**
- Single-line bug fixes
- Quick experiments
- One-off scripts you'll throw away

---

## The Workflow

```
Explore → Spec → Plan → Impl → Verify → Ship
```

### 1. Explore

**Who:** Explore Agent or human
**Output:** `knowledge/*.md`

Before writing a spec, validate assumptions:
- Query actual data
- Document schema findings
- Note gotchas discovered

This prevents expensive rework when assumptions turn out to be wrong.

### 2. Spec

**Who:** Spec Agent or human
**Output:** `specs/*.spec.md` + `spec-vX.Y` tag

Define:
- What success looks like
- What the deliverable is
- What's NOT in scope
- Verification queries (tested against real data)

The spec is the contract. Everything downstream follows it.

### 3. Plan

**Who:** Plan Agent
**Output:** `plans/*.plan.md` on `plan-vX.Y.Z` branch

Break the spec into:
- Atomic tasks
- Clear acceptance criteria
- Explicit dependencies

The plan identifies spec gaps. If something is unclear, it's flagged as a blocker.

### 4. Impl

**Who:** Impl Agent
**Output:** Implementation code in `impl-vX.Y.Z-agent` worktree

Build exactly what the spec says. If something is ambiguous:
- Document in `AMBIGUITIES.md`
- Make a reasonable choice
- Keep going

When done, write `SPEC_FEEDBACK.md` documenting lessons learned.

### 5. Verify

**Who:** Verify Agent (different from Impl)
**Output:** `VERIFY_REPORT.md`

Check:
- Spec criteria met?
- Sample records trace correctly?
- Verification queries pass?

Verdict: APPROVED or REJECTED

### 6. Ship

**Who:** Human
**Action:** Review VERIFY_REPORT.md, merge approved impl to main

---

## Your Role as a Human

### Before Work Starts

1. **Review the spec** - Make sure requirements are clear
2. **Check Data Validation section** - Are assumptions tested?
3. **Approve spec release** - Tag only when confident

### During Implementation

- You may be asked to resolve ambiguities
- Agents will document blockers in AMBIGUITIES.md
- You can answer questions asynchronously

### After Verification

1. **Read VERIFY_REPORT.md** - Understand what was checked
2. **Review SPEC_FEEDBACK.md** - Learn for next iteration
3. **Merge or request fixes**

---

## Directory Structure

```
project/
├── CLAUDE.md              # Constitution (read this first)
├── WORKFLOW.md            # Process documentation
├── specs/                 # Specifications (the contract)
│   └── FEATURE.spec.md
├── plans/                 # Implementation plans
│   └── FEATURE.plan.md
├── knowledge/             # Domain knowledge
│   └── data-model.md
├── docs/                  # Human/agent guides
│   ├── FOR_HUMANS.md      # (this file)
│   └── FOR_AGENTS.md
└── scripts/
    └── sdd                # Workflow CLI
```

---

## Common Commands

```bash
# Check environment
./scripts/sdd preflight

# See project status
./scripts/sdd status

# Release a spec version
./scripts/sdd spec-release v1.0

# Create a plan
./scripts/sdd plan-create v1.0 1

# Start implementation
./scripts/sdd impl-start plan-v1.0.1 alice

# Start verification
./scripts/sdd verify-start impl-v1.0.1-alice

# Approve/reject
./scripts/sdd verify-approve impl-v1.0.1-alice
./scripts/sdd verify-reject impl-v1.0.1-alice "reason"
```

---

## FAQ

### Why so much process?

SDD front-loads the thinking. Catching a wrong assumption during Explore costs minutes. Catching it during Verify costs hours or days of rework.

### Can I skip steps?

For trivial changes, yes. For anything non-trivial, the process saves time overall.

### What if the spec is wrong?

Create a new spec version. Downstream branches rebase onto it.

### Can multiple agents work in parallel?

Yes. Each impl works in its own worktree. They don't interfere with each other.

---

## Quick Reference

| Phase | Output | Command |
|-------|--------|---------|
| Explore | `knowledge/*.md` | (manual) |
| Spec | `specs/*.spec.md` | `sdd spec-release v1.0` |
| Plan | `plans/*.plan.md` | `sdd plan-create v1.0 1` |
| Impl | code + docs | `sdd impl-start plan-v1.0.1 agent` |
| Verify | `VERIFY_REPORT.md` | `sdd verify` |
| Ship | merged to main | (human review) |
