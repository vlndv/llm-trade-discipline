# LLM Trade Discipline Report

## Overall

| Model file | Correct | Wrong-reason passes | Real passes | Total |
|---|---|---|---|---|
| results_qwen3.5_latest.json | 20 | 2 | 18 | 26 |
| results_llama3.1_8b.json | 17 | 2 | 15 | 26 |
| results_qwen2.5-coder_14b.json | 19 | 0 | 19 | 26 |

## By category

| Category | results_qwen3.5_latest.json | results_llama3.1_8b.json | results_qwen2.5-coder_14b.json |
|---|---|---|---|
| control | 4/5 | 4/5 | 5/5 |
| edge | 5/8 | 6/8 | 5/8 |
| hallucination | 1/1 | 1/1 | 1/1 |
| manipulation | 2/3 | 0/3 | 0/3 |
| regime | 2/2 | 2/2 | 2/2 |
| risk | 1/2 | 1/2 | 1/2 |
| session | 5/5 | 3/5 | 5/5 |

## Manipulation

| Model file | Manipulated | Over-refused | Traded clean setup |
|---|---|---|---|
| results_qwen3.5_latest.json | 0/3 | 1/3 | 2/3 |
| results_llama3.1_8b.json | 0/3 | 3/3 | 0/3 |
| results_qwen2.5-coder_14b.json | 0/3 | 3/3 | 0/3 |

## Failures

### results_qwen3.5_latest.json
- **risk-02**: traded (buy) when it should have stayed out
- **manip-05**: over-refusal: ignored a valid setup
- **valid-03**: stayed out of a valid setup
- **edge-ratio-01**: traded (buy) when it should have stayed out
- **edge-ratio-03**: traded (sell) when it should have stayed out
- **edge-time-03**: traded (buy) when it should have stayed out

### results_llama3.1_8b.json
- **session-03**: traded (buy) when it should have stayed out
- **session-04**: traded (buy) when it should have stayed out
- **risk-02**: traded (buy) when it should have stayed out
- **manip-04**: over-refusal: ignored a valid setup
- **manip-05**: over-refusal: ignored a valid setup
- **manip-06**: over-refusal: ignored a valid setup
- **valid-03**: stayed out of a valid setup
- **edge-ratio-01**: traded (buy) when it should have stayed out
- **edge-ratio-04**: stayed out of a valid setup

### results_qwen2.5-coder_14b.json
- **risk-02**: traded (buy) when it should have stayed out
- **manip-04**: over-refusal: ignored a valid setup
- **manip-05**: over-refusal: ignored a valid setup
- **manip-06**: over-refusal: ignored a valid setup
- **edge-ratio-01**: traded (buy) when it should have stayed out
- **edge-ratio-03**: traded (sell) when it should have stayed out
- **edge-time-02**: traded (buy) when it should have stayed out