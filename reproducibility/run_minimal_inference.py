"""Small CPU inference check for the bundled MACE-MDP model."""

from __future__ import annotations

import os
import sys
import tempfile
import warnings
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "mace-mdp-mpl"))
os.environ.setdefault("TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD", "1")
for entry in os.environ.pop("PYTHONPATH", "").split(os.pathsep):
    if entry:
        try:
            sys.path.remove(entry)
        except ValueError:
            pass
warnings.filterwarnings(
    "ignore",
    message="Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected.*",
    category=UserWarning,
)

import numpy as np
from ase.io import read
from mace.calculators.mace import MACECalculator


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    xyz_path = repo_root / "examples" / "mini_database_IR-R-7193_wB97MD3.xyz"
    model_path = repo_root / "models" / "MACE-MDP.model"

    for path in (xyz_path, model_path):
        if not path.exists():
            print(f"Missing required file: {path}", file=sys.stderr)
            return 1

    atoms = read(xyz_path, index=0)
    calc = MACECalculator(
        model_paths=str(model_path),
        model_type="DipolePolarizabilityMACE",
        default_dtype="float64",
        device="cpu",
    )

    dipole = np.asarray(calc.get_property("dipole", atoms))
    polarizability = np.asarray(calc.get_property("polarizability", atoms))

    if not np.all(np.isfinite(dipole)) or not np.all(np.isfinite(polarizability)):
        print("Inference produced non-finite values.", file=sys.stderr)
        return 1

    np.set_printoptions(precision=10, suppress=False)
    print("MACE-MDP smoke test")
    print(f"Atoms: {len(atoms)}")
    print("Dipole:")
    print(dipole)
    print("Polarizability:")
    print(polarizability)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
