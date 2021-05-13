import random


class Demonstrator:
    def __init__(self):
        self.population = [1 if random.random() < settings.priorProbability else 0
                           for _ in range(settings.populationSize)]
        self.display()

    def display(self):
        print(self.population)
        print("Infected : %d" % self.population.count(1))
        print("Uninfected : %d" % self.population.count(0))


class Settings:
    def __init__(self):
        self.populationSize = 100
        self.priorProbability = 0.1
        self.sensitivity = 0.9
        self.specificity = 0.8


if __name__ == "__main__":
    settings = Settings()

    demonstrator = Demonstrator()

    pass
