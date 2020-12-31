# Cerebellum Value Map

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This package can show values as colors on top of a cerebellum illustration:

![example_lobe](https://raw.githubusercontent.com/shuohan/cerebellum-value-map/master/docs/source/_static/example_lobe.svg) ![example_lobule](https://raw.githubusercontent.com/shuohan/cerebellum-value-map/master/docs/source/_static/example_lobules.svg)

It is used in the paper [Longitudinal analysis of regional cerebellum volumes during normal aging](https://www.sciencedirect.com/science/article/pii/S1053811920305486?via%3Dihub).

### Install

Install from GitHub:

```bash
   pip install git+https://github.com/shuohan/cerebellum-value-map
```

Install from PyPI:

```bash
   pip install cerebellum-value-map
```

Use the source code:

```bash
   git clone https://github.com/shuohan/cerebellum-value-map
   # see https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
   export PYTHONPATH=$(realpath cerebellum-value-map):$PYTHONPATH
   cd cerebellum-value-map/scripts
   ./show_cerebellum.py -h
```

See the [documentation](https://shan-utils.gitlab.io/cerebellum-value-map) for more details.
