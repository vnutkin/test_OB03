class Animal:
    def __init__(self, args):
        self.name = args[0]
        self.age = args[1]

    def make_sound(self):
        print(f'{self.name} издает звук')

    def eat(self):
        print(f'{self.name} ест')


class Bird(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.sound = args[2]
        self.food = args[3]

    def make_sound(self):
        super().make_sound()
        print(self.sound)

    def eat(self):
        super().eat()
        print(self.food)

    def save(self):
        return 'Bird' + '|\''+self.name+'\'|' + str(self.age) + '|\''+self.sound+'\'|\''+self.food+'\''


class Mammal(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.sound = args[2]
        self.food = args[3]

    def make_sound(self):
        super().make_sound()
        print(self.sound)

    def eat(self):
        super().eat()
        print(self.food)

    def save(self):
        return 'Mammal' + '|\''+self.name+'\'|' + str(self.age) + '|\''+self.sound+'\'|\''+self.food+'\''

class Reptile(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.sound = args[2]
        self.food = args[3]

    def make_sound(self):
        super().make_sound()
        print(self.sound)

    def eat(self):
        super().eat()
        print(self.food)

    def save(self):
        return 'Reptile' + '|\''+self.name+'\'|' + str(self.age) + '|\''+self.sound+'\'|\''+self.food+'\''


class Person:
    def __init__(self, args):
        self.name = args[0]
        self.birth_date = args[1]


class Veterinarian(Person):
    def heal_animal(self, animal):
        print(f'лечит {animal.name}')

    def save(self):
        return 'Veterinarian'+'|\''+self.name+'\'|\''+self.birth_date+'\''


class ZooKeeper(Person):
    def feed_animal(self, animal):
        print(f'кормит {animal.name}, дает {animal.food} ')

    def save(self):
        return 'ZooKeeper'+'|\''+self.name+'\'|\''+self.birth_date+'\''


class Zoo:
    def __init__(self):
        self.__animals = []
        self.__persons = []

    def animal_sound(self):
        for animal in self.__animals:
            animal.make_sound()

    def animal_eat(self):
        for animal in self.__animals:
            animal.eat()

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

    def save_history(self, history):
        with open(history, 'w') as file:
            file.write(str(len(self.__animals)) + '\n')
            for animal in self.__animals:
                file.write(animal.save() + '\n')
            file.write(str(len(self.__persons)) + '\n')
            for person in self.__persons:
                file.write(person.save() + '\n')

    def restore_history(self, history):
        with open(history, 'r') as file:
            line = file.readline()
            len_list = int(line)
            self.__animals = []
            for i in range(len_list):
                line = file.readline()
                list_in = line.split(sep='|')
                animal = globals()[list_in[0]](list_in[1:])
                self.__animals.append(animal)
            line = file.readline()
            len_list = int(line)
            self.__persons = []
            for i in range(len_list):
                line = file.readline()
                list_in = line.split(sep='|')
                person = globals()[list_in[0]](list_in[1:])
                self.__persons.append(person)


bird = Bird
b1 = bird(['Птица воробей', 2, 'чирик', 'зерно'])
b2 = bird(['Птица журавль', 4, 'курлык', 'лягушки'])
mammal = Mammal
m1 = mammal(['Млекопитающее коза', 5, 'бее', 'трава'])
m2 = mammal(['Млекопитающее лошадь', 6, 'игого', 'сено'])
zoo = Zoo()
zoo.add_animal(b1)
zoo.add_animal(b2)
zoo.add_animal(m1)
zoo.add_animal(m2)
veter = Veterinarian
v1 = veter(['Ветеринар Иванов', '21.12.1975'])
zoo.add_person(v1)
zookip = ZooKeeper
z1 = zookip(['Служитель Петров', '15.02.1980'])
z2 = zookip(['Служитель Сидоров', '15.04.1989'])
zoo.add_person(z1)
zoo.add_person(z2)
zoo.list_animals()
zoo.list_persons()
zoo.animal_sound()
zoo.animal_eat()
zoo.save_history('history.txt')
zoo.restore_history('history.txt')
zoo.list_animals()
zoo.list_persons()
