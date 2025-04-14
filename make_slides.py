import svgwrite
import os
import logging
import argparse

# Constants for default values
DEFAULT_SIZE = "1920x1080"
DEFAULT_HEADER = "header.svg"
DEFAULT_BOTTOM = "bottom.svg"

# Configure logging
logging.basicConfig(level=logging.INFO)

def create_svg(filename, size=("1920px", "1080px"), header_href="header.svg", bottom_href="bottom.svg"):
    """
    Create an SVG file with a header image at the top and bottom.

    :param filename: Name of the output SVG file.
    :param size: Tuple defining the width and height of the SVG canvas.
    :param header_href: Path to the header image file.
    :param bottom_href: Path to the bottom image file.
    """
    # Validate the header file existence
    if not os.path.exists(header_href):
        raise FileNotFoundError(f"The file {header_href} does not exist.")
    
    # Validate the bottom file existence
    if not os.path.exists(bottom_href):
        raise FileNotFoundError(f"The file {bottom_href} does not exist.")

    # Create an instance of svgwrite.Drawing with updated dimensions
    dwg = svgwrite.Drawing(filename, size=size)

    # Add the header SVG image at the top
    dwg.add(dwg.image(href=header_href, insert=(0, 0)))

    # Add the bottom SVG image at the bottom
    dwg.add(dwg.image(href=bottom_href, insert=(0, int(size[1].replace("px", "")) - 150)))

    # Save the SVG to the specified file
    dwg.save()
    logging.info(f"SVG image saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="

