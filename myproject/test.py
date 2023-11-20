from manimlib import *

class P2(Scene):

    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def construct(self):
        self.camera.frame.set_euler_angles(*[ 1.91802677e+00,  7.68256198e-01, -3.88578059e-15])

        axes = ThreeDAxes(z_axis_config={'include_tip': True, 'include_numbers': True},
                          axis_config={'include_tip': True, 'include_numbers': True}).apply_depth_test()
        axes.add_axis_labels()
        self.add(axes)

        


        surface = ParametricSurface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            color=BLUE,
            resolution=(100,100)
           
        ).apply_depth_test()
        mesh = SurfaceMesh(surface).apply_depth_test()
        self.add(axes,surface,mesh)
        # self.embed()
