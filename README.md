> "True general intelligence begins exactly where the training data ends. We are no longer testing memory; we are testing reasoning under structural collapse."

<div align="center">
  <h1>AGI Gauntlet</h1>
  <p><b>A neuro-symbolic evaluation framework and lifecycle engine designed to test the true frontiers of artificial general intelligence.</b></p>
  
  [![PyPI Version](https://img.shields.io/pypi/v/agi-gauntlet.svg)](https://pypi.org/project/agi-gauntlet/)
  [![Python Versions](https://img.shields.io/pypi/pyversions/agi-gauntlet.svg)](https://pypi.org/project/agi-gauntlet/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
</div>

**© 2026 AGI Systems Directorate. Authored by Ananya Soni, Founder & CEO.**

---

## The Contamination Crisis

The current landscape of open-source artificial intelligence benchmarking is structurally compromised. Standardized tests like MMLU, HumanEval, and traditional logic benchmarks have become training targets. Large Language Models (LLMs) consistently ingest fragments, discussions, and variations of these exact evaluation prompts during their pre-training phases. 

When a model solves a complex reasoning task on these platforms, it is rarely demonstrating emergent intelligence; it is demonstrating high-dimensional curve fitting and retrieval. The "reasoning" is a synthesized mirage built on contaminated pre-training data.

**AGI Gauntlet** is built differently.

## Zero-Contamination Progressive Benchmarking

This package introduces a fundamentally new paradigm for evaluating AI models. The prompts and logic constraints embedded within the Gauntlet **do not exist on the open web**. They have never been indexed, they are not part of any existing dataset, and they are dynamically obfuscated within the package source code to prevent casual scraping by web crawlers.

The Gauntlet is a progressive evaluation matrix:
1. **Foundational Verification:** Begins with standard cognitive and agentic constraints that any competent model should handle.
2. **Dynamic Plasticity:** Introduces shifting logical rules and constraint adaptation (e.g., altering the definition of fundamental constants or linguistic operators mid-prompt).
3. **The Nightmare Gates:** Pushes models into extreme multi-domain synthesis, temporal resource poverty, and recursive meta-logic. If a model passes the final gates without a neuro-symbolic architecture or active memory integration, it is an anomaly.

## Core Capabilities

While `agi-gauntlet` serves primarily as an uncompromising benchmark, it is engineered to be the foundation for an entire AI project lifecycle. 

* **The Obfuscated Vault:** Evaluation prompts are shielded. Models must rely on actual zero-shot inference, not latent space memorization.
* **Dynamic Model Registry:** Bring your own compute. The framework does not lock you into specific providers. Easily plug in cloud APIs, local Hugging Face pipelines, or custom Gradio endpoints.
* **Lifecycle Hooks (Experimental):** Early-stage architectural stubs for full lifecycle management, allowing you to bridge the gap between evaluation, dataset injection, and eventual model training in future releases.

## Quickstart

Install the package via pip:

    pip install agi-gauntlet

Integrate your own models and execute the Gauntlet in less than 15 lines of code:

    from agi_gauntlet import ModelRegistry, GauntletEngine

    registry = ModelRegistry()

    # 1. Connect any standard API endpoint
    registry.register_api_endpoint(
        name="cloud_model_alpha", 
        url="https://api.example.com/v1/generate", 
        auth_env_var="API_KEY",
        is_judge=False
    )

    # 2. Or connect your own custom local functions
    async def local_judge(prompt: str) -> str:
        # Your local inference logic here
        return "PASS"

    registry.register_custom_function("local_evaluator", local_judge, is_judge=True)

    # 3. Initialize and serve the execution engine
    engine = GauntletEngine(registry)
    engine.serve(port=8000)

*(Note: For advanced lifecycle features, dataset hooks, and full neuro-symbolic evaluation pipelines, refer to the core source code.)*

## Contributing

The pursuit of Artificial General Intelligence is a collaborative imperative. `agi-gauntlet` is open source, and architectural contributions, new evaluation gates, and framework optimizations are welcome. 

Please review the open issues on our GitHub Repository before submitting a pull request. Keep your code clean, your logic sound, and leave the contaminated benchmarks in the past.
