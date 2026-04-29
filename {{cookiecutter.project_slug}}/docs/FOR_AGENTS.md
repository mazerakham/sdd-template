# SDD for AI Agents

This guide explains how AI agents should work within a Spec-Driven Development project.

---

## First Steps (Every Session)

1. **Read CLAUDE.md** - The constitution defines your constraints
2. **Run `./scripts/sdd preflight`** - Fix any environment issues
3. **Identify your role** - Check branch/worktree name
4. **Check file ownership** - Know what you can and cannot modify

---

## Role Identification

Your role is determined by where you are:

| Location | Role |
|----------|------|
| `main` branch | Spec Agent or Explore Agent |
| `plan-v*` branch | Plan Agent |
| `.worktrees/impl-v*` | Impl Agent |
| Reviewing impl worktree | Verify Agent |

Run `./scripts/sdd validate` to confirm your role.

---

## Role-Specific Guidance

### Explore Agent

**Purpose:** Validate assumptions before specs are written.

**Can modify:** `knowledge/`
**Cannot modify:** `specs/`, `plans/`, implementation code

**How to work:**
1. Query real data sources
2. Document findings in `knowledge/*.md`
3. Include actual query results, not estimates
4. Flag surprises that would affect specs

**Before finishing:**
- [ ] All assumptions have queries
- [ ] Query results are documented
- [ ] Gotchas are clearly noted

---

### Spec Agent

**Purpose:** Define what success looks like.

**Can modify:** `specs/`, `knowledge/`
**Cannot modify:** `plans/`, implementation code

**Before starting:**
- Read `knowledge/EXPLORATION_GUIDE.md`
- Review existing `knowledge/*.md` files

**How to work:**
1. Define clear success criteria
2. Specify exact deliverable format
3. Include "NOT in scope" section
4. Add Data Validation section with tested queries
5. Include verification queries that have been run

**Before releasing:**
- [ ] Data Validation section complete
- [ ] Verification queries tested against real data
- [ ] NOT in scope section present
- [ ] Success criteria are measurable

Release with: `./scripts/sdd spec-release v1.0`

---

### Plan Agent

**Purpose:** Break spec into implementable tasks.

**Can modify:** `plans/`
**Cannot modify:** `specs/`, `knowledge/`, implementation code

**Before starting:**
- Read `knowledge/PLANNING_GUIDE.md`
- Read the spec thoroughly
- Review relevant knowledge files

**How to work:**
1. Check spec stability (version, status, open questions)
2. Identify any spec gaps - mark as BLOCKERS
3. Create atomic tasks with clear acceptance criteria
4. Note dependencies between tasks
5. Assess risks

**Before publishing:**
- [ ] Spec gaps identified or marked as blockers
- [ ] All knowledge files referenced in tasks
- [ ] Deliverable has explicit task
- [ ] Risks section completed
- [ ] Tasks are consistently sized

Create with: `./scripts/sdd plan-create v1.0 1`

---

### Impl Agent

**Purpose:** Build exactly what the spec says.

**Can modify:** Implementation code, `AMBIGUITIES.md`, `SPEC_FEEDBACK.md`
**Cannot modify:** `specs/`, `knowledge/`, `plans/`

**Before starting:**
1. Run `./scripts/sdd preflight` - fix any issues
2. Read the spec
3. Read the plan
4. Read relevant knowledge files

**How to work:**
1. Follow plan tasks in order
2. When blocked by ambiguity:
   - Document in `AMBIGUITIES.md`
   - Make a reasonable choice
   - Continue (don't wait for answers)
3. Track lessons learned for `SPEC_FEEDBACK.md`

**Before submitting:**
- [ ] All plan tasks completed
- [ ] AMBIGUITIES.md updated
- [ ] SPEC_FEEDBACK.md written
- [ ] Code runs without errors

Submit with: `./scripts/sdd impl-submit`

---

### Verify Agent

**Purpose:** Check implementation against spec criteria.

**Can modify:** `VERIFY_REPORT.md`
**Cannot modify:** Everything else (including implementation code)

**Before starting:**
- You must be independent from the Impl Agent
- Fresh perspective is critical

**How to work:**
1. Start with direct data queries, not build tools
2. Verify spec assumptions first
3. Sample records and trace end-to-end
4. Check all success criteria from spec
5. Have fallback when automated tools fail

**Verification steps:**
1. Run `./scripts/sdd verify`
2. Sample 3-5 records, trace through system
3. Run verification queries from spec
4. Document findings in VERIFY_REPORT.md

**What to look for (beyond automated tests):**
- Integration issues between components
- Race conditions or timing issues
- Error handling paths not covered
- Real-world data edge cases
- Performance under load

**Verdict:**
- APPROVE if all criteria met
- REJECT with specific reasons if not

**If you find basic failures** (duplicates, nulls, broken FKs, balance equations), note in VERIFY_REPORT.md that the plan should have specified these tests.

Commands:
```bash
./scripts/sdd verify-start impl-v1.0.1-agent
./scripts/sdd verify-approve impl-v1.0.1-agent
./scripts/sdd verify-reject impl-v1.0.1-agent "reason"
```

---

## Common Mistakes

| Mistake | Prevention |
|---------|------------|
| Skip preflight | Script won't run without it |
| Modify wrong files | `sdd validate` catches this |
| Assume spec is correct | Query the data yourself |
| Get stuck on ambiguity | Document in AMBIGUITIES.md, continue |
| Estimate instead of measure | Run actual queries |
| Skip verification queries | They're there for a reason |
| Verify your own impl | Must be independent agent |

---

## File Ownership Matrix

| Path | Explore | Spec | Plan | Impl | Verify |
|------|:-------:|:----:|:----:|:----:|:------:|
| `knowledge/` | Write | Write | Read | Read | Read |
| `specs/` | Read | Write | Read | Read | Read |
| `plans/` | - | - | Write | Read | Read |
| impl code | - | - | - | Write | Read |
| `AMBIGUITIES.md` | - | - | - | Write | Read |
| `SPEC_FEEDBACK.md` | - | - | - | Write | Read |
| `VERIFY_REPORT.md` | - | - | - | Read | Write |

---

## When Things Go Wrong

### Spec has errors
- Document in SPEC_FEEDBACK.md
- Work around if possible
- Flag for next spec version

### Plan has gaps
- Document in AMBIGUITIES.md
- Make reasonable choices
- Note what you assumed

### Environment issues
- Run `./scripts/sdd preflight`
- Check SETUP.md
- Ask human for help if stuck

### Verification fails
- Document specific failures
- REJECT with clear reasons
- Impl agent fixes and resubmits

---

## Quick Reference

```bash
# Every session
./scripts/sdd preflight

# Spec agent
./scripts/sdd spec-release v1.0

# Plan agent
./scripts/sdd plan-create v1.0 1

# Impl agent
./scripts/sdd impl-start plan-v1.0.1 myname
./scripts/sdd impl-submit

# Verify agent
./scripts/sdd verify-start impl-v1.0.1-myname
./scripts/sdd verify
./scripts/sdd verify-approve impl-v1.0.1-myname

# Always
./scripts/sdd validate
./scripts/sdd status
```
