# Exploration Guide

**Purpose:** How to validate assumptions before writing specs.
**Read this before:** Writing any `specs/*.spec.md` file.

---

## The Problem This Solves

Specs built on unvalidated assumptions propagate errors expensively:

```
Knowledge (wrong assumption)
    ↓
Spec (uses wrong assumption)
    ↓
Plan (propagates wrong assumption)
    ↓
Impl (implements wrong assumption)
    ↓
Verify (catches it, but LATE)
```

If someone validates the assumption with a simple query FIRST, they save everyone time.

---

## Before Writing a Spec

### 1. Schema Validation

Do the tables/columns you expect actually exist?

```sql
-- WRONG: Assume the schema
-- "We'll use the users.email column for notifications"

-- RIGHT: Check first
DESCRIBE users;
-- Does 'email' exist? Is it nullable? What type?
```

### 2. Data Distribution

What values actually appear in the data?

```sql
-- WRONG: Assume values
-- "Transaction types 8, 9, 10 are for solar"

-- RIGHT: Check the data
SELECT transaction_type, COUNT(*)
FROM transactions
GROUP BY 1
ORDER BY 2 DESC;
-- What types actually exist? What are the counts?
```

### 3. Coverage Estimation

How many records match your criteria?

```sql
-- WRONG: Estimate
-- "About 70% of records will match"

-- RIGHT: Count
SELECT
  COUNT(*) as total,
  SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as matching,
  ROUND(100.0 * SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) / COUNT(*), 1) as pct
FROM records;
-- Actual result: 43%
```

### 4. Join Validation

Do your expected joins work?

```sql
-- WRONG: Assume tables join
-- "We'll join users to orders on user_id"

-- RIGHT: Verify the join
SELECT
  COUNT(*) as orders_total,
  COUNT(u.user_id) as orders_with_user,
  COUNT(*) - COUNT(u.user_id) as orphaned_orders
FROM orders o
LEFT JOIN users u ON o.user_id = u.user_id;
-- Are there orphaned records?
```

---

## Example: What NOT To Do

**Spec v2.0 said:**
> "Use transaction_type_id IN (8, 9, 10) for solar detection"

**Nobody ran this query:**
```sql
SELECT COUNT(*)
FROM bill_transaction_joins btj
JOIN transactions t ON btj.transaction_id = t.transaction_id
WHERE t.transaction_type_id IN (8, 9, 10);
-- Result: 0 rows
```

**What actually worked:**
```sql
SELECT COUNT(*)
FROM transactions
WHERE description LIKE '%Solar Surplus%';
-- Result: 15,000 rows
```

**Cost of not validating:** Multi-agent rework across Spec → Plan → Impl → Verify.

---

## Spec Requirements

Before marking a spec "Ready for Implementation":

- [ ] All assumptions validated with queries
- [ ] Query results documented (not estimates)
- [ ] Verification queries tested against real data
- [ ] Column names verified to match actual schema

### Data Validation Section Template

Add this to your spec:

```markdown
## Data Validation (Required Before Approval)

| Assumption | Query | Result | Date Validated |
|------------|-------|--------|----------------|
| "Types 8,9,10 are solar" | `SELECT COUNT(*) FROM...` | 0 rows (WRONG) | 2026-04-29 |
| "Solar via description" | `SELECT COUNT(*) WHERE desc LIKE...` | 15,000 rows | 2026-04-29 |
```

---

## When to Explore

| Situation | Explore? |
|-----------|----------|
| New data source | **YES** - understand schema first |
| Complex transformation | **YES** - validate join paths |
| Coverage estimates | **YES** - count actual records |
| Well-known internal API | Maybe - spot check assumptions |
| Simple CRUD operation | No - standard patterns apply |

---

## Documenting Findings

Put exploration findings in `knowledge/`:

```markdown
# Data Model: [Source Name]

**Explored:** 2026-04-29
**Validated against:** production database

## Tables

| Table | Rows | Purpose |
|-------|------|---------|
| users | 50K | User accounts |
| orders | 1.2M | Purchase records |

## Key Findings

1. **Solar detection** - Must use `description LIKE '%Solar%'`, not type_id
   - Query: `SELECT COUNT(*) WHERE description LIKE '%Solar%'`
   - Result: 15,000 rows

2. **Orphaned orders** - 3% of orders have no user
   - Query: `SELECT COUNT(*) FROM orders WHERE user_id IS NULL`
   - Result: 36,000 rows

## Gotchas

- `transaction_type_id` 8, 9, 10 exist but aren't in `bill_transaction_joins`
- Column is `created_at`, not `created` (different from docs)
```

---

## Key Insight

**One query before spec = many hours saved after.**

The explore phase is cheap. Rework across spec/plan/impl/verify is expensive.
