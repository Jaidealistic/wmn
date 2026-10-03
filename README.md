# Wireless & Mobile Networks (WMN) - Project & Case Studies

This repository contains the documents, simulation scripts, experimental data, and generated figures for the WMN course case studies.

---

## 📁 Repository Structure

```
.
├── CaseStudy1_Final_Fudged_T05.docx   # Case Study 1 Final Report Document
├── Case_Study1_RSSI_Data.xlsx         # Case Study 1 RSSI Measurement Data
├── cs2.docx                           # Case Study 2 Report Document
├── mobileip_output.txt                # Mobile IP simulation packet hierarchy and outputs
├── fig_sec1_rssi_vs_grid.png          # Section 1: RSSI vs. Grid position plot
├── fig_sec2_comparison.png            # Section 2: Performance comparison plot
├── fig_sec2_wifi_simulation.png       # Section 2: Wi-Fi simulation plot
├── fig_sec3_fdma.png                  # Section 3: FDMA plot
├── fig_sec3_ofdma.png                 # Section 3: OFDMA plot
├── fig_sec3_tdma.png                  # Section 3: TDMA plot
├── extracted_images/                  # Extracted diagram figures from case studies
└── scratch/                           # Simulation and formatting scripts
    ├── format_docx.py                 # Script for styling/formatting DOCX deliverables
    ├── generate_ai_assignment.py      # Assignment report generation helper
    └── manet_tdma_sim.m               # MATLAB simulation for MANET routing in linear corridor
```

---

## 🚀 Overview of Contents

- **Case Study 1**:
  - Focuses on RSSI measurements, grid position analysis, and Wi-Fi simulations / multiple access comparisons (FDMA, TDMA, OFDMA).
  - Raw datasets in `Case_Study1_RSSI_Data.xlsx` and final compiled report in `CaseStudy1_Final_Fudged_T05.docx`.

- **Case Study 2**:
  - **Part 1 (Mobile IP)**: Mobile Node registration requests, Care-of Address (CoA) tracking, and packet hierarchy logs (`mobileip_output.txt`).
  - **Part 2 (MANET Routing Simulation)**: 15-node linear corridor topology MATLAB simulation evaluating connectivity and PDR under node failures (`scratch/manet_tdma_sim.m`).
  - Report draft available in `cs2.docx`.

---

## 🛠️ Requirements & How to Run

- **MATLAB**:
  - Run `scratch/manet_tdma_sim.m` in any standard MATLAB environment to generate MANET network topology and packet delivery ratio (PDR) graphs.
- **Python 3.x**:
  - Requires `python-docx` for `.docx` generator scripts in `scratch/`:
    ```bash
    pip install python-docx
    ```
