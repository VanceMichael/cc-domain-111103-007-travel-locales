from pathlib import Path
from app.locale import read_page
print(read_page("fixtures/zh.json")["alternate"])
