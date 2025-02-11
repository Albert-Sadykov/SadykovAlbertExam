from stage import *
from construction import Construction

stages = [
    Project(1000, "01.01.2025", "10.01.2025", "Проект"),
    Foundation(5000, "11.01.2025", "20.01.2025", "Фундамент"),
    Walls(10000, "21.01.2025", "10.02.2025", "Стены"),
    Roof(7000, "11.02.2025", "20.02.2025", "Крыша"),
    WindowsInstallation(3000, "21.02.2025", "25.02.2025", "Установка окон"),
    Finishing(6000, "26.02.2025", "10.03.2025", "Отделка")
]

def test_construction_runs(runs=1000):
    success_count = 0
    for _ in range(runs):
        construction = Construction(stages)
        result = construction.run()
        if result == "Успешно":
            success_count += 1
    success_rate = success_count / runs
    print(f"Вероятность успешного завершения стройки: {success_rate:.2%}")

test_construction_runs()