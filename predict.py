



import sys
import json

from model import *



def main(file_path):
    model = MODEL()
    result = []
    code_mapping = {0:"000001", 1:"020121", 2:"02051", 3:"020811", 4:"020819"}
    for i in range(10):
        pred = model.predict(0)
        result.append({"id":i, "file_name":"file_"+str(i), "class code":code_mapping[pred]})
   
   
    with open('result.json', 'w', encoding='utf-8') as make_file:
        json.dump(result, make_file, indent="\t")
    


if __name__ =="__main__":
    file_path = sys.argv[1]
    main(file_path)








