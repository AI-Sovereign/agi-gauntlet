> "True general intelligence begins exactly where the training data ends. We are no longer testing memory; we are testing reasoning under structural collapse."

<div align="center">
  <h1>AGI Gauntlet</h1>
  <p><b>A neuro-symbolic evaluation framework and lifecycle engine designed to test the true frontiers of artificial general intelligence.</b></p>
  
  [![PyPI Version](https://img.shields.io/pypi/v/agi-gauntlet.svg)](https://pypi.org/project/agi-gauntlet/)
  [![Python Versions](https://img.shields.io/pypi/pyversions/agi-gauntlet.svg)](https://pypi.org/project/agi-gauntlet/)
  [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
</div>

**© 2026 AGI Systems Directorate.**
**Authored by Ananya Soni, Founder & CEO.**

---

> "In the age of recursive self-correction, compute is cheap, but verifiable logic is the ultimate bottleneck."

## The Contamination Crisis

The current landscape of open-source artificial intelligence benchmarking is structurally compromised. Standardized evaluations (MMLU, HumanEval, standard logic suites) have inevitably become pre-training targets. When a large language model (LLM) solves a complex reasoning task today, it is rarely demonstrating emergent intelligence; it is executing high-dimensional curve fitting on memorized test data. 

**AGI Gauntlet** is engineered to bypass latent space memorization entirely. 

## Zero-Contamination Progressive Benchmarking

This package introduces a fundamentally rigorous paradigm for evaluating and orchestrating AI models. The logical constraints and evaluation matrices embedded within the Gauntlet **do not exist on the open web**. They are dynamically obfuscated at the source level to prevent crawler ingestion.

The framework enforces a progressive cognitive stress-test:
1. **Foundational Verification:** Establishes baselines for spatial, temporal, and economic reasoning.
2. **Dynamic Plasticity:** Injects real-time semantic shifts (e.g., redefining fundamental constants mid-inference) to break standard transformer next-token prediction loops.
3. **Neuro-Symbolic Synthesis:** Forces models to operate under severe temporal resource poverty, multi-actor paradoxes, and recursive logic structures.

## What's New in v0.1.1

The `0.1.1` release transforms `agi-gauntlet` from a strict benchmark into a comprehensive lifecycle and agentic workflow engine:

* **Universal Model Hooks:** Seamlessly connect frontier commercial models (via API keys), self-hosted Gradio clients, or custom private server endpoints using the new `ModelRegistry` architecture.
* **Agentic Workspace:** A dedicated environment to plug in autonomous AI assistants, granting them tool access to manage data parsing and evaluation pipelines.
* **Lifecycle Manager:** Stage and fetch curated datasets across remote, secure endpoints to seamlessly transition from evaluation to fine-tuning.
* **Test-Time Compute Guardrail:** An advanced 2026 monitoring feature that analyzes semantic entropy during Monte Carlo Tree Search (MCTS). It forces a deterministic circuit-break if a multi-agent loop enters a hallucinated self-correction spiral, saving compute and preventing silent failures.

## Quickstart

Install the package via pip:

```bash
pip install agi-gauntlet
```

Integrate your infrastructure and execute evaluations cleanly:

```python
import os
from agi_gauntlet import ModelRegistry, GauntletEngine, AgentWorkspace

registry = ModelRegistry()

# 1. Connect a Frontier Commercial Model
registry.register_commercial_api(
    name="frontier_model_alpha",
    provider="anthropic",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 2. Connect a custom Gradio hosted model
registry.register_gradio_client(
    name="local_qwen_instance", 
    gradio_url="http://localhost:7860", 
    fn_index=0
)

# 3. Initialize the Engine and Agent Workspace
workspace = AgentWorkspace()
workspace.plug_agent(agent_id="eval_orchestrator", tools_granted=["database_read", "run_gauntlet"])

engine = GauntletEngine(registry)
engine.serve(port=8000)
```

## Contributing

The pursuit of Artificial General Intelligence is a collaborative imperative. `agi-gauntlet` is open source, and architectural contributions, new evaluation matrices, and framework optimizations are welcome. 

Please review the open issues on our GitHub Repository before submitting a pull request. Keep your code modular, ensure logical determinism, and leave contaminated benchmarks in the past.
