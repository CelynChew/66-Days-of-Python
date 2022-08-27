# Aim: Extract data from multiple files

AGE_DATA_A = '2016Census_G04A_AUS.csv'
AGE_DATA_B = '2016Census_G04B_AUS.csv'

def read_data(files):
    with open(AGE_DATA_A, 'r') as A, open(AGE_DATA_B, 'r') as B:
        category_A = A.readline()
        data_A = A.readline()
        category_A = category_A.split(',')
        data_A = data_A.split(',')
        
        category_B = B.readline()
        data_B = B.readline()
        category_B = category_B.split(',')
        data_B = data_B.split(',')
        
        category = category_A + category_B
        data = data_A + data_B
    
        cat_for_totals = []
        for total in category:
            if total[-1] == 'P':
                cat_for_totals.append(total)
    
        indexes = []
        new_cats_for_totals = []
        for cats in cat_for_totals:
            if cats in category:
                indexes.append(category.index(cats))
                new_cats_for_totals.append(str(cats[:-2]))
    
        data_for_totals = []
        for i in indexes:
            data_for_totals.append(int(data[i]))
    
        return new_cats_for_totals, data_for_totals