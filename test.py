file='test.xlsx'
if file.endswith('.csv'):
    print('file is CSV')
elif file.endswith('.xlsx'):
    print('file is excel')
else:
    print('none of them')