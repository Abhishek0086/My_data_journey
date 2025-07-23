class FixedFloot:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'<FixedFloat {self.value:.2f}>'
    

numbers = FixedFloot(18.5837)
print(numbers)