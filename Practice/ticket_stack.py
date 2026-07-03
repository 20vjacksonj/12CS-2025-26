class TicketStack:

    def __init__(self):

        self.max = 10 #max number of tickets
        self.tickets = [] #empty ticket list
        self.pointer = -1 #pointer starts at -1 because 0 would be the first item in a list

    #enddef

    def push(self, ticket_num, ticket_time):

        if self.pointer < self.max-1: #pointer isnt at maximum
            ticket = f"{ticket_num}-{ticket_time}" #combines two values in one string
            self.tickets.append(ticket) #adds ticket to tickets
            self.pointer+=1 #increment pointer
            return True
        
        else:
            return False
        
    #enddef

    def pop(self):

        if self.pointer == -1: #empty stack
            return None
        
        ticket = self.tickets.pop() #LIFO
        self.pointer -= 1 #decrement pointer 
        return ticket
    
    #enddef
    
    def peek(self):

        if self.pointer == -1: #empty stack
            return None
        
        return self.tickets[self.pointer] #ticket in place of pointer
    
    #enddef

    def display(self):

        output = "Recent Tickets: "
        count = self.pointer + 1 #counts tickets, adds 1 because pointer is at -1
        for i in range(self.pointer, -1, -1): #counts down by 1
            output += f"{count}.{self.tickets[i]} " #output string
            count -= 1 #decrement counter
        print(output.strip()) #prints total output 

    #enddef

#endclass


#testing
stack = TicketStack()

stack.push("AB123", "09:15")
stack.push("AB124", "09:18")
stack.push("AB125", "09:22")
stack.push("AB126", "09:30")
stack.push("AB127", "09:45")

stack.display()

last = stack.peek()
print(f"Last ticket: {last}")

cancelled = stack.pop()
print(f"Cancelled: {cancelled}")

stack.display()