#!/use/bin/python3
"""
graph plooter
@graphplotter
"""
import graph_plotter_module

def main() -> int:

  me = graph_plotter_module.GraphPlotter()
  x = [0,1,2,3,4]
  y = [0,3,1,5,2]

  me.plot_graph(x,y)

if __name__ == '__main__':
  main()