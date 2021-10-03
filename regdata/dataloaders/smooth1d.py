import numpy as np
from .base import Base

class Smooth1D(Base):
    def __init__(self, return_test=True, scale_X = True, scale_y = False, 
                mean_normalize_y=True, test_train_ratio=2, 
                s_to_n_ratio=10, noise_variance=None, scaler='std', 
                min=-2, max=2, samples=101, random_state=0, backend=None):

        synthetic = True
        file_name = None
        f = lambda x: np.sin(x) + 2 * np.exp(-30 * np.square(x)) 
        X = np.linspace(min, max, samples).reshape(-1,1)
        y = f(X)

        X_names = ['X']
        y_names = ['y']
        super().__init__(X=X, 
                         y=y,
                         file_name=file_name, 
                         f=f,                        
                         X_names=X_names,
                         y_names=y_names,
                         return_test=return_test,
                         scale_X=scale_X, 
                         scale_y=scale_y, 
                         mean_normalize_y=mean_normalize_y,
                         test_train_ratio=test_train_ratio, 
                         s_to_n_ratio=s_to_n_ratio,
                         noise_variance=noise_variance, 
                         scaler=scaler, 
                         backend=backend, 
                         random_state=random_state, 
                         synthetic=synthetic)