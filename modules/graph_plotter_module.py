#!/use/bin/python3
"""
graph plotter
@graphplooter
"""
import matplotlib.pyplot as plt


class GraphPlotter:
  """
  """

  def __init__(self):
    """
    """
    pass

  def plot_graph(self,x,y):

    plt.plot(x,y)
    plt.show()


if __name__ == '__main__':
    print('module only, not main')