from dataclasses import dataclass


@dataclass
class MenuEntity:
    id: int = None
    time: str = None
    menu: str = None
    day: int = None

