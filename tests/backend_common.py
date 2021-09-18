from lib import *

def backend_test(func, **kwargs):
    import regdata
    regdata.set_backend('numpy')
    X, y, X_test = func(**kwargs).get_data()
    assert X.dtype == y.dtype == X_test.dtype == np.float64
    regdata.set_backend('torch')
    X, y, X_test = func(**kwargs).get_data()
    assert X.dtype == y.dtype == X_test.dtype == torch.float64
    regdata.set_backend('tf')
    X, y, X_test = func(**kwargs).get_data()
    assert X.dtype == y.dtype == X_test.dtype == tf.float64