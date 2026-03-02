import matplotlib.pyplot as plt
import sys

def plot_data():
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.savefig('plot.png')
    print("Done!")

if __name__ == "__main__":
    try:
        plot_data()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)