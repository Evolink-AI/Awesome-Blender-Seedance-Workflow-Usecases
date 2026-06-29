# Maintenance

## Source of Truth

- Public curated source: `blender-seedance-usecase-curated.json`
- Human-readable curated source: `blender-seedance-usecase-curated.md`
- Owner-provided input: `data/primary-use-case-posts.json`

## Current State

- Selected public cases: 35
- Primary CTA: pending owner-provided landing page
- Public push: not approved
- GitHub repository creation: not approved; push target approved after local verification

## Case Rules

Each public case must include:

- Stable `<a id="case-x"></a>` anchor
- Source-linked `### Case X` heading
- Creator attribution
- Bold usage takeaway
- Source-grounded notes
- `Type: ... | Date: YYYY-MM-DD`

Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.

## Validation

```bash
python3 scripts/verify_repo.py
git diff --check
```

## Release Blockers

Replace `#conversion-path-pending` with the final landing page before claiming release-ready. The landing page should explain MCP installation, EvoLink skill installation, recharge, and agent usage.
