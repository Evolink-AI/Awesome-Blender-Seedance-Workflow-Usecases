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

## Validation

- [ ] `python3 scripts/verify_repo.py`
- [ ] `git diff --check`
