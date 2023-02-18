"""Main module."""
import logging
import os

import appdirs
from cachelib import FileSystemCache, NullCache


CACHE_EMPTY_VAL = "NULL"
CACHE_DIR = appdirs.user_cache_dir("xlsx_automate")
CACHE_ENTRY_MAX = 128


if os.getenv("XLSX_DISABLE_CACHE"):
    # works like an always empty cache
    cache = NullCache()
else:
    cache = FileSystemCache(CACHE_DIR, CACHE_ENTRY_MAX, default_timeout=0)


def _get_from_cache(cache_key):
    # As of cachelib 0.3.0, it internally logging a warning on cache miss
    current_log_level = logging.getLogger().getEffectiveLevel()
    # Reduce the log level so the warning is not printed
    logging.getLogger().setLevel(logging.ERROR)
    area = cache.get(cache_key)  # pylint: disable=assignment-from-none
    # Restore the log level
    logging.getLogger().setLevel(current_log_level)
    return area


def _clear_cache():
    global cache  # pylint: disable=global-statement,invalid-name
    if not cache:
        cache = FileSystemCache(CACHE_DIR, CACHE_ENTRY_MAX, 0)

    return cache.clear()


# cache.set(cache_key, res) <= for setting cache values

if __name__ == "__main__":
    pass
    # load workbook
    # workbook = open(xlsx_file)

    # # get active worksheet
    # ws = workbook.active

    # # find column by title

    # col = find_column(ws)  # param: query_string="area" => (3, 'Area')

    # # get all data from column column_idx => 3
    # data = get_column_data(ws, column_idx=col.col_idx)
    # print(data)

    # # get all rows data
    # data = get_rows_data(ws)
    # print(data)

    # insert area column
    # insert_area_column(ws, workbook, find_column(ws[1])[0], xlsx_file)

    # set rows data
    # set_rows_data(ws, find_column(ws[1])[0], area_data)
