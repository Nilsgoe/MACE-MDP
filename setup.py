from setuptools import setup


setup(
    name="mace-mdp",
    version="0.1.0",
    description=(
        "Trained MACE-MDP model and examples for molecular dipole moments "
        "and polarizabilities."
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Nils Gonnheimer, Karsten Reuter, Venkat Kapil, Johannes T. Margraf",
    url="https://github.com/Nilsgoe/MACE-MDP",
    py_modules=[],
    install_requires=[
        "ase==3.28.0",
        "mace-torch==0.3.15",
        "numpy==2.4.4",
        "torch==2.9.0",
    ],
    python_requires=">=3.10",
    license="Academic Software License v1.0",
)
