from decimal import Decimal
from typing import Iterator


def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    if not step:
        raise ValueError("Step can not be 0")

    current = Decimal(start)
    step_decimal = Decimal(step)
    if step_decimal > 0:
        while current < stop:
            yield float(current)
            current += step_decimal
    else:
        while stop < current:
            yield float(current)
            current += step_decimal
