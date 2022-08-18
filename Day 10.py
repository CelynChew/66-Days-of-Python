# Aim: Try cleaning data

file = 'daily-tests-per-thousand-people-smoothed-7-day.csv'

def clean(data_row):
    # Remove white spaces from end of line
    line_stripped = data_row.strip()
    
    # Removing information after '(' from header
    if '"' not in line_stripped: 
        header = line_stripped[:line_stripped.index('(')]
        return header

    try:
       # Obtaining date without '"'
        first_double_quote = line_stripped.index('"')
        second_double_quote = line_stripped.index('"', line_stripped.index('"') + 1)
        date_string = line_stripped[first_double_quote: second_double_quote + 1]
        no_double_quotes = date_string.replace('"', "")
        # Removing ',' from date
        no_double_quantes_and_commas = no_double_quotes.replace(',', "")
        # Assembling cleaned data
        cleaned_data = line_stripped[:first_double_quote] + no_double_quantes_and_commas + line_stripped[second_double_quote + 1:]
        return cleaned_data
    
    # Handle ValueError so that code can run through whole file despite ValueError
    except ValueError:
        return ValueError

with open(file,'r') as f:
    print(clean(f.readline()))
    print(clean(f.readline()))
    print(clean(f.readline()))
    print(clean(f.readline()))


print(clean('text"moretext'))
