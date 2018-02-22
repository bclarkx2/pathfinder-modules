#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
# from collections import namedtuple


###############################################################################
# Constants                                                                   #
###############################################################################

BLUEPRINT_TO_IMAGE = "bti"
IMAGE_TO_BLUEPRINT = "itb"

OPERATIONS = [
    BLUEPRINT_TO_IMAGE,
    IMAGE_TO_BLUEPRINT
]

###############################################################################
# Classes                                                                     #
###############################################################################

# ImageCoord = namedtuple("ImageCoord", ["x", "y"])
# BlueprintCoord = namedtuple("BlueprintCoord", ["u", "v"])


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

def format_coord(coord):
    return "{}\n{}".format(*coord)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("op",
                        choices=OPERATIONS,
                        help="Mapping operation")
    parser.add_argument("coord",
                        type=float,
                        nargs=2,
                        help="coordinates to map")
    parser.add_argument("manifest",
                        help="job_manifest_file")
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    if args.op == BLUEPRINT_TO_IMAGE:
        coord = blueprint_to_image(tuple(args.coord))
    elif args.op == IMAGE_TO_BLUEPRINT:
        coord = image_to_blueprint(tuple(args.coord))

    print(format_coord(coord))


if __name__ == '__main__':
    main()
