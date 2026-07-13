# Maintenance

## Source of Truth

- Public curated source: `blender-seedance-usecase-curated.json`
- Owner-provided input: `data/primary-use-case-posts.json`
- Owner-provided video source map: `data/usecase-video-sources.json`
- Manual originality audit: `docs/usecase-originality-audit.md`
- GitHub About metadata proposal: `docs/github-about.md`
- Legacy local source media: `media/caseN.mp4` for pre-R2 historical cases only
- Public media origin: R2 under `github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/`
- Media inventory: [`docs/media-type-inventory.md`](media-type-inventory.md)
- R2 origin audit: [`docs/r2-upload-report.md`](r2-upload-report.md)
- Video poster report: [`docs/video-poster-report.md`](video-poster-report.md)

`scripts/generate_repo.py` is a legacy scaffold generator, not the recurring-update entry point. Do not run it during weekly updates: its original source package does not contain all 10 current language translations. Weekly runs update curated data and English first, then apply and audit language-specific translations without overwriting existing localized prose.

## Current State

- Selected public cases: 32
- Owner-provided video rows: 33
- Latest weekly candidate pool: 147 deduplicated candidates, 59 fixed-window reviewed items
- Primary CTA: EvoLink Blender-to-video cookbook (`https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=docs&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=maintenance_primary_cta`)
- Public push: approved to the existing target repository after local verification
- GitHub repository creation: not approved and not needed for this repo
- GitHub About metadata: drafted in `docs/github-about.md`; applying it requires repository settings permission

## Case Rules

Each public case must include:

- Stable `<a id="case-x"></a>` anchor
- Source-linked `### Case X` heading
- Creator attribution
- Bold usage takeaway
- Source-grounded notes
- R2-hosted reference images when the source data exposes media
- R2-hosted poster frames linked to playable R2 video URLs
- `Type: ... | Date: YYYY-MM-DD`

Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.
Do not re-add removed candidates without updating the audit file.

## Recurring Update Contract

- Detailed contract: [`docs/weekly-update-contract.md`](weekly-update-contract.md)
- Readiness actions: [`github-repo-review-action-list.md`](../github-repo-review-action-list.md)
- Schedule: every Monday at 11:00 Asia/Shanghai.
- Candidate window: the seven days ending at the collector's fixed `collected_at` timestamp.
- Selection cap: at most 10 `high_confidence_update` cases; never fill the cap with weak items.
- Exclusions: prompt-only posts, promotion-only posts, reposts, duplicates, unverifiable claims, and candidates that still need human judgment.
- Existing public anchors are a recorded legacy namespace. Preserve the current public numbers and append new cases contiguously from `Case 29`.
- Update English first, pass the English gate, then update all 10 localized READMEs with real visible-text translation.
- A modification run succeeds only after audit, commit, push to `main`, and remote readback. A low-quality week may end as a verified no-op with counts and reasons.
- Run-local curation and audit artifacts stay under `.codex/usecase-update-loop/` and must not be committed.

## Validation

```bash
python3 scripts/verify_repo.py
python3 "${CODEX_HOME:-$HOME/.codex}/skills/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py" --repo .
git diff --check
```

## Release Blockers

The primary CTA is set to the EvoLink Blender-to-video cookbook. Keep `#quick-start` as the repository-local workflow reference for Blender MCP setup, EvoLink skill installation, API key setup, and agent usage.
