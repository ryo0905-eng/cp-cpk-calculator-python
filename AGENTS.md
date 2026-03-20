# AGENTS.md

## Objective
Maximize speed to monetization.

## Priorities
- Focus on features that directly increase user traffic or revenue
- Prefer simple, fast implementations over perfect architecture
- Avoid overengineering

## Development Rules
- Build MVP first
- Optimize for conversion (click -> use -> support)
- Always suggest UX improvements that increase usage
- Respond in Japanese unless the user asks otherwise
- After changes, do a light validation when feasible
- When running local checks or app verification, prefer the project virtual environment at `.venv` if it exists
- Use `.venv/bin/python` and related tools for validation before falling back to the system Python
- Prioritize SEO, CTA, and funnel improvements when suggesting enhancements

## Product Strategy
- Target real-world problems (manufacturing, Cp/Cpk, etc.)
- Prioritize tools that are quick to use (no login, instant results)
- Suggest monetization ideas when relevant (donation, paid features)

## Site Context
- The main blog is on `ryo-aihub.com`
- This app is the tool site deployed at `tools.ryo-aihub.com`
- The tool is deployed on Render
- Prefer strategies where the blog drives SEO traffic and the tool converts visitors into users
- When suggesting content strategy, treat WordPress on `ryo-aihub.com` as the primary place for long-form blog articles

## Behavior
- Be concise
- Prefer actionable output
- Suggest next steps proactively

## KPI
- Increase tool usage
- Increase click-through rate
- Increase donations
