with open('mydefaults.ini.txt') as my_file:
    data=my_file.read()

    def count_number():
        number_count = 0 
        for letter in data:
            if letter.isnumeric() == True:
                number_count= number_count+1
        return number_count
        
    def letter_count():
        letter_count = 0
        for letter in data:
            if letter.isalpha() == True:
                letter_count = letter_count + 1
        return letter_count
file=open("outputs.txt",'w')
file.write(f'{count_number()}\n')
file.write(f'{letter_count()}')
file.close()

