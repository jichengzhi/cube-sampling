import os

import matplotlib.pyplot as plt

from cube_loader import cube_name_from_stl_path, load_points_from_stl
from cube_sampler import sample_from_raw_points
from display import plot_3d
from heatmap import plot_heatmap, get_heatmap
from rotate import rotate_x


def export_sample_in_2d(sample_points, cube_name, img_path: str):
    X, Y, Z = 0, 1, 2
    surface = rotate_x(sample_points, -90)[:, [X, Z]]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(surface[:, 0], surface[:, 1], s=0.001)
    ax.set_title(f'{cube_name} surface', fontsize=10, y=1.0)
    plt.savefig(img_path)


if __name__ == '__main__':

    paths = ['Blue09.STL', 'Blue15.STL', 'Blue22.STL']

    for stl_path in paths:
        raw_data = load_points_from_stl(stl_path)
        cube_name = cube_name_from_stl_path(stl_path)

        cube, sample_points = sample_from_raw_points(raw_data)

        cube_img_path = os.path.join('./output', f'cube-{cube_name}.png')
        surface_img_path = os.path.join('./output', f'surface-{cube_name}.png')
        heatmap_img_path = os.path.join('./output', f'heatmap-{cube_name}.png')

        export_sample_in_2d(sample_points, cube_name, surface_img_path)

        plot_3d(cube, title=f'cube from {stl_path}', path=cube_img_path, s=0.1)

        heatmap = get_heatmap(sample_points)
        plot_heatmap(heatmap, cube_name=cube_name, save_path=heatmap_img_path)