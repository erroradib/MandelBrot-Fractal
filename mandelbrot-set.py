import numpy as np
import matplotlib.pyplot as plt

def mndlbrt(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def generate_mndlbrt_img(w, h, x_min, x_max, y_min, y_max, max_iter):
    img = np.zeros((h, w))
    real = (x_max - x_min) / w
    imag = (y_max - y_min) / h

    for row in range(h):
        for col in range(w):
            real_part = x_min + col * real
            imag_part = y_min + row * imag
            c = complex(real_part, imag_part)
            img[row, col] = mndlbrt(c, max_iter)
    return img

if __name__ == "__main__":

    WIDTH, HEIGHT = 600, 600
    X_MIN, X_MAX = -2.0, 1.0
    Y_MIN, Y_MAX = -1.5, 1.5
    MAX_ITERATIONS = 50

    mandelbrot_data = generate_mndlbrt_img(WIDTH, HEIGHT, X_MIN, X_MAX, Y_MIN, Y_MAX, MAX_ITERATIONS)

    plt.imshow(mandelbrot_data, cmap='hot', extent=[X_MIN, X_MAX, Y_MIN, Y_MAX])
    plt.title("MANDELBROT SET")
    plt.xlabel("REAL")
    plt.ylabel("IMAGINARY")
    plt.colorbar(label='ITERATIONS')
    plt.show()
