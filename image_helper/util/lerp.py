def lerp(value: float, min_current: float, max_current: float, min_new: float, max_new: float) -> float:
    offset = (value - min_current) / (max_current - min_current)
    return min_new + offset * (max_new - min_new)
