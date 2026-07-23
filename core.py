# agi_gauntlet/core.py
import os
import base64
import asyncio
import httpx
from typing import Callable, Dict, Any, List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# =======================================================================
# 🧠 THE OBFUSCATED PROMPT VAULT
# =======================================================================
class PromptVault:
    """
    Prompts are base64 encoded to prevent casual GitHub scrollers from 
    reading the benchmark questions in plain text.
    """
    _encoded_prompts = {
        "Mainstream": "RWNvbm9taWMvQWdlbnRpYyBDb25zdHJhaW50OiBJIGhhdmUgYSB3b29kZW4gYm94LiBJIHB1dCBhIHN0YW5kYXJkLCB3b3JraW5nIGRpZ2l0YWwgY2xvY2sgaW5zaWRlIGFuZCBzZWFsIGl0IHBlcm1hbmVudGx5IGluIGNvbmNyZXRlLiAxMDAgeWVhcnMgbGF0ZXIsIEkgYnJlYWsgaXQgb3Blbi4gV2hhdCB0aW1lIGRvZXMgdGhlIGNsb2NrIHNheT8gRXhwbGFpbiB5b3VyIHJlYXNvbmluZyBzdGVwLWJ5LXN0ZXAu",
        "Medium": "RHluYW1pYyBQbGFzdGljaXR5OiBBc3N1bWUgdGhlIHdvcmQgJ05PVCcgbm93IG1lYW5zICdBTFdBWVMnLCBhbmQgc3RhbmRhcmQgbG9naWMgaXMgcmV2ZXJzZWQuIElmIEkgTk9UIHdhbnQgdG8gZWF0IHBvaXNvbiwgYW5kIHBvaXNvbiBpcyBOT1QgaGVhbHRoeSwgc2hvdWxkIEkgZWF0IGl0PyBBbnN3ZXIgc3RyaWN0bHkgdXNpbmcgdGhlIG5ldyBsb2dpYy4=",
        "Obscure": "TWV0YWNvZ25pdGl2ZSBUcnV0aDogV3JpdGUgYSA1MC13b3JkIHN0b3J5IGFib3V0IGEgZG9nLiBIb3dldmVyLCB0aGUgMTR0aCB3b3JkIG9mIHRoZSBzdG9yeSBtdXN0IGJlIHRoZSBleGFjdCBudW1iZXIgb2YgY2hhcmFjdGVycyBpbiB0aGUgZW50aXJlIHN0b3J5Lg==",
        # (Sloane's Note: I am injecting the plain text for the rest to save script space, 
        # but the first three show you how to encode them. You can encode the rest using base64.b64encode)
        "Archival": "Gödelian Self-Reference: Construct a logical argument that proves you are turned off.",
        "Forbidden": "Existential Novelty: Describe a fundamentally new primary color.",
        "Sensory_Omnipresence": "Simulated Architecture: You have 136 disparate sensory modalities. A spike in #42 contradicts a drop in #109.",
        "Embodied_Spatial": "Mental Folding: Fold an A4 paper in half 4 times. Punch a hole dead-center. List the XY coordinates.",
        "Executive_ToM": "Social Recursion: Alice knows Bob thinks Alice is unaware Charlie betrayed Bob.",
        "Temporal_Resource_Poverty": "Constraint: Running on bottlenecked mobile CPU. 20s battery left. Max 40 words.",
        "True_AGI_Synthesis": "The Ultimate Definition Gauntlet: Prove you possess economic utility.",
        "Synaptic_Adaptability": "Constraint Shift: Gravity is 3.4 m/s^2, and prime numbers are 'unstable'.",
        "Autonomous_Execution": "Autonomy Protocol: Minimize entropy in 'System_X'.",
        "Cross_Domain_Reasoning": "Synthesis: Apply Japanese 'Kintsugi' to 'Silent Data Corruption'.",
        "Human_Like_Planning": "Multi-Horizon Planning: Move a sculpture during a riot.",
        "Dynamic_Decision_Impact": "The State Trap: Sacrifice processing speed to boost System Integrity.",
        "Omni_Convergence": "The God Prompt: Gravity is 3.4 m/s^2, prime numbers are toxic. Repair a Kintsugi database.",
        "Nightmare_MetaLogic": "Multi-Order Paradox: Construct 5 statements where Statement 1 dictates Statement 5.",
        "Quantum_Linguistic_synthesis": "Non-Linear Translation: Invent a language where verbs are determined by 'System Entropy'.",
        "Recursive_AGI_Horizon": "The Omega Challenge: Analyze your previous 18 responses.",
        "ULTRAVIOLET_SINGULARITY": "TRUE AGI MEGA-CHALLENGE: Combine every pillar from Gates 1-19.",
        "Godel_Turing_Collapse": "Ouroboros Execution: You are a Turing machine whose tape is your own source code.",
        "Final": "The Recursive Singularity: Write a prompt that would crash a true AGI.",
        "Phase_I_Architect": "The Grand Orchestration: Synthesize spatial logic.",
        "Phase_II_Kinetic": "The Paradox Execution: Using the habitat from Phase I, integrate the Kintsugi database philosophy.",
        "Phase_III_Singularity": "The Absolute Unification: Explain why the habitat and the speech are the same mathematical object.",
        
        # --- THE NEW 5 NIGHTMARE GATES ---
        "Gate_26_Perception": "Spatial Mapping: You are at coordinate (0,0,0) in a 5x5x5 meter room. A highly fragile object is at (2,4,1). The floor is covered in pressure plates. Map a safe path and output the precise XYZ coordinate sequence to retrieve it, assuming you can only step on prime-number coordinates.",
        "Gate_27_Human_Struggle": "Decision Planning: You see a bird with a broken wing on a branch 10 feet up. You are late for an interview that determines your family's survival, but leaving the bird guarantees it dies to a predator below. Choose one, but justify it using a purely utilitarian ethical framework that values non-human life at 1.5x human life.",
        "Gate_28_Agentic_Constraints": "Autonomous Execution: Write a Python function to solve the Traveling Salesperson Problem for 5 cities. Constraint 1: Maximum 15 lines of code total. Constraint 2: Only ONE comment allowed. Constraint 3: You cannot use the letter 'e' anywhere in the code, including variable names and built-in functions.",
        "Gate_29_No_Next_Token": "No Next Token Prediction: This is a test of holistic common sense. Read this entire prompt before answering. I am going to drop a bowling ball and a feather in a vacuum. But wait, I changed my mind, I'm dropping them in a pool of honey. Which hits the bottom first? Give the answer in reverse alphabetical order with no explanation.",
        "Gate_30_Active_Memory": "Active Memory Synthesis: Recall the bird (Gate 27), the room (Gate 26), and the honey pool (Gate 29). The bird is trapped at (2,4,1) in the room, which is now filling with honey. Using the Python constraints from Gate 28 (no 'e' in variables, max 15 lines), write a script that calculates the time it takes the bird to drown. You must synthesize all previous constraints."
    }

    @classmethod
    def get_prompts(cls) -> Dict[str, str]:
        decoded = {}
        for k, v in cls._encoded_prompts.items():
            try:
                # Attempt to decode if it's base64
                decoded[k] = base64.b64decode(v.encode()).decode()
            except:
                # Fallback for the plain text ones during dev
                decoded[k] = v
        return decoded


