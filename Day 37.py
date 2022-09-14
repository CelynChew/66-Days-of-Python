# Aim: CLeaning data

airport_data = "IDCJAC0001_009021_Data1.csv"

def valid_data(site):
    with open(site, 'r') as f:
        header = list((f.readline().strip()).split(','))
        
        lines = f.readlines()
        data = []
        body = []
        for l in lines:
            data.append((l.strip()).split(','))
        for d in data:
            if d[-2] != '' and d[-2][0] in '1234567890' and d[-1] in 'YN':
                body.append(d)
        return header, body
    
print(valid_data(airport_data))