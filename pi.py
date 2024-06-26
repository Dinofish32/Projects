import matplotlib.pyplot as plt
import random
from matplotlib.patches import Arc


def in_circle(x: float, y: float) -> bool:
    """Return whether the given point would be inside or on the arc."""
    return x**2 + y**2 <= 1


def graph(dp: int = 2) -> None:
    if dp >= 10:
        raise ValueError("The number of decimal places inputted is too high!")
    
    fig, ax = plt.subplots(figsize=(1,1))
    ax.set(xlim=(0, 1), ylim=(0, 1), aspect="equal")
    ax.grid(True)
    
    arc = Arc((0,0), width=2, height=2, angle=90)
    ax.add_patch(arc)

    ins = 0
    outs = 0
    total_dots = 10**dp
    for _ in range(total_dots):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        plt.scatter(x, y, color="red" if in_circle(x, y) else "blue", s=5)

        if in_circle(x, y):
            ins += 1
        else:
            outs += 1

    print(f"{ins} dots were inside the circle out of {total_dots} dots.")

    pi_approx = 4 * ins / total_dots

    print(f"The approximation for pi is {pi_approx}")

    plt.show()

if __name__ == "__main__":
    graph(4)
