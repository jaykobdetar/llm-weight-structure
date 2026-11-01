# LLM weight-structure search

This repository records a series of bounded searches for mathematical and causal structure in small language models. It is a research ledger, not a library or a claim that a general weight-based algorithm has been discovered. All layer, head and coordinate indices are zero-based.

The strongest positive in this collection is **a known receiver-copy operation by SmolLM2-135M layer 18 head 6 under observed routing**: it passed the frozen swap, specificity and removal gates on eight paired confirmation clusters. A separately nominated layer 29 head 1 had a removal effect but failed the joint copying tests. This does not establish the key-construction mechanism, a predecessor circuit, two-hop computation, or a new large coherent weight group. The scalar-record audit cannot reconstruct the unsaved vectors and logits. See [findings and limits](docs/FINDINGS.md#receiver-comparison).

Other searches produced bounded negative or inconclusive results. A later Smol capability-only development check passed eight correlated cases; its proposed bilinear Stage B **was not qualified or executed**. A subsequent generated-only attempt stopped before its numerical worker because a watchdog had stale completion hashes. That is a technical failure, not a finding against a native mathematical hypothesis. The trained Pythia MLP pilot has complete conditional worker records, but the overall run retains a monitoring technical hold.

- [Findings, negative results and technical stops](docs/FINDINGS.md)
- [Experiment, controls and evidence index](docs/EXPERIMENTS.md)
- [Method, limitations and next questions](docs/METHOD.md)
- [Evidence file hashes and scope](evidence/MANIFEST.json)

The separate [super-weight research repository](https://github.com/jaykobdetar/superweight-research/tree/ce1629a0e0c6b41baa9e204437f1055b33fbce89) covers the OLMo super-weight mechanism and other-model comparisons. Its results do not imply a shared mechanism here. The revision shown is the historical publication snapshot, not a claim about the current branch head.

## What is and is not included

The [`evidence`](evidence/) directory contains selected frozen scalar summaries and one independent audit text, with SHA-256s and source-record names. A selected-field MLP monitoring summary is explicitly marked as derived. These files support auditing the recorded reductions and limitations; they do not reproduce omitted activations, full logits, source code paths, model execution, intervention provenance, or all original raw evidence. Some richer records are retained externally and are not included because they contain fitted vectors or require source-access review. See [experiments](docs/EXPERIMENTS.md#external-dependencies-and-reproduction).

No model checkpoints, model-weight slices, full prompt strings, private conversations, credentials or large corpora are included. Nothing here authorizes new model work, reopening a closed branch, changing a frozen gate, or claiming a result from an unrun panel. New work requires an explicit new question, freeze, resource budget and authorization.

## Lightweight integrity check

From the repository root, run `python3 scripts/check_evidence.py`. This checks the recorded file sizes and hashes only. It does not run experiments, validate checkpoint provenance or prove model behavior. Python's standard library is sufficient.
