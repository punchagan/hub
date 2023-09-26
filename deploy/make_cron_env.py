#!/usr/bin/env python

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent

ENV = ["PATH", "DJANGO_SETTINGS_MODULE"]


def main() -> None:
    cron_dir = ROOT / "cron"
    os.makedirs(cron_dir, exist_ok=True)
    with open(cron_dir / "env", "w") as f:
        for var in ENV:
            value = os.environ.get(var)
            f.write(f"export {var}={value}\n")
        f.write("cd $HOME/app\n")


if __name__ == "__main__":
    main()
