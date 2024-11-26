size_button = 44
diameter_top = 48
size_text = 14
width_pen = 3
angle_arrow = 24
size_arrow = 30

arr_name_button = ["Setting", "Tools",
                   ("Arrows", ("Arrow", "Stick", "Loop")),
                   "Top", "Edit", "Delete", "Refund",
                   "Recover", "Clear", "Done"
                   ]

setting_button = {"Setting": {"image": ['Icon_for_button/sheet.png', None], "type": "clicked"},
                  "Tools": {"image": ["Icon_for_button/three_point_none.png", 'Icon_for_button/three_line.png'],
                            "type": "clicked"},
                  "Arrow": {"image": ['Icon_for_button/default_arrow.png', None], "type": "sticking"},
                  "Stick": {"image": ['Icon_for_button/stick.png', None], "type": "sticking"},
                  "Loop": {"image": ['Icon_for_button/loop_arrow.png', None], "type": "sticking"},
                  "Top": {"image": ['Icon_for_button/top.png', None], "type": "sticking"},
                  "Edit": {"image": ['Icon_for_button/edit.png', None], "type": "sticking"},
                  "Delete": {"image": ['Icon_for_button/delete.png', None], "type": "sticking"},
                  "Refund": {"image": ['Icon_for_button/refund.png', None], "type": "clicked"},
                  "Recover": {"image": ['Icon_for_button/recover.png', None], "type": "clicked"},
                  "Clear": {"image": ['Icon_for_button/recycle_bin.png', None], "type": "clicked"},
                  "Done": {"image": ['Icon_for_button/done.png', None], "type": "clicked"}
                  }

color_dict = {"Top": "white",
              "Arrow": "white",
              "Stick": "white",
              "Loop": "white"
              }

radius_top = diameter_top / 2
proximity_coefficient = 1.3
depth_coefficient = 0.75

background_color = "black"
color_top = "white"
color_stick = "white"
color_arrow = "white"
color_loop = "white"

button_disabled_color = "#434343"
button_active_color = "#b7b7b7"

radius_loop = 38
depth_loop_coefficient = 0.3
joint = radius_top * depth_loop_coefficient + radius_loop
dist_loop = joint + radius_loop

depth_due_arrow = radius_top * depth_coefficient