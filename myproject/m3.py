import os,sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)


from manimlib import *
from surface import *





class ConicalSurface2(ThreeDScene):

    def construct(self) -> None:
        # 文字部分
        tex = TexText("圆锥面:$\\dfrac{x^2}{a^2}+\\dfrac{y^2}{a^2}=z^2$")
        tex.fix_in_frame()
        self.play(Write(tex))
        self.play(tex.animate.scale(0.5).to_corner([-1, 1, 0]))
        # 相机部分
        camera = self.camera.frame
        camera.set_euler_angles(phi=PI/2.5, theta=PI/2+0.1)
        # 坐标轴
        axes = ThreeDAxes(z_axis_config={'include_tip': True, 'include_numbers': True},
                          axis_config={'include_tip': True, 'include_numbers': True})
        axes.add_axis_labels()
        self.add(axes[0][0])

        # updater
        count = 0
        def updater(m: ConicalSurface):
            nonlocal count
            a = count/301*TAU+PI/2
            # print(f"count={count},a={a}")
            m.become(ConicalSurface(axes=axes, opacity=0.9, theta_range=(
                PI/2, a), resolution=(4, 100), color=BLUE_C))
            count = count + 1

        def updater2(m: SurfaceMesh):
            m.become(SurfaceMesh(sur, stroke_color=BLUE_D,stroke_width=2, normal_nudge=0.001,resolution=(10,10)))
        # 直线
        start= axes.c2p(0,(np.sqrt(2)*3/2)*np.sqrt(2),(np.sqrt(2)*3/2)*np.sqrt(2))
        end = axes.c2p(0,(-np.sqrt(2)*3/2)*np.sqrt(2),(-np.sqrt(2)*3/2)*np.sqrt(2))
        line = Line3D(start,end,color='#0000FF',width=0.05)
        self.add(line)
        self.wait(1)
        # 曲面
        sur = ConicalSurface(axes=axes, opacity=0.9, theta_range=(
            PI/2, PI/2), resolution=(4, 100), color=BLUE_C)
        self.add(sur)
        sur.add_updater(updater)
        # 网格
        mesh = SurfaceMesh(sur, stroke_color=BLUE_D,stroke_width=2.5, normal_nudge=0.001,resolution=(10,10))
        self.add(mesh)
        mesh.add_updater(updater2)

        self.play(Rotate(line,TAU,rate_func=linear),camera.animate.increment_phi(-0.4),run_time=10)
        # 椭圆锥面
        sur.remove_updater(updater)
        mesh.remove_updater(updater2)
        self.play(camera.animate.set_euler_angles(PI/2,0),run_time=5)
        sg = Group(mesh,sur)

        tex3 =TexText("沿Y轴方向伸缩$\dfrac{b}{a}倍$").scale(0.5).next_to(tex,DOWN)
        tex3.fix_in_frame()
        self.play(FadeIn(tex3))


        tex2 =TexText("椭圆锥面:$\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=z^2$").scale(0.5).to_corner([-1, 1, 0])
        tex2.fix_in_frame()

        self.play(sg.animate.stretch_to_fit_width(3),Transform(tex,tex2),FadeOut(tex3),run_time=3)
        self.play(camera.animate.set_euler_angles(PI/2+1,PI/4+0.2,0),run_time=5)
        
