# RegData

[![CI](https://github.com/patel-zeel/regdata/workflows/CI/badge.svg)](https://github.com/patel-zeel/regdata/actions?query=workflow%3ACI)
[![Coverage Status](https://coveralls.io/repos/github/patel-zeel/regdata/badge.svg?branch=main)](https://coveralls.io/github/patel-zeel/regdata?branch=main)

A collection of regression datasets.

## Install
```bash
pip install regdata
```
## Quick example

```python
import regdata as rd
rd.set_backend('torch') # numpy, tf (numpy is default)
X, y, X_test = rd.Step().get_data() # Loads step function dataset
```

## Features

* Simple API for quick benchmarking on various datasets.
* Get data in any framework: ```torch```, ```tensorflow``` or ```numpy``` by setting a global backend.
* Scale ```X``` and/or ```y``` data with ```MinMaxScaler``` or ```StandardScaler```.
* Get ```y``` in squeezed ```(n,)``` or unsqueezed ```(n,1)``` format.
* Perform only mean normalization on ```y```.
* Add custom noise to the observations (```y```).
* Get consistent data with fixed random seed.

## Plot datasets to have a quick glance

```python
import regdata as rd
rd.Olympic().plot()
```

Checkout all plots [here](https://nbviewer.jupyter.org/github/patel-zeel/regdata/blob/main/notebooks/visualize.ipynb).

## Datasets

```python
from regdata import (
    DellaGattaGene,
    MotorcycleHelmet,
    Olympic,
    SineJump1D,
    Smooth1D,
    Step
)
```

## References

* [DellaGattaGene](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
* [MotorcycleHelmet](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
* [Olympic](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
* [SineJump1D](https://github.com/jmetzen/gp_extras/blob/master/examples/plot_gpr_lls.py)
* [Smooth1D](http://www.stat.cmu.edu/~kass/papers/bars.pdf) - Example 2
* [Step](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
