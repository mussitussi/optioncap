from enum import Enum, auto


class Color(Enum):
    w = auto()
    b = auto()


class OptCap:
    def __init__(self, tag: Color, inst_id: str, x: str):
        self.tag = tag
        self.instr_id = inst_id
        self.x = x  # represents the maturity, premium, and strike price

    def __eq__(self, other):
        if not isinstance(other, OptCap):
            return False

        return self.x == other.x

    def __str__(self):
        name = OptCap.__name__
        return f"{name}(tag={self.tag.name}, id={self.instr_id}, x={self.x})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.x)
