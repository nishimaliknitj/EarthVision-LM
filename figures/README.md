# Figures

All figures in the EarthVision-LM paper are generated from LaTeX/TikZ source code embedded in the section files.

## Figure List

| Figure | Section File | Description |
|--------|-------------|-------------|
| Fig. 1 | sec1_introduction.tex | Motivation: RS-MLLM gap overview |
| Fig. 2 | sec2_background.tex | Five-dimensional design space schematic |
| Fig. 3 | sec2_background.tex | **PRISMA 2020 dual-source flow diagram** |
| Fig. 4 | sec2_background.tex | Coding schema overview |
| Fig. 5 | sec3_taxonomy.tex | HBB vs OBB illustration (nadir-view problem) |
| Fig. 6 | sec3_taxonomy.tex | RS-MLLM architecture overview (encoder→connector→LLM) |
| Fig. 7 | sec3_taxonomy.tex | Connector type comparison |
| Fig. 8 | sec3_taxonomy.tex | **Spatial output capability ladder** (Level 0–5; OBB at Level 3) |
| Fig. 9–21 | sec3–sec6 | Architecture taxonomy, backbone distribution, PEFT methods |
| Fig. 22 | sec7_hallucination.tex | **Three-type hallucination taxonomy visual** |
| Fig. 23 | sec7_hallucination.tex | Hallucination triggers by task |
| Fig. 24 | sec8_datasets.tex | **Publication trend (97 RS-MLLM-specific papers 2022–2026)** |
| Fig. 25 | sec8_datasets.tex | Corpus A category breakdown |
| Fig. 26 | sec5_multimodal.tex | **Modality distribution pie + bar (Optical 84.6%; SAR 11.9%; HSI 2.9%)** |
| Fig. 27 | sec8_datasets.tex | Venue distribution |
| Fig. 28 | sec8_datasets.tex | Preprint sensitivity analysis |
| Fig. 29 | sec9_future.tex | Eight research directions roadmap |
| Fig. 30 | sec9_future.tex | Spatiotemporal reasoning gap |

## Data Files for Figures

Numerical data underlying key figures is available in `../data/figure_data/`:

- `fig_publication_trend_data.csv` — Fig. 24 data
- `fig_modality_distribution_data.csv` — Fig. 26 data  
- `fig_venue_distribution_data.csv` — Fig. 27 data

## Reproducing Figures

All figures are TikZ-generated. To reproduce:
```bash
cd ../latex/
pdflatex earthvision_main.tex
```
Individual figures can be extracted from the compiled PDF using tools like `pdfcrop`.
