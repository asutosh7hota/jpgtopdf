"""
skele
Usage:
  skele hello
  skele -h | --help
  skele --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  skele hello
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""

import glob
import os, sys

from fpdf import FPDF #
from inspect import getmembers, isclass
from PIL import Image
from docopt import docopt

from . import __version__ as VERSION


def main():
    
    for infile in sys.argv[1:]:
        f = infile
    imagelist = glob.glob('*.jpg') # imagelist is the list with all image filenames
    # print(imagelist)
    output = f + ".pdf"
    pdf = FPDF()
    for image in imagelist:
        cover = Image.open(image)
        width, height = cover.size

        pdf.add_page()
        pdf.image(image,0,0,width,height)
    pdf.output(output, "F")