from pathlib import Path

# ===== Inference =====
TOKENIZER = "klue/bert-base"
MAX_LENGTH = 62

# ===== Path =====
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models" / "best_bert.pt"