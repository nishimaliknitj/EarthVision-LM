# EarthVision-LM — PRISMA 2020 Methodology

## Search Strategy

### Databases (9 sources)
| Database | Coverage | Fields | Records |
|----------|----------|--------|---------|
| IEEE Xplore | All IEEE/IET journals + conferences | All Metadata | 214 |
| arXiv cs.CV | Computer vision preprints 2022–2026 | Title + Abstract | 318 |
| arXiv eess.IV | Image/video signal processing preprints | Title + Abstract | 87 |
| Springer Link | Springer Nature journals + chapters | Title + Abstract + Keywords | 89 |
| CVPR 2022–2026 | IEEE/CVF CVPR proceedings | Title + Abstract | 42 |
| ICCV 2023, 2025 | IEEE/CVF ICCV proceedings | Title + Abstract | 28 |
| NeurIPS 2022–2025 | NeurIPS proceedings | Title + Abstract | 19 |
| AAAI 2023–2026 | AAAI proceedings | Title + Abstract | 32 |
| ISPRS 2022–2026 | ISPRS Congress + Annals + JPRS | Title + Abstract + Keywords | 18 |
| **TOTAL** | | | **847** |

### Master Boolean Query (Three-Conjunct Structure)

```
(  "remote sensing"
   OR "earth observation"
   OR "satellite imagery"                    )  ← Conjunct 1: RS domain anchor
AND
(  "multimodal large language model"
   OR "MLLM"
   OR "vision-language model"
   OR "large vision-language model"
   OR "visual question answering"
   OR "VLM"                                  )  ← Conjunct 2: Model type
AND
(  "survey"
   OR "model"
   OR "benchmark"
   OR "detection"
   OR "segmentation"                         )  ← Conjunct 3: Task/study scope
```

**Note:** Outer parentheses on Conjunct 1 are mandatory to prevent AND-before-OR precedence errors in database engines.

### Supplementary Targeted Queries
- `"remote sensing MLLM"`
- `"RS vision language model"`
- `"multimodal LLM remote sensing"`
- `"RS VLM"`

### Update Search (24 August 2026)
Nine targeted queries across arXiv + Semantic Scholar:
- `"RS-MLLM"`, `"RS-VLM"`, `"remote sensing MLLM"`, `"Earth observation VLM"`,
  `"multimodal remote sensing 2026"`, `"spatial reasoning remote sensing"`,
  `"temporal RS video VLM"`, `"SAR VLM"`, `"hyperspectral MLLM"`

---

## PRISMA 2020 Dual-Source Flow

```
Database Pathway                    Snowball Pathway (§S7b)
─────────────────────               ─────────────────────────
847 records identified              265 candidates identified
                                    (forward+backward citation
 -37 duplicates (dedup)              of 412 screened records)
= 810 unique
                                     -247 already in DB path
 -398 off-topic screening           = 18 NEW records passing
= 412 full-text                       eligibility

 -183 full-text excluded            ──────────────────────────
   E5: 107 no RS-MLLM scope
   E6: 76  no code/weights          MERGE: 229 + 18 = 247
= 229 DB-eligible                         total eligible pool

                                     -37 post-eligibility
                                       E7: 25 no quant results
                                       E8: 12 duplicate model
                                   = 210 full reference corpus
                                   
                                   Of 210:
                                     97 = Corpus A (primary)
                                    113 = contextual supporting
```

**Saturation check:** 18/265 = 6.8% new-pass rate → below 10% threshold → no second round needed.

---

## Inclusion/Exclusion Criteria

### Inclusion (all three must be met)
| ID | Criterion |
|----|-----------|
| I1 | Paper processes RS imagery through a language-model interface |
| I2 | Published peer-reviewed OR arXiv preprint with public code/weights |
| I3 | Reports quantitative results on ≥1 standard RS or MLLM benchmark |

### Exclusion
| ID | Stage | Criterion |
|----|-------|-----------|
| E1 | Title/Abs | Off-topic — no RS or EO imagery |
| E2 | Title/Abs | No language model interface |
| E3 | Title/Abs | Not RS modality (ground-level photography) |
| E4 | Pre-screen | Duplicate cross-database record |
| E5 | Full-text | No RS-MLLM scope (RS paper but no LM; goes to contextual) |
| E6 | Full-text | No public code or weights (preprints only) |
| E7 | Post-elig | No quantitative benchmark evaluation |
| E8 | Post-elig | Duplicate model report (companion/extension paper) |

---

## Inter-Rater Reliability

| Stage | Sample | Cohen's κ | Agreement |
|-------|--------|-----------|-----------|
| Title/Abstract screening | 20% random sample (n=162) | 0.83 | Substantial |
| Full-text eligibility | All 412 records | 0.89 | Almost perfect |

---

## Corpus Definitions

| Level | Name | n | Definition |
|-------|------|---|------------|
| Corpus A | Primary RS-MLLM synthesis | 97 | Model + Benchmark + Dataset + Hallucination + Foundation (2022–2026) papers |
| Corpus B | Architecture registry | 26 | Distinct RS-MLLM architectures from 31 model papers |
| Corpus C | Task-comparable subset | 18 | Models with sufficient comparable benchmark data |
| Contextual | Supporting literature | 113 | RS domain + pre-2022 FM papers; cited but not in primary synthesis |

---

## Quality Assessment

Category-specific rubrics applied to all 97 Corpus A papers:

| Category | Papers | Criteria | Mean Score |
|----------|--------|----------|------------|
| Model papers | 31 | M1–M6 (architecture, dataset, eval, baseline, code, limitations) | 4.1/6 |
| Benchmark papers | 18 | B1–B5 (construction, tasks, QC, protocol, access) | 3.6/5 |
| Dataset papers | 14 | D1–D5 (scale, source, annotation, access, docs) | 3.4/5 |
| Hallucination papers | 9 | H1–H5 (task, benchmark, taxonomy, reproducibility, mitigation) | 3.3/5 |
| Foundation models | 25 | M1–M6 (M4 relaxed) | 3.9/6 |

Quality tiers: High ≥75%; Medium 50–74%; Low <50%.
