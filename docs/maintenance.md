# Maintenance

## Source of Truth

- Public curated source: `blender-seedance-usecase-curated.json`
- Human-readable curated source: `blender-seedance-usecase-curated.md`
- Owner-provided input: `data/primary-use-case-posts.json`
- Manual originality audit: `docs/usecase-originality-audit.md`
- Downloaded public media: `media/case-XX/`

## Current State

- Selected public cases: 20
- Candidate pool before audit: 35
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
- Local media links when the source data exposes media
- `Type: ... | Date: YYYY-MM-DD`

Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.
Do not re-add removed candidates without updating the audit file.

## Validation

```bash
python3 scripts/verify_repo.py
git diff --check
```

## Release Blockers

Replace `#conversion-path-pending` with the final landing page before claiming release-ready. The landing page should explain MCP installation, EvoLink skill installation, recharge, and agent usage.
