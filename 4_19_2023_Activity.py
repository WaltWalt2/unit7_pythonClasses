class pizza:
    def __init__(self, ingredientsA, ingredientsB, ingredientsC):
        self.ingredientsA = ingredientsA
        self.ingredientsB = ingredientsB
        self.ingredientsC = ingredientsC
        
order = pizza ('Cheese', 'Pepperoni', 'Ham')

print(order.ingredientsA)
print(order.ingredientsB)
print(order.ingredientsC)