# SOEN 6011 D2 - F3: Hyperbolic Sine Calculator

**Student:** Arvind Lakshmanan  
**Student ID:** 40310757  
**Course:** SOEN 6011 - Software Engineering Processes  
**Function:** F3 - `sinh(x)`

## What this project contains

This D2 implementation modifies the D1 textual calculator into a Tkinter GUI calculator and implements `sinh(x)` from scratch in Python.

The function is calculated using the Maclaurin series:

`sinh(x) = x + x^3/3! + x^5/5! + ...`

The mathematical implementation does not use `math.sinh`, `math.exp`, or any Python math-library function. Tkinter is used only for the graphical user interface.

## Supported input

- One finite real number `x`
- Supported D2 range: `-20 <= x <= 20`
- Examples: `0`, `1`, `-2.5`, `3e-2`

Inputs outside this range, blank inputs, non-numeric inputs, NaN, and infinity are rejected with helpful error messages.

## How to run

From the project folder, run:

```bash
python3 D2_F3_sinh_gui.py
```

On Windows, the command may be:

```bash
python D2_F3_sinh_gui.py
```

## Main files

- `D2_F3_sinh_gui.py` - Tkinter GUI and from-scratch calculation.
- `Arvind_Lakshmanan_40310757_D2_Report.pdf` - D2 written answers for Problems 5, 6, and 7.
- `Arvind_Lakshmanan_40310757_D2_Report.tex` - LaTeX source for the report.
- `Arvind_Lakshmanan_40310757_D2_Slides.pdf` - D2 presentation slides.
- `Arvind_Lakshmanan_40310757_D2_Slides.tex` - Beamer source for the slides.
- `commit_messages.md` - High-quality commit message examples.

## Example outputs

| Input | Expected approximate output |
|---:|---:|
| `0` | `0` |
| `1` | `1.1752011936438` |
| `-1` | `-1.1752011936438` |
| `3` | `10.0178749274099` |