# Contributing to AGI Gauntlet

The pursuit of Artificial General Intelligence is not a solo endeavor, but it requires strict architectural discipline. We welcome contributions from researchers, engineers, and theorists who understand that current AI benchmarking is fundamentally broken.

## The Golden Rule: Zero Contamination
If you are submitting new prompts, gates, or logical paradoxes, **they must be entirely original**. Do not submit variations of existing MMLU, HumanEval, or ARC challenges. If it exists on the open web, it is contaminated. All new evaluation strings must be obfuscated before merging.

## Where to Contribute
To clarify standard open-source mechanics: **You cannot contribute directly to the Python Package Index (PyPI).** PyPI is our distribution channel for compiled releases. 

All development, issue tracking, and pull requests must be routed through our official GitHub repository.

## How to Submit Changes
1. **Fork the Repository:** Create your own working copy on GitHub.
2. **Branch Out:** Create a feature branch (`git checkout -b feature/neuro-symbolic-patch`).
3. **Write Clean Code:** Follow PEP 8 standards. If you are adding a lifecycle hook, ensure the async functions don't block the main thread.
4. **Test:** Run the existing benchmark against a dummy model to ensure you haven't broken the evaluation loop.
5. **Open a Pull Request:** Submit your PR on GitHub with a detailed explanation of the logic behind your code. "Fixed a typo" is fine. "Altered the mathematical constraints of Gate 29" requires a thesis.

By contributing to this repository, you agree that your code will be licensed under the MIT License and attributed to the AGI Systems Directorate ecosystem.

