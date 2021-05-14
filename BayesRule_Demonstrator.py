import random


class Settings:
    def __init__(self):
        self.priorProbability = 0.023
        self.sensitivity = 0.891
        self.specificity = 0.992

        self.populationSize = 1000
        self.simulationTime = 1000


class Demonstrator:
    def __init__(self):
        self.infected = 0
        self.positive = 0
        self.positive_infected = 0
        self.spreadDisease()
        self.diagnosticTest()

        self.postProbability = self.calculate_postProbability()

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
            if random.random() < 1 - settings.specificity:
                self.positive += 1

    def calculate_postProbability(self):
        if not self.positive:
            return False
        else:
            return self.positive_infected / self.positive

    def __str__(self):
        return "Total: {}, Infected: {}, Positive: {}, Positive&Infected: {}, Post-Probability: {}"\
            .format(settings.populationSize, self.infected, self.positive,
                    self.positive_infected, self.postProbability)


def bayesRule():
    prior = settings.priorProbability
    sensitivity = settings.sensitivity
    specificity = settings.specificity
    return sensitivity * prior / (sensitivity * prior + (1 - specificity) * (1 - prior))


def calculateAverage(lastAverage, n, an):
    return lastAverage * (n - 1) / n + an / n


if __name__ == "__main__":
    settings = Settings()
    postProbability_calculated = bayesRule()

    average = 0
    for loop in range(settings.simulationTime):
        demonstrator = Demonstrator()
        if not demonstrator.positive:
            print("Simulation #%d skipped due to no positive response.\n" % (loop + 1))
            continue
        else:
            average = calculateAverage(average, loop + 1, demonstrator.postProbability)

        print("Simulation #%d" % (loop + 1))
        print(demonstrator)
        print("Post-probability calculated by Bayes' rule: %f" % postProbability_calculated)
        print("Current average post-probability: %f\n" % average)

    print("="*20, "Simulation Over", "="*20)
    print("Post-probability calculated by Bayes' rule: %f" % postProbability_calculated)
    print("Post-probability measured by simulation: %f\n" % average)
