#!/usr/bin/env bash

../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv \
    -o results/continuous_lobe.svg -M continuous -w 1
../scripts/show_cerebellum.py -i ../sample_data/data_lobule.csv \
    -o results/discrete_lobule.svg -M discrete -w 1
../scripts/show_cerebellum.py -i ../sample_data/pvals.csv \
    -o results/pvals.svg -M discrete -w 1 -p
../scripts/show_cerebellum.py -i ../sample_data/data_lobe.csv \
    -o results/continuous_vmin.svg -M continuous -w 2 -v -1 -V 1 \
    -s 320 250 -S 0.6 -f 16 -a -T
../scripts/show_cerebellum.py -o results/label_lobe.svg -l -w 1 -m lobe
../scripts/show_cerebellum.py -o results/label_lobule.svg -l -w 1
../scripts/show_cerebellum.py -o results/label_lobe_colormap.svg -l -w 1 \
    -m lobe -C colormap_label.txt -n "Left X" "Right X"
../scripts/show_cerebellum.py -i data.csv \
    -o results/discrete_colormap.svg -M discrete -w 1 -C colormap.txt
../scripts/show_cerebellum.py -i data.csv -v 0 -V 3 \
    -o results/continuous_colormap.svg -M discrete -w 1 -c hot
