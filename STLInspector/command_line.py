""" this file provides the command line functionality, registered with setuptools """
import argparse
import STLInspector.frontend.Server as server

def main():
    """
    start the frontend server
    """

    parser = argparse.ArgumentParser(
        description='Systematic validation of Signal Temporal Logic (STL) specifications against informal textual requirements.'
    )
    parser.add_argument('datadir', help='directory used for saving and loading project files.')
    args = parser.parse_args()

    server.run(args.datadir)
