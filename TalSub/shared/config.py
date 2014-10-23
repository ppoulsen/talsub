import ConfigParser, os


def get_config(section, key, is_int=False):
    # Get filepath
    this_filepath = os.path.abspath(__file__)
    this_dir = os.path.pardir(this_filepath)
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
