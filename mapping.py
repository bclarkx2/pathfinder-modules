#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from collections import namedtuple


###############################################################################
# Constants                                                                   #
###############################################################################


###############################################################################
# Classes                                                                     #
###############################################################################

ImageCoord = namedtuple("ImageCoord", ["x", "y"])
BlueprintCoord = namedtuple("BlueprintCoord", ["u", "v"])


###############################################################################
# Mapping Functions                                                           #
###############################################################################

def image_to_blueprint(image_coord):
    blueprint_coord = image_coord
    return blueprint_coord


def blueprint_to_image(blueprint_coord):
    image_coord = blueprint_coord
    return image_coord


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg")
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()


if __name__ == '__main__':
    main()
