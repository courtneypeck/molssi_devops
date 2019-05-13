"""
molssi_devops
Package containing useful math functions
"""

# Add imports here
from .molssi_math import mean, canvas
from .util import title_case

=======
from .molssi_math import *
from .util import *
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
