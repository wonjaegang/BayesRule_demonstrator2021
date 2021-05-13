import random


class Settings:
    def __init__(self):
        self.populationSize = 1000
        self.priorProbability = 0.1
        self.sensitivity = 0.9
        self.specificity = 0.8

        self.simulationTime = 1000


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


def calculateAverage(lastAverage, n, an):
    return lastAverage * (n - 1) / n + an / n


if __name__ == "__main__":
    settings = Settings()
    average = 0
    for loop in range(settings.simulationTime):
        demonstrator = Demonstrator()
        average = calculateAverage(average, loop + 1, demonstrator.posterioriProbability)
        print(demonstrator)
        print("Current Average Posteriori Probability: %f" % average)
    print("="*20, "Simulation Over", "="*20)
    print("Final Average Posteriori Probability: %f" % average)
