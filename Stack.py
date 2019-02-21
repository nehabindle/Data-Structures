#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:11:15 2019

@author: sanket
"""

class EmptyStackError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:
    
    def __init__(self,max_size=10):
        self.items = [None]*max_size
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
    def is_full(self):
        return self.count == len(self.items)
    
    def push(self, x):
        if self.is_full():
            raise StackFullError("Stack is full, cannot push more element :")
            
            
        self.items[self.count] = x
        self.count += 1
        
        
        
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        
        x = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return x


    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]
    
    def display (self):
        print(self.items)


if __name__ == "__main__":
    st = Stack(4)
    
    while True:
        print(" 1. Push into the Stack ")
        print(" 2. Pop from the Stack ")
        print(" 3. Peek at the top of the Stack ")
        print(" 4. Size of Stack ")
        print(" 5.Display the Stack ")
        print(" 6.Quit")
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            x = int(input("Enter the element to be inserted : "))
            st.push(x)
        elif choice == 2:
             
            x = st.pop()
            print("The popped element is : " , x)
            
        elif choice == 3:
             
            x = st.peek()
            print("The top element is : " , x)
            
        elif choice == 4:
             
            x = st.size()
            print("The size of stack is : " , x)
        elif choice == 5:
             st.display()
        elif choice == 6:
            break
        else:
            print("Wrong Choice")
       # print()   
            
                  
            
                      
            
        
        