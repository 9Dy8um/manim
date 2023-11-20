import os,sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)


from manimlib import *
from surface import *






class SphereSurface(ThreeDScene):

    def construct(self) -> None:
        # 文字部分
        tex = TexText("球面:$\\dfrac{x^2}{a^2}+\\dfrac{y^2}{a^2}+\\dfrac{z^2}{a^2}=1$")
        tex.fix_in_frame()
        self.play(Write(tex))
        self.play(tex.animate.scale(0.5).to_corner([-1, 1, 0]))
        # 相机部分
        camera:CameraFrame = self.camera.frame
        camera.set_euler_angles(phi=PI/2.5, theta=PI/2+0.2)
        # 坐标轴
        axes = ThreeDAxes(z_axis_config={'include_tip': True, 'include_numbers': True},
                          axis_config={'include_tip': True, 'include_numbers': True})
        axes.add_axis_labels()

        # 球面
        sphere =SphereInAxes(axes,radius=2,color=BLUE,opacity=0.6)
        self.add(sphere)
        # 环
        torus_xoy =TorusInAxes(axes,r1=2,r2=0.01,color=RED)
        torus_xoz = torus_xoy.copy().rotate(PI/2,(1,0,0)).set_color(YELLOW_C)
        torus_yoz = torus_xoy.copy().rotate(PI/2,(0,1,0)).set_color(GREEN_C)
        g = Group(torus_xoy,torus_xoz,torus_yoz,sphere)
        self.add(axes,g)
        self.wait(0.1)
        # 文本
        tex2 = TexText("沿Z轴方向伸缩$\dfrac{c}{a}倍$").scale(0.5).next_to(tex,DOWN)
        tex2.fix_in_frame()
        self.play(Write(tex2))
        # 旋转椭球面
        self.play(g.animate.stretch_to_fit_depth(0.6*g.get_depth()),run_time=3)
        self.play(camera.animate.increment_phi(-0.5))
        self.play(FadeOut(tex2))
        tex3 = TexText("旋转椭球面:$\\dfrac{x^2}{a^2}+\\dfrac{y^2}{a^2}+\\dfrac{z^2}{c^2}=1$").scale(0.5).move_to(tex)
        tex3.fix_in_frame()
        self.play(TransformMatchingTex(tex,tex3))
        
        self.play(camera.animate.set_theta(PI-0.2),run_time=2)
        self.play(camera.animate.set_euler_angles(theta=PI/2+0.2,phi=PI/2-0.5),run_time=2)

        # 文本
        tex4 = TexText("沿Y轴方向伸缩$\dfrac{b}{a}倍$").scale(0.5).next_to(tex,DOWN)
        tex4.fix_in_frame()
        self.play(Write(tex4))
        # 椭球面
        self.play(g.animate.stretch_to_fit_height(0.3*g.get_height()),run_time=3)
        self.play(FadeOut(tex4))
        tex5 = TexText("椭球面:$\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1$").scale(0.5).move_to(tex)
        tex5.fix_in_frame()
        self.play(TransformMatchingTex(tex3,tex5))
        
        self.play(camera.animate.scale(0.6))

        self.play(camera.animate.set_theta(PI/2).set_phi(PI/2),run_time=3)
        self.play(camera.animate.set_theta(PI).set_phi(PI/2),run_time=3)
        self.play(camera.animate.set_theta(PI/2).set_phi(0),run_time=3)
        self.play(camera.animate.set_euler_angles( 2.20412966e+00,  3.92805571e-01, -2.88657986e-15))
        


        




        
