class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
    def make_sound(self):
        print('издает звук')
    def eat(self):
        print('ест')
class Bird(Animal):
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food
    def make_sound(self):
        super().make_sound(self)
        print(self.sound)
    def eat(self):
        super().eat(self)
        print(self.food)
    def save(self):
        return 'Bird'+'|'+self.name+'|'+self.age+'|'+self.sound+'|'+self.food
class Mammal(Animal):
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food
    def make_sound(self):
        super().make_sound(self)
        print(self.sound)
    def eat(self):
        super().eat(self)
        print(self.food)
    def save(self):
        return 'Mammal'+'|'+self.name+'|'+self.age+'|'+self.sound+'|'+self.food
class Reptile(Animal):
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food
    def make_sound(self):
        super().make_sound(self)
        print(self.sound)
    def eat(self):
        super().eat(self)
        print(self.food)
    def save(self):
        return 'Reptile'+'|'+self.name+'|'+self.age+'|'+self.sound+'|'+self.food
class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
class Veterinarian(Person):
    def heal_animal(self, animal):
        print(f'лечит {animal.name}')
    def save(self):
        return 'Veterinarian'+'|'+self.name+'|'+self.birth_date
class ZooKeeper(Person):
    def feed_animal(self, animal):
        print(f'кормит {animal.name}, дает {animal.food} ')
    def save(self):
        return 'ZooKeeper'+'|'+self.name+'|'+self.birth_date
class Zoo:
    def __init__(self):
        self.__animals = []
        self.__persons = []
    def animal_sound(self):
        for animal in self.__animals:
            animal.make_sound()
    def add_animal(self, animal):
        self.__animals.append(animal)
    def add_person(self, person):
        self.__persons.append(person)
    def list_animals(self):
        for animal in self.__animals:
            print(f'Животное {animal.name}, возраст {animal.age}')
    def list_persons(self):
        for person in self.__persons:
            print(f'Сотрудник {person.name}, дата рождения {person.birth_date}')
    def save_history(self,history):
        file = open(history,'w')
        file.write(str(len(self.__animals))+'\n')
        for animal in self.__animals:
            file.write(animal.save()+'\n')
        file.write(str(len(self.__persons))+'\n')
        for person in self.__persons:
            file.write(person.save()+'\n')
   def restore_history(self,history):
        file = open(history,'r')
        file.read(line)
        len_list = int(line)
        self.__animals = []
        for i in range(len_list):
            file.read(line)
            list_in = line.split(sep='|')
            animal = globals()[list_in(0)].restore(list_in[1:])
            self.__animals.append(animal)
        file.read(line)
        len_list = int(line)
        self.__persons = []
        for i in range(len_list):
            file.read(line)
            list_in = line.split(sep='|')
            person = globals()[list_in(0)].restore(list_in[1:])
            self.__persons.append(person)

bird = Bird
b1 = bird(name='Птица воробей', age='2', sound='чирик',food='зерно')
b2 = bird(name='Птица журавль', age='4', sound='курлык',food='лягушки')
mammal = Mammal
m1 = mammal(name='Млекопитающее коза', age='5', sound='бее',food='трава')
m2 = mammal(name='Млекопитающее лошадь', age='6', sound='игого',food='сено')
zoo = Zoo()
zoo.add_animal(b1)
zoo.add_animal(b2)
zoo.add_animal(m1)
zoo.add_animal(m2)
veter = Veterinarian
v1 = veter('Ветеринар Иванов','21.12.1975')
zoo.add_person(v1)
zookip = ZooKeeper
z1 = zookip('Служитель Петров','15.02.1980')
z2 = zookip('Служитель Сидоров','15.04.1989')
zoo.add_person(z1)
zoo.add_person(z2)
zoo.list_animals()
zoo.list_persons()
zoo.save_history('history.txt')


