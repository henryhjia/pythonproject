#!/use/bin/python3
"""
@brief csv reader 
@csvreader
"""
import csv


class CsvReader:
  """
  """

  def __init__(self, filename):
    """
    """
    self._filename = filename
    print(self._filename)
    pass

  def read_csv(self):

    with open(self._filename) as csvfile:
      mpg = list(csv.DictReader(csvfile))

    for i in mpg:
      print(i)

    print(mpg[0].keys())
    print(len(mpg))

    ave_pulse = sum(float(d['cty']) for d in mpg) / len(mpg)
    print(f'{ave_pulse:.2f}')

    cylinders = set(d['cyl'] for d in mpg)
    print(cylinders)

    CtyMpgCyl = []
    for c in cylinders:
      summpg = 0
      cyltypecount = 0
      for d in mpg:
        if d['cyl'] == c:
          summpg += float(d['cty'])
          cyltypecount += 1

      CtyMpgCyl.append((c, summpg/cyltypecount))

    CtyMpgCyl.sort(key=lambda x: x[0])

    for i in CtyMpgCyl:
      print(f'{i[0]} {i[1]:.2f}')


if __name__ == '__main__':
    print('module only, not main')