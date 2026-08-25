#!/usr/bin/env python3
"""
generate_summary_stats.py
Reproduce key summary statistics from EarthVision-LM data files.
Run: python scripts/generate_summary_stats.py
"""

import csv
import os
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_csv(rel_path):
    path = os.path.join(DATA_DIR, rel_path)
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

print("=" * 65)
print("EarthVision-LM — Summary Statistics Generator")
print("=" * 65)

# ── Corpus A breakdown ────────────────────────────────────────
print("\n📊 CORPUS A (97 primary papers) — by category")
papers = load_csv('corpus_csv/corpus_A_97_primary_papers.csv')
cats = Counter(p['category'] for p in papers)
for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"   {cat:<30s}: {n:3d} papers")
print(f"   {'TOTAL':<30s}: {sum(cats.values()):3d} papers")

# ── Year distribution ─────────────────────────────────────────
print("\n📅 CORPUS A — by year")
years = Counter(p['year'] for p in papers)
for y in sorted(years):
    print(f"   {y}: {years[y]:3d} papers")

# ── Modality distribution ─────────────────────────────────────
print("\n📡 MODALITY DISTRIBUTION (Corpus A papers)")
modalities = Counter(p['modality'] for p in papers)
for mod, n in sorted(modalities.items(), key=lambda x: -x[1]):
    print(f"   {mod:<30s}: {n:3d} papers")

# ── Model registry ────────────────────────────────────────────
print("\n🤖 ARCHITECTURE REGISTRY (26 RS-MLLMs)")
models = load_csv('model_registry/model_registry_26_architectures.csv')
print(f"   Total architectures: {len(models)}")
obb = [m for m in models if m.get('has_obb', '').lower() in ('yes','true','1')]
general_obb = [m for m in models if m.get('obb_type','').lower() == 'general conversational']
optical_only = [m for m in models if m.get('modality_scope','').lower() == 'optical']
print(f"   Optical-only:        {len(optical_only)}/26 = {len(optical_only)/26:.1%}")
print(f"   Any OBB:             {len(obb)}/26")
print(f"   General conv. OBB:   {len(general_obb)}/26")

# ── Encoder distribution ──────────────────────────────────────
print("\n🔍 ENCODER DISTRIBUTION (Corpus B)")
encoders = Counter(m.get('encoder','').split('(')[0].strip() for m in models)
for enc, n in sorted(encoders.items(), key=lambda x: -x[1]):
    if enc:
        print(f"   {enc:<35s}: {n}")

# ── LLM backbone distribution ─────────────────────────────────
print("\n🧠 LLM BACKBONE DISTRIBUTION (Corpus B)")
llms = Counter(m.get('llm_backbone','') for m in models)
for llm, n in sorted(llms.items(), key=lambda x: -x[1]):
    if llm:
        print(f"   {llm:<30s}: {n}")

# ── Quality assessment ────────────────────────────────────────
print("\n✅ QUALITY ASSESSMENT (97 papers)")
qa = load_csv('quality_assessment/quality_assessment_97_papers.csv')
tiers = Counter(p.get('quality_tier','') for p in qa)
print(f"   High  (≥75%): {tiers.get('High',0):3d} papers ({tiers.get('High',0)/len(qa):.1%})")
print(f"   Medium(50-74%): {tiers.get('Medium',0):3d} papers ({tiers.get('Medium',0)/len(qa):.1%})")
print(f"   Low   (<50%):   {tiers.get('Low',0):3d} papers ({tiers.get('Low',0)/len(qa):.1%})")

# ── PRISMA flow verification ──────────────────────────────────
print("\n🔄 PRISMA FLOW VERIFICATION")
prisma = load_csv('prisma_flow/prisma_flow_data.csv')
flow = {r['stage']: r['count'] for r in prisma if r['count'].isdigit()}
print(f"   Database records identified: {flow.get('Identification — Database TOTAL', 'N/A')}")
print(f"   After dedup:                 {flow.get('Unique database records after dedup', 'N/A')}")
print(f"   Passing screening:           {flow.get('Records passing to full-text', 'N/A')}")
print(f"   DB-eligible:                 {flow.get('Database-eligible records', 'N/A')}")
print(f"   Snowball new records:        {flow.get('Snowball — New records passing eligibility', 'N/A')}")
print(f"   Total eligible pool:         {flow.get('Total eligible pool', 'N/A')}")
print(f"   Full reference corpus:       {flow.get('Full reference corpus', 'N/A')}")
print(f"   Primary RS-MLLM (Corpus A):  {flow.get('Primary RS-MLLM synthesis corpus (Corpus A)', 'N/A')}")
print(f"   Contextual supporting:       {flow.get('Contextual supporting literature', 'N/A')}")

print("\n" + "=" * 65)
print("✅ Summary statistics generated from data files")
print("=" * 65)
