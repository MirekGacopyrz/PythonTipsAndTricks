import svgwrite

def create_svg(filename):
    # Create an instance of svgwrite.Drawing with updated dimensions
    dwg = svgwrite.Drawing(filename, size=("1920px", "1080px"))

    # Add the header SVG image
    dwg.add(dwg.image(href="header.svg", insert=(0, 0), size=(1920, 150)))
    dwg.add(dwg.image(href="header.svg", insert=(0, 1920-150), size=(1920, 150)))

    # Save the SVG to the specified file
    dwg.save()
    print(f"SVG image saved as {filename}")

# Call the function to create the SVG
create_svg("example.svg")
