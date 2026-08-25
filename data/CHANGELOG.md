# Changelog

All notable changes to this repository are documented here.
Format: [Version] — Date — Description

---

## [v1.0] — 2026-08-25 — Initial Submission Version

### Paper
- Title: "EarthVision-LM: A Systematic Review of Multimodal Large Language Models for Remote Sensing"
- Submitted to: Artificial Intelligence Review (Springer)
- 107 pages; PRISMA 2020 compliant

### Search and Corpus
- Primary database search: 14 August 2026 (9 databases; 847 records)
- Update search: 24 August 2026 (targeted; 31 candidates; 3 post-cutoff works noted)
- Corpus A: 97 primary RS-MLLM papers
- Contextual supporting literature: 113 papers
- Architecture registry (Corpus B): 26 RS-MLLMs

### Key Fixes in this Version (v1.0)
- RF1: 85.2% → 84.6% (22/26 optical-only architectures; correct arithmetic)
- RF2: Fig. 8 OBB Level 3 corrected: 4/26 any OBB; 1/26 general conversational
- RF3: PRISMA flow rebuilt with proper dual-source PRISMA 2020 §S7b accounting (229 DB + 18 snowball = 247 eligible; 247-37=210)
- RF4: Corpus A redefined as 97 primary (not 210); 113 = contextual supporting
- RF5: Boolean query parentheses fixed (3-conjunct structure explicit)
- RF6: Literature updated to 24 August 2026; LongEarth-R1; RSVideo; IGARSS 2026 noted
- RF7: Zenodo repository — placeholder pending acceptance
- RF8: Reference audit; [Preprint] labels removed; LLaVA-1.5/MiniGPT-4/SAM/POPE/InternVL published entries updated
- RF9: Placeholder DOI (XXXXX) replaced with actual DOI 10.1038/s41598-026-63018-9
- RF11: Hallucination frequency (55%/30%/15%) removed — heterogeneous denominators
- RF12: "All 18 show spectral hallucination" softened to "empirical motivation for Type III"
- RF13: "One new model per week" removed
- RF14: "<5% coverage bias" unsupported claim removed
- RF15: 31→26 explanation standardised to one consistent sentence
- RF16: Category-specific QA rubric (M1-M6 / B1-B5 / D1-D5 / H1-H5)
- Title updated: "Survey" → "Systematic Review"
- LLM use disclosure added per AIR guidelines
- Authors corrected: Rahul Malik + Nishi Madaan (corresponding)

### Data Files Added
- data/corpus_csv/corpus_A_97_primary_papers.csv
- data/screening_log/prisma_screening_log.csv
- data/screening_log/inclusion_exclusion_coding.csv
- data/search_strings/search_strings_all_databases.csv
- data/prisma_flow/prisma_flow_data.csv
- data/model_registry/model_registry_26_architectures.csv
- data/benchmark_matrix/benchmark_performance_matrix.csv
- data/figure_data/ (publication trend; modality distribution; venue distribution)
- data/quality_assessment/quality_assessment_97_papers.csv

---

## [Planned — v1.1] — Post-Acceptance

- Zenodo DOI assignment and data archival
- Final published PDF with journal page numbers
- Any reviewer-requested corpus updates
