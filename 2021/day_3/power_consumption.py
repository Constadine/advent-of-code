if __name__ == "__main__":

    with open('input.txt') as f:

        lines = f.readlines()
        gamma_rate = ""
        epsilon_rate = ""
        for digit in range(0, 12):
            # print(f"Checking the: {digit} digit")
            zeros = 0
            ones = 0

            for x, line in enumerate(lines):
                bit = line[digit]
                # print(f'In line: {x} the bit:{bit}')
                if bit == '0':
                    zeros += 1
                    # print(f"Added a zero, zeros:{zeros}")
                elif bit == '1':
                    ones += 1
            #         print(f"Added a one, ones:{ones}")
            # print(f"zeros:{zeros}, ones:{ones}")
            if zeros > ones:
                gamma_rate += "0"
                # print(f"More zeros, joined 0")
            else:
                gamma_rate += "1"
                # print(f"More ones, joined 1")
        for i in range(len(gamma_rate)):  
            if gamma_rate[i] == "1":
                epsilon_rate += "0"
            else:
                epsilon_rate += "1"
        gamma_deci = int(gamma_rate, 2)
        epsilon_deci = int(epsilon_rate, 2)
        print(f"Gamma-rate: {gamma_rate} = {gamma_deci}")
        print(f"Epsilon-rate: {epsilon_rate} = {epsilon_deci}")
        print(f"Power consumption: {gamma_deci*epsilon_deci}")
  



