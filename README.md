# SOEN 6011 Delivery 3 - F3: Hyperbolic Sine Calculator

**Student:** Arvind Lakshmanan  
**Student ID:** 40310757  
**Function:** F3 - `sinh(x)`  
**Semantic version:** `1.1.0`

## D3 implementation

D3 keeps the D2 from-scratch Maclaurin calculation and the supported range
`-20 <= x <= 20`. It improves the implementation for code quality, usability,
accessibility, debugging, static analysis, semantic versioning, and unit tests.

### Main D3 changes

- PEP-8-oriented formatting, naming, docstrings, and separation of GUI helpers.
- Semantic version `1.1.0` displayed in the source and GUI.
- Keyboard alternatives: Enter or Alt+C to calculate, Alt+L to clear, Escape
  to exit, plus ordinary Tab navigation.
- Visible instructions and textual status/error feedback; the interface does
  not depend on color alone.
- Read-only result area, sensible initial focus, resizable window, and concise
  labels.
- PyUnit (`unittest`) test suite with 16 tests.
- `pdb` debugging demonstration.
- Commands prepared for Flake8 and Pylint evidence.

## Run the application

```bash
python D3_F3_sinh_gui.py
```

## Run unit tests

```bash
python -m unittest -v test_D3_F3_sinh_gui.py
```

Expected result: `Ran 16 tests ... OK`.

## Required quality-tool evidence

Install the tools if necessary:

```bash
python -m pip install flake8 pylint
```

Run Flake8:

```bash
python -m flake8 D3_F3_sinh_gui.py test_D3_F3_sinh_gui.py
```

A clean Flake8 run normally prints no violations. Capture a screenshot that
shows the command and the terminal prompt returning.

Run Pylint:

```bash
python -m pylint D3_F3_sinh_gui.py
```