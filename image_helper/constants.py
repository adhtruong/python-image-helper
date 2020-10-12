from enum import Enum

from cairo import LINE_CAP_BUTT, LINE_CAP_ROUND, LINE_CAP_SQUARE, LINE_JOIN_BEVEL, LINE_JOIN_MITER, LINE_JOIN_ROUND

from image_helper.models import Colour

BLACK = Colour(0, 0, 0)
WHITE = Colour(1, 1, 1)


class LineCap(Enum):
    BUTT = LINE_CAP_BUTT
    ROUND = LINE_CAP_ROUND
    SQUARE = LINE_CAP_SQUARE


class LineJoin(Enum):
    BEVEL = LINE_JOIN_BEVEL
    MITER = LINE_JOIN_MITER
    ROUND = LINE_JOIN_ROUND
