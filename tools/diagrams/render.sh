#!/bin/sh
# Renders the Graphviz diagrams of the docs (tools/diagrams/*.dot) into static/images/diagrams/.
# Needs Graphviz (`dot`). Run from anywhere: sh tools/diagrams/render.sh
set -e
here=$(dirname "$0")
out="$here/../../static/images/diagrams"
mkdir -p "$out"
for source in "$here"/*.dot; do
	name=$(basename "$source" .dot)
	dot -Tsvg "$source" -o "$out/$name.svg"
	echo "wrote $name"
done
