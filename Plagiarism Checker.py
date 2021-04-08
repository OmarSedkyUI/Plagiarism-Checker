import nltk

file1 = open("MainFile.txt", 'r')
file2 = open("ComparedFile.txt", 'r')
Similarity = open("Output.txt", "w")

content1 = file1.read()
content2 = file2.read()

file1_list = nltk.tokenize.sent_tokenize(content1)
file2_list = nltk.tokenize.sent_tokenize(content2)
length = (len(file1_list)+len(file2_list))/2

count = 0

for i in file1_list:
    a = i.upper()
    x = set(a)
    for j in file2_list:
        b = j.upper()
        y = set(b)
        ed = nltk.jaccard_distance(x, y)
        if ed == 0:
            count += 1
            print(i,j)
            z = i + j
            Similarity.write(z)
            Similarity.write("\n")


Plagarism = round(count/length*100)

print("Plagarism: ",Plagarism,"%")
Z = "Plagarism: " + str(Plagarism) + "%"
Similarity.write(Z)
Similarity.write("\n")

print("Unique: ",100-Plagarism,"%")
Z = "Unique: " + str(100-Plagarism) + "%"
Similarity.write(Z)

file1.close()
file2.close()
Similarity.close()