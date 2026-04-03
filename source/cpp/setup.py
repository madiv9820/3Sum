"""
⚙️ Build Script for Cython + C++ Integration

📌 Purpose:
This file is used to compile the Cython wrapper (`solution.pyx`) into a
Python extension module, enabling seamless interaction between Python and C++ code.

🔍 What this file does:
- 🧩 Defines a C++ extension module using setuptools
- 🔄 Compiles `.pyx` (Cython) → `.cpp` → shared object (`.so` / `.pyd`)
- 🔗 Links Cython code with underlying C++ implementation

🧾 Key Features:
- Uses `setuptools` for build configuration
- Uses `cythonize` to handle Cython compilation
- Enables C++ support via `language='c++'`
- Sets Python language level to 3 for compatibility

⚙️ Workflow:
1. Read Cython file (`solution.pyx`) 📄
2. Convert to C++ code via Cython 🔄
3. Compile into a Python extension module ⚙️
4. Generate `.so` (Linux/macOS) or `.pyd` (Windows) file 📦

🚀 Goal:
Allow high-performance C++ logic to be accessed directly from Python
through a compiled extension module.
"""

from setuptools import setup, Extension
from Cython.Build import cythonize

# 🧩 Define extension module configuration
ext = Extension(
    name='solution',              # 📦 Name of the compiled module (import name in Python)
    sources=['solution.pyx'],     # 📄 Source file (Cython file)
    language='c++'                # ⚙️ Enable C++ compilation
)

# 🚀 Setup configuration to build the extension
setup(
    ext_modules=cythonize(
        ext,
        language_level=3          # 🐍 Use Python 3 syntax and semantics
    )
)