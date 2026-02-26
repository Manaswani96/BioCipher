from pathlib import Path
import runpy

HERE = Path(__file__).parent

for name in ["demo_sequence.py", "demo_spectrum.py"]:
    print("\n" + "=" * 60)
    print(f"Running {name}")
    print("=" * 60)
    runpy.run_path(str(HERE / name), run_name="__main__")
