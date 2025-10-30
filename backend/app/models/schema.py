from pydantic import BaseModel
from typing import List, Dict

class CSVInfo(BaseModel):
    columns: List[str]
    types: Dict[str,str]
    preview: List[Dict]
