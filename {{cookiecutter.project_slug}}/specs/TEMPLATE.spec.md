# Feature Name Spec

**Version:** 1.0
**Status:** Draft | Ready for Implementation
**Last Updated:** YYYY-MM-DD

---

## 1. Overview

### Objective
[One sentence: what does this feature accomplish?]

### Success Definition
[How will we know this is done? What is the measurable outcome?]

### Deliverable
[What is produced? Be specific: file path, format, endpoint, etc.]

---

## 2. Data Validation (Required Before Approval)

**IMPORTANT:** All assumptions must be validated against real data before this spec is approved.

| Assumption | Query | Result | Date Validated |
|------------|-------|--------|----------------|
| [Assumption 1] | `SELECT COUNT(*) FROM...` | [Result] | YYYY-MM-DD |
| [Assumption 2] | `...` | [Result] | YYYY-MM-DD |

---

## 3. Requirements

### Inputs
- **Source:** [Where does data come from?]
- **Format:** [Structure, schema]
- **Access:** [How do we get it?]

### Outputs
- **Destination:** [Where does it go?]
- **Format:** [Structure, schema, columns]
- **Naming:** [File naming convention]

### Transformations
1. [Step 1]
2. [Step 2]
3. [Step 3]

---

## 4. Constraints

### Performance
- [Any performance requirements?]

### Dependencies
- [What must exist before this can run?]

### Assumptions
- [What are we assuming is true?]

---

## 5. NOT in Scope

**Explicitly excluded from this spec:**

- [Thing 1 that is NOT being built]
- [Thing 2 that is NOT being built]
- [Thing 3 that is NOT being built]

---

## 6. Success Criteria

Implementation is complete when:

- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Measurable criterion 3]
- [ ] Verification queries pass (see below)

---

## 7. Verification Queries (Tested)

These queries have been tested against real data:

```sql
-- Query 1: [Description]
-- Tested: YYYY-MM-DD, Result: [expected result]
SELECT ...

-- Query 2: [Description]
-- Tested: YYYY-MM-DD, Result: [expected result]
SELECT ...
```

---

## 8. Open Questions

- [ ] [Question 1]
- [ ] [Question 2]

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | YYYY-MM-DD | Initial spec |
