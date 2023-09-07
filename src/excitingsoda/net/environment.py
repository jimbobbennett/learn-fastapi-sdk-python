"""
An enum class containing all the possible environments that 
a user can switch between in this SDK.
"""
from enum import Enum


class Environment(Enum):
    """The environments available for this SDK"""

    DEFAULT = "http://na.exciting.soda"
    NORTHAMERICA = "https://na.exciting.soda"
    EU = "https://eu.exciting.soda"
    APAC = "https://apac.exciting.soda"
