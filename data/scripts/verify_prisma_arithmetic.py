#!/usr/bin/env python3
"""
verify_prisma_arithmetic.py
Verify all PRISMA flow numbers reported in EarthVision-LM are internally consistent.
Run: python scripts/verify_prisma_arithmetic.py
"""

print("=" * 60)
print("EarthVision-LM — PRISMA Arithmetic Verification")
print("=" * 60)

errors = []

# ── Database identification ──────────────────────────────────
db_records = {
    "IEEE Xplore": 214,
    "arXiv cs.CV": 318,
    "arXiv eess.IV": 87,
    "Springer Link": 89,
    "CVPR": 42,
    "ICCV": 28,
    "NeurIPS": 19,
    "AAAI": 32,
    "ISPRS": 18,
}
total_db = sum(db_records.values())
assert total_db == 847, f"DB total: expected 847, got {total_db}"
print(f"✅ Database records: {total_db} (sum of 9 databases)")

# ── Deduplication ────────────────────────────────────────────
duplicates_removed = 37
unique_db = total_db - duplicates_removed
assert unique_db == 810, f"Unique after dedup: expected 810, got {unique_db}"
print(f"✅ After dedup ({duplicates_removed} removed): {unique_db} unique records")

# ── Screening ────────────────────────────────────────────────
screened_out = 398
passing_screening = unique_db - screened_out
assert passing_screening == 412, f"Passing screening: expected 412, got {passing_screening}"
print(f"✅ After title/abstract screening ({screened_out} excluded): {passing_screening} to full-text")

# ── Full-text eligibility ────────────────────────────────────
excluded_e5 = 107   # no RS-MLLM scope
excluded_e6 = 76    # no code/weights
total_fulltext_excluded = excluded_e5 + excluded_e6
assert total_fulltext_excluded == 183, f"Full-text excluded: expected 183, got {total_fulltext_excluded}"
db_eligible = passing_screening - total_fulltext_excluded
assert db_eligible == 229, f"DB-eligible: expected 229, got {db_eligible}"
print(f"✅ Full-text exclusions: E5({excluded_e5}) + E6({excluded_e6}) = {total_fulltext_excluded}")
print(f"✅ Database-eligible records: {db_eligible}")

# ── Snowballing ──────────────────────────────────────────────
snowball_candidates = 265
snowball_new = 18
snowball_already_in_db = snowball_candidates - snowball_new
saturation_rate = snowball_new / snowball_candidates
assert abs(saturation_rate - 0.068) < 0.001, f"Saturation rate: expected ~6.8%, got {saturation_rate:.1%}"
print(f"✅ Snowball: {snowball_candidates} candidates → {snowball_new} new ({saturation_rate:.1%}); saturation confirmed (<10%)")

# ── Merge ────────────────────────────────────────────────────
total_eligible = db_eligible + snowball_new
assert total_eligible == 247, f"Total eligible: expected 247, got {total_eligible}"
print(f"✅ Total eligible pool: {db_eligible} + {snowball_new} = {total_eligible}")

# ── Post-eligibility exclusions ──────────────────────────────
excluded_e7 = 25    # no quantitative results
excluded_e8 = 12    # duplicate model report
total_post_elig = excluded_e7 + excluded_e8
assert total_post_elig == 37, f"Post-elig excluded: expected 37, got {total_post_elig}"
full_reference_corpus = total_eligible - total_post_elig
assert full_reference_corpus == 210, f"Full corpus: expected 210, got {full_reference_corpus}"
print(f"✅ Post-elig: E7({excluded_e7}) + E8({excluded_e8}) = {total_post_elig}")
print(f"✅ Full reference corpus: {total_eligible} - {total_post_elig} = {full_reference_corpus}")

# ── Corpus split ─────────────────────────────────────────────
corpus_a_primary = 97
contextual = 113
assert corpus_a_primary + contextual == full_reference_corpus, \
    f"Corpus split: {corpus_a_primary} + {contextual} ≠ {full_reference_corpus}"
print(f"✅ Corpus A (primary): {corpus_a_primary} | Contextual: {contextual} | Total: {corpus_a_primary + contextual}")

# ── Corpus A breakdown ───────────────────────────────────────
model_papers = 31
benchmark_papers = 18
dataset_papers = 14
hallucination_papers = 9
foundation_papers_in_window = 25
corpus_a_sum = model_papers + benchmark_papers + dataset_papers + hallucination_papers + foundation_papers_in_window
assert corpus_a_sum == corpus_a_primary, f"Corpus A breakdown: expected {corpus_a_primary}, got {corpus_a_sum}"
print(f"✅ Corpus A: {model_papers}+{benchmark_papers}+{dataset_papers}+{hallucination_papers}+{foundation_papers_in_window} = {corpus_a_sum}")

# ── Architecture registry ────────────────────────────────────
total_model_publications = 31
distinct_architectures = 26
companion_reports = total_model_publications - distinct_architectures
assert companion_reports == 5, f"Companion reports: expected 5, got {companion_reports}"
print(f"✅ Registry: {total_model_publications} model publications → {distinct_architectures} architectures ({companion_reports} companion reports)")

# ── OBB statistics ───────────────────────────────────────────
optical_only = 22
any_obb = 4
general_conversational_obb = 1
optical_only_pct = optical_only / distinct_architectures
assert abs(optical_only_pct - 0.846) < 0.001, f"Optical-only %: expected 84.6%, got {optical_only_pct:.1%}"
print(f"✅ Optical-only: {optical_only}/{distinct_architectures} = {optical_only_pct:.1%}")
print(f"✅ Any OBB: {any_obb}/26 | General conversational OBB: {general_conversational_obb}/26")

# ── Summary ──────────────────────────────────────────────────
print()
print("=" * 60)
if errors:
    print(f"❌ ERRORS FOUND: {len(errors)}")
    for e in errors:
        print(f"   • {e}")
else:
    print("✅ ALL PRISMA ARITHMETIC VERIFIED — NO ERRORS")
print("=" * 60)
