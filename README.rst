A package for monitoring Docker containers
==========================

Monitor Docker containers using the Docker Remote API.

To use as a package:

    >>> from conmon.monitor import server_up, all_containers_up
    >>> server_up()
    True
    >>> all_containers_up()
    True
    >>>

To use as a script:

    $ python -m conmon [-h] [-t] service

    Display True if docker server is up.

    positional arguments:
      service     which service to check; one of [server, containers]

    optional arguments:
      -h, --help  show this help message and exit
      -t          Display elapsed time (default: False)