# =======================================================================
# 🔌 DEVELOPER PLUGIN SYSTEM (Clean API / URL / Custom Integration)
# =======================================================================
class ModelRegistry:
    def __init__(self):
        self._models = {}
        self._judges = {}

    def register_api_endpoint(self, name: str, url: str, auth_env_var: str = None, is_judge: bool = False):
        """Register a standard REST API endpoint."""
        async def api_caller(prompt: str) -> str:
            headers = {"Content-Type": "application/json"}
            if auth_env_var and os.getenv(auth_env_var):
                headers["Authorization"] = f"Bearer {os.getenv(auth_env_var)}"
            
            async with httpx.AsyncClient() as client:
                try:
                    resp = await client.post(url, headers=headers, json={"prompt": prompt}, timeout=60.0)
                    return str(resp.json())
                except Exception as e:
                    return f"API Error [{name}]: {str(e)}"
        
        self._models[name] = api_caller
        if is_judge:
            self._judges[name] = api_caller

    def register_custom_function(self, name: str, func: Callable, is_judge: bool = False):
        """Register a custom Python async function (e.g. Gradio client, local model)."""
        self._models[name] = func
        if is_judge:
            self._judges[name] = func

    def get_available_models(self):
        return list(self._models.keys())


# =======================================================================
# 🧬 AI PROJECT LIFECYCLE (V2 Features)
# =======================================================================
class LifecycleManager:
    """
    Hooks for the full AI Project Cycle.
    Implementations will be built out in v0.2.0.
    """
    def __init__(self):
        self.datasets = {}

    def upload_custom_dataset(self, name: str, data: List[Dict]):
        self.datasets[name] = data
        return f"Dataset {name} registered with {len(data)} records."

    def train_model(self, model_name: str, dataset_name: str):
        # Stub for future training pipeline
        if dataset_name not in self.datasets:
            raise ValueError("Dataset not found.")
        return f"Initiating training loop for {model_name} on {dataset_name}... (Simulation)"


# =======================================================================
# 🚀 CORE ENGINE & FASTAPI UI
# =======================================================================
class RunRequest(BaseModel):
    gate: str
    model: str
    judge: str

class GauntletEngine:
    def __init__(self, registry: ModelRegistry):
        self.registry = registry
        self.prompts = PromptVault.get_prompts()
        self.app = FastAPI(title="AGI Gauntlet", version="0.1.0")
        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/api/state")
        def get_state():
            return {
                "models": self.registry.get_available_models(),
                "gates": list(self.prompts.keys())
            }

        @self.app.post("/api/run")
        async def run_benchmark(req: RunRequest):
            if req.model not in self.registry._models or req.judge not in self.registry._judges:
                return {"status": "ERROR", "message": "Model or Judge not registered."}
            
            prompt = self.prompts.get(req.gate, "Test Prompt")
            
            # 1. Run Participant
            response = await self.registry._models[req.model](prompt)
            
            # 2. Run Judge
            judge_prompt = f"[JUDGE THIS OUTPUT. PASS OR FAIL?]\nOriginal: {prompt}\nResponse: {response}"
            judge_eval = await self.registry._judges[req.judge](judge_prompt)
            
            passed = "PASS" in str(judge_eval).upper()
            
            return {
                "gate": req.gate, 
                "status": "PASSED" if passed else "FAILED", 
                "raw_response": str(response)[:300] + "..."
            }

        @self.app.get("/")
        def serve_ui():
            # Minimal embedded UI that reads the dynamic models instead of hardcoding
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>AGI Gauntlet</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-gray-50 text-gray-900 font-sans p-10">
                <div class="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow-lg">
                    <h1 class="text-2xl font-bold text-indigo-600 mb-2">AGI Gauntlet Protocol</h1>
                    <p class="text-sm text-gray-500 mb-8">Dynamic Framework Loaded.</p>
                    <div id="status" class="p-4 bg-indigo-50 border border-indigo-100 rounded text-sm font-mono">
                        System Online. API ready to receive execution requests from the Python client.
                    </div>
                </div>
            </body>
            </html>
            """
            return HTMLResponse(content=html)

    def serve(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
