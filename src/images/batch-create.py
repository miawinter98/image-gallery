import argparse
import json
import sys
from pathlib import Path

def print_verbose(*messages):
    global verbose
    if verbose:
        print(*messages)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Batch Image Create", description="Helps you create the necessary meta files for all images in a folder")
    parser.add_argument('directory', help="the directory to traverse when looking for images to generate metadata for")
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-a', '--author', help="the author of these images")
    parser.add_argument('-s', '--source', help="a link for where to find that image from the author")
    parser.add_argument('-cc', '--license', help="the license to use, like CC BY-SA (look up creative commons for details)")

    args = parser.parse_args()
    global verbose
    verbose = args.verbose

    directory = Path(args.directory)
    print_verbose("Checking Directory", directory, "...")

    # check directory is valid
    if directory.is_dir() is False:
        raise ValueError("Path is not a directory")
    if directory.exists() is False:
        raise ValueError("Directory does not exist")

    counter = 0
    # traverse directory
    for image in directory.glob("*.jpg"):
        print_verbose("Checking Image", image, "...")
        jsonFile = Path(directory, image.stem + ".meta.json")
        print_verbose("Creating", jsonFile, "...")
        data = {
            "image": "./" + image.name,
            "author": args.author,
            "src": args.source,
            "license": args.license
        }
        with open(jsonFile, "w") as j:
            json.dump({k: v for k, v in data.items() if v is not None}, j, indent=4)
        counter += 1


    print("...done.", str(counter), "Image metafiles created")

    command_file = Path(directory, "_command.txt")
    with open(command_file, "w") as cmd:
        cmd.write(" ".join(sys.argv))



