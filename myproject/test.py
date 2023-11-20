from manimlib import *

class P2(ThreeDScene):

    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def construct(self):
        self.camera.frame.set_euler_angles(*[ 1.91802677e+00,  7.68256198e-01, -3.88578059e-15])

        axes = myThreeDAxes()
        lab = axes.get_axis_labels()
        num = axes.get_numbers()
        self.add(axes)
        self.add(lab,num,set_depth_test=False)
   
        surface = ParametricSurface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            color=BLUE,
            resolution=(100,100)
           
        )
        mesh = SurfaceMesh(surface)
        self.add(surface,mesh)
        # self.embed()


class P3(ThreeDScene):
    def construct(self) -> None:
        axes = myThreeDAxes()
        numbers=axes.get_numbers()
        labels = axes.get_axis_labels()
        self.add(axes)
        self.add(numbers,labels,set_depth_test=False)

