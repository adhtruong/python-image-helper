from decimal import Decimal
from typing import Iterator


def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    if not step:
        raise ValueError("Step can not be 0")

    step_decimal = Decimal(step)
    if step_decimal > 0:
        while start < stop:
            yield float(start)
            start += step_decimal
    else:
        while stop < start:
            yield float(start)
            start += step_decimal
