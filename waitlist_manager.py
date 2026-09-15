# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None 




# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None # Head is intialized with a value of none

    def add_front(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node  # Head now points to the new node
        print(new_node.name, 'added to the waitlist')

    def print_list(self):
        temp = self.head # Start from the head of the list
        while temp:
            print('-',temp.name) # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

    def add_end(self, new_data):
        new_node = Node(new_data)
        print(new_node.name, 'added to the waitlist')
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, value):
        current = self.head  # Start with the head of the list
        while current: # Traverse the list
            if current.name == value: # Compare the list's data to the search value
                self.head = None
                return print(f"{value} successfully deleted") # Print the value if a match is found
            current = current.next
        return print(f"{value} is not in waitlist")


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()


