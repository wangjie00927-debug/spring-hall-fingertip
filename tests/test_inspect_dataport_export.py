# Copyright (C) 2026 Wangjie Ma
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))

from inspect_dataport_export import (  # noqa: E402
    REQUIRED_DIRECTORIES,
    SELECTED_CSV_FILES,
    SELECTED_JSON_FILES,
    inspect_package,
)


class InspectDataPortExportTests(unittest.TestCase):
    def test_complete_fixture(self) -> None:
        package = ROOT / "tests" / "fixtures" / "package"
        report = inspect_package(package)
        self.assertTrue(report["required_directories_present"])
        self.assertEqual(report["missing_selected_files"], [])
        self.assertEqual(len(report["selected_csv_files"]), len(SELECTED_CSV_FILES))
        self.assertEqual(len(report["selected_json_files"]), len(SELECTED_JSON_FILES))

    def test_missing_required_directory(self) -> None:
        package = ROOT / "tests" / "fixtures" / "incomplete_package"
        with self.assertRaisesRegex(ValueError, "Missing required package directories"):
            inspect_package(package)


if __name__ == "__main__":
    unittest.main()
