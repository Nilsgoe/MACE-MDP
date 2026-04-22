# Reproducibility Smoke Test

This directory contains a small CPU inference check for the bundled MACE-MDP
model and example structure.

## Environment setup

From the repository root:

```bash
pip install .
```

This installs the same pinned dependencies listed in `reproducibility/requirements.txt`.

## Run the smoke test

From the repository root:

```bash
python reproducibility/run_minimal_inference.py
```

The script prints the number of atoms, one dipole vector, and one
polarizability tensor. It writes no files.
