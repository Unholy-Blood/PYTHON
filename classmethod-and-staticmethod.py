### @classmethod and @staticmethod
class person:
    
    people_count = 0
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        person.people_count += 1


    # @classmethod refers to the class rather than the instance of the class
    @classmethod
    def people(cls): # here cls is the class param
        # cls refers to the class itself
        return cls.people_count, person.people_count


    # @staticmethod is useful for storing func
    # can be called by person.info() directly without calling an instance of the class
    @staticmethod
    def info(name:str, age:int):
        age = int(age)
        return name, age, age >= 18

loki = person("loki",15)
print(person.people())

steve = person('steve',17)
print(person.people())

x,y,z = person.info("voter_bot", 24)
print(f'name = {x}, ', f'age = {y}, ', f'Eligible to vote = {z}')
