from enum import Enum


class PatternType(Enum):
    KNIT = "knitting pattern"
    SEW = "sewing pattern"





class Pattern:
    def __init__(self,name,attributes = None):
        self.name = name
        self.attributes = attributes


    def __repr__(self):
        return f"Pattern object({self.name})"
    





class KnittingPattern(Pattern):
    def __init__(self,name,attributes=None):
        super().__init__(name,attributes)
        