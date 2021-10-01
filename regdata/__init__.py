from ._version import version as __version__ 

import os
os.environ['BACKEND'] = 'numpy'
os.environ['DATAPATH'] = '/tmp/somerandomtexthere_'

from .config import set_backend


# Dataloaders
from .dataloaders.step import Step
from .dataloaders.smooth1d import Smooth1D
from .dataloaders.olympic import Olympic