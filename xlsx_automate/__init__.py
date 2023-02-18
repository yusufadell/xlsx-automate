"""Top-level package for xlsx automate."""
import xlsx_automate._constants as constants

from xlsx_automate.conf import (
    xlsx_file,
    area_header,
    area_data,
    area_data_en,
    area_data_ar,
)
from xlsx_automate.utils import (
    xlsx_file,  # xlsx file path
    get_column_data,
    get_rows_data,
    find_column,
    insert_area_columns,
    set_rows_data,
    set_header_data,
    save_to_xlsx_file,
)

# Expose constants especially the version number
__author__ = constants.__author__
__email__ = constants.__email__
__version__ = constants.__version__
__python__ = constants.__python__
