# GitHub Repo Action List

Repo: `Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases`
Review date: 2026-07-11
Review mode: Review + Fix + weekly automation readiness

## P0

- [x] Migrate all public README media to R2 and create poster images for every video.
  - Why: The current contract requires R2-hosted public media, video poster links, a media inventory, an upload report, and rendered GitHub/camo verification. The repository still references local `media/*.mp4` and `media/*.jpg` files.
  - Owner: EvoLink repository automation owner
  - Expected result: Media, link, fresh-clone, and rendered-GitHub gates pass without relying on large repository blobs.

- [x] Record and wire the audited `shared-r2` brand banner policy for all 11 READMEs.
  - Why: The model-repo contract requires R2 public media, while the usecase template now permits an explicitly recorded shared brand banner when origin/render evidence covers it.
  - Owner: EvoLink content/design owner
  - Expected result: The template banner and multilingual first-screen audit pass.

- [x] Run and save a complete public-surface link audit after the R2 and banner migration.
  - Why: A recurring run cannot be labeled `published` while public links, images, video targets, anchors, and redirects lack a P0/P1 audit report.
  - Owner: Weekly usecase automation
  - Expected result: Link audit reports P0=0 and P1=0 and is usable by the completion gate.

## P1

- [x] Register the repository in `usecase-update-loop` with a seven-day external X collector and a maximum of 10 selected cases.
  - Why: An unregistered repository or missing collector adapter must fail closed rather than look like a no-op.
  - Owner: Model Repo Pipeline
  - Expected result: Curation manifest proves one requested, resolved, executed, non-skipped repository.

- [x] Record the existing public numbers as a legacy namespace and require a contiguous tail beginning at Case 29.
  - Why: Existing public anchors have gaps and should not be silently renumbered, while all new cases still need deterministic numbering.
  - Owner: Model Repo Pipeline
  - Expected result: Existing links remain stable and future cases are numbered 29, 30, 31, and so on without gaps.

- [x] Replace stale `cheercheung/Awesome-Blender-Seedance-Workflow-Usecases` public links with the live `Evolink-AI` owner.
  - Why: Contribution and Star History links otherwise route to the wrong repository surface.
  - Owner: Repository maintainer
  - Expected result: Public repository links resolve to the current owner.

- [x] Add `CODE_OF_CONDUCT.md` and `SECURITY.md`; verify the issue form again after push.
  - Why: The public repository community profile is currently 75%, with no code of conduct or security policy and no recognized issue template.
  - Owner: Repository maintainer
  - Expected result: Community profile exposes actionable contribution, conduct, security, issue, and PR paths.

- [x] Add a `Related Repositories` section with verified adjacent Seedance API/skill surfaces.
  - Why: The active template requires the usecase surface to route API and Skill intent without implementing those releases inside this repository.
  - Owner: Repository maintainer
  - Expected result: Readers can move from examples to verified execution surfaces.

- [ ] Expand GitHub topics with Blender and workflow discovery terms.
  - Why: Current topics cover Seedance variants but omit `blender`, `blender-mcp`, `ai-filmmaking`, `previs`, and `video-workflow`.
  - Owner: Repository maintainer
  - Expected result: Repository metadata aligns with its description and user search intent.

## P2

- [x] Add a timeout and explicit per-query failure surface to the weekly collector.
  - Why: A slow X search should end as a visible blocked run rather than leave the automation hanging or incorrectly report no-op.
  - Owner: Model Repo Pipeline
  - Expected result: Every query has bounded execution and failures are explicit in the run report.

## Notes

- Blockers: final public-surface and rendered GitHub/camo audit after push.
- Out of scope: API/Skill release work and changes to model availability or pricing.
- Follow-up check: Activate the weekly schedule only after every P0 item passes.
- Link copy issues: The Quick Start API-key action is clear; old-owner repository links were corrected locally.
