with open("macro_input.txt", "r") as file:
    lines = file.readlines()
print(lines)
mnt = []
mdt = []
ala = []
# i = int (0)
i=0

while i < len(lines):

    if lines[i].strip().upper() == "MACRO":
        counter = int(0)
        i+=1

        while lines[i].strip().upper() != "MEND":
            if counter == 0:
                mac = lines[i].strip().split(' ')
                print(mac)
                if mac[0] not in ala:
                    ala.append(mac[0])

                temp_ind = ala.index(mac[0])
                mdt.append(mac)
                mdtIndex = len(mdt)
                mnt.append([mac[1], str(mdtIndex)])

                for itr in mac[2].split(','):
                    print(itr)
                    if itr not in ala:
                        ind = itr.find('=')
                        if ind == -1:
                            ala.append(itr)
                        else:
                            ala.append(itr[:ind])

                counter += 1
                i+=1
            else:
                mac = lines[i].strip().split(' ')
                print(mac)

                if len(mac) == 2:
                    ala_temp = mac[1].split(',')
                    index = str(ala.index(ala_temp[1]))
                    mdt.append(['', mac[0] ,f"{ala_temp[0]}," + "#" + index])

                elif len(mac) == 3:
                    ala_temp = mac[2].split(',')
                    index = str(ala.index(ala_temp[1]))

                    temp = str(ala.index(mac[0]))

                    mdt.append([f'#{temp}', mac[1], f"{ala_temp[0]}," + "#" + index])

                i+=1
    else:
        if lines[i].strip().upper() == "MEND":
            mdt.append([' ', "MEND", ' '])
        i+=1

print ("\nMNT")
print("Index\tName\tMDT index")

for count, itr in enumerate(mnt) :
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}")

print("\nMDT")
print("Index\t\tName" )
for count, itr in enumerate(mdt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1] }\t{itr[2]}")

print("\nDummy ALA in Pass 1")
print("Index\tArguements" )
for count, itr in enumerate(ala):
    print(f"{count}\t{itr}")
