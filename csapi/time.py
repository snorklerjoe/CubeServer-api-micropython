"""Timing, scheduling, and timeout utilities
"""

import time as systime

SECONDS_PER_MIN = 60
SECONDS_PER_HOUR = 60*60
SECONDS_PER_DAY = 60*60*24


def lightsleep(seconds: int):
    """ Temporary light sleep
    Forces the microcontroller to light sleep for a given number of seconds.

    seconds (int): Number of seconds to sleep for
    """


def timeout(seconds: int, function: callable):
    """ Time out of a function
    Utilizes the microcontroller's watchdog timer to set a time limit on a function.
    If the function returns before the specified timeout, nothing happens.

    If the watchdog is already in use, this will raise an exception.

    seconds (int): Maximum number of seconds to allow the function to run for
    function (callable): Function to run
    """


def time() -> int:
    """ UNIX timestamp

    Returns the current number of seconds since midnight (UTC) on 1 Jan 1970.
    This is different than the built-in `time.time()`, because it will account for the time adjustment
    upon syncing with the server. If it has not been synced with the server, this will raise
    an exception.
    """

    return -1


def get_offset() -> int:
    """ Unix time/monotonic offset

    Returns `<UNIX timestamp> - <monotonic time>`.
    This is updated whenever time is synced with the server.
    If the time has not been synced with the server, this will raise an exception.
    """

    return -1


def time_hrs_min_sec() -> tuple[int, int, int]:
    """ Tuple-format time

    Returns the tuple `(hours, minutes, seconds)` since the start of the day (24-hour time).
    i.e. if it is 12 seconds after 7:03pm, this function will return the tuple `(19, 3, 12)`.
    """
    epoch_time: int = time()
    seconds: int = epoch_time % SECONDS_PER_MIN
    minutes: int = epoch_time % SECONDS_PER_HOUR // SECONDS_PER_MIN
    hours:   int = epoch_time % SECONDS_PER_DAY // SECONDS_PER_HOUR

    return (hours, minutes, seconds)
