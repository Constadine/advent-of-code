def rec_oxygen(l):
    if len(l) == 1:
        return l
    else:
        for column in range(12):
            temp = ''
            for x, line in enumerate(l):
                temp += line[column]
                zeros = temp.count('0')
                ones = temp.count('1')
            if zeros > ones:
                for x, line in reversed(list(enumerate(l))):
                    if line[column] == '1':
                        l.pop(x)
            elif zeros <= ones:
                for x, line in reversed(list(enumerate(l))):
                    if line[column] == '0':
                        l.pop(x)
            if len(l) == 1:
                break
        return rec_oxygen(l)

def rec_co2(l):
    if len(l) == 1:
        return l
    else:
        for column in range(12):
            temp = ''
            
            for x, line in enumerate(l):
                temp += line[column]
                zeros = temp.count('0')
                ones = temp.count('1')
            if zeros <= ones:
                for x, line in reversed(list(enumerate(l))):
                    if line[column] == '1':
                        l.pop(x)
            elif zeros > ones:
                for x, line in reversed(list(enumerate(l))):
                    if line[column] == '0':
                        l.pop(x)
            if len(l) == 1:
                break
        return rec_co2(l)



if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
        lines_copy = lines[:]

        oxygen_rate = rec_oxygen(lines)[0].strip()
        oxygen_deci = int(oxygen_rate, 2)
        print(f"oxygen rate: {oxygen_rate}, oxygen decimal: {oxygen_deci}")

        co2_rate = rec_co2(lines_copy)[0].strip()
        co2_deci = int(co2_rate, 2)
        life_support_rating = oxygen_deci*co2_deci
        print(f"co2 rate: {co2_rate}, co2 decimal: {co2_deci}.\nLife support: {life_support_rating}")







