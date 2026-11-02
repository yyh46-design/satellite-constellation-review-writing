"""Current V3.1 checks. Historical comparison is preserved in Git at 297ea57."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("verify_current.py")),run_name="__main__")
