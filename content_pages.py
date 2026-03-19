CONTENT_PAGES = {
    "what-is-cp": {
        "title": "What Is Cp? Cp Formula, Meaning, and Good Cp Values",
        "description": "Learn what Cp means in process capability analysis, how to use the Cp formula, and what a good Cp value looks like in manufacturing.",
        "heading": "What Is Cp?",
        "intro": "Cp is a process capability index that compares the specification width with the natural spread of the process. Engineers use Cp when they want to understand potential capability before judging whether the process is centered.",
        "faqs": [
            {
                "question": "What does Cp mean?",
                "answer": "Cp measures potential process capability by comparing the specification width with process spread, assuming the process is centered.",
            },
            {
                "question": "What is a good Cp value?",
                "answer": "Many teams use Cp 1.33 or higher as a practical target, although the right requirement depends on the process and customer expectations.",
            },
            {
                "question": "Can Cp be high when the process is off-center?",
                "answer": "Yes. Cp does not reflect centering, so a process can show a high Cp while still drifting toward one specification limit.",
            },
        ],
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
            {
                "title": "How engineers use Cp in real manufacturing work",
                "body": "In practice, engineers often look at Cp early in a capability review to see whether the process spread is fundamentally narrow enough for the tolerance. If Cp is weak, the first discussion is usually about reducing variation. If Cp looks healthy, the next step is checking whether the process is actually centered by reviewing Cpk and the process mean.",
            },
            {
                "title": "What Cp does not tell you",
                "body": "Cp does not explain why variation is large, and it does not show whether the process is stable over time. A process can have a reasonable Cp in one study and still perform poorly later if setup, material, environment, or measurement conditions drift. That is why many teams pair Cp with Cpk, Pp, Ppk, and control charts.",
            },
        ],
    },
    "what-is-cpk": {
        "title": "What Is Cpk? Cpk Formula, Meaning, and Good Cpk Values",
        "description": "Understand what Cpk means, how the Cpk formula works, and what a good Cpk value looks like for process capability analysis.",
        "heading": "What Is Cpk?",
        "intro": "Cpk is a process capability index that reflects both process variation and process centering. It shows how close the process mean is to the nearest specification limit, which makes it one of the most common metrics in manufacturing capability analysis.",
        "faqs": [
            {
                "question": "What does Cpk measure?",
                "answer": "Cpk measures actual process capability by considering both process spread and how close the process mean is to the nearest specification limit.",
            },
            {
                "question": "What is a good Cpk value?",
                "answer": "A Cpk of 1.33 is a common target in manufacturing, although some high-risk processes need a higher value.",
            },
            {
                "question": "Why can Cpk be lower than Cp?",
                "answer": "Cpk drops below Cp when the process is not centered, even if the underlying variation is relatively small.",
            },
        ],
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
            {
                "title": "How to read Cpk in real process reviews",
                "body": "When engineers review a low Cpk, they often ask two questions. First, is the process variation too wide? Second, is the average shifted toward one side? Looking at Cp together with Cpk helps separate those two cases. That distinction matters because variation reduction and centering correction are different improvement actions.",
            },
            {
                "title": "Why Cpk can change quickly",
                "body": "Cpk is sensitive to mean shifts, which means it can move quickly when the process target drifts. Tool wear, setup offsets, calibration issues, raw material changes, and measurement problems can all pull the process mean toward a specification limit. That is one reason Cpk is often monitored closely in ongoing production.",
            },
        ],
    },
    "cp-vs-cpk": {
        "title": "Cp vs Cpk: Difference, Interpretation, and Examples",
        "description": "Compare Cp vs Cpk, understand the key difference between process spread and centering, and learn how to interpret both metrics together.",
        "heading": "Cp vs Cpk",
        "intro": "Cp and Cpk are closely related process capability metrics, but they answer different questions. Looking at both helps you avoid misreading a process that is statistically tight but operationally off-center.",
        "faqs": [
            {
                "question": "What is the main difference between Cp and Cpk?",
                "answer": "Cp looks at process spread only, while Cpk includes both spread and centering relative to the specification limits.",
            },
            {
                "question": "Should Cp and Cpk be reviewed together?",
                "answer": "Yes. Looking at both metrics helps you separate variation problems from centering problems.",
            },
            {
                "question": "What does it mean if Cp is high and Cpk is low?",
                "answer": "That usually means the process has enough potential capability but is shifted away from the target center.",
            },
        ],
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
            {
                "title": "A practical way to read Cp vs Cpk",
                "body": "A simple rule of thumb is this: if Cp and Cpk are both high, the process is narrow and centered. If Cp is high but Cpk is lower, centering is likely the issue. If both are low, the spread itself is the bigger concern. This kind of side-by-side interpretation is often more useful than focusing on one index by itself.",
            },
        ],
    },
    "what-is-pp-ppk": {
        "title": "What Are Pp and Ppk? Process Performance Indices Explained",
        "description": "Learn what Pp and Ppk mean, how they differ from Cp and Cpk, and when to use process performance indices in quality analysis.",
        "heading": "What Are Pp and Ppk?",
        "intro": "Pp and Ppk are process performance indices that look similar to Cp and Cpk, but they are typically used to evaluate overall performance over a broader time period rather than short-term capability.",
        "faqs": [
            {
                "question": "What is the difference between Pp and Ppk?",
                "answer": "Pp reflects overall long-term spread, while Ppk also includes how centered the long-term process mean is relative to the specification limits.",
            },
            {
                "question": "How are Pp and Ppk different from Cp and Cpk?",
                "answer": "Cp and Cpk are commonly used for short-term capability, while Pp and Ppk are used for broader long-term process performance.",
            },
            {
                "question": "Why do engineers compare Ppk with Cpk?",
                "answer": "Comparing Ppk with Cpk can reveal whether long-term performance is weaker than short-term capability because of drift or instability over time.",
            },
        ],
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
        "faqs": [
            {
                "question": "Is Cpk 1.33 good?",
                "answer": "In many manufacturing settings, yes. Cpk 1.33 is a common target because it gives more margin than a process that is only just capable.",
            },
            {
                "question": "Is Cpk 1.00 enough?",
                "answer": "A Cpk of 1.00 means the process is just fitting inside the specifications, so many teams consider it too risky for routine production.",
            },
            {
                "question": "When do teams aim above Cpk 1.33?",
                "answer": "Higher-risk products, safety-critical features, or strict customer requirements often lead teams to aim for 1.67 or higher.",
            },
        ],
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
            {
                "title": "Why a single Cpk threshold is not always enough",
                "body": "Many teams like simple rules such as Cpk 1.33 or Cpk 1.67, but real capability decisions usually depend on more than one cutoff. Customer requirements, process maturity, part criticality, and cost of failure all influence what counts as acceptable. A value that is good enough for one feature may not be good enough for another.",
            },
            {
                "title": "How engineers respond to a low Cpk",
                "body": "When Cpk is below target, teams usually check whether the process is off-center or whether the spread is too wide. If centering is the problem, setup adjustment may help. If variation is the issue, the response may involve machine condition, material consistency, measurement stability, or process method review.",
            },
        ],
    },
    "how-to-calculate-cp-cpk": {
        "title": "How to Calculate Cp and Cpk Step by Step",
        "description": "Learn how to calculate Cp and Cpk step by step using specification limits, sample mean, and standard deviation.",
        "heading": "How to Calculate Cp and Cpk",
        "intro": "To calculate Cp and Cpk, you need process data, an upper specification limit, a lower specification limit, the sample mean, and the process standard deviation. Once you have those values, the formulas are straightforward.",
        "faqs": [
            {
                "question": "What do I need to calculate Cp and Cpk?",
                "answer": "You need the process data, the upper and lower specification limits, the sample mean, and the process standard deviation.",
            },
            {
                "question": "Can I calculate Cp and Cpk from a CSV file?",
                "answer": "Yes. If your measurement values are in the first column of a CSV file, you can upload them and calculate both metrics directly.",
            },
            {
                "question": "Why do I need both Cp and Cpk?",
                "answer": "Cp shows potential capability based on spread, while Cpk shows actual capability after centering is considered.",
            },
        ],
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
            {
                "title": "Common mistakes when calculating Cp and Cpk",
                "body": "One common mistake is mixing data from different machines, shifts, or setup conditions into one dataset. Another is using unclear specification limits or including non-comparable measurements. Engineers also need to watch for very small sample sizes, because unstable estimates of mean and standard deviation can make the capability numbers misleading.",
            },
            {
                "title": "How teams use the results after calculation",
                "body": "After calculating Cp and Cpk, teams usually decide whether the next step is variation reduction, process centering, or further monitoring. If Cp is low, the spread may need improvement. If Cp is acceptable but Cpk is lower, the process may need target adjustment. The calculation itself is only useful when it leads to a practical decision.",
            },
        ],
    },
    "cp-formula": {
        "title": "Cp Formula Explained with Example",
        "description": "Understand the Cp formula, what each part means, and how to use it to evaluate process capability against specification limits.",
        "heading": "Cp Formula",
        "intro": "The Cp formula is one of the most common ways to estimate potential process capability. It compares the width of the specification limits with the natural spread of the process.",
        "faqs": [
            {
                "question": "What is the Cp formula?",
                "answer": "The Cp formula is Cp = (USL - LSL) / (6 sigma).",
            },
            {
                "question": "What does sigma mean in the Cp formula?",
                "answer": "Sigma represents the process standard deviation, which describes how much the process values vary around the mean.",
            },
            {
                "question": "Does the Cp formula include process centering?",
                "answer": "No. Cp assumes the process is centered, so you need Cpk if you want centering to be included.",
            },
        ],
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
            {
                "title": "How to use the Cp formula in practice",
                "body": "The Cp formula is most useful as an early capability check. It helps you answer whether the process spread is fundamentally narrow enough for the engineering tolerance. In production settings, this often becomes the starting point for deciding whether the bigger problem is variation, centering, or time-based instability.",
            },
            {
                "title": "What the Cp formula cannot tell you by itself",
                "body": "Even when the Cp formula returns a strong value, it does not guarantee good production performance. The process may still be off-center, unstable over time, or influenced by special causes that are hidden in the dataset. That is why capability studies usually include Cpk, process context, and often a control chart review.",
            },
        ],
    },
    "pp-vs-ppk": {
        "title": "Pp vs Ppk: What Is the Difference?",
        "description": "Compare Pp vs Ppk and learn how long-term process performance indices differ from short-term capability indices like Cp and Cpk.",
        "heading": "Pp vs Ppk",
        "intro": "Pp and Ppk are long-term process performance metrics that are closely related to Cp and Cpk. Comparing Pp vs Ppk helps you understand whether overall process performance is wide, centered, and stable over time.",
        "faqs": [
            {
                "question": "What is the main difference between Pp and Ppk?",
                "answer": "Pp looks at overall long-term spread, while Ppk includes both long-term spread and how centered the process is.",
            },
            {
                "question": "When should I use Pp and Ppk?",
                "answer": "Use Pp and Ppk when you want to understand overall process performance over time rather than only short-term capability.",
            },
            {
                "question": "Why compare Pp and Ppk with Cp and Cpk?",
                "answer": "Comparing them helps you see whether the process behaves differently over the long term than it does in a shorter capability study.",
            },
        ],
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
            {
                "title": "How to read Pp vs Ppk in practice",
                "body": "A practical interpretation is similar to Cp vs Cpk. If Pp is much higher than Ppk, long-term centering is likely an issue. If both are low, the process probably has too much overall variation. These readings are especially useful when you want to understand whether the process stays capable beyond a short study window.",
            },
            {
                "title": "Why long-term performance can be weaker than short-term capability",
                "body": "Processes often look cleaner in a short capability study than they do over longer production periods. Environmental changes, shift differences, lot-to-lot variation, operator effects, and maintenance cycles can all widen the long-term distribution. That is why Pp and Ppk can reveal risk that short-term capability indices do not fully capture.",
            },
        ],
    },
}


