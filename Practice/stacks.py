'''
This code demonstrates stacks
'''

class stack:
    max = 10
    items = ["" for index in range(max)]
    stack_pointer = -1

    def push(self,item):
        #check stack overflow
        if self.stack_pointer < self.max:
            self.stack_pointer += 1

            #push the item
            self.items[self.stack_pointer] = item
            return True
        
        else:
            return False
    #endfunc

    def pop(self):
        #check stack underflow
        if self.stack_pointer != -1:
            #pop the item
            item = self.items[self.stack_pointer]
            self.stack_pointer -= 1
            return item

        else:
            return None
    #endfunc

    def peek(self):
        #check stack underflow
        if self.stack_pointer != -1:
            #peek the item
            return self.items[self.stack_pointer]
        else:
            return None
    #endfunc
    
#endclass


#main program starts here
items = ["Florida", "Georgia", "Delaware", "Alabama", "California"]

s = stack()
#add items to stack
for index in range(0, len(items)):
    s.push(items[index])
#endfor

#remove items from the stack
print(s.pop())

#output the next item in the stack
print(s.peek())