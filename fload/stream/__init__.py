from ..base import Pipeline
from .source.csv import CSVSource
from .pipeline.last_field_to_file import LastFieldToFile

csvsource = CSVSource
last_field_to_field = LastFieldToFile
