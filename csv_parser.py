import pandas as pd

table = pd.read_csv('Table_input.csv')
idx = table.set_index('Index #')

table.to_html('table.html', index = False)

a = idx.loc['A5', 'Value'] + idx.loc['A20', 'Value']
b = idx.loc['A15', 'Value'] / idx.loc['A7', 'Value']
c = idx.loc['A13', 'Value'] * idx.loc['A12', 'Value']

new_table = pd.DataFrame({
    'Category': ['Alpha', 'Beta', 'Charlie'],
    'Value': [a, b, c] })


with open('table.html', 'a') as table_html:
    table_html.write(new_table.to_html(index = False))
