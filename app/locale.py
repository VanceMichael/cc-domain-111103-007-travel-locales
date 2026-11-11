import json
from pathlib import Path

def read_page(path):
    value=json.loads(Path(path).read_text(encoding="utf-8"))
    for key in ("url","locale","title","body"):
        if key not in value: raise ValueError("页面缺少字段："+key)
    return value
