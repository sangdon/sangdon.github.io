#!/bin/bash
set -e
cd "$(dirname "$0")/../team-src/CV"

latexmk -lualatex -jobname=CV -outdir=.build -interaction=nonstopmode -halt-on-error main.tex > .build.log 2>&1 \
  || { echo "CV compile failed; see team-src/CV/.build.log"; tail -30 .build.log; exit 1; }
cp .build/CV.pdf ../CV.pdf
echo "CV.pdf updated"
