# Cp vs Cpk Calculator (Python) – Free Process Capability Tool

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Tool-blue)](https://tools.ryo-aihub.com/)
[![GitHub stars](https://img.shields.io/github/stars/ryo0905-eng/cp-cpk-calculator-python?style=social)](https://github.com/ryo0905-eng/cp-cpk-calculator-python)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Calculate Cp and Cpk instantly with this free, interactive web tool. No Excel needed – just input your data and get results with visualizations.

👉 **Try it now:** [Live Cp/Cpk Calculator](https://tools.ryo-aihub.com/)

![Cp/Cpk Calculator Interface](tool%20screenshot.png)

*Input your process data and instantly see Cp, Cpk values with interactive visualization.*

---

## 🚀 What is Cp and Cpk?

- **Cp** (Process Capability): Measures how well your process fits within specification limits, focusing on variation.
- **Cpk** (Process Capability Index): Measures both variation and how centered your process is.

In manufacturing and quality control, **Cpk is crucial** because it accounts for process centering. A high Cp with low Cpk means your process is stable but off-target, leading to defects.

---

## ⚠️ Why Cp Alone Can Be Misleading

Imagine a process with:
- Cp = 1.8 (seems excellent)
- Cpk = 0.6 (actually poor)

This indicates the process is consistent but shifted away from the target, potentially causing quality issues.

👉 **Don't get fooled – always check Cpk!**

---

## 📊 Quick Python Example

```python
def calc_cp_cpk(mean, std, lsl, usl):
    cp = (usl - lsl) / (6 * std)
    cpk = min((usl - mean) / (3 * std), (mean - lsl) / (3 * std))
    return cp, cpk

# Example usage
mean, std, lsl, usl = 10, 1, 8, 12
cp, cpk = calc_cp_cpk(mean, std, lsl, usl)
print(f"Cp: {cp:.2f}, Cpk: {cpk:.2f}")
```

---

## 📈 Tool Screenshot

Here's what the live Cp/Cpk calculator looks like in action:

![Cp/Cpk Calculator Interface](tool%20screenshot.png)

*Input your process data and instantly see Cp, Cpk values with interactive visualization.*

---

## ✨ Features

- ✅ **Instant Calculations**: Get Cp and Cpk values in seconds
- ✅ **Interactive Visualizations**: See your process distribution
- ✅ **No Software Required**: Works directly in your browser
- ✅ **Free to Use**: Open-source and ad-free
- ✅ **Educational**: Learn with built-in examples
- ✅ **Mobile-Friendly**: Use on any device

---

## 🎯 Who Should Use This?

- Manufacturing Engineers
- Quality Control Specialists
- Six Sigma Practitioners
- Data Analysts
- Students learning process capability

---

## 🛠️ How to Use

1. Visit the [Live Tool](https://tools.ryo-aihub.com/)
2. Enter your process mean, standard deviation, LSL, and USL
3. Click "Calculate" to see Cp, Cpk, and visualization
4. Interpret results: Cpk > 1.33 is typically excellent

---

## 🔍 SEO Keywords

Cp calculator, Cpk calculator, process capability index, quality control tool, Six Sigma calculator, manufacturing quality, statistical process control, capability analysis, Python quality tool

---

## 📞 Contact & Support

Found this helpful? Star the repo ⭐ and share with colleagues!

For questions or contributions, open an issue on GitHub.

---

*Built with Python, hosted on a custom web platform. Open-source under MIT License.*
