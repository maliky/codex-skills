from __future__ import annotations

import os
import shutil
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "tu-curriculum-transformation"
    / "scripts"
    / "export_org_curriculum.el"
)


@unittest.skipUnless(shutil.which("emacs"), "Emacs is not installed")
class ExportCurriculumTests(unittest.TestCase):
    def run_export(self, lualatex_exit: int | None) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "source.org"
            source.write_text("#+TITLE: Test\n* Heading\nBody\n", encoding="utf-8")
            fake_bin = temp / "bin"
            fake_bin.mkdir()
            if lualatex_exit is not None:
                lualatex = fake_bin / "lualatex"
                lualatex.write_text(
                    f"#!/bin/sh\nexit {lualatex_exit}\n", encoding="utf-8"
                )
                lualatex.chmod(lualatex.stat().st_mode | stat.S_IXUSR)
            env = os.environ.copy()
            env["PATH"] = str(fake_bin)
            return subprocess.run(
                [
                    str(shutil.which("emacs")),
                    "--batch",
                    "--quick",
                    "--load",
                    str(SCRIPT),
                    "--",
                    str(source),
                ],
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_successful_lualatex_returns_zero(self) -> None:
        result = self.run_export(0)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_lualatex_keeps_successful_tex_export(self) -> None:
        result = self.run_export(None)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_failing_lualatex_returns_nonzero(self) -> None:
        result = self.run_export(7)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("lualatex pass 1 failed", result.stderr)


if __name__ == "__main__":
    unittest.main()
