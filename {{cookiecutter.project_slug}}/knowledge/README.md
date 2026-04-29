# Knowledge Directory

This directory contains **discovered facts** about the domain, data, and systems we work with.

---

## Purpose

Knowledge files document:
- Data schemas and their quirks
- API behaviors discovered through testing
- Business rules learned from exploration
- Gotchas and edge cases

**Key principle:** Knowledge comes from exploration, not assumption.

---

## Who Writes Here

| Agent | Can Write? |
|-------|------------|
| Explore Agent | Yes |
| Spec Agent | Yes |
| Plan Agent | No (read only) |
| Impl Agent | No (read only) |
| Verify Agent | No (read only) |

---

## File Structure

```
knowledge/
├── README.md                 # This file
├── EXPLORATION_GUIDE.md      # How to validate assumptions
├── PLANNING_GUIDE.md         # Best practices for plans
├── data-model.md             # Schema documentation
├── api-behaviors.md          # API quirks and behaviors
└── business-rules.md         # Domain logic
```

---

## Template for Knowledge Files

```markdown
# [Topic Name]

**Explored:** YYYY-MM-DD
**Validated against:** [data source]

## Summary

[One paragraph overview]

## Key Findings

### Finding 1: [Title]

**Query:**
```sql
SELECT ...
```

**Result:** [Actual result]

**Implication:** [What this means for specs/impl]

### Finding 2: [Title]
...

## Gotchas

- [Thing that surprised us]
- [Common mistake to avoid]

## References

- [Link to external docs]
- [Link to related spec]
```

---

## Best Practices

1. **Always include queries** - Show how you discovered the fact
2. **Include actual results** - Don't estimate, measure
3. **Date your findings** - Data changes over time
4. **Note the source** - Which database? Which API version?
5. **Document gotchas** - Prevent others from making the same mistakes

---

## When to Update

Update knowledge files when:
- You discover something new during exploration
- A spec assumption turns out to be wrong
- The underlying system changes
- You find a better way to query something

---

## Relationship to Other Files

```
knowledge/ (discovered facts)
    ↓ informs
specs/ (requirements)
    ↓ broken into
plans/ (tasks)
    ↓ implemented as
code (solution)
```

Knowledge is the foundation. Wrong knowledge propagates expensive errors.
