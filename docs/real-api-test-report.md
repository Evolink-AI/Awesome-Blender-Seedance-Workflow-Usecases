# Seedance Real API Test Report

## Scope

- Test date: 2026-07-10
- Verification date: 2026-07-11
- API: EvoLink Seedance 2.0 family
- Endpoint lifecycle: create task, poll task, retrieve final video
- Parameters: 4 seconds, 480p, 16:9, audio disabled
- Submission rule: each task was submitted exactly once

## Results

| Tier | Model | Task ID | Status | Elapsed | Credits | Final video |
|---|---|---|---|---:|---:|---|
| Mini | `seedance-2.0-mini-text-to-video` | `task-unified-1783694290-g6q7sla2` | completed | 109s | 10.23 | [Play verified Mini result](https://files.evolink.ai/000BG2E93TVWN41W8S/videos/2026/07/10/b35f41e735fe42539f822b6249f2ce68.mp4) |
| Fast | `seedance-2.0-fast-text-to-video` | `task-unified-1783694416-25p9g1ww` | completed | 113s | 16.5726 | [Play verified Fast result](https://files.evolink.ai/000BG2E93TVWN41W8S/videos/2026/07/10/5e4146ed9d20474ba6040479411fce46.mp4) |
| Standard | `seedance-2.0-text-to-video` | `task-unified-1783694546-i1b0di77` | completed | 156s | 20.46 | [Play verified Standard result](https://files.evolink.ai/000BG2E93TVWN41W8S/videos/2026/07/10/a61fa3851b0d4c8b8ad8ec82081998bf.mp4) |

On 2026-07-11 all three final video URLs returned HTTP `206` with `video/mp4` content type. The returned usage and EvoLink dashboard billing remain authoritative; these observed credit values are evidence, not fixed pricing claims.

## Coverage Boundary

This evidence verifies the live Seedance 2.0 task lifecycle for Mini, Fast, and Standard text-to-video. The repository's Blender + Seedance examples primarily document reference-driven workflows; their case evidence comes from attributed public sources rather than a claim that every referenced workflow was rerun by EvoLink.
