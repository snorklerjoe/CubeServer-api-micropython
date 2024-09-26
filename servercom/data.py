"""Data representations for communicating with CubeServer.
"""

from collections import namedtuple
from json import dumps
from ._utils import enum

DEGREE_SIGN = u"\xb0"


GameStatus = namedtuple("GameStatus",
                        ['time',
                         'score',
                         'CubeServer_version']
                        )

HTTPResponse = namedtuple("HTTPResponse",
                          ['code', 'body']
                          )


class Email:
    """Holds an email to be sent to the team"""

    def __init__(self, subject, message) -> None:
        self.subject = subject
        self.message = message

    def dumps(self) -> str:
        return dumps(
            {
                'subject': self.subject,
                'message': self.message
            }
        )


DataClass = enum(
    TEMPERATURE="temperature",
    PRESSURE="pressure",
    COMMENT="comment",
    BATTERY="battery voltage",
    BEACON="beacon challenge"
)


class DataPoint():
    """A class for storing and handling datapoints"""

    @property
    def UNIT(self) -> str:
        """A standard string representation of the unit for this datapoint"""
        raise NotImplementedError("Subclasses must define UNIT")

    def __init__(self, data_class: 'DataClass', value: int | float | str):
        """Initializes a piece of data to send to the server"""
        self.data_class = data_class
        self.value = value

    def dumps(self) -> str:
        """Dumps a JSON string out that the server will (hopefully) accept"""
        return dumps(
            {
                "type": self.data_class,
                "value": self.value
            }
        )

    def __str__(self) -> str:
        return f"{self.value} {self.UNIT}"


class Temperature(DataPoint):
    """A class for DataPoints that store temperature values"""
    UNIT = f"{DEGREE_SIGN}F"

    def __init__(self, value):
        super().__init__(DataClass.TEMPERATURE, value)


class Pressure(DataPoint):
    """A class for DataPoints that store barometric pressure values"""
    UNIT = "inHg"

    def __init__(self, value):
        super().__init__(DataClass.PRESSURE, value)


class Text(DataPoint):
    """A class reserved for DataPoints that are intended as a text comment"""
    UNIT = ""  # No unit for regular strings of text

    def __init__(self, value: str):
        super().__init__(DataClass.COMMENT, value)


class BeaconChallenge(DataPoint):
    """A class reserved for DataPoints that are in response to a message from the beacon"""
    UNIT = ""  # No unit for regular strings of text

    def __init__(self, value: str):
        super().__init__(DataClass.BEACON, value)


class BatteryLevel(DataPoint):
    """A class reserved for DataPoints that are intended as an indication of battery level"""
    UNIT = "V"

    def __init__(self, value: float):
        super().__init__(DataClass.BATTERY, value)
