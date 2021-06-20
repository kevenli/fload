from ..base import Pipeline, Source
from .source.csv import CSVSource
from .source.range import RangeSource
from .pipeline.last_field_to_file import LastFieldToFile

csv = CSVSource
last_field_to_field = LastFieldToFile
range = RangeSource
