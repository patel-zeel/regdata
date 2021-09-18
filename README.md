# RegData

Collection of regression datasets.

* Get data in any framework: ```torch```, ```tensorflow``` or ```numpy```

## Quick example

```python
from regdata import load_olympic, set_backend
set_backend('torch') # numpy, tf (numpy is default)
X, y, X_test = load_olympic()
```

## Plot datasets to have a quick glance

```python
from regdata import load_olympic
load_olympic.plot()
```

## Datasets

```python
from regdata import (
    load_olympic,
    load_step,
    load_motor,
    load_jump1d,
    load_smooth1d
)
```