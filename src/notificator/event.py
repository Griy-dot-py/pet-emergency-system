from dataclasses import dataclass


@dataclass
class NotificationEvent:
    address: str
    message: str
