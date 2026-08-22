#!/usr/bin/env python3
# Copyright (C) 2026 Wangjie Ma
# SPDX-License-Identifier: GPL-3.0-only
"""Inspect the released structure of a locally extracted DataPort package."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


REQUIRED_DIRECTORIES = (
    "01_FORCE_CONTACT_CALIBRATION",
    "02_MAGNETIC_DISTURBANCE",
    "03_CROSS_INSTANCE_CALIBRATION",
    "04_ROBOTIC_TASKS",
    "05_FIGURE_SOURCE_DATA",
    "06_PROVENANCE",
    "07_MODEL_TRAINING",
    "08_GUI_SOFTWARE",
)

SELECTED_CSV_FILES = (
    "01_FORCE_CONTACT_CALIBRATION/location_trial_metrics.csv",
    "02_MAGNETIC_DISTURBANCE/unloaded_raw.csv",
    "03_CROSS_INSTANCE_CALIBRATION/learning_curve.csv",
    "04_ROBOTIC_TASKS/solder_paste/fig13_paste_plot.csv",
    "05_FIGURE_SOURCE_DATA/fig7_force/fx_scatter.csv",
)

SELECTED_JSON_FILES = (
    "01_FORCE_CONTACT_CALIBRATION/force_summary_table2.json",
    "01_FORCE_CONTACT_CALIBRATION/location_summary.json",
    "02_MAGNETIC_DISTURBANCE/acquisition_summary.json",
    "07_MODEL_TRAINING/model/model_manifest.json",
)


def inspect_csv(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        columns = next(reader, [])
        rows = sum(1 for _ in reader)
    return {"rows": rows, "columns": columns}


def inspect_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(value, dict):
        return {"type": "object", "top_level_keys": sorted(value.keys())}
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    return {"type": type(value).__name__}


def inspect_package(package: Path) -> dict[str, Any]:
    package = package.resolve()
    if not package.is_dir():
        raise ValueError(f"Package directory does not exist: {package}")

    missing_directories = [
        name for name in REQUIRED_DIRECTORIES if not (package / name).is_dir()
    ]
    if missing_directories:
        joined = ", ".join(missing_directories)
        raise ValueError(f"Missing required package directories: {joined}")

    csv_reports: dict[str, Any] = {}
    json_reports: dict[str, Any] = {}
    missing_files: list[str] = []

    for relative in SELECTED_CSV_FILES:
        path = package / relative
        if path.is_file():
            csv_reports[relative] = inspect_csv(path)
        else:
            missing_files.append(relative)

    for relative in SELECTED_JSON_FILES:
        path = package / relative
        if path.is_file():
            json_reports[relative] = inspect_json(path)
        else:
            missing_files.append(relative)

    return {
        "package_name": package.name,
        "required_directories_present": not missing_directories,
        "selected_csv_files": csv_reports,
        "selected_json_files": json_reports,
        "missing_selected_files": sorted(missing_files),
    }


def print_text(report: dict[str, Any]) -> None:
    print(f"Package: {report['package_name']}")
    print("Required directories: present")
    print("Selected CSV files:")
    for relative, details in report["selected_csv_files"].items():
        print(
            f"  - {relative}: {details['rows']} rows, "
            f"{len(details['columns'])} columns"
        )
    print("Selected JSON files:")
    for relative, details in report["selected_json_files"].items():
        print(
            f"  - {relative}: {details['type']}, "
            f"{len(details.get('top_level_keys', []))} top-level keys"
        )
    if report["missing_selected_files"]:
        print("Missing selected files:")
        for relative in report["missing_selected_files"]:
            print(f"  - {relative}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect selected files in a local Spring-Hall DataPort export."
    )
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = inspect_package(args.package)
    except (OSError, ValueError, json.JSONDecodeError, csv.Error) as exc:
        raise SystemExit(f"Inspection failed: {exc}") from exc

    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text(report)
    return 1 if report["missing_selected_files"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
