import imageio
import os
import os.path as osp


def img2gif(img_dir, gif_path, duration):
    frames = []
    for idx in sorted(os.listdir(img_dir)):
        img = osp.join(img_dir, idx)
        frames.append(imageio.imread(img))

    imageio.mimsave(gif_path, frames, 'GIF', duration=duration)
    print('Finish changing!')


if __name__ == '__main__':
    img_dir = 'out'
    par_dir = osp.dirname(img_dir)
    gif_path = osp.join(par_dir, 'output.gif')
    img2gif(img_dir=img_dir, gif_path=gif_path, duration=0.1)
