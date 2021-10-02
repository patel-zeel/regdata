from .base import Base

class MotorcycleHelmet(Base):
    def __init__(self, return_test=True, scale_X = True, scale_y = False, 
                mean_normalize_y=True, noisy=True, test_train_ratio=2, s_to_n_ratio=20,
                noise_variance=None, scaler='std', random_state=0, backend=None):

        name = 'motorcycle_helmet.csv'
        X, y, Xnames, ynames = self.check_download_and_get(name)

        super().__init__(X, y, Xnames, ynames, return_test, scale_X, scale_y, 
                mean_normalize_y, noisy, test_train_ratio, s_to_n_ratio,
                noise_variance, scaler, random_state, backend=backend)