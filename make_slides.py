import svgwrite
import os
import logging

logging.basicConfig(level=logging.INFO)

def create_svg(filename, size=("1920px", "1080px"), header_href="header.svg"):
    """
    Create an SVG file with a header image at the top and bottom.

    :param filename: Name of the output SVG file.
    :param size: Tuple defining the width and height of the SVG canvas.
    :param header_href: Path to the header image file.
    """
    # Validate the header file existence
    if not os.path.exists(header_href):
        raise FileNotFoundError(f"The file {header_href} does not exist.")

    # Create an instance of svgwrite.Drawing with updated dimensions
    dwg = svgwrite.Drawing(filename, size=size)

    # Add the header SVG image at the top and bottom
    header_height = 150  # Default header height
    for y_pos in [0, int(size[1].replace("px", "")) - header_height]:
        dwg.add(dwg.image(href=header_href, insert=(0, y_pos), size=(size[0], f"{header_height}px")))

    # Save the SVG to the specified file
    dwg.save()
    logging.info(f"SVG image saved as {filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create an SVG slide with headers.")
    parser.add_argument("filename", help="Output SVG file name")
    parser.add_argument("--size", default="1920x1080", help="SVG dimensions (e.g., 1920x1080)")
    parser.add_argument("--header", default="header.svg", help="Header image file")
    args = parser.parse_args()

    width, height = args.size.split("x")
    create_svg(args.filename, size=(f"{width}px", f"{height}px"), header_href=args.header)
