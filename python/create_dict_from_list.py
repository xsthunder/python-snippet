def f(row):
  index, row = row
  return (row.get('ID'), row.get('column1'))
# dict accepts array of tuple with size 2, using tp[0] as key, tp[1] as value 
dic = dict(map(f, df.iterrows()))
