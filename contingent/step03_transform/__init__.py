import os
import sys

from project import Project
from utils import relative_of


def main():
    base_dir = relative_of(__file__, '../docs')
    proj = Project(base_dir)
    if len(sys.argv) < 2:
        proj.usage()
        sys.exit(0)
    target_name = sys.argv[1]
    proj.run(target_name)
