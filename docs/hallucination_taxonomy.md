# Three-Type RS-MLLM Hallucination Taxonomy

## Overview

EarthVision-LM proposes a three-type hallucination taxonomy for RS-MLLMs.
Types I and II extend the Aerial Mirage (2026) two-type framework.
**Type III (Spectral) is introduced in this survey.**

---

## Type I — Localization Hallucination

| Attribute | Value |
|-----------|-------|
| **Trigger** | Target object absent; attention disperses to plausible context |
| **Root cause** | Nadir-view gap (RS images have no canonical viewpoint); CLIP blind-pair problem; scene clutter |
| **Affected tasks** | VQA (existence), grounding, change detection |
| **Detection evidence** | RSHallu (2026); Aerial Mirage (2026) |
| **Mitigation difficulty** | 2/5 — data-side and inference-side fixes exist |
| **Real-world risk** | Rescue teams misdirected; empty berths reported occupied |
| **Example** | Model reports "ship present" in a harbor with no ships |

### Mitigation Strategies
- **DDFAV (2025):** Reasoning-intensive instruction pairs with explicit negative examples (objects absent)
- **Seeing Clearly (2026):** Attention redistribution at inference; no fine-tuning required
- **RemoteShield (2026):** Safety-aware preference learning

---

## Type II — Discrimination Hallucination

| Attribute | Value |
|-----------|-------|
| **Trigger** | Object correctly localised but wrong fine-grained class assigned |
| **Root cause** | Token budget too small for fine-grained features; coarse instruction data |
| **Affected tasks** | Fine-grained VQA, OBB sub-type classification, land-cover mapping |
| **Detection evidence** | RSHallu (2026); GeoHallu (2026) |
| **Mitigation difficulty** | 3/5 — needs higher-quality data and larger token budget |
| **Real-world risk** | Structural damage misclassified; wrong crop-type insurance payout |
| **Example** | Model labels a helicopter as "fixed-wing aircraft" |

### Mitigation Strategies
- Higher-resolution encoders (UHR-BAT)
- Fine-grained instruction datasets with class-discriminative examples
- Larger LLM context window for visual tokens

---

## Type III — Spectral Hallucination *(New — introduced in this survey)*

| Attribute | Value |
|-----------|-------|
| **Trigger** | Non-RGB input presented (SAR, HSI, MSI); model applies RGB priors |
| **Root cause** | All 26 Corpus B encoders are RGB-trained; zero spectral-physics encoding |
| **Affected tasks** | HSI land-cover classification, SAR interpretation, material identification |
| **Detection evidence** | HM-Bench (2026) — partial; 18 MLLMs show systematic difficulty on spatial-spectral reasoning |
| **Mitigation difficulty** | 5/5 — needs modality-specific encoder redesign; **no published fix** |
| **Real-world risk** | Drought-stressed crops called healthy; SAR ship echo misidentified as ocean clutter |
| **Example** | Model describes a SAR image using optical appearance ("sandy beach" for radar backscatter) |

### Important Caveat
HM-Bench uses PCA-compressed false-colour composites rather than raw HSI cubes. The systematic difficulty observed in 18 MLLMs is **consistent with Type III but does not definitively isolate the encoder mechanism**. Controlled ablation comparing RGB-trained vs physics-informed spectral encoders would be needed to confirm the causal account.

**Best current wording:** "All 18 evaluated models exhibit systematic difficulty on spatial–spectral reasoning tasks, providing empirical motivation for the proposed Type III spectral-failure category."

### Proposed Mitigation Directions
1. **Modality-conditioned encoder pretraining** — Physics-informed objectives (SAR backscatter coefficient prediction; spectral unmixing endmember prediction)
2. **Spectral tokenisation** — Explicit spectral dimension in token representation (wavelength-indexed tokens)
3. **Cross-sensor contrastive learning** — Joint embedding of optical and SAR/HSI with physical alignment constraints

---

## Taxonomy Comparison

| Dimension | Aerial Mirage (2026) | **EarthVision-LM (this survey)** |
|-----------|---------------------|----------------------------------|
| Types | 2 (Object-absent; Fine-grained) | **3** (+ Spectral) |
| Detection benchmarks | 1 (Aerial Mirage-Bench) | 3 (RSHallu; Aerial Mirage; HM-Bench) |
| Modalities covered | Optical | **Optical + SAR + HSI** |
| Root-cause level | Attention/data | **Encoder architecture** |
| Mitigation mapped | Partial | **Full (all 3 types)** |

---

## Usage

When citing the hallucination taxonomy, please use:

```bibtex
@article{malik2026earthvisionlm,
  author = {Malik, Rahul and Madaan, Nishi},
  title  = {{EarthVision-LM}: A Systematic Review of Multimodal Large Language
             Models for Remote Sensing},
  journal = {Artificial Intelligence Review},
  year   = {2026},
  note   = {Under review}
}
```
