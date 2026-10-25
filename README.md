# Catalytic Magic Cost archival snapshot

Source: https://github.com/GoGoKo699/Catalytic-Magic-Cost

Captured 2026-10-25. Main commit: `eaef69ef4e22cc998abd4a38d9176ca9db15faab`. Main tree: `b41d3c487bc5512a9b83a9c2533e1aac1768e58a`. The source repository was read only; this package contains no server credentials.

## What is preserved

The self-contained Git bundle preserves all **7 original commits, 4 branches, 1 tag, and 3 pull-request head refs** advertised by the source. It contains 46 unique objects: 7 commits, 11 trees, and 28 blobs. Commit IDs, parent relationships, author and committer identities/timestamps/timezones, messages, file bytes, paths and modes, and original signature bytes are retained exactly. Four commits have signatures. GitHub's recorded signature-verification metadata is retained; no independent OpenPGP trust-chain verification is claimed.

The compressed metadata preserves repository information; all three merged PRs, including their descriptions, details, changed-file lists, commits, events, and timelines; the single release; and explicit empty comment/review/asset/run inventories. There are 0 standalone issues, 0 discussion/review/commit comments on reachable commits, 0 reviews, 0 release assets and 0 Actions runs. Six issue events and nine PR timeline entries are retained. GitHub-generated tag ZIP/tar downloads can be regenerated from the preserved Git tag; they are not separate uploaded release assets.

## File map

| File | Purpose |
|---|---|
| `catalytic-magic-cost.bundle` | Complete original reachable Git history and refs; no prerequisite repository or network required. |
| `catalytic-magic-cost-metadata.json.gz` | UTF-8 JSON: original source/API records, capture provenance, completeness/limitations manifest, Git commit/tree API data, and object reconstruction procedure. |
| `verification.json` | Original ref map, object hashes and byte counts, signature preservation notes, snapshot hashes, metadata counts, and independent restoration results. |
| `MIGRATION.md` | Source-to-destination scientific map for all 17 source files. |
| `SHA256SUMS` | SHA-256 integrity checks for the other five archive files. |

These files are intended to be retained together on the dedicated permanent destination branch `archive/catalytic-magic-cost-history-20261025` in `GoGoKo699/Catalytic-Magic-Memory`. The source paths remain unchanged inside the bundle. This archive is independent of any scientific consolidation on the destination's main branch. Git data and GitHub metadata are mapped by original object IDs, PR/issue numbers and URLs; the archive does not rename or rewrite them.

The destination also contains a separately browsable [exact source snapshot](https://github.com/GoGoKo699/Catalytic-Magic-Memory/tree/32222d9143ea8b796b5143ac038afb90effd85bb), at commit `32222d9143ea8b796b5143ac038afb90effd85bb` on branch `archive/catalytic-magic-cost-source-20261025`. Its tree is the original source tree `b41d3c487bc5512a9b83a9c2533e1aac1768e58a`. That new snapshot commit is a destination copy; the bundle preserves the original source commit IDs and full history. Source-to-destination scientific mapping is documented separately by the migration's `MIGRATION.md` and provenance records.

## Restore and inspect offline

Run these commands in the directory containing the six archive files, using a new destination path:

```bash
sha256sum -c SHA256SUMS
git -c protocol.allow=never -c protocol.file.allow=always clone --mirror catalytic-magic-cost.bundle Catalytic-Magic-Cost.git
git --git-dir=Catalytic-Magic-Cost.git fsck --full --strict
git --git-dir=Catalytic-Magic-Cost.git bundle verify "$PWD/catalytic-magic-cost.bundle"
git --git-dir=Catalytic-Magic-Cost.git for-each-ref --format='%(refname) %(objectname)'
git --git-dir=Catalytic-Magic-Cost.git log --all --oneline --decorate
gzip -dc catalytic-magic-cost-metadata.json.gz > catalytic-magic-cost-metadata.json
git --git-dir=Catalytic-Magic-Cost.git archive --format=tar refs/heads/main > catalytic-magic-cost-main.tar
```

For an ordinary working copy after restoring the mirror:

```bash
git clone Catalytic-Magic-Cost.git Catalytic-Magic-Cost
```

A mirror restore keeps the three `refs/pull/*/head` refs. An ordinary clone does not normally copy these special refs, so retain the mirror/bundle for a complete archive. GitHub treats `refs/pull/*` as server-owned refs; do not blindly mirror-push the restored repository over an existing destination. Any future repository publication should use a new repository and deliberately choose writable branch/tag names for PR heads. Restoring metadata JSON does not recreate GitHub-managed issue/PR IDs, URLs, authorship records or server timestamps.

## Original ref map

| Ref | Original object ID |
|---|---|
| `refs/heads/docs/chitambar-gour-learning-route` | `6b7b4d44138ef56d4ae6600dfda72248b5ace068` |
| `refs/heads/fix/numbered-math-layout` | `379834e60c3df486f0cb63313712245703237087` |
| `refs/heads/main` | `eaef69ef4e22cc998abd4a38d9176ca9db15faab` |
| `refs/heads/research/catalyst-resource-converse` | `eb4396d43e906faebd944de87e04b2551e6a8023` |
| `refs/pull/1/head` | `eb4396d43e906faebd944de87e04b2551e6a8023` |
| `refs/pull/2/head` | `6b7b4d44138ef56d4ae6600dfda72248b5ace068` |
| `refs/pull/3/head` | `379834e60c3df486f0cb63313712245703237087` |
| `refs/tags/v1.0.0` | `eaef69ef4e22cc998abd4a38d9176ca9db15faab` |

## Verification performed

Every reconstructed Git object was checked against its original SHA-1 before being written. The bundle passed `git bundle verify` with no prerequisites. A fresh offline mirror clone with network protocols disabled passed `git fsck --full --strict`; all 8 refs and all 46 object IDs, types, byte lengths and SHA-256 hashes matched. All 17 files in the main snapshot were independently recovered and compared byte-for-byte. Source refs were re-read at `2026-10-25T14:11:08.942Z` and still matched. The compressed JSON passed a decompression/parse round trip.

## Coverage limits

This is a complete backup of Git objects reachable from the captured branch/tag/PR-head refs and the requested available public discussion/release/run metadata. It is **not a certified backup of every GitHub service feature**:

- Wiki is enabled in repository settings, but whether wiki pages exist was not verified and wiki content is not archived.
- Repository-wide labels, milestones, workflow-definition and artifact inventory endpoints were unsupported by the connected reader. All issue/PR label and milestone assignments are preserved (empty/null); tracked workflow files are covered by Git. Actions reports 0 runs, so no current run logs/artifacts were available to archive.
- The repository-wide commit-comment collection endpoint was unsupported; all 7 reachable commits were queried individually and have no comments. Comments on unreachable/deleted commits are outside coverage.
- Deleted/unadvertised refs and unreachable objects, expired/deleted Actions data, external link targets, admin configuration, secrets, collaborators, webhooks and environment settings are outside scope. Discussions are disabled.

Resolve any relevant wiki or service-configuration gaps before relying on this package as a complete service-level prerequisite for deleting the source. Keep the archive branch and these files permanently if the source is later removed.
