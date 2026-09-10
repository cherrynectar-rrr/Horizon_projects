# 2026 Qingdao Agri Data Competition Project Status

Last Updated: 2026-09-10
Status: Active — Bounded Short-Term Project / Phase 2 MVP Analysis

## Current Goal
Build the minimum reproducible egg-price MVP authorized by Horizon Core: historical dataset, loading/cleaning pipeline, basic indicators, time-series chart, simple explainable risk rule and concise documentation.

## Current Stage
Phase 0 exit decision: **GO**. Egg-price topic is authorized for end-to-end delivery through the competition deadline. Phase 2 basic analysis is active while historical coverage continues to expand.

## Completed
- P0.1 Data Heartbeat completed and previously verified on remote.
- Real Qingdao government weekly reports were manually preserved as raw text and parsed with Python.
- `parser.py` v2 extracts report date and the `鸡蛋平均价格为X元` field from real Qingdao official reports; three official reports with different dates were successfully validated.
- `batch_parser.py` can discover multiple raw reports, parse them, collect results, convert them into a pandas DataFrame, drop rows missing required `date` or `price`, sort by date, and write `data/processed/egg_price.csv`.
- `check_history.py` converts dates to datetime, calculates inter-record day gaps, and identifies non-contiguous weekly history.
- The July 2026 continuous sequence has been verified as 2026-07-10 4.75, 2026-07-17 4.92, 2026-07-24 5.15, and 2026-07-31 5.26 yuan per 500 g; the previously pending 2026-07-24 5.15 observation was reconciled against the official Qingdao weekly report.
- `analyze_price.py` calculates valid week-to-week percentage changes only across 7-day intervals, recent four-week average price, recent high/low range, relative price range, recent average weekly change, and a simple explainable trend classification.
- Current verified July analysis output includes: recent four-week average 5.02 yuan/500 g, range 4.75–5.26, relative range 10.16%, three valid weekly changes of approximately +3.58%, +4.67%, +2.14%, continuous upward trend, and recent average weekly change about +3.46%.
- A conservative market notice is generated from the observed trend without assigning unsupported high/medium/low risk thresholds.

## In Progress
- Expand the sparse official history into a longer continuous Qingdao egg-price time series with cited sources.
- Produce a real-data time-series chart using a continuous segment and avoid visually implying continuity across known gaps.
- Refine the simple risk/trend rule only after enough history exists to justify thresholds or baselines.

## Next Milestone
A longer reproducible continuous official egg-price dataset with source traceability, plus a verified real-data trend chart and basic explainable indicators ready for competition documentation.

## Evidence
- Current local project modules include `parser.py`, `batch_parser.py`, `check_history.py`, and `analyze_price.py`.
- Official Qingdao weekly-report observations verified during execution include 2026-01-09 (3.58), 2026-07-10 (4.75), 2026-07-17 (4.92), 2026-07-24 (5.15), and 2026-07-31 (5.26), unit yuan per 500 g.
- Historical evidence commit for the earlier heartbeat remains `da184e3064d6062554d013194c98a5c046dc052e`.

## Blockers
- Historical coverage is still sparse outside the verified July continuous segment; broader trend and risk conclusions are not yet justified.

## Needs Core Decision
No

## Migration Note
Physical workspace migrated on 2026-09-04. This migration does not itself change project execution state.
