# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

---

## Environment Setup (REQUIRED - READ FIRST)

**Before any work, run:**

```bash
./scripts/sdd preflight
```

If preflight fails, fix your environment before proceeding. See `SETUP.md` for details.

---

## SDD Structure

This project uses **Spec-Driven Development**:

```
{{ cookiecutter.project_slug }}/
├── CLAUDE.md              # Constitution (this file)
├── WORKFLOW.md            # SDD process documentation
├── specs/                 # Specifications (the contract)
├── plans/                 # Implementation plans
├── knowledge/             # Domain knowledge (discovered facts)
└── [your impl folders]    # Implementation code
```

### Document Types

| Type | Purpose | Changes When |
|------|---------|--------------|
| **Spec** | Contract (what to build) | Requirements change |
| **Knowledge** | Domain facts (how things work) | We learn something new |
| **Plan** | Implementation tasks | Approach changes |
| **Constitution** | Immutable rules | Rarely |

---

## Workflow

See **`WORKFLOW.md`** for complete documentation.

**Quick reference:**
1. **Explore** - Validate assumptions against real data
2. **Spec** - Define what success looks like (tag: `spec-vX.Y`)
3. **Plan** - Break spec into tasks (branch: `plan-vX.Y.Z`)
4. **Impl** - Build to spec (worktree: `impl-vX.Y.Z-agent`)
5. **Verify** - Check against spec success criteria

---

## Agent Roles

**Before starting work, identify your role:**

| Role | Branch/Location | Can Modify | Cannot Modify |
|------|-----------------|------------|---------------|
| **Explore Agent** | `main` | knowledge/ | specs/, plans/ |
| **Spec Agent** | `main` | specs/, knowledge/ | plans/, impl code |
| **Plan Agent** | `plan-*` | plans/ | specs/, knowledge/, impl code |
| **Impl Agent** | worktree `impl-*` | impl code, AMBIGUITIES.md, SPEC_FEEDBACK.md | specs/, knowledge/, plans/ |
| **Verify Agent** | worktree `impl-*` | VERIFY_REPORT.md | everything else |

**Run `./scripts/sdd validate` before committing.**

---

## Commands

```bash
# Check environment
./scripts/sdd preflight

# Spec agent: release new spec version
./scripts/sdd spec-release v1.0

# Plan agent: create plan from spec
./scripts/sdd plan-create v1.0 1

# Impl agent: start implementation
./scripts/sdd impl-start plan-v1.0.1 myname

# Run verification
./scripts/sdd verify

# Verify agent commands
./scripts/sdd verify-start impl-v1.0.1-myname
./scripts/sdd verify-approve impl-v1.0.1-myname
```

---

## Standards

- Document assumptions in knowledge/ before writing specs
- Validate assumptions with real data queries
- All specs must have "Data Validation" section
- All specs must have "NOT in scope" section
- Use AMBIGUITIES.md when blocked, don't get stuck
