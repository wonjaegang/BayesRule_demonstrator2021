import random


class Settings:
    def __init__(self):
        self.populationSize = 100
        self.priorProbability = 0.1
        self.sensitivity = 0.9
        self.specificity = 0.8


class Demonstrator:
    def __init__(self):
        self.infected = 0
        self.positive = 0
        self.positive_infected = 0
        self.spreadDisease()
        self.diagnosticTest()

        self.posterioriProbability = self.calculate_posterioriProbability()

    def spreadDisease(self):
        for _ in range(settings.populationSize):
            if random.random() < settings.priorProbability:
                self.infected += 1

    def diagnosticTest(self):
        for _ in range(self.infected):
            if random.random() < settings.sensitivity:
                self.positive += 1
                self.positive_infected += 1
        for _ in range(settings.populationSize - self.infected):
            if random.random() < 1 - settings.sensitivity:
                self.positive += 1

    def calculate_posterioriProbability(self):
        return self.positive_infected / self.positive

    def __str__(self):
        return "Total: {}, Infected: {}, Positive: {}, Positive&Infected: {}, Posteriori Probability: {}"\
            .format(settings.populationSize, self.infected, self.positive,
                    self.positive_infected, self.posterioriProbability)


if __name__ == "__main__":
    settings = Settings()

    demonstrator = Demonstrator()
    print(demonstrator)
