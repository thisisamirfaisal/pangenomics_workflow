# Bacterial Pangenome Analysis Workflow

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a complete workflow for bacterial pangenome analysis using three popular tools: **Panaroo**, **anvi'o**, and **Roary**. It includes installation instructions, example scripts, troubleshooting tips, and guidance on result interpretation.

## Features
- Step‑by‑step commands for Panaroo, anvi'o, and Roary.
- Conda environment with all dependencies.
- Test dataset instructions to verify the workflow.
- Detailed troubleshooting for common errors (anvi’o COG mismatch, pyANI matplotlib issue, etc.).
- Interpretation guide for Cytoscape and anvi’o visualizations.

## Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pangenome-workflow.git
   cd pangenome-workflow
2. **Create the Conda envirnment
   ```bash
   conda env create -f environment.yml
   conda activate pangenome
3. **Run a test with provided example data (see test_data/README.md)
4. Explore the scripts in the scripts/ folder and adapt them to your own data.
