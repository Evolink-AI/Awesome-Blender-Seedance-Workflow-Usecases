## Source-backed case checklist

- [ ] Original source URL is included.
- [ ] Creator profile is included.
- [ ] Date is present or explicitly unavailable.
- [ ] Evidence type is one of Demo, Tutorial, Evaluation, Integration, Benchmark, or Limit.
- [ ] No prompt, result, benchmark, price, or API claim is invented.

## Localization checklist

- [ ] All 11 README files keep the same case count.
- [ ] All case anchors remain `#case-x`.
- [ ] Source URLs and creator URLs match the English source.

## Media and repository boundary checklist

- [ ] New public images, GIFs, posters, and videos use the recorded R2 contract; no new raw repository-local videos were added.
- [ ] Poster-frame links point to playable public video URLs.
- [ ] Related repository links stay within the adjacent Blender/Seedance guide, prompt, and skill surfaces for this repo family.

## Validation

- [ ] `python3 scripts/verify_repo.py`
- [ ] `python3 "${CODEX_HOME:-$HOME/.codex}/skills/usecase-update-loop/scripts/verify_usecase_update.py" --repo . --config data/usecase-update-config.json`
- [ ] `python3 scripts/audit_public_links.py`
- [ ] `git diff --check`
