#!/bin/bash
set -e
cd "$(dirname "$0")/.."

echo "=== Compiling BibTeX ==="
python3 scripts/bib2yaml.py

echo "=== Generating authors ==="
python3 scripts/gen_authors.py

echo "=== Done ==="
