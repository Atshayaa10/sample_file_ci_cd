import matplotlib.pyplot as plt  # This package is NOT in requirements.txt

def plot_data():
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.savefig('plot.png')
    print("Done!")

if __name__ == "__main__":
    plot_data()
