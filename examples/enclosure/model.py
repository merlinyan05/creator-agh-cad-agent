import cadquery as cq
import math

# Top-level editable parameters (mm)
box_length = 95
port_width = 12
box_width = 50
box_height = 30
wall = 2
bottom = 2
port_center_y = 25
port_z_bottom = 5
port_z_top = 11
lid_z_bottom = 30.3
lid_z_top = 32.3
lip_z_bottom = 27
lip_z_top = 30.3
lip_outer_inset = 2.3
lip_inner_inset = 3.8

outer_body = cq.Workplane("XY").box(
    box_length, box_width, box_height, centered=(False, False, False)
)
inner_body = cq.Workplane("XY").box(
    box_length - 2 * wall,
    box_width - 2 * wall,
    box_height - bottom,
    centered=(False, False, False),
).translate((wall, wall, bottom))
body = outer_body.cut(inner_body)

port = cq.Workplane("XY").box(
    wall + 2,
    port_width,
    port_z_top - port_z_bottom,
    centered=(False, False, False),
).translate((-1, port_center_y - port_width / 2, port_z_bottom))
body = body.cut(port)

lid_plate = cq.Workplane("XY").box(
    box_length,
    box_width,
    lid_z_top - lid_z_bottom,
    centered=(False, False, False),
).translate((0, 0, lid_z_bottom))

lip_outer = cq.Workplane("XY").box(
    box_length - 2 * lip_outer_inset,
    box_width - 2 * lip_outer_inset,
    lip_z_top - lip_z_bottom,
    centered=(False, False, False),
).translate((lip_outer_inset, lip_outer_inset, lip_z_bottom))
lip_inner = cq.Workplane("XY").box(
    box_length - 2 * lip_inner_inset,
    box_width - 2 * lip_inner_inset,
    lip_z_top - lip_z_bottom,
    centered=(False, False, False),
).translate((lip_inner_inset, lip_inner_inset, lip_z_bottom))
locating_lip = lip_outer.cut(lip_inner)
lid = lid_plate.union(locating_lip)

show_object(body, id="body", name="body")
show_object(lid, id="lid", name="lid")