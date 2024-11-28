import tempfile
import shutil
import logging
from pathlib import Path

from git import Repo


def gpkgs():
    current_gpkgs = {"BRA": 205215006, "ARG": 9677025}

    url = "https://github.com/AlertaDengue/satellite-weather-downloader.git"
    src = "satellite/data/gpkgs"
    dst = Path(__file__).parent / "gpkgs"

    def check_integrity(locale, size_in_bytes):
        size = 0

        if locale == "BRA":
            data = dst / "BRA"
            for file in data.rglob("BRA*.zip"):
                size += file.stat().st_size
        else:
            file = dst / f"{locale}.zip"
            if file.exists():
                size += file.stat().st_size

        return size == size_in_bytes

    if dst.exists():
        if all(check_integrity(loc, s) for loc, s in current_gpkgs.items()):
            return
        logging.warning("inconsistency found on %s", dst)

    shutil.rmtree(str(dst), ignore_errors=True)
    with tempfile.TemporaryDirectory() as tmp:
        logging.info("donwloading GPKG files")
        Repo.clone_from(url, tmp, depth=1)
        shutil.copytree(str(Path(tmp) / src), str(dst))

    if not all(check_integrity(loc, s) for loc, s in current_gpkgs.items()):
        gpkgs()
