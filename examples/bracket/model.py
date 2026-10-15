import cadquery as cq
import math

foot_length = 75.0
hole_diameter = 6.0
width = 40.0
thickness = 4.0
height = 44.0

base = (
    cq.Workplane("XY")
    .box(foot_length, width, thickness, centered=(False, False, False))
)
wall = (
    cq.Workplane("XY")
    .box(thickness, width, height - thickness, centered=(False, False, False))
    .translate((0, 0, thickness))
)

bracket = base.union(wall)

for x in (20.0, 45.0):
    base_hole = (
        cq.Workplane("XY")
        .workplane(offset=-1.0)
        .center(x, 20.0)
        .circle(hole_diameter / 2.0)
        .extrude(thickness + 2.0)
    )
    bracket = bracket.cut(base_hole)

wall_hole = (
    cq.Workplane("YZ")
    .workplane(offset=-1.0)
    .center(20.0, 24.0)
    .circle(hole_diameter / 2.0)
    .extrude(thickness + 2.0)
)
bracket = bracket.cut(wall_hole)

show_object(bracket, options={"id": "bracket", "name": "bracket"}, name="bracket")