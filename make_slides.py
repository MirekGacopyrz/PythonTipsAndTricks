import svgwrite

def create_svg(filename):
    # Create an instance of svgwrite.Drawing
    dwg = svgwrite.Drawing(filename, size=("200px", "200px"))

    # Add a rectangle (x, y, width, height, fill color)
    dwg.add(dwg.rect(insert=(10, 10), size=(180, 180), fill="lightblue"))

    # Add a circle (center x, center y, radius, fill color)
    dwg.add(dwg.circle(center=(100, 100), r=50, fill="red"))

    # Add a line (start x, start y, end x, end y, stroke color and width)
    dwg.add(dwg.line(start=(10, 10), end=(190, 190), stroke="black", stroke_width=2))

    # Add some text (position x, position y, text content, font size, and color)
    dwg.add(dwg.text("Hello SVG", insert=(50, 195), fill="black", font_size="15px"))

    # Save the SVG to the specified file
    dwg.save()
    print(f"SVG image saved as {filename}")

# Call the function to create the SVG
create_svg("example.svg")
