import sklearn
# make sure that the usage of the library is not possible
# without metadata routing being enabled in the configuration
sklearn.set_config(enable_metadata_routing=True)

from . import model_selection
from . import metrics
from .base import BaseAdapter
from ._mapping import (
    ClassRegularizerOTMappingAdapter,
    CORALAdapter,
    EntropicOTMappingAdapter,
    LinearOTMappingAdapter,
    OTMappingAdapter,
)
from ._reweight import (
    DiscriminatorReweightDensityAdapter,
    GaussianReweightDensityAdapter,
    KLIEPAdapter,
    ReweightDensityAdapter,
)
from ._subspace import (
    SubspaceAlignmentAdapter,
    TransferComponentAnalysisAdapter,
)
from ._pipeline import make_da_pipeline


__all__ = [
    "metrics",
    "model_selection",

    "BaseAdapter",

    "ClassRegularizerOTMappingAdapter",
    "CORALAdapter",
    "EntropicOTMappingAdapter",
    "LinearOTMappingAdapter",
    "OTMappingAdapter",

    "DiscriminatorReweightDensityAdapter",
    "GaussianReweightDensityAdapter",
    "KLIEPAdapter",
    "ReweightDensityAdapter",

    "SubspaceAlignmentAdapter",
    "TransferComponentAnalysisAdapter",

    "make_da_pipeline",
]
