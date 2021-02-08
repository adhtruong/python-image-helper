from decimal import Decimal
from itertools import accumulate, chain, repeat, takewhile
from typing import Iterable


def float_range(start: float, stop: float, step: float) -> Iterable[float]:
    if not step:
        raise ValueError("Step can not be 0")

    step_value = Decimal(step)
    end_value = Decimal(stop)
    if step_value > 0:

        def predicate(current):
            return current < end_value

    else:

        def predicate(current):
            return end_value < current

    values = accumulate(chain([Decimal(start)], repeat(step_value)))
    yield from map(float, takewhile(predicate, values))
