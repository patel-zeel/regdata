# RegData

Collection of regression datasets.

* Get data in any framework: ```torch```, ```tensorflow``` or ```numpy```

## Quick example

```python
import regdata as rd
rd.set_backend('torch') # numpy, tf (numpy is default)
X, y, X_test = rd.Step().get_data()
```

## Plot datasets to have a quick glance

```python
import regdata as rd
rd.Olympic().plot()
```

## Datasets

```python
from regdata import (
    Step,
    Olympic,
    Smooth1D
)
```

## References

* [Step](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
* [Olympic](http://inverseprobability.com/talks/notes/deep-gaussian-processes.html)
* [Smooth1D](http://www.stat.cmu.edu/~kass/papers/bars.pdf) - Example 2