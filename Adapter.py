#Adapter
# I will use adapter design pattern here because I can only connect string to string

# Creating string part
class String:
    def get(self):
        return "56456456"

# Creating integer part
class Integer:
    def get_int(self):
        return 76767

# Creating adapter part which is converts the int to str
class Adapter(Integer):
    def get(self):
        return str(self.get_int())

# 
def main(obj):
    print ("Result is : " + obj.get())

#run
if __name__ == '__main__':
    obj = Adapter()
    main(obj)
