import os
import tempfile
from functools import partial
from typing import Callable, Iterable, Tuple, TypeVar

import cv2

from .canvas import Canvas

_RENDER_STATE_TYPE = TypeVar("_RENDER_STATE_TYPE")
_RENDER_METHOD = Callable[[_RENDER_STATE_TYPE], Tuple[Canvas, _RENDER_STATE_TYPE]]


def _render_frame(render_method: _RENDER_METHOD, state: int) -> os.PathLike:
    canvas = render_method(state)
    file, path = tempfile.mkstemp(suffix=".png")
    os.close(file)
    canvas.write_to_png(path)
    return path


def create_video_from_images(paths: Iterable[os.PathLike], frame_rate: int, output_path: os.PathLike) -> None:
    if frame_rate <= 0:
        raise ValueError("Frame rate must be positive")

    paths = iter(paths)
    first_path = next(paths)
    width, height = cv2.imread(first_path).shape[:2]

    codec = cv2.VideoWriter_fourcc(*"H264")
    out = cv2.VideoWriter(output_path, codec, frame_rate, (width, height))
    for path in (first_path, *paths):
        out.write(cv2.imread(path))
    out.release()


def render_canvases(render_method: _RENDER_METHOD, frames: int, frame_rate: int, output_path: os.PathLike) -> None:
    if frames <= 0:
        raise ValueError("Number of frames must be positive")

    render_frame = partial(_render_frame, render_method)
    paths = map(render_frame, range(frames))
    create_video_from_images(paths, frame_rate, output_path)
