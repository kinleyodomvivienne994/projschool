class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def display_data(self):
        if not self.data:
            print("No data to display.")
        else:
            for item in self.data:
                print(item)
