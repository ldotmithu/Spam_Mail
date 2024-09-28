from dataclasses import dataclass
from pathlib import Path

class DataIngestion:
    root_dir:Path
    URL:str
    local_data_path:Path
    unzip_dir:Path