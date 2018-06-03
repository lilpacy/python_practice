import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars+1)
    plt.barh(positions, data)
    plt.yticks(positions, labels)
    plt.show()

steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
create_bar_chart(steps, labels)
