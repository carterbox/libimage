"""libimage provides color images from Wikimedia Commons.

The images have been cropped (modified) to a 2048 x 2048 size.

All images in this library require attribution, but all the images are all
licensed under the (Creative Commons Attribution-Share Alike license)[
https://creativecommons.org/licenses/by-sa/3.0/deed.en] which means they may be
used for free and for whatever purpose. Citation information is included in the
citations.bib file. Each image has a separate attribution.
"""
import lzma
import os.path
import pickle
import warnings

import numpy as np

__root__ = os.path.dirname(__file__)

def _downsample(rgb, size):
    """Shrink the 2048 x 2048 rgb image to size  x size by averaging pixels."""
    rgb = rgb.reshape(size, 2048 // size, size, 2048 // size, 3)
    return np.mean(rgb, axis=(1, 3))

def load(name, size=2048, color=False):
    """Return an image from the library by name.

    Images are stored as LZMA compressed pickles and returned as NumPy arrays.

    Parameters
    ----------
    size : 1 <= power of 2 <= 2048
        The width of the requested image.
    color : bool
        Whether the returned image is three channel color. Grey by default.
    """
    warnings.warn("Using images from this library requires attribution to "
                  "their original creators. See the module docs for citation "
                  "details.")
    if size > 2048 or 2048 % size != 0:
        raise ValueError('size can only be powers of 2 <= 2048.')
    filename = os.path.join(__root__, f"{name}.lzma.p")
    with lzma.open(filename, "rb") as f:
        rgb = pickle.load(f) / 255
    rgb = _downsample(rgb, size)
    if color:
        return rgb
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def _save(name):
    """Convert an RGB PNG to LZMA compressed pickle."""
    import skimage.io
    rgb = skimage.io.imread(f'{name}-2048.png')
    filename = os.path.join(__root__, f"{name}.lzma.p")
    with lzma.open(filename, "wb", preset=9) as f:
        pickle.dump(rgb, f)
