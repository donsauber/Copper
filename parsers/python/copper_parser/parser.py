"""
Copper (.copr) Parser — Python reference implementation
"""

from pathlib import Path

def parse_copr(path):
    """Parse a .copr file into a nested dictionary."""
    data, section, subsection = {}, None, None
    lines = Path(path).read_text(encoding="utf-8").splitlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith(("#", "//")):
            continue

        if line.startswith("{") and line.endswith("}"):
            section = line.strip("{}= ").strip()
            data[section] = {}
            subsection = None

        elif line.startswith("[") and line.endswith("]"):
            subsection = line.strip("[]- ").strip()
            data[section][subsection] = {}

        elif ":" in line and section:
            k, v = [p.strip() for p in line.split(":", 1)]
            target = data[section][subsection] if subsection else data[section]
            target[k] = v

    return data
