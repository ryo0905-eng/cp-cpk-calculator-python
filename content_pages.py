CONTENT_PAGES = {
    "what-is-cp": {
        "title": "What Is Cp? Cp Formula, Meaning, and Good Cp Values",
        "description": "Learn what Cp means in process capability analysis, how to use the Cp formula, and what a good Cp value looks like in manufacturing.",
        "heading": "What Is Cp?",
        "intro": "Cp is a process capability index that compares the specification width with the natural spread of the process. Engineers use Cp when they want to understand potential capability before judging whether the process is centered.",
        "sections": [
            {
                "title": "What Cp tells you in process capability analysis",
                "body": "Cp measures whether process variation can fit inside the specification window if the process average is centered. A higher Cp means the process spread is small relative to the tolerance, which suggests stronger potential process capability.",
            },
            {
                "title": "Cp formula and calculation",
                "body": "The Cp formula is Cp = (USL - LSL) / (6 sigma). In plain terms, you compare the distance between the upper and lower specification limits with six standard deviations of the process. If Cp is below 1.00, the process spread is wider than the specification width.",
            },
            {
                "title": "Why Cp alone is not enough",
                "body": "Cp does not tell you whether the process mean is centered between the specification limits. A process can have a strong Cp but still produce defects if the average shifts too close to one side. That is why Cp is usually reviewed together with Cpk.",
            },
            {
                "title": "What is a good Cp value",
                "body": "Many quality teams consider Cp 1.33 or higher a practical target, but the correct requirement depends on process risk, customer specifications, and the maturity of the manufacturing process.",
            },
        ],
    },
    "what-is-cpk": {
        "title": "What Is Cpk? Cpk Formula, Meaning, and Good Cpk Values",
        "description": "Understand what Cpk means, how the Cpk formula works, and what a good Cpk value looks like for process capability analysis.",
        "heading": "What Is Cpk?",
        "intro": "Cpk is a process capability index that reflects both process variation and process centering. It shows how close the process mean is to the nearest specification limit, which makes it one of the most common metrics in manufacturing capability analysis.",
        "sections": [
            {
                "title": "What Cpk tells you",
                "body": "Cpk measures actual process capability by combining spread and centering. Even when Cp looks strong, Cpk can fall if the process average drifts toward the upper or lower specification limit.",
            },
            {
                "title": "Cpk formula and interpretation",
                "body": "Cpk is the smaller of CPU and CPL. CPU compares the process mean to the upper specification limit, while CPL compares the mean to the lower specification limit. The lower side becomes the effective Cpk because it reflects the closest risk point.",
            },
            {
                "title": "What is a good Cpk value",
                "body": "A Cpk of 1.33 is a common target for many production processes, although high-risk products or strict customer requirements may demand higher capability. The correct benchmark depends on context, not just a generic threshold.",
            },
            {
                "title": "Why Cpk matters in manufacturing",
                "body": "Because Cpk includes centering, it helps teams decide whether they should reduce variation, adjust the process target, or investigate a recent shift in setup, material, or measurement behavior.",
            },
        ],
    },
    "cp-vs-cpk": {
        "title": "Cp vs Cpk: Difference, Interpretation, and Examples",
        "description": "Compare Cp vs Cpk, understand the key difference between process spread and centering, and learn how to interpret both metrics together.",
        "heading": "Cp vs Cpk",
        "intro": "Cp and Cpk are closely related process capability metrics, but they answer different questions. Looking at both helps you avoid misreading a process that is statistically tight but operationally off-center.",
        "sections": [
            {
                "title": "Cp focuses on potential capability",
                "body": "Cp asks whether process variation is narrow enough for the tolerance range if the process is perfectly centered. It is best understood as a measure of potential capability rather than actual performance.",
            },
            {
                "title": "Cpk includes centering and actual performance",
                "body": "Cpk asks whether the real process location and variation together can meet the specification limits. That makes Cpk more useful when you want to understand actual production risk.",
            },
            {
                "title": "How to interpret Cp vs Cpk together",
                "body": "If Cp is high and Cpk is low, the process may have enough potential capability but is likely off target. If both Cp and Cpk are low, excessive variation is usually the main issue. If both are high, the process is generally narrow and well-centered relative to the specification limits.",
            },
            {
                "title": "When engineers search for Cp vs Cpk",
                "body": "Teams often compare Cp vs Cpk when preparing customer reports, troubleshooting defects near a specification limit, or deciding whether a process needs centering adjustment or variation reduction.",
            },
        ],
    },
    "what-is-pp-ppk": {
        "title": "What Are Pp and Ppk? Process Performance Indices Explained",
        "description": "Learn what Pp and Ppk mean, how they differ from Cp and Cpk, and when to use process performance indices in quality analysis.",
        "heading": "What Are Pp and Ppk?",
        "intro": "Pp and Ppk are process performance indices that look similar to Cp and Cpk, but they are typically used to evaluate overall performance over a broader time period rather than short-term capability.",
        "sections": [
            {
                "title": "What Pp measures",
                "body": "Pp compares the specification width with the overall variation of the process. It is similar to Cp, but it uses long-term performance data rather than a short-term estimate of capability.",
            },
            {
                "title": "What Ppk measures",
                "body": "Ppk adds process centering to the picture, much like Cpk. It shows how close the long-term process mean is to the nearest specification limit while accounting for overall variation.",
            },
            {
                "title": "Pp and Ppk vs Cp and Cpk",
                "body": "Cp and Cpk are often used for short-term process capability, while Pp and Ppk are commonly used for long-term process performance. Comparing both sets of indices can reveal whether capability holds up over time.",
            },
            {
                "title": "Why Pp and Ppk matter",
                "body": "If short-term capability looks strong but long-term performance is weak, the process may be drifting over time due to setup changes, material shifts, environmental conditions, or measurement instability.",
            },
        ],
    },
    "what-is-a-good-cpk-value": {
        "title": "What Is a Good Cpk Value? Common Targets Explained",
        "description": "Learn what is considered a good Cpk value, why 1.33 is common, and how to interpret Cpk targets in process capability analysis.",
        "heading": "What Is a Good Cpk Value?",
        "intro": "A good Cpk value depends on process risk, customer requirements, and how stable the process is over time. Still, many engineers use a few common thresholds as a starting point when judging process capability.",
        "sections": [
            {
                "title": "Why Cpk 1.33 is a common target",
                "body": "In many manufacturing environments, a Cpk of 1.33 is treated as a practical baseline for a capable process. It suggests that the process spread and centering are strong enough to meet specifications with some margin.",
            },
            {
                "title": "When 1.00 may not be enough",
                "body": "A Cpk of 1.00 means the process is just fitting inside the specification limits. In real production, small shifts in setup, material, or measurement can quickly create defects, so many teams require more than that.",
            },
            {
                "title": "When higher Cpk targets are used",
                "body": "High-risk products, safety-critical parts, or strict customer programs may require Cpk targets above 1.33. Some teams look for 1.67 or even higher when process failure is especially costly.",
            },
            {
                "title": "How to use Cpk correctly",
                "body": "Cpk is most useful when it is reviewed together with Cp, control charts, and process knowledge. A good Cpk value is not just a number. It should reflect a process that is both centered and stable over time.",
            },
        ],
    },
    "how-to-calculate-cp-cpk": {
        "title": "How to Calculate Cp and Cpk Step by Step",
        "description": "Learn how to calculate Cp and Cpk step by step using specification limits, sample mean, and standard deviation.",
        "heading": "How to Calculate Cp and Cpk",
        "intro": "To calculate Cp and Cpk, you need process data, an upper specification limit, a lower specification limit, the sample mean, and the process standard deviation. Once you have those values, the formulas are straightforward.",
        "sections": [
            {
                "title": "Step 1: Collect process data",
                "body": "Start with a set of measured values from your process. The data should come from the same characteristic and should reflect a meaningful production window rather than mixed conditions from unrelated setups.",
            },
            {
                "title": "Step 2: Define USL and LSL",
                "body": "Set the upper specification limit and lower specification limit based on the engineering requirement for the feature you are measuring. Cp and Cpk are only meaningful when those limits are clear.",
            },
            {
                "title": "Step 3: Calculate mean and standard deviation",
                "body": "Calculate the process mean to understand centering, then calculate the sample standard deviation to estimate variation. These values are required for both Cp and Cpk formulas.",
            },
            {
                "title": "Step 4: Apply the formulas",
                "body": "Cp = (USL - LSL) / (6 sigma). CPU = (USL - mean) / (3 sigma). CPL = (mean - LSL) / (3 sigma). Cpk is the smaller of CPU and CPL. Once calculated, compare both Cp and Cpk to understand spread and centering together.",
            },
        ],
    },
    "cp-formula": {
        "title": "Cp Formula Explained with Example",
        "description": "Understand the Cp formula, what each part means, and how to use it to evaluate process capability against specification limits.",
        "heading": "Cp Formula",
        "intro": "The Cp formula is one of the most common ways to estimate potential process capability. It compares the width of the specification limits with the natural spread of the process.",
        "sections": [
            {
                "title": "The Cp formula",
                "body": "Cp = (USL - LSL) / (6 sigma). USL is the upper specification limit, LSL is the lower specification limit, and sigma represents the process standard deviation.",
            },
            {
                "title": "What the formula means",
                "body": "The numerator shows how much room the specification allows. The denominator shows how wide the process variation is. If the specification window is much wider than the process spread, Cp becomes larger.",
            },
            {
                "title": "How to interpret Cp results",
                "body": "If Cp is below 1.00, the process spread is wider than the specification width. If Cp is above 1.33, the process may have good potential capability, but only if the process is also centered.",
            },
            {
                "title": "Why Cp should be paired with Cpk",
                "body": "Cp alone does not tell you whether the process mean is close to the center of the tolerance. That is why teams usually review Cp and Cpk together instead of relying on only one index.",
            },
        ],
    },
    "pp-vs-ppk": {
        "title": "Pp vs Ppk: What Is the Difference?",
        "description": "Compare Pp vs Ppk and learn how long-term process performance indices differ from short-term capability indices like Cp and Cpk.",
        "heading": "Pp vs Ppk",
        "intro": "Pp and Ppk are long-term process performance metrics that are closely related to Cp and Cpk. Comparing Pp vs Ppk helps you understand whether overall process performance is wide, centered, and stable over time.",
        "sections": [
            {
                "title": "Pp focuses on overall spread",
                "body": "Pp compares the specification width with the overall variation of the process across a broader time period. It is similar to Cp, but it reflects long-term performance rather than short-term capability.",
            },
            {
                "title": "Ppk adds centering",
                "body": "Ppk includes how close the long-term process mean is to the nearest specification limit. In that sense, it works like Cpk but on a longer time horizon.",
            },
            {
                "title": "How to interpret Pp vs Ppk together",
                "body": "If Pp is high and Ppk is low, the process may have acceptable long-term spread but poor centering. If both are low, long-term variation is usually the main issue. Looking at both helps reveal whether the process stays healthy over time.",
            },
            {
                "title": "Why compare Pp Ppk with Cp Cpk",
                "body": "Comparing short-term and long-term indices helps you see whether capability degrades over time. A process can look strong in a short study but still drift when viewed across shifts, lots, or environmental conditions.",
            },
        ],
    },
}
