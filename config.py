import os
from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent

# Reproducibility
RANDOM_STATE = 42

# Subset Size
SUBSET_SIZE = 20000

# Raw Data
DATA_ROOT = BASE_DIR / "data" / "raw"
RAW_CSV = DATA_ROOT / "Suicide_Detection.csv"

# Processed Data
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LABELLED_DATASET = str(PROCESSED_DIR / "labelled_dataset.csv")
BEST_BASELINE_PKL = str(PROCESSED_DIR / "best_baseline.pkl")
ROBERTA_PREDS_PKL = str(PROCESSED_DIR / "preds_roberta.pkl")
TWITTERROBERTA_PREDS_PKL = str(PROCESSED_DIR / "preds_twitterroberta.pkl")
DISTILROBERTA_PREDS_PKL = str(PROCESSED_DIR / "preds_distilroberta.pkl")

# Results
VISUALISATION_DIR = BASE_DIR / "results" / "visualisations"
CSV_DIR = BASE_DIR / "results" / "csv"
BASELINE_RESULTS_CSV = str(CSV_DIR / "baseline_results.csv")
ROBERTA_RESULTS_CSV = str(CSV_DIR / "roberta_results.csv")
TWITTERROBERTA_RESULTS_CSV = str(CSV_DIR / "twitterroberta_results.csv")
DISTILROBERTA_RESULTS_CSV = str(CSV_DIR / "distilroberta_results.csv")
ALL_RESULTS_CSV = str(CSV_DIR / "all_models_results.csv")

# Label Definitions
LABEL2ID = {"non-suicide": 0, "suicide": 1}
ID2LABEL = {0: "non-suicide", 1: "suicide"}
NUM_LABELS = 2
POSITIVE_CLASS = "suicide"   

# Data Splits
TEST_SIZE = 0.15
VAL_SIZE  = 0.176   

# Dataset Subsampling 
MAX_TRAIN_SAMPLES = 10000
MAX_VAL_SAMPLES   = 2000
USE_SUBSET = True

# Transformer Hyperparameters
MAX_LENGTH = 128
NUM_EPOCHS = 3
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
WEIGHT_DECAY = 0.01
WARMUP_RATIO = 0.1
EARLY_STOPPING_PATIENCE = 2

# Model Directories
MODELS_DIR = BASE_DIR / "models"
ROBERTA_DIR = str(MODELS_DIR / "roberta")
TWITTERROBERTA_DIR = str(MODELS_DIR / "twitterroberta")
DISTILROBERTA_DIR = str(MODELS_DIR / "distilroberta")

# HuggingFace Model IDs
ROBERTA_MODEL_ID = "roberta-base"
TWITTERROBERTA_MODEL_ID = "cardiffnlp/twitter-roberta-base-sentiment-latest"
DISTILROBERTA_MODEL_ID = "distilroberta-base"

# Linguistic Signal Configuration
NEGATION_CUES = [
    "not", "no", "never", "neither", "nobody", "nothing",
    "nowhere", "nor", "cannot", "can't", "won't", "don't",
    "doesn't", "didn't", "isn't", "aren't", "wasn't", "weren't",
    "haven't", "hasn't", "hadn't", "wouldn't", "couldn't",
    "shouldn't", "n't"
]

INTENSIFIERS = [
    "very", "extremely", "completely", "totally", "absolutely",
    "utterly", "deeply", "terribly", "incredibly", "awfully",
    "so", "such", "really", "quite", "rather", "too",
    "entirely", "fully", "thoroughly", "desperately", "severely"
]

NEGATION_WINDOW = 5   

# Early Detection Experiment
EARLY_DETECTION_WINDOWS = [32, 64, 128]   

# EDA Configuration 
TOP_N_NGRAMS  = 20
WORDCLOUD_MAX = 200

# Create Output Directories\
for _d in [PROCESSED_DIR, VISUALISATION_DIR, CSV_DIR,
           MODELS_DIR, DATA_ROOT]:
    Path(_d).mkdir(parents=True, exist_ok=True)