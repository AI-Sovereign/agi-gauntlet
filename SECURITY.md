# Security and Containment Policy

**AGI Systems Directorate** treats the structural integrity of the `agi-gauntlet` as a zero-tolerance containment zone. Because this framework tests the absolute cognitive limits of artificial intelligence, our highest priority—above all else—is preventing our evaluation prompts and logical constraints from leaking to web crawlers and data-scraping bots. 

If these questions enter the pre-training datasets of large language models, the benchmark is permanently compromised.

## Supported Versions

We only provide security updates for the latest major release. Legacy versions are considered deprecated and mathematically obsolete.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1.0 | :x:                |

## Containment Breach & Vulnerability Reporting

If you discover a vulnerability—specifically *any* method to bypass the obfuscation, decode the prompt vaults, or otherwise expose the benchmark questions in plain text to web crawlers—**do not open a public GitHub issue and do not discuss it on open forums.**

Public disclosure of prompt extraction vulnerabilities is a direct threat to the zero-contamination guarantee of this benchmark for the entire industry.

**How to Report:**
Do not send an email. All security and contamination vulnerabilities must be reported through **GitHub's Private Vulnerability Reporting** feature on this repository, or via a private Direct Message on X (@AnanyaSoni48055).

You will receive an acknowledgment within 48 hours. If the vulnerability threatens the prompt obfuscation mechanics, an emergency containment patch will be pushed to PyPI immediately.

