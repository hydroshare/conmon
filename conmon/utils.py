"""
Utilities for the conmon package.
"""

import os
import yaml

config_filespec = os.environ("CONMON_CONFIG_FILE")


def config():
    """
    config() -> dict

    Return the configuration dictionary.
    """

    with open(config_filespec) as configfile:
        cfg = yaml.load(configfile, Loader=yaml.SafeLoader)
    return cfg
