#
# config.py
# A module for encapsulating config.ini interactions
#

import ConfigParser
import os


def get_config(section, key, is_int=False):
    """
    Use this function to easily interface with config.ini
    :param section: The section (e.g. [data]) in the config.ini file
    :param key: The key under the section
    :param is_int: If integer, convert before returning
    :return: The value in the config or None if it doesn't exists
    """
    # Get filepath
    this_filepath = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_filepath)
    config_filepath = os.path.join(this_dir, '../config.ini')

    # Initialize config
    config = ConfigParser.ConfigParser()
    config.read(config_filepath)

    # Verify exists
    if not config.has_option(section, key):
        return None

    # Return key from section
    if is_int:
        return config.getint(section, key)
    else:
        return config.get(section, key)
