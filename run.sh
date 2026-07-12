#!/bin/bash
set -e

for script in Code/[0-9][0-9]_*.ipynb; do
    echo "=================================="
    echo "Running $(basename "$script")"
    echo "=================================="
    jupyter nbconvert --to notebook --execute "$script" --output "executed_$(basename "$script")"
done

echo "Pipeline completed successfully."