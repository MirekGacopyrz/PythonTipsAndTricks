import svgwrite

def create_svg(filename):
    # Create an instance of svgwrite.Drawing with updated dimensions
    dwg = svgwrite.Drawing(filename, size=("1920px", "1080px"))

    # Add a rectangle for the header (x, y, width, height, fill color)
    dwg.add(dwg.rect(insert=(0, 0), size=(1920, 150), fill="lightblue", id="header"))

    # Save the SVG to the specified file
    dwg.save()
    print(f"SVG image saved as {filename}")

# Call the function to create the SVG
create_svg("example.svg")
