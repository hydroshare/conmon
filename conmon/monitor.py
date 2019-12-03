"""
Monitor Docker containers
"""

import os
import logging
import docker

LOGFILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "conmon.log")
FORMAT = "%(asctime)-15s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT,
                    filename=LOGFILE)


def server_up():
    """
    server_up() -> bool

    Return True if docker daemon is up.
    """

    rc = False
    try:
        client = docker.from_env()
        rc = client.ping()
        if rc:
            logging.info("Docker daemon up.")
        else:
            logging.warning("Docker daemon down.")
    except:
        logging.error("Exception occurred whilc checking docker daemon:", exc_info=True)
    return rc


def all_containers_up():
    """
    all_containers_up() -> bool

    Return True if all containers up.
    """

    rc = False
    try:
        client = docker.from_env()
        statuses = {container.name : (container.status == "running") for container in client.containers.list()}
        if all(statuses.values()):
            rc = True
            logging.info("All containers up.")
        else:
            down_containers = [key for key, value in statuses.items() if not value]
            logging.warning(f"Down containers: {down_containers}")
    except:
        logging.error("Exception occurred while checking container statuses:", exc_info=True)
    return rc
