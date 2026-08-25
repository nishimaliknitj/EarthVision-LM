# EarthVision-LM

## A Systematic Review of Multimodal Large Language Models for Remote Sensing — Architectures, Limitations, and the Road to Geospatial Intelligence

[![Paper](https://img.shields.io/badge/Paper-PDF-red)](paper/EarthVision_LM_SystematicReview.pdf)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![PRISMA](https://img.shields.io/badge/PRISMA-2020_Compliant-green)](data/prisma_flow/)
[![Models](https://img.shields.io/badge/Architectures-26_RS--MLLMs-orange)](data/model_registry/)
[![Papers](https://img.shields.io/badge/Corpus_A-97_Papers-purple)](data/corpus_csv/)

---

**Authors:** Rahul Malik, Nishi Madaan (Corresponding: nishimaliknitj@gmail.com)  
**Affiliation:** Department of Computer Science and Engineering, Galgotias University, Greater Noida, India  
**Target Journal:** Artificial Intelligence Review (Springer)  
**Status:** Under Review

---

## Overview

EarthVision-LM is a PRISMA 2020-compliant systematic review of **Multimodal Large Language Models for Remote Sensing (RS-MLLMs)**. The paper proposes a five-dimensional design space that maps RS domain physics, MLLM architecture, sensor modality, spatial output, and hallucination mechanisms into a unified analytical framework.

### Key Numbers

| Item | Count |
|------|-------|
| Primary RS-MLLM papers (Corpus A) | **97** |
| Contextual supporting references | 113 |
| Total retrieved (PRISMA pool) | 210 |
| RS-MLLM architectures (Corpus B) | **26** |
| Task-comparable models (Corpus C) | 18 |
| Databases searched | 9 |
| Search window | Jan 2022 – Aug 2026 |
| PRISMA inter-rater κ (full-text) | 0.89 |

---

## Four Primary Contributions

1. **Five-Dimensional Design Space** — Vision encoder adaptation × Connector design × LLM backbone strategy × Sensor modality scope × Spatial output capability
2. **Multimodal Coverage Analysis** — 84.6% of RS-MLLMs are optical-only; cross-sensor OBB is entirely absent
3. **Three-Type Hallucination Taxonomy** — Type I (Localization), Type II (Discrimination), Type III (Spectral) — extending prior frameworks with HM-Bench empirical grounding
4. **Structured Quantitative Synthesis** — Publication trends, venue distribution, backbone usage, benchmark coverage across 97 primary papers

---

## Repository Structure

```
EarthVision-LM/
│
├── README.md                          ← This file
├── LICENSE                            ← MIT License
├── CITATION.cff                       ← BibTeX citation
├── CHANGELOG.md                       ← Version history
├── CONTRIBUTING.md                    ← Contribution guide
├── .gitignore
│
├── paper/
│   └── EarthVision_LM_SystematicReview.pdf    ← Full paper PDF (107 pages)
│
├── latex/                             ← Complete LaTeX source
│   ├── earthvision_main.tex           ← Main LaTeX file
│   ├── refs.bib                       ← Bibliography (220 references)
│   ├── sec1_introduction.tex
│   ├── sec2_background.tex            ← PRISMA methodology
│   ├── sec3_taxonomy.tex              ← Five-dimensional design space
│   ├── sec4_tasks.tex                 ← Task coverage analysis
│   ├── sec5_multimodal.tex            ← Modality coverage
│   ├── sec6_peft.tex                  ← Training efficiency (LoRA/PEFT)
│   ├── sec7_hallucination.tex         ← Three-type hallucination taxonomy
│   ├── sec8_datasets.tex              ← Quantitative synthesis
│   ├── sec9_future.tex                ← Research directions
│   ├── sec10_conclusion.tex
│   ├── sn-jnl.cls                     ← Springer journal class
│   └── sn-mathphys-num.bst            ← Bibliography style
│
├── data/
│   ├── corpus_csv/
│   │   └── corpus_A_97_primary_papers.csv     ← All 97 primary papers coded
│   ├── screening_log/
│   │   ├── prisma_screening_log.csv            ← Full PRISMA record log
│   │   └── inclusion_exclusion_coding.csv      ← I/E criteria coding sheet
│   ├── search_strings/
│   │   └── search_strings_all_databases.csv    ← All 9 databases + adapted queries
│   ├── prisma_flow/
│   │   └── prisma_flow_data.csv               ← All PRISMA flow numbers
│   ├── model_registry/
│   │   └── model_registry_26_architectures.csv ← 26 RS-MLLM registry
│   ├── benchmark_matrix/
│   │   └── benchmark_performance_matrix.csv    ← Cross-model benchmark scores
│   ├── figure_data/
│   │   ├── fig_publication_trend_data.csv
│   │   ├── fig_modality_distribution_data.csv
│   │   └── fig_venue_distribution_data.csv
│   └── quality_assessment/
│       └── quality_assessment_97_papers.csv    ← Per-paper QA scores
│
├── figures/
│   └── README.md                      ← Figure descriptions
│
├── docs/
│   ├── methodology.md                 ← Detailed PRISMA methodology
│   ├── design_space.md                ← Five-dimensional design space guide
│   └── hallucination_taxonomy.md      ← Type I/II/III taxonomy guide
│
├── scripts/
│   ├── verify_prisma_arithmetic.py    ← Verify all PRISMA flow numbers
│   └── generate_summary_stats.py      ← Reproduce Table statistics
│
└── .github/
    └── workflows/
        └── latex_compile.yml          ← Auto-compile LaTeX on push
```

---

## Architecture Registry (Corpus B — 26 RS-MLLMs)

| # | Model | Year | Venue | Encoder | Modality | OBB |
|---|-------|------|-------|---------|----------|-----|
| 1 | **GeoChat** | 2024 | CVPR | CLIP-ViT-L/14 | Optical | ✅ General conversational |
| 2 | **EarthGPT** | 2025 | TGRS | EVA-CLIP | Optical+SAR+HSI | ✅ Task-constrained |
| 3 | **EarthGPT-X** | 2026 | arXiv | InternViT-6B | Optical+SAR+HSI | ✅ Task-constrained |
| 4 | **GeoGround** | 2025 | arXiv | CLIP-ViT-L/14 | Optical | ✅ Task-constrained |
| 5 | Earth-OneVision | 2026 | arXiv | InternViT-6B | Optical+SAR+MSI | ❌ |
| 6 | SkySenseGPT | 2024 | arXiv | RS-ViT-L | Optical | ❌ |
| 7 | GeoLLaVA | 2025 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 8 | UHR-BAT | 2025 | arXiv | CLIP+UHR | Optical | ❌ |
| 9 | GeoPixel | 2025 | arXiv | SAM2+CLIP | Optical | ❌ (segmentation) |
| 10 | LHRSBot | 2024 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 11 | LHRSBot-Nova | 2024 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 12 | GeoPix | 2025 | arXiv | EVA-CLIP | Optical | ❌ (segmentation) |
| 13 | TEOChat | 2025 | arXiv | CLIP-ViT-L/14 | Optical (temporal) | ❌ |
| 14 | SegEarth | 2026 | arXiv | SAM2 | Optical | ❌ (segmentation) |
| 15 | SAR-VLM | 2026 | arXiv | CLIP-SAR | SAR | ❌ |
| 16 | GeoRS-CLIP | 2024 | arXiv | CLIP-ViT-L/14 | Optical | ❌ (retrieval) |
| 17 | SkyCLIP | 2024 | arXiv | CLIP-ViT-B/16 | Optical | ❌ (retrieval) |
| 18 | RSChat | 2025 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 19 | GeoCodeGPT | 2025 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 20 | ChangeAgent | 2025 | arXiv | CLIP-ViT-L/14 | Optical (temporal) | ❌ |
| 21 | OmniEarth | 2026 | arXiv | InternViT-6B | Optical+SAR | ❌ |
| 22 | OmniEarth-v2 | 2026 | arXiv | InternViT-6B | Optical+SAR+MSI | ❌ |
| 23 | GeoReasoning | 2026 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 24 | SAMRSeg | 2024 | arXiv | SAM-ViT-H | Optical | ❌ (segmentation) |
| 25 | RLHF-RS | 2025 | arXiv | CLIP-ViT-L/14 | Optical | ❌ |
| 26 | GeoSAM | 2024 | arXiv | SAM-ViT-B/L/H | Optical | ❌ (segmentation) |

**OBB Summary:** 4/26 models support any OBB; 1/26 (GeoChat) provides general conversational OBB; cross-sensor OBB = 0/26.

---

## Three-Type Hallucination Taxonomy

| Type | Name | Root Cause | Detection | Mitigation Difficulty |
|------|------|------------|-----------|----------------------|
| I | **Localization** | Nadir-view gap; CLIP blind-pair | RSHallu; Aerial Mirage | 2/5 — data-side fixes exist |
| II | **Discrimination** | Token budget; coarse instruction data | RSHallu; GeoHallu | 3/5 — needs higher-quality data |
| III | **Spectral** *(new)* | RGB-only encoders; no spectral-physics encoding | HM-Bench (partial) | 5/5 — no published fix |

---

## How to Compile the LaTeX

```bash
cd latex/
pdflatex earthvision_main.tex
bibtex earthvision_main
pdflatex earthvision_main.tex
pdflatex earthvision_main.tex
```

Requires: TeX Live 2023+ or MiKTeX with `tikz`, `booktabs`, `multirow`, `xcolor`, `amsmath`.

---

## Citation

```bibtex
@article{malik2026earthvisionlm,
  author    = {Malik, Rahul and Madaan, Nishi},
  title     = {{EarthVision-LM}: A Systematic Review of Multimodal Large Language Models
               for Remote Sensing---Architectures, Limitations, and the Road to Geospatial Intelligence},
  journal   = {Artificial Intelligence Review},
  year      = {2026},
  note      = {Under review}
}
```

---

## License

MIT License — see [LICENSE](LICENSE).

---

## Contact

Corresponding author: **Nishi Madaan** — nishimaliknitj@gmail.com  
Department of Computer Science and Engineering, Galgotias University, Greater Noida, India
