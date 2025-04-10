class Config:
    # Audio processing parameters
    RATE = 16000
    MAX_PARTIAL_SECONDS = 6
    PROCESS_INTERVAL = 0.5
    
    # Silence detection parameters
    SILENCE_THRESHOLD = 0.005
    SILENCE_DURATION = 2.0
    
    # Model configuration
    MODEL_TYPE = "huggingface"  # Options: "vosk" or "huggingface"
    
    # Model specific settings
    VOSK_MODEL_PATH = "models/vosk-model-small-en-us-0.15"
    # HUGGINGFACE_MODEL = "openai/whisper-large-v3-turbo"
    HUGGINGFACE_MODEL = "openai/whisper-tiny"
    
    # Server settings
    HOST = "127.0.0.1"
    PORT = 8000