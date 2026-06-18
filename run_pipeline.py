import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

def run_step(script):
    path = BASE / "scripts" / script

    print(f"\n🚀 Running {script} ...")

    result = subprocess.run([sys.executable, str(path)])

    if result.returncode != 0:
        print(f"❌ Failed: {script}")
        sys.exit(1)

    print(f"✅ Completed: {script}")

def main():
    run_step("DataIngest.py")
    run_step("TransformWeather.py")
    run_step("Load-db.py")

    print("\n🎉 FULL PIPELINE COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()