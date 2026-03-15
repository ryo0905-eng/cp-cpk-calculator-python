CONTENT_PAGES = {
    "what-is-cp": {
        "title": "What Is Cp? Process Capability Index Explained",
        "description": "Learn what Cp means, how to calculate it, and when it helps evaluate process spread against specification limits.",
        "heading": "What Is Cp?",
        "intro": "Cp compares your specification width with the natural spread of the process. It is useful when you want a quick view of potential capability.",
        "sections": [
            {
                "title": "What Cp tells you",
                "body": "Cp measures whether the process spread can fit inside the specification window if the process is centered. A higher Cp means the spread is small relative to the tolerance.",
            },
            {
                "title": "Cp formula",
                "body": "Cp = (USL - LSL) / (6 sigma). If Cp is below 1.00, the process spread is wider than the specification width.",
            },
            {
                "title": "Important limitation",
                "body": "Cp does not tell you whether the process average is centered. That is why engineers usually check Cpk together with Cp.",
            },
        ],
    },
    "what-is-cpk": {
        "title": "What Is Cpk? Process Centering and Capability",
        "description": "Understand Cpk, how it differs from Cp, and how it reflects both variation and process centering.",
        "heading": "What Is Cpk?",
        "intro": "Cpk adds process centering to the capability picture. It shows how close the process mean is to the nearest specification limit.",
        "sections": [
            {
                "title": "What Cpk tells you",
                "body": "Cpk captures both variation and off-center behavior. Even if Cp looks strong, Cpk can be low when the mean drifts toward one side.",
            },
            {
                "title": "Cpk formula",
                "body": "Cpk is the smaller of CPU and CPL. CPU compares the mean to the upper spec limit, while CPL compares the mean to the lower spec limit.",
            },
            {
                "title": "How teams use it",
                "body": "Manufacturing and quality teams often use Cpk thresholds such as 1.33 or higher as a target for stable production, depending on the process and customer requirements.",
            },
        ],
    },
    "cp-vs-cpk": {
        "title": "Cp vs Cpk: What Is the Difference?",
        "description": "Compare Cp and Cpk side by side and learn when each process capability metric matters most.",
        "heading": "Cp vs Cpk",
        "intro": "Cp and Cpk are related, but they answer different questions. Looking at both helps you avoid misreading a process that is tight but off-center.",
        "sections": [
            {
                "title": "Cp focuses on spread",
                "body": "Cp asks whether the process variation is narrow enough for the tolerance range, assuming the process is centered.",
            },
            {
                "title": "Cpk includes centering",
                "body": "Cpk asks whether the actual process location and variation together can meet the specification limits.",
            },
            {
                "title": "How to interpret them together",
                "body": "If Cp is high and Cpk is low, the process could be capable but is likely off target. If both are low, the process spread is usually the main concern.",
            },
        ],
    },
}
