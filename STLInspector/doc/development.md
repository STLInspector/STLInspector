# STLInspector development information

## Install from source

1. Install the required package: `pip install pypandoc`
2. Build the stlinspector package: `python generate_distribution.py`
3. Install the stlinspector package: `python setup.py` or `python setup.py develop`

## Testing

Tests for the core of STLInspector are available. The tests can be executed with `python -m unittest discover`.

## Bump version

Edit `STLInspector/VERSION` and increase version number according to semantic versioning.
