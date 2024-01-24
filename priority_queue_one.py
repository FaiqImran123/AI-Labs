class Node:
    def __init__(self, obj, priority):
        self.obj =obj
        self.priority =priority
        self.next =None
        self.depth =0
        
class Priority_Queue:
    def __init__(self):
        self.front =None
        self.count =0
        

    def enqueue(self, priority, obj, depth):
    
        self.count +=1
        
        
        if self.front==None:
            self.front =Node(obj, priority)
            self.front.depth =depth
        else:
      
            if priority<self.front.priority:
                o =Node(obj, priority)
                o.depth =depth
                o.next =self.front
                self.front =o
            else:
                c =self.front
              
                
                while c!=None:
                    if priority>=c.priority:
                        o =Node(obj, priority)
                        o.depth =depth
                        tmp =c.next
                        c.next =o
                        o.next =tmp
                        break
                    c =c.next
            
    def dequeue(self):
        if self.front!=None:
            self.count -=1
            tmp =self.front
            self.front =self.front.next
            return tmp
            

        else:
            raise Exception("Queue is Empty")
                    





    def remove_from_last(self, beam_width):
        for i in range(self.count-beam_width):
            self.removeFromLast()

        
    def removeFromLast(self):
        if self.front!=None:
            if self.front.next==None:
                self.front =None
            else:
                c =self.front

                while c.next.next!=None:
                    c =c.next
                    
                c.next =None

        


    def is_empty(self):
        return self.front==None
    def search(self, obj): #will search for object and will return its priority
        c =self.front
        while c!=None:
            if c.obj==obj:
                return c.priority
            c =c.next
        return False
    def update(self, priority, obj, d):
        if self.front==None:
            raise Exception("Empty Queue")
        elif self.front.obj ==obj:
            
            self.front =self.front.next
            self.enqueue(priority, obj, d)
        else:
            c =self.front
            while c.next!=None:
                if c.next.obj==obj:
                    c.next =c.next.next
                    self.enqueue(priority, obj, d)
                c =c.next
            
    def display(self):
        c =self.front
        while c!=None:
            print(c.obj)
            c =c.next

            
    