RELATED_PAGE_MAP = {
    "what-is-cp": ["cp-vs-cpk", "cp-formula", "how-to-calculate-cp-cpk"],
    "what-is-cpk": ["what-is-a-good-cpk-value", "cp-vs-cpk", "how-to-calculate-cp-cpk"],
    "cp-vs-cpk": ["what-is-cp", "what-is-cpk", "what-is-a-good-cpk-value"],
    "what-is-pp-ppk": ["pp-vs-ppk", "cp-vs-cpk", "how-to-calculate-cp-cpk"],
    "what-is-a-good-cpk-value": ["what-is-cpk", "cp-vs-cpk", "how-to-calculate-cp-cpk"],
    "how-to-calculate-cp-cpk": ["cp-formula", "what-is-cp", "what-is-cpk"],
    "cp-formula": ["what-is-cp", "how-to-calculate-cp-cpk", "cp-vs-cpk"],
    "pp-vs-ppk": ["what-is-pp-ppk", "cp-vs-cpk", "what-is-a-good-cpk-value"],
}


def get_related_pages(slug: str) -> list[dict]:
    related_slugs = RELATED_PAGE_MAP.get(slug, [])
    related_pages = []

    for related_slug in related_slugs:
        page = CONTENT_PAGES.get(related_slug)
        if page is None:
            continue
        related_pages.append(
            {
                "slug": related_slug,
                "heading": page["heading"],
                "description": page["description"],
            }
        )

    return related_pages


def get_page_faqs(slug: str) -> list[dict]:
    page = CONTENT_PAGES.get(slug)
    if page is None:
        return []
    return page.get("faqs", [])
