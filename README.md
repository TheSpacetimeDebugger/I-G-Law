# I-G Law – Information-Gravity Law  
**"Order is the Hidden Gravity"**  
A computational exploration of an emergent gravity model based on structural information complexity

## Important Legal & Attribution Notice

**This repository uses publicly available astronomical data from the SPARC database.**  
All rotation curve data, baryonic mass models, and related measurements shown in plots or used in simulations are derived from:

- Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016).  
  *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*  
  The Astronomical Journal, 152(6), 157.  
  DOI: https://doi.org/10.3847/0004-6256/152/6/157  
  Public data access: http://astroweb.cwru.edu/SPARC/

**The original SPARC data are used here strictly for non-commercial, educational, and research exploration purposes.**  
This work strictly adheres to the open-science usage policy of the SPARC team.  
If you use any data or plots derived from this repository in your own work, **you must cite the above SPARC paper** as the source of the underlying astronomical measurements.

**The I-G Law model, the mathematical formulation, the complexity factor (ℂ), the simulation logic, and all interpretations presented here are original work of the author (@TheSpacetimeDebugger) and do not represent any official scientific claim or peer-reviewed publication (yet).**  
This is a personal proof-of-concept project and should be treated as exploratory / theoretical speculation until further validation.

## Project Description

This repository contains a simple Python simulation demonstrating a conceptual modification to Newtonian gravity:  
adding an emergent term based on **structural information complexity** (ℂ) to help explain flat rotation curves in disk galaxies **without** invoking non-baryonic dark matter particles.

### Core Idea (very simplified)
F_total ≈ G M m / r² + Ω ⋅ ℂ(r)  

Where ℂ(r) is a proxy for the "information/structural order" in the mass distribution (currently implemented via a simple radial scaling function for demonstration).

### Current Status – NGC 3198 Demonstration
The included plot shows:
- Red points → observed rotation curve (from SPARC)
- Blue dashed → pure Newtonian prediction from baryons (disk + gas)
- Green line → I-G modified curve (flat at ~155 km/s in the outer regions)

This is **not** a claim that dark matter does not exist, nor a replacement for ΛCDM cosmology.  
It is an experimental toy model to explore whether information-theoretic or complexity-based corrections could mimic some dark-matter-like effects on galactic scales.

## Usage & Requirements

```bash
git clone https://github.com/TheSpacetimeDebugger/I-G-Law.git
cd I-G-Law
pip install -r requirements.txt
python simulation.py   # or whatever your main script name is
