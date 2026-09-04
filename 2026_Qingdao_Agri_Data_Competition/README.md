# 2026 Qingdao Agri Data Competition Project

Status: **Active — Bounded Short-Term Project / Phase 0 Feasibility**

Owner after handoff: **Project Specialist Thread**

Core decision owner: **Horizon Core**

Target competition: **2026 青岛市农业农村领域数据驱动创新应用竞赛**

Working track: **赛道二 — 农业大数据挖掘分析**

Working title: **青岛蛋鸡行情波动风险提示系统**

Fallback topic if egg-price data is insufficient: **青岛蔬菜价格—上市量波动监测**

---

## 1. Why This Project Exists

This is not a new permanent Horizon main line.

It is a short, deadline-bounded experiment intended to answer three questions:

1. Can the user use current Python foundations to solve a small real-world data problem?
2. Can one competition produce stronger project evidence than another isolated tutorial exercise?
3. Is the project feasible without materially displacing Python foundation completion, Algorithm, academic work, or Embedded exploration?

The project is successful even if the final decision is **SKIP**, provided Phase 0 quickly discovers that the data, problem, or workload is not viable.

---

## 2. Competition Constraints

Source: official competition notice issued by Qingdao Municipal Agriculture and Rural Affairs Bureau on 2026-08-18.

Relevant constraints:

- submission deadline: **2026-09-30**;
- individual or team participation is allowed;
- team size: maximum **3 people**;
- current project targets **Track 2: Agricultural Big Data Mining and Analysis**;
- initial submission may be a **PPT or PDF design work**;
- final-round entrants are evaluated on site and the first author presents/answers questions;
- judging emphasizes theme fit, innovation, overall logic, practical usefulness, replicability, and economic/social/ecological value;
- practical usefulness includes real investigation/needs evidence, feasibility, and user acceptance.

The project must not fabricate agricultural data, field research, user interviews, or impact evidence.

---

## 3. Project in Plain Language

The project is a small **egg-price trend and risk assistant**.

Instead of asking farmers or other users to read many historical price tables manually, the project will try to turn public data into simple answers such as:

- What is the latest observed egg price?
- Is the recent trend mainly rising, falling, or stable?
- Has volatility recently increased?
- Are there unusual changes worth paying attention to?
- Can the result be shown clearly through a simple chart/dashboard?

The first version is **not an AI forecasting system**.

The minimum useful pipeline is:

```text
public data
→ Python reads and cleans it
→ simple statistics
→ trend / change / volatility analysis
→ chart
→ simple risk提示
```

Machine learning or forecasting may be considered only after the basic system works and only if it creates clear additional value.

---

## 4. Scope Guardrails

### Authorized

- public-data collection and verification;
- CSV / spreadsheet data cleaning;
- Python data processing;
- basic statistics and trend analysis;
- charts and simple visualizations;
- simple transparent risk rules;
- a lightweight dashboard if useful;
- limited domain research needed to interpret the data;
- contact with a relevant teacher / agricultural-domain teammate if available;
- competition PPT/PDF preparation after the project itself has evidence.

### Not Authorized During Phase 0–1

- creating a new AI/ML curriculum;
- deep learning merely to make the project sound advanced;
- mobile-app development;
- building a generic "smart agriculture platform";
- inventing user research or field-investigation evidence;
- large-scale web infrastructure;
- unrelated feature expansion;
- allowing this project to silently become the new Horizon main line.

---

## 5. Phase 0 — Feasibility Gate

Timebox: **2–3 focused sessions / no more than 3 days before a GO/SKIP decision.**

Phase 0 must answer data, problem, buildability and domain-support questions before a GO/PIVOT/SKIP decision.

## 6. Phase 1 — Minimum Viable Project

Minimum output:

1. one reproducible dataset;
2. Python script/notebook that loads and cleans the data;
3. basic indicators such as latest value, week-to-week change, recent average, and recent volatility;
4. one clear time-series chart;
5. one simple, explainable trend/risk rule;
6. concise README explaining what the program does and what it does **not** claim.

## 7. Phase 2 — Competition-Useful Version

Possible additions after the MVP works include cleaner visualization, stronger Qingdao context, justified comparisons, feasibility/replication discussion and limitations.

## 8. Phase 3 — Submission

Before 2026-09-30, freeze project evidence, prepare competition PPT/PDF, verify citations/originality and prepare presentation/Q&A if selected.

## 9. Horizon Resource Rule

This project is a **bounded short-term application project**, not a replacement for the current Horizon capability structure.

Python knowledge should be learned just in time from project needs rather than by opening a second Python curriculum.

## 10. First Verifiable Milestone

**Milestone P0.1 — Data heartbeat**

Produce one small, reproducible table of real price observations and one Python-generated line chart from it.

## 11. Thread Ownership

The dedicated Project Specialist Thread may create and maintain this project directory, including `STATUS.md`, data, scripts, notebooks and competition-specific artifacts.

It must not modify `Project_Horizon/00_Project_Control/MASTER_STATUS.md`, another Specialist STATUS, or cross-thread priorities.

Use `Needs Core Decision: Yes` when a material scope/resource conflict requires Core judgment.

---

## Migration Note — 2026-09-04

This project moved from `Project_Horizon/13_Projects/2026_Qingdao_Agri_Data_Competition/` to `Horizon_projects/2026_Qingdao_Agri_Data_Competition/`.

`STATUS.md` is the canonical current-stage record; this README preserves the original project framing and may contain older phase wording until a future meaningful project update justifies editing it.
