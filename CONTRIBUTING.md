# Contributing

Thank you for your interest in MACE-MDP. This repository is maintained as a
research software and model release for academic non-commercial use under the
Academic Software License v1.0.

## Reporting issues

Please report problems through the GitHub issue tracker:

https://github.com/Nilsgoe/MACE-MDP/issues

Include:

- the operating system and Python version,
- the installation method for `mace-torch`,
- the command or notebook cell that failed,
- the complete error message,
- whether the minimal smoke test below succeeds.

## Smoke test

Before reporting a reproducibility issue, please try the minimal CPU inference
check from the repository root:

```bash
pip install .
python reproducibility/run_minimal_inference.py
```

The script should load the bundled example structure and `models/MACE-MDP.model`,
print the dipole vector and polarizability tensor, and write no files.
