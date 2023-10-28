import pandas as pd
import plotly.graph_objects as go

while True:
    data = pd.read_csv('nintendo.csv', encoding='ISO-8859-1')

    Columns = '''\n-title\n-copies_sold\n-genre\n-developer\n-publisher\n-as_of\n-release_date'''
    print('Columns 🢃 '+Columns)

    numberColumn = int(input('How many columns do you want to compare: '))
    columnNames = []

    for i in range(numberColumn):
        colName = input(f'Column {i + 1} name: ')
        columnNames.append(colName)

    choose = input('run/quit: ')

    if choose == 'run':
        player = data.groupby(columnNames).size().reset_index()
        header_values = columnNames
        cell_values = [player[colName] for colName in columnNames]

        figA = go.Figure(data=[go.Table(
            header=dict(values=header_values,
                        fill=dict(color=['brown']),
                        height=50,
                        align='center',
                        font=dict(size=25, color='white'),
                        line=dict(width=5, color='black')
                        ),
            cells=dict(values=cell_values,
                       fill=dict(color=['cornflowerblue']),
                       height=50,
                       align='center',
                       font=dict(size=22,color='white'),
                       line=dict(width=5, color='black')
                       )
        )])
        figA.show()

    elif choose == 'quit':
        break
