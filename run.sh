#!/bin/bash
# usage: ./run.sh 01_two_sum dfs.rs
set -e

PROB=$1
SOL=$2

SRC="src/problems/$PROB/$SOL"
OUT_DIR="target/run/$PROB"
OUT="$OUT_DIR/$SOL"

if [ ! -f "$SRC" ]; then
  echo "Error: $SRC not found"
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "=== Building $SRC ==="
rustc "$SRC" -o "$OUT"

echo "=== Running $PROB/$SOL ==="
"$OUT"
