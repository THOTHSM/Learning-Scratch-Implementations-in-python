import json
class to_do_list:
    def __init__(self,list_of_features):
        self.lof = list_of_features
        self.dict_cr()
    

    def dict_cr(self):
        self.data = {}
        for i in self.lof:
            self.data[i]=[]
        
    def print_dict(self):
        print(self.data)

    def append(self,feature):
        if feature in self.lof:
            value = input("Enter value ")
            self.data[feature].append(value)
        else :
            print("No such feature ")

    def append_list(self,feature, list_to_add):
        if feature in self.lof and  isinstance(list_to_add,list):
            for i in list_to_add:
                self.data[feature].append(i)
        else:
            print('No such feature ')
            

    def convert_to_json(self,json_file_name):
        with open(f"{json_file_name}.json",'w') as file:
            json.dump(self.data, file, indent=4)

    
s = to_do_list(['id',"name","city"])
s.print_dict()
s.append_list('id',[1,2,3,4])
s.print_dict()
s.convert_to_json('pd')