import arcade
arcade.open_window(700, 700, "Dibujo 1")
arcade.set_background_color(arcade.color.EERIE_BLACK)
arcade.start_render()
#MURO
arcade.draw_lrtb_rectangle_filled(0, 700, 250, 0, arcade.color.OUTER_SPACE)
#ASFALTO
arcade.draw_lrtb_rectangle_filled(0, 700, 280, 220, arcade.color.OLD_LACE)
#COCHE
arcade.draw_polygon_filled([[130, 60],
                            [120, 150],
                            [250, 190],
                            [380,190],
                            [460,140],
                            [550,120],
                            [620, 50]],
                            arcade.color.FERRARI_RED)
#VENTANAS
arcade.draw_polygon_filled([[397,180],
                            [460,140],
                            [300,140],
                            [275,180]],
                            arcade.color.BLACK)
arcade.draw_polygon_filled([[397,180],
                            [420,140],
                            [418,140],
                            [395,180]],
                            arcade.color.GLITTER)
#PUERTA
arcade.draw_rectangle_filled(300, 99, 2, 85, arcade.color.CRIMSON)
arcade.draw_rectangle_filled(420, 99, 2, 85, arcade.color.CRIMSON)
arcade.draw_rectangle_filled(380, 110, 20, 5, arcade.color.CRIMSON)
#RUEDA DELANTERA
arcade.draw_circle_filled(490, 75, 50, arcade.color.LICORICE)
arcade.draw_circle_filled(490, 75, 45, arcade.color.LICORICE)
arcade.draw_circle_filled(490, 75, 30, arcade.color.GLITTER)
arcade.draw_circle_filled(490, 75, 5, arcade.color.MANATEE)
#RUEDA TRASERA
arcade.draw_circle_filled(200, 75, 50, arcade.color.LICORICE)
arcade.draw_circle_filled(200, 75, 45, arcade.color.LICORICE)
arcade.draw_circle_filled(200, 75, 30, arcade.color.GLITTER)
arcade.draw_circle_filled(200, 75, 5, arcade.color.MANATEE)
arcade.finish_render()
arcade.run()