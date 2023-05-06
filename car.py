class Car:
    make="Subaru"
    def __init__(self,color,year,model):
        self.color=color
        self.year=year
        self.model=model
    def car_color(self):
        return f'{self.color}'
    def car_year(self):
        return f'{self.year}'
    def car_model(self):
        return f'{self.model}'
    
