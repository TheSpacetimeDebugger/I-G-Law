# 🌌 I-G Law – Information-Gravity Law  
**"Order is the Hidden Gravity"**  
A Python-based simulation exploring an emergent gravity model based on structural information complexity

![Simulation Result](IG%20Simulation.png)  
*(Green: I-G Law – maintains flat rotation curve; Red: Newtonian only – declining)*

## Important Legal & Attribution Notice

**This repository uses publicly available astronomical data from the SPARC database.**  
All rotation curve data, baryonic mass models (e.g., v_disk), and related measurements shown in plots or used in the simulation are derived from:

- Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016).  
  *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*.  
  The Astronomical Journal, 152(6), 157.  
  DOI: https://doi.org/10.3847/0004-6256/152/6/157  
  Public data access: http://astroweb.cwru.edu/SPARC/

**The original SPARC data are used here strictly for non-commercial, educational, and exploratory research purposes.**  
This usage fully complies with the open-science policy of the SPARC team.  
**If you use any data, plots, results, or code derived from this repository in your own work (scientific, educational, or otherwise), you must cite the above SPARC paper** as the source of the underlying astronomical measurements.

**The I-G Law model, the concept of Structural Complexity Factor (ℂ), the simulation logic, the code implementation, and all interpretations and conclusions presented here are the original work of the author (@TheSpacetimeDebugger).**  
This project is a personal proof-of-concept and exploratory toy model. It is **not** a peer-reviewed scientific publication, nor does it constitute an official claim to have solved or replaced established cosmological models (such as ΛCDM or dark matter paradigms).

## Project Description

The I-G Law proposes that gravitational attraction in galaxies includes an emergent component arising from **structural information complexity** (ℂ) within ordered cosmic systems.  
This additional term aims to provide a computational explanation for flat rotation curves at large galactic radii **without** requiring non-baryonic dark matter particles.

### Simplified Core Idea (Conceptual)
F_total ≈ G M m / r² + Ω ⋅ ℂ(r)  

Where:
- ℂ(r) = Structural Complexity Factor (currently implemented as a simple radial scaling proxy for demonstration purposes)
- Ω = universal balance constant (tuned in the simulation)

This is **not** a complete physical theory yet — it is an experimental computational exploration.

### Current Demonstration: NGC 3198
The included plot shows:
- Red points → Observed rotation velocities (from SPARC data)
- Blue dashed line → Pure Newtonian prediction from baryonic matter only
- Green line → I-G Law modified velocity — flat at approximately 155 km/s in the outer regions

This qualitative match illustrates the potential of the complexity-based term to reproduce observed flatness in this simplified case.

## How to Run the Simulation

Requirements:
- Python 3.x
- numpy
- matplotlib

```bash
git clone https://github.com/TheSpacetimeDebugger/I-G-Law.git
cd I-G-Law
pip install numpy matplotlib
python IG_Law_Simulation.py

(Adjust the script name if your main file is named differently.)LicenseMIT License — see the LICENSE file for full details.
(The code is free to use, modify, and share; astronomical data remain governed by their original open-science terms.)DisclaimerThis is an independent, non-peer-reviewed personal project.
No warranty is made regarding scientific accuracy, physical correctness, cosmological validity, or reproducibility in all cases.
Use at your own risk.
Constructive feedback, criticism, suggestions, and collaborative improvements are very welcome via issues or pull requests.Contact & DiscussionX / Twitter: @thesbctd
  
Feel free to open issues or pull requests — let's debug spacetime together! 

Star  if you're interested in alternative ideas in galaxy dynamics and emergent gravity!

