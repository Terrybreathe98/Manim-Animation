from manim import *
import math

class Cover(Scene):                    
    def geneSector(self,pieces,r,pos):           #Generate sectors with different angle
        angles = []
        sectors = VGroup()
        colorLi = [BLUE,LIGHT_BROWN]
        for i in range(pieces):
            sector = Sector(
                arc_center = pos, 
                radius = 1, 
                angle = 2*PI/pieces, 
                start_angle = i * 2 * PI / pieces, 
                color = colorLi[i%2]
                
            )
            angles.append(i * 2 * PI / pieces)
            sectors.add(sector)
        
        sectors.scale(r)
        

        return sectors,angles
    
    def construct(self):
        r = 2
        pieces = 48
        angle = 2*PI/pieces

        init_appear_pos = [0,1.5,0]

        title = Text(
            "圆的面积",
            font = 'Alimama DongFangDaKai',
            font_size = 60,
            color = YELLOW
        )
        title.move_to([0,0,0])
        self.play(
            FadeIn(
                title,
                shift = UP
            ),
            run_time = 0.6
        )

        self.wait(0.5)
        self.play(
            title.animate.scale(
                0.5
            ),
            run_time = 0.6
        )
        self.play(
            title.animate.move_to(
                [-6,3.5,0]
            ),
            run_time = 0.6
        )
        

        self.wait(0.5)

        c = Circle(
            radius = r,
            arc_center = init_appear_pos,
            fill_color = BLUE,
            color = BLUE,
            fill_opacity = 1
        )
        self.play(
            FadeIn(
                c,
                shift = UP
            ),
            run_time = 0.6
        )
        c.add_updater(
            lambda m: self.bring_to_front(m)   #keep circle in the front
        )

        sectors,angles = self.geneSector(pieces,r,init_appear_pos)  
        self.play(
            FadeIn(
                sectors
            ),
            run_time = 0.6
        )

        self.wait(1)
        
        c.clear_updaters()
        
        self.play(
            FadeOut(
                c
            ),
            run_time = 0.6
        )

        self.wait(0.6)
      
        pos = -(pieces/2*r*math.sin(angle/2))
        half_angles = [PI/2-angle/2,3*PI/2-angle/2]
        half_angle = half_angles[1]
        run_timeLi = [0.4,1/pieces]   #两种不同的动画播放速度
        for i in range(pieces):
            if i>8:
                run_Time = run_timeLi[1]
            else:
                run_Time = run_timeLi[0]

            curAng = angles[i]
            tarAng = half_angle-curAng

            self.play(
                sectors[i].animate.rotate(
                    tarAng
                ), 
                run_time = run_Time
            )
            self.play(
                sectors[i].animate.move_to(
                    [pos,-2,0]
                    ), 
                run_time = run_Time
            )
            pos += r * math.sin(angle/2)
            half_angle = half_angles[i%2]

        self.wait(0.6)

        run_Time = run_timeLi[0]
        self.play(
            sectors.animate.move_to(
                UP
            ),
            run_time = run_Time
        )

        self.wait(0.6)

        width = DoubleArrow(
            [
                sectors[0].get_x()-3*r*math.sin(PI/pieces),   #线左端
                sectors.get_y()-0.5*r-0.5,
                0
            ],
            [
                sectors[-1].get_x()+2*r*math.sin(PI/pieces),                        #线右端
                sectors.get_y()-0.5*r-0.5,
                0
            ],
            color = YELLOW,
            stroke_width = 3,
            tip_length = 0.3
        )
        self.play(
            FadeIn(
                width
            ),
            run_time = 0.6
        )

        self.wait(0.8)

        r_text = Text(
            "π * R",
            color = WHITE,
            font = 'Alibaba PuHuiTi 3.0',
            font_size = 48 
        )
        
        r_text.move_to(
            [
                0,
                sectors.get_y()-0.5*r-1,
                0
            ]
        )

        self.play(
            FadeIn(
                r_text
            ),
            run_time = 0.6
        )

        height = DoubleArrow(
            [
                sectors[-1].get_x()+0.5,
                sectors[-1].get_y()+r*0.6,
                0
            ],
            [
                sectors[-1].get_x()+0.5,
                sectors[-1].get_y()-r*0.6,
                0
            ],
            color = YELLOW,
            stroke_width = 3,
            tip_length = 0.3
        )
        self.play(
            FadeIn(
                height
            ),
            run_time = 0.6
        )

        self.wait(0.5)

        h_text = Text(
            "R",
            color = WHITE,
            font = 'Alibaba PuHuiTi 3.0',
            font_size = 48 
        )

        h_text.move_to(
            [
                height.get_x()+0.5,
                sectors[-1].get_y(),
                0
            ]
        )

        self.play(
            FadeIn(
                h_text,
                shift = UP*0.5
            ),
            run_time = 0.6
        )

        r_text2 = r_text.copy()
        h_text2 = h_text.copy()
        times = Text(
            "*",
            color = YELLOW,
            font = 'Alimama DongFangDaKai',
            font_size = 48 
        )
        times.move_to(
            [
                0,-2,0
            ]
        )

        self.add(r_text2,h_text2)
        self.wait(0.2)
        self.play(
            r_text2.animate.move_to(
                [
                    -1,-2,0
                ]
            ),
            h_text2.animate.move_to(
                [
                    0.5,-2,0
                ]
            ),
            run_time = 0.6
        )

        self.wait(0.5)

        self.play(
            FadeIn(
                times
            ),
            run_time = 0.6
        )

        formula = VGroup()
        formula.add(r_text2,h_text2,times)

        self.play(
            formula.animate.move_to(
                [
                    -2,-2,0
                ]
            ),
            run_time = 0.6
        )

        ans = Text(
            "= π*R^2 = 面积S",
            color = YELLOW,
            font = 'Alibaba PuHuiTi 3.0',
            font_size = 48
        )
        ans.move_to(
            [
                1.5,
                -2,
                0
            ]
        )
        self.play(
            FadeIn(
                ans
            ),
            run_time = 0.6
        )

        self.wait(5)