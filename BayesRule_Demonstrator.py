import random


class Settings:
    def __init__(self):
        print("사후확률을 구하고자하는 진담검사를 고르시오.")
        print("1.COVID-19: 비인두도말 PCR 법   2.COVID-19: 타액 PCR 법   3.COVID-19: 신속항원검사법   4.사용자 설정")
        name = int(input())

        # === 코로나바이러스감염증-19 관련 ===
        # 21.05.18. 09시 기준, 국내 코로나19 확진확률: 인구 10만 명당 256명
        # 세가지 진단검사 관련 상수 https://www.medric.or.kr/Controls/Sub.aspx?d=03&s=02&s2=01&g=TENDENCY&c&m=VIEW&i=3455

        # COVID-19: 비인두도말 PCR 법
        if name == 1:
            self.name = "COVID-19: 비인두도말 PCR 법"
            self.priorProbability = 0.00256
            self.sensitivity = 0.98
            self.specificity = 1
        # COVID-19: 타액 PCR 법
        elif name == 2:
            self.name = "COVID-19: 타액 PCR 법"
            self.priorProbability = 0.00256
            self.sensitivity = 0.92
            self.specificity = 1
        # COVID-19: 신속항원검사법
        elif name == 3:
            self.name = "COVID-19: 신속항원검사법"
            self.priorProbability = 0.00256
            self.sensitivity = 0.90
            self.specificity = 0.96
        # 사용자 설정
        elif name == 4:
            self.name = "사용자 설정"
            self.priorProbability = 0.23
            self.sensitivity = 0.891
            self.specificity = 0.992
        else:
            print("Setting value error")

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
    skipped = 0
    for loop in range(settings.simulationTime):
        demonstrator = Demonstrator()
        if not demonstrator.positive:
            print("Simulation #%d skipped due to no positive response.\n" % (loop + 1))
            skipped += 1
            continue
        else:
            average = calculateAverage(average, loop + 1 - skipped, demonstrator.postProbability)

        print("Simulation #%d" % (loop + 1))
        print(demonstrator)
        print("Post-probability calculated by Bayes' rule: %f" % postProbability_calculated)
        print("Current average post-probability: %f\n" % average)

    print("="*20, "Simulation Over", "="*20)
    print("Diagnostic test: [%s]" % settings.name)
    print("Post-probability calculated by Bayes' rule: %f" % postProbability_calculated)
    print("Post-probability measured by simulations: %f\n" % average)
