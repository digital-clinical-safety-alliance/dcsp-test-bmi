""" BMI calculator """


class BMICalculator:
    def __init__(self):
        pass

    def BMI(sel, weight: float, height: float) -> float:
        """ """
        BMI: float = weight / ((height / 100) * (height / 100))

        return BMI
