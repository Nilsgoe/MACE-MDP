# MACE-MDP: Dipole and Polarizability Models for Organic Systems

[**MACE-MDP**](https://chemrxiv.org/doi/full/10.26434/chemrxiv.15000716/v1) is a machine-learning model for predicting **molecular dipole moments** and **fully anisotropic polarizability tensors** for organic systems. The model is based on an **E(3)-equivariant message-passing neural network architecture (MACE)** and is trained on the **SPICE-α dataset**.

MACE-MDP enables efficient prediction of dielectric response properties that are central to **infrared (IR) and Raman spectroscopy**, electrostatics, and molecular response to external electric fields. When combined with **machine-learning interatomic potentials (MLIPs)**, the model allows **rapid, first-principles–accurate vibrational spectroscopy calculations** across molecules, clusters, and condensed-phase systems.

MACE-MDP provides trained MACE models and ready-to-run tutorials for:

- Dipole ($e\ \text{Å}$) | Polarizability ($e\ \text{Å}^2/\text{V}$)
- IR spectra
- Raman spectra


---

## What you need to use MACE-MDP

This repository already contains everything required for inference and tutorial use:

- model file: `models/MACE-MDP.model`
- tutorials and scripts: `examples/`
- example structure set: `examples/mini_database_IR-R-7193_wB97MD3.xyz`

---

## Installation

Install **MACE** and its dependencies using **pip**.

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install torch mace-torch
```
Better: clone the [MACE repository](https://github.com/ACEsuit/mace) and follow the installation instructions there.

---

## Tutorials

The repository includes example notebooks demonstrating how to use MACE-MDP:

* `examples/IR/IR_tutorial.ipynb`
* `examples/Raman/Raman_tutorial.ipynb`
* `examples/Dipole_Polarizability/Dipoles_Polarizability_tutorial.ipynb`

These tutorials are configured to use:

* XYZ file: `examples/mini_database_IR-R-7193_wB97MD3.xyz`
* model path: `models/MACE-MDP.model`

---

## Repository layout

* `models/` – trained MACE-MDP model(s)
* `examples/` – notebooks, scripts, and example inputs

---

## Citation

If you use MACE-MDP in your research, please cite:

Gönnheimer, N.; Reuter, K.; Kapil, V.; Margraf, J. T.
**MACE-MDP: A Foundation Model for Molecular Dipole Moments and Polarizabilities.**
ChemRxiv (2025).
[https://chemrxiv.org/doi/full/10.26434/chemrxiv.15000716/v1](https://chemrxiv.org/doi/full/10.26434/chemrxiv.15000716/v1)

---

## License

Copyright [MACE-MDP] is © 2026, [Nils Gönnheimer] 

MACE-MDP is distributed under the **Academic Software License v1.0 (ASL)**.

See `LICENSE.md` for details.

