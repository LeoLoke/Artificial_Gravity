import plotly
import numpy as np
import plotly.figure_factory as FF
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d


class GraphType(object):
    PLOTLY = 0
    MPL = 1


opacity = 0.5


def draw_torus(total_radius, outer_radius, kind=GraphType.MPL, z_ratio=1, iterations=50):

    R = round(float(total_radius - outer_radius), 2)
    r = round(float(outer_radius), 2)

    if z_ratio == 0 or z_ratio is None:
        z_ratio = (r / R)

    u = np.linspace(0, 2 * np.pi, iterations)
    v = np.linspace(0 * np.pi, 2 * np.pi, iterations)
    u, v = np.meshgrid(u, v)

    if kind == GraphType.PLOTLY:
        plotly.offline.init_notebook_mode(connected=True)

        u = u.flatten()
        v = v.flatten()

        x = (R + r * np.cos(u)) * np.cos(v)
        y = (R + r * np.cos(u)) * np.sin(v)
        z = r * np.sin(u)

        points2d = np.vstack([u, v]).T
        tri = Delaunay(points2d)
        simplices = tri.simplices

        fig1 = FF.create_trisurf(x=x, y=y, z=z,
                                 simplices=simplices,
                                 title="Torus", aspectratio=dict(x=1, y=1, z=z_ratio))
        plotly.offline.plot(fig1)
    elif kind == GraphType.MPL:

        x = (R + r * np.cos(u)) * np.cos(v)
        y = (R + r * np.cos(u)) * np.sin(v)
        z = r * np.sin(u)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.set_xlabel('x axis')
        ax.set_ylabel('y axis')
        ax.set_zlabel('z axis')
        ax.set_xlim(-R, R)
        ax.set_ylim(-R, R)
        ax.set_zlim(-r, r)

        z = z * z_ratio

        # ax.plot_surface(x, y, z, alpha=0.8, cmap=cm.Wistia)
        ax.plot_surface(x, y, z, color='yellow', alpha=opacity, rstride=3, cstride=3, cmap=cm.Wistia)

        plt.show()

