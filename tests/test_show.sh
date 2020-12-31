#!/usr/bin/env bash

../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv \
    -o ../docs/source/_static/example_lobe.svg -M continuous -w 1 \
    -s 256 256 -S 0.69
../scripts/show_cerebellum.py -i ../sample_data/data_lobule.csv \
    -o ../docs/source/_static/example_lobule.svg -M discrete -w 1 \
    -s 256 256 -S 0.69

../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv \
    -o ../docs/source/_static/example_continuous_colormap.svg \
    -M continuous -w 1
../scripts/show_cerebellum.py -i ../sample_data/data_lobule.csv \
    -o ../docs/source/_static/example_discrete_colormap.svg \
    -M discrete -w 1

../scripts/show_cerebellum.py -i ../sample_data/pvals.csv \
    -o ../docs/source/_static/example_pvals.svg \
    -M discrete -w 1 -p

../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv \
    -o ../docs/source/_static/example_scale_annot.svg -M continuous \
    -w 5 -s 400 250 -S 0.6 -f 16 -a -T

../scripts/show_cerebellum.py \
    -o ../docs/source/_static/example_label_lobe.svg -l -w 1 -m lobe
../scripts/show_cerebellum.py \
    -o ../docs/source/_static/example_label_lobule.svg -l -w 1

../scripts/show_cerebellum.py \
    -o ../docs/source/_static/example_custom_labels.svg -l -w 1 \
    -m lobe -C colormap_label.txt -n "Left X" "Right X"

../scripts/show_cerebellum.py -i data.csv \
    -o ../docs/source/_static/example_custom_discrete.svg \
    -M discrete -w 1 -C colormap.txt

../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv -v 0 -V 3 \
    -o ../docs/source/_static/example_custom_continuous.svg \
    -M continuous -w 1 -c viridis -v -1 -V 1
