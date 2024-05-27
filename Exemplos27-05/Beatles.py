import time

Beatles = []

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

print(Beatles)

for i in range(2):
    new_member = input("Adicione os seguintes membros da banda à lista: ")
    #Digite Stu Sutcliffe e Pete Best
    Beatles.append(new_member)

print(Beatles)

del Beatles[3:7]

Beatles.insert(0, "Ringo Starr")

print("Beatles:", Beatles)
    
time.sleep(3)