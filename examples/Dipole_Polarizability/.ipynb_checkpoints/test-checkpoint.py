from pathlib import Path
import numpy as np

from ase.io import read
from mace.calculators.mace import MACECalculator



cwd = Path.cwd().resolve()
examples_dir = cwd if cwd.name == "examples" else cwd.parent

xyz_path = examples_dir / "mini_database_IR-R-7193_wB97MD3.xyz"
model_path = examples_dir / ".." / "models" / "MACE-MDP.model"  # requested path

atoms = read(xyz_path,index=":")[0]
print(f"Using structure with {len(atoms)} atoms")
print(f"Model path: {model_path}")


device = "cpu"  # switch to "cuda" if available

calc = MACECalculator(
    model_paths=str(model_path),
    model_type="DipolePolarizabilityMACE",
    default_dtype="float64",
    device=device,
)

mu = calc.get_property("dipole", atoms)
alpha = calc.get_property("polarizability", atoms)

print("Dipole vector:")
print(mu)
print("\nPolarizability tensor:")
print(alpha)

