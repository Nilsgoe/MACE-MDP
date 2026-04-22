# Code Availability

MACE-MDP is available from:

https://github.com/Nilsgoe/MACE-MDP

The repository contains the trained model `models/MACE-MDP.model`, tutorial
notebooks, example input structures, and a minimal CPU smoke test in
`reproducibility/`.

MACE-MDP was trained on the SPICE-alpha dataset:

https://zenodo.org/records/19205036

The same dataset record also includes the IR-R-7193 and R-3B69 test sets.

MACE-MDP is distributed under the Academic Software License v1.0 (ASL). The ASL
permits academic non-commercial use. Commercial use is outside the scope of the
ASL and requires a separate commercial license from the original licensor.

For replication or verification, run:

```bash
pip install .
python reproducibility/run_minimal_inference.py
```

The package metadata and `reproducibility/requirements.txt` use the same pinned
dependencies.

The smoke test loads `models/MACE-MDP.model` and
`examples/mini_database_IR-R-7193_wB97MD3.xyz`, computes dipole and
polarizability predictions for the first structure on CPU, prints the outputs,
and writes no files.
