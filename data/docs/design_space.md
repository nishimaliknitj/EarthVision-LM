# Five-Dimensional RS-MLLM Design Space

## Overview

EarthVision-LM proposes a **five-dimensional design space** (𝒟) for RS-MLLMs:

```
𝒟 = {E, K, L, M, S}
```

| Dimension | Symbol | Description |
|-----------|--------|-------------|
| Vision Encoder Adaptation | **E** | How the visual backbone is adapted for RS domain |
| Connector Design | **K** | How visual features are projected into the LLM token space |
| LLM Backbone Strategy | **L** | Which LLM is used and how it is fine-tuned |
| Sensor Modality Scope | **M** | Which sensor modalities the model supports |
| Spatial Output Capability | **S** | Level of spatial precision in model outputs |

---

## Dimension E — Vision Encoder Adaptation

| Level | Name | Description | Examples |
|-------|------|-------------|---------|
| E0 | Frozen CLIP | Off-the-shelf CLIP-ViT; no RS adaptation | Early RS-MLLMs |
| E1 | RS-Finetuned CLIP | CLIP fine-tuned on RS data (contrastive) | GeoRS-CLIP; SkyCLIP |
| E2 | RS-Pretrained ViT | ViT pretrained on RS data from scratch | SkySenseGPT |
| E3 | Large-scale RS ViT | Large RS FM encoder (InternViT-6B; EVA-CLIP) | EarthGPT-X; EarthGPT |
| E4 | Modality-specific | SAR-adapted or HSI-adapted encoder | SAR-VLM; HyperSIGMA |
| E5 | Foundation model | SAM/SAM2 encoder adapted for RS | GeoPixel; SegEarth; GeoSAM |

**Key finding:** 22/26 architectures use E0–E2 (CLIP-based); no architecture uses physics-informed spectral encoding (the root of Type III hallucination).

---

## Dimension K — Connector Design

| Type | Description | Models |
|------|-------------|--------|
| Linear projector | Single linear layer visual→text | Early LLaVA-style |
| MLP projector | 2-layer MLP (dominant) | GeoChat; Earth-OneVision; GeoGround |
| Q-Former | Cross-attention query transformer | BLIP-2-based RS models |
| Cross-attention | Dedicated cross-attention module | UHR-BAT |
| Adapter | Lightweight adapter modules | GeoSAM; RS-SAM |

**Key finding:** MLP connector dominates (18/26). Q-Former largely displaced by MLP for efficiency.

---

## Dimension L — LLM Backbone Strategy

| Strategy | Description | Models |
|----------|-------------|--------|
| Full fine-tune (7B) | All LLM weights updated | Most RS-MLLMs |
| LoRA/QLoRA | Low-rank adaptation | SM²-LF; PEFT-heavy models |
| Instruction tuning only | Freeze LLM; tune connector | Retrieval models |
| Larger LLM (13B–20B) | Scaled backbone | OmniEarth-v2 (20B); UHR-BAT (13B) |
| Code LLM | Code-generating backbone | GeoCodeGPT |

**LLM distribution in Corpus B:**
- Vicuna-7B: 3 models
- LLaMA-2-7B: 5 models
- LLaMA-3-8B: 4 models
- InternLM2-7B: 4 models
- Qwen2-7B: 2 models
- Mistral-7B: 2 models
- Other: 6 models

---

## Dimension M — Sensor Modality Scope

| Scope | Count | Percentage | Models |
|-------|-------|------------|--------|
| Optical-only | 22 | **84.6%** | GeoChat; GeoGround; most |
| SAR input | 3 | 11.5% | EarthGPT; EarthGPT-X; SAR-VLM |
| HSI input | 2 | 7.7% | EarthGPT-X; HyperSIGMA |
| MSI input | 3 | 11.5% | Earth-OneVision; SatMAE; CROMA |
| Cross-sensor OBB | **0** | **0.0%** | **THE CRITICAL GAP** |

---

## Dimension S — Spatial Output Capability Ladder

| Level | Name | Description | Models (Corpus B) |
|-------|------|-------------|-------------------|
| 0 | Retrieval | Image-text retrieval; no localization | GeoRS-CLIP; SkyCLIP |
| 1 | Caption | Image-level description | RSChat; ChangeAgent; LHRSBot |
| 2 | HBB | Horizontal bounding box output | UHR-BAT; Earth-OneVision; GeoLLaVA |
| 3 | OBB | Oriented bounding box output | **GeoChat** (general conversational); **EarthGPT; GeoGround; EarthGPT-X** (task-constrained) |
| 4 | Segmentation | Pixel-level mask | GeoPixel; GeoPix; SegEarth; SAMRSeg; GeoSAM |
| 5 | Cross-sensor OBB + Seg | OBB + segmentation on SAR/HSI | **UNOCCUPIED** |

**OBB detail:**
- 4/26 models provide any OBB capability
- 1/26 (GeoChat) provides **general conversational OBB** (arbitrary queries)
- 3/26 (EarthGPT; GeoGround; EarthGPT-X) provide **task-constrained OBB** (specific detection mode only)
- All 4 are confined to optical DOTA imagery; none extends to SAR or HSI

---

## Design Gap Summary

| Gap | Dimension | Affected Models | Priority |
|-----|-----------|-----------------|----------|
| Cross-sensor OBB | M + S | 0/26 models | Critical |
| Spectral encoder redesign | E + M | 26/26 | Critical |
| Long-horizon temporal reasoning | S + L | 24/26 | High |
| General conversational OBB | S | 25/26 | High |
| Physics-informed connector | K | 26/26 | High |
| Uncertainty quantification | L | 26/26 | Medium |
| Efficient UHR processing | E + K | 25/26 | Medium |
| Cross-sensor benchmark | — | Field-wide | High |
