# Experiment and evidence index

## Model identities and recorded execution

| Asset | Recorded immutable revision | Recorded payload SHA-256 | Notes |
| --- | --- | --- | --- |
| SmolLM2-135M | `93efa2f097d58c2a74874c7e644dbc9b0cee75a2` | `80521b40281d6ce74e35c9282c22539e75aa0ac8578892b2a59955ef78d55da1` | BF16-stored weights promoted to CPU FP32 in the recorded work. |
| Pythia-160M final | `50f5173d932e8e61f858120bcb800b97af589f46` | `29d2e457a664e41c12c735f20a36dc0956a665f614a54ce5db21a32e75965270` | F16-stored learned tensors in the recorded final checkpoint. |
| Pythia-160M step 0 | `0cf035e7d55e9b2fbec7f2db0c0c32670146b9b1` | `87c169cd152db340535d6f330af0e2eed7578484ef2d23dd44ca90cbcc215ba7` | F32-stored; direct precision comparisons require care. |

These are historical receipt identities; the payload bytes are not in this repository and were not rehashed during this documentation work. Historical native inference used Python 3.12.3, Torch 2.8.0+cpu and Transformers 4.56.2, CPU FP32 eager, batch one and cache off. Static work used Python 3.13.13 and NumPy 2.4.6. Environment versions are not proof of byte-identical kernels.

Smol uses nine query heads, three KV groups, head width 64 and `kv(h) = h // 3`; H6 maps to KV2. Its RMSNorm does not center, and attention and MLP have distinct inlet gains. Pythia uses 12 independent heads, biased per-head packed QKV, partial 16-coordinate RoPE and parallel attention/MLP residual branches. Its final LayerNorm centers before the learned gain. Neither port convention is interchangeable with the other.

## Controls, seeds and counts

| Study | Inputs, controls and decisive limits | Included evidence |
| --- | --- | --- |
| Collective synthetic selector | 16 selector starts, 64-unit supports; planted known support acts as a sensitivity control. Fixture seed and frozen search records are saved. | [Synthetic record](../evidence/collective-synthetic.json) |
| Prompted pointer and induction | Pointer: 8 development and 32 confirmation clusters, 160 observations; both unrestricted and forced-choice scoring. Induction: 32 paired clusters and 64 prompts, both scoring modes. | [Pointer](../evidence/pointer.json), [induction](../evidence/induction.json) |
| Receiver comparison | PCG64 seeds `260102620` discovery, `260102621` confirmation, `260102622` controls. Two selectors, fixed 261-head universe; 8 confirmation pairs; target swap, norm-matched synthetic control, removal, identity and fixed-final-scale checks. 132 forward intents/completions. | [Saved comparison](../evidence/receiver-comparison.json), [independent scalar closure](../evidence/receiver-closure.md) |
| Projection and depth | Projection: 264 candidates per checkpoint, frozen defect ≤0.15. Depth: four fit windows, 184 block calls, 18 nonanchor strata with optimistic bound ≤0.25; validation/confirmation remained unrun. | [Projection summary](../evidence/projection.json); original depth result hash in [manifest](../evidence/MANIFEST.json), omitted because it contains fitted vectors. |
| Match/copy, shared factor, matrix gate, GQA | Fixed nomination and static-screen universes; 0/6 tuples, 0/6,144 rows, 0/6,144 signed cohorts, 0/12 sites respectively. These are different gates and must not be pooled. | [Match/copy](../evidence/matchcopy.json), [shared factor](../evidence/shared-factor.json), [matrix gate](../evidence/matrix-gate.json), [GQA](../evidence/gqa-geometry.json) |
| Key relay, Pythia receiver, context collision | Respectively 16 capability forwards; 34 forwards ending at first failed identity; 24 completed of 64 planned. The remaining collision prompts are unrun. | [Key relay](../evidence/key-relay.json), [Pythia stop](../evidence/pythia-transfer-stop.json), [collision stop](../evidence/context-order-stop.json) |
| C2 interface | 26 ASCII pairs; one fit plus 19 fixed cyclic mismatches at each of final/initialization, all evaluated on saved rows. Threshold ≤0.10; no full-model forward. | [Independent audit](../evidence/c2-independent-audit.txt) |
| Trained MLP pilot | Frozen eight-state panel; worker completed local program, reference and controls, but guardian stop remained unresolved. Full local call counts are separate units. | [Derived monitoring subset](../evidence/trained-mlp-monitoring-subset.json) |
| Smol Stage A | Sham PCG64 seed base `2026102801`, fixed-norm QR null, eight correlated 18-token development cases; four parity, then 24 capability forwards. Frozen thresholds: clean margin ≥0.5, swap loss ≥0.5, swap–sham ≥0.25 and at least six of eight cases. | [Independent receipt](../evidence/stage-a-audit.json) |
| Generated qualifiers | V8 failed a fixed absolute comparator; fresh exploratory attempt stopped before its worker on watchdog pins. Neither qualifies Stage B. | [v8 comparator](../evidence/selector-v8-comparator.json), [fresh stop](../evidence/fresh-attempt-summary.json) |

## External dependencies and reproduction

The [evidence manifest](../evidence/MANIFEST.json) records file byte hashes and original research-record names. The original October 26 ledger SHA-256 is `7d6cbb9795f4479e7403bc7c872cfc19297fa720a171e268a6689d8c09e14313`; its reconciliation is a saved-record audit, not a model replay. Original frozen protocols, runner sources, token manifests, ledgers, audit outputs and full tensors/activation evidence are not all included. An auditor without them can check internal consistency of included records and identify assumptions, but cannot independently reproduce every result.

The full depth record SHA-256 is `78110b2391ae49ebdb3fc9c0814965048b616a6579432941c880b3b9af06f9c4`; omitted here because it includes fitted mean vectors. The complete Stage A evidence archive SHA-256 is `a74e8c4223af5a5821906e13244a65de606fc4c129f7001c1de82f42006ba747` and includes public-model weight slices; it is not bundled. The final fresh-selector partial evidence ZIP is `c358e35f38fc671d36d3ba16dd8702851dca120b760cd1ad197cd09bd9a98754`. Its archived watchdog failure is an instrument error, not a result of the intended fresh fixtures.

The prior exact receiver export, original ledgers and other external artifacts should be obtained through their authorized owner and verified by hash. No unrun split becomes fresh merely because it was not evaluated by one branch. Model files, tokenizer files, raw input material and original environments are external dependencies; licensing, independent data status and resource permission must be checked before use. `python3 scripts/check_evidence.py` is an offline hash check of only the files included here; it is not a model reproduction.
