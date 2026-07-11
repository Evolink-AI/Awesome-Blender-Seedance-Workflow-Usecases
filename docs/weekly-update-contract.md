# Weekly Usecase Update Contract

## Schedule

- Cadence: weekly
- Start: Monday 11:00 Asia/Shanghai
- Candidate window: the seven days ending at the collector's fixed `collected_at` timestamp
- Selection cap: at most 10 cases per run
- Completion state: `published` or verified `no-op`

## Candidate Boundary

Keep only concrete, public Blender + Seedance workflows, tutorials, demos, integrations, evaluations, benchmarks, or limitations.

Drop pure prompts, promotion-only posts, reposts, duplicate sources, finance noise, unverifiable claims, ambiguous dates, missing attribution, and any item that still needs human judgment. Quality takes priority over count; a run may publish fewer than 10 cases.

## Execution Gates

1. Update local `main` from `origin/main` and stop on unrelated dirty changes.
2. Collect all configured X queries and save a fixed-window external candidate artifact.
3. Run curation prep and require one requested, resolved, executed, non-skipped repository result.
4. Review every queued candidate into `high_confidence_update`, `deferred`, `unsure`, or `drop`.
5. Select at most 10 `high_confidence_update` items and write the semantic review and handoff package.
6. Pass the handoff verifier before changing any public file.
7. Update English and structured data first. Preserve the recorded legacy case namespace and append new cases contiguously from Case 29.
8. Pass the English gate, then update all localized READMEs with real visible-text translation.
9. Pass repository, usecase, localization, media, public-link, template, general GitHub, clean-diff, and completion gates.
10. Commit on an isolated weekly branch, fast-forward merge the audited commit into local `main`, push `main`, and verify remote commit plus rendered public surfaces.

If no candidate qualifies, save reconciled no-op evidence and report why the cap was not reached. If collection, baseline, handoff, audit, merge, push, or remote readback fails, report `blocked`; do not weaken the quality bar and do not push partial work.

## Conversation Report

Every run reports raw, seven-day, reviewed, selected, deferred, unsure, and dropped counts; selected case numbers and source URLs; grouped drop/no-op reasons; verifier results; artifact paths; commit hash; merge result; push result; public readback; and blockers.
