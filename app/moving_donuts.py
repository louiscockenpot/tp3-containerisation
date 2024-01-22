import numpy as np
import os
import time

A, B = 0, 0  # Rotating animation
theta_spacing = 10
phi_spacing = 2
chars = ".,-~:;=!*#$@"  # Luminance index

# Clear Screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Loop
while True:
    z = [0] * 1760
    b = [' '] * 1760

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            c = np.sin(i)
            d = np.cos(j)
            e = np.sin(A)
            f = np.sin(j)
            g = np.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = np.cos(i)
            m = np.cos(B)
            n = np.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < 1760 and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    # Clear the screen
    clear_screen()

    # Print the frame
    for i in range(0, 1760, 80):
        print(''.join(b[i:i + 80]))

    A += 0.04
    B += 0.02

    # Control frame rate
    time.sleep(0.03)
