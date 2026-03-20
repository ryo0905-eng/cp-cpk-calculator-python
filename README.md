# Cp / Cpk Calculator

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Tool-blue)](https://tools.ryo-aihub.com/)
[![GitHub stars](https://img.shields.io/github/stars/ryo0905-eng/cp-cpk-calculator-python?style=social)](https://github.com/ryo0905-eng/cp-cpk-calculator-python)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple Flask web app for process capability analysis.

This tool lets you upload measurement data from a CSV file, enter `USL` and `LSL`, and instantly calculate:

- `Cp`
- `CPU`
- `CPL`
- `Cpk`

It also shows a histogram, capability interpretation, sample datasets, and practical next-step guidance for manufacturing and quality teams.

👉 **Live demo:** [tools.ryo-aihub.com](https://tools.ryo-aihub.com/)

![Cp / Cpk Calculator screenshot](tool%20screenshot.png)

## Why This Project

Process capability checks are often done in spreadsheets, which makes quick reviews harder than they need to be.

This app gives you a lightweight browser-based workflow for:

- checking whether a process is capable
- seeing whether the process is off-center
- comparing sample scenarios before using real data
- reviewing results in a way that is easier to explain to teammates

If you just want to answer "Is this process actually healthy?" without building an Excel sheet first, this tool is for you.

## What This Tool Is For

This project is designed for people who want to quickly check whether a process is capable and whether it is centered within specification limits.

- `Cp` tells you how much process spread fits inside the spec width.
- `Cpk` tells you how capable the process actually is after considering centering.

A process can have a high `Cp` but still a poor `Cpk` if the mean is shifted toward one limit. That is why `Cpk` is often the more practical number when reviewing process risk.

## Features

- Upload a CSV file and use the first column as measurement data
- Use built-in sample datasets for quick testing
- Calculate `Cp`, `CPU`, `CPL`, and `Cpk`
- Visualize the distribution with spec limits and mean
- Get a plain-language capability interpretation
- Review recommended next checks based on the result
- Run everything locally with Python and Flask

## At A Glance

- Input: sample data or your own CSV
- Required values: `USL` and `LSL`
- Output: capability metrics, histogram, interpretation, and suggested next checks
- Best for: manufacturing, quality, process engineering, and teaching basic capability analysis

## How To Use

1. Open the [live tool](https://tools.ryo-aihub.com/) or run the app locally.
2. Choose sample data or upload a CSV file.
3. Enter `USL` and `LSL`.
4. Click `Calculate capability`.
5. Review the metrics, chart, and interpretation.

### CSV Format

The app reads the **first column** of the CSV as numeric measurement values.

Example:

```csv
value
9.8
10.1
9.9
10.0
10.2
```

## Formula Reference

```text
Cp  = (USL - LSL) / (6 x sigma)
CPU = (USL - Mean) / (3 x sigma)
CPL = (Mean - LSL) / (3 x sigma)
Cpk = min(CPU, CPL)
```

## Quick Python Example

```python
def calc_cp_cpk(mean, std, lsl, usl):
    cp = (usl - lsl) / (6 * std)
    cpu = (usl - mean) / (3 * std)
    cpl = (mean - lsl) / (3 * std)
    cpk = min(cpu, cpl)
    return cp, cpk


mean, std, lsl, usl = 10, 1, 8, 12
cp, cpk = calc_cp_cpk(mean, std, lsl, usl)
print(f"Cp: {cp:.2f}, Cpk: {cpk:.2f}")
```

## Run Locally

Python `3.11` is recommended for local development and deployment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./.venv/bin/python app.py
```

Then open `http://127.0.0.1:8000`.

## Example Interpretation

- High `Cp` and high `Cpk`: the process is tight and well-centered
- High `Cp` and low `Cpk`: variation may be acceptable, but the process is shifted
- Low `Cp` and low `Cpk`: the process spread itself is too wide for the spec

This side-by-side view is one of the main reasons engineers review `Cp` and `Cpk` together instead of looking at only one metric.

## FAQ

### What is the difference between Cp and Cpk?

`Cp` looks at spread only. `Cpk` looks at spread plus centering.

### What is a good Cpk value?

Many teams use `1.33` as a practical target, but the right threshold depends on customer requirements, product risk, and process stability.

### What kind of CSV can I upload?

Any CSV where the first column contains numeric measurement values. Non-numeric values are ignored.

## Project Structure

```text
app.py                  Flask entry point
web/routes.py           Routes and page rendering
services/analysis.py    Capability calculations and chart helpers
services/calculator.py  Form handling and calculator flow
data/sample_catalog.py  Built-in sample datasets
templates/              HTML templates
static/                 CSS assets
```

## Who This Is Useful For

- Manufacturing engineers
- Quality engineers
- Six Sigma practitioners
- Process engineers
- Students learning process capability

## Contributing

Issues and pull requests are welcome. If you find a bug, want to improve the UX, or want to expand the capability analysis content, feel free to open a discussion.

## License

MIT License. See [LICENSE](LICENSE).
