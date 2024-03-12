
from enum import Enum


class MpesaStatus(Enum):
    Pending = "Pending"
    Failed = "Failed"
    Canceled = "Canceled"
    Completed = "Completed"
    Invalid = "Invalid"
