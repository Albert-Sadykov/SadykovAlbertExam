import random
from stage import *

class Construction:
    def __init__(self, stages):
        self.stages = stages
        self.current_stage_index = 0

    def run(self):
        while self.current_stage_index < len(self.stages):
            current_stage = self.stages[self.current_stage_index]
            current_stage.start()
            if random.randint(1, 100) <= 13:
                current_stage.reject()
                self.handle_rejection()
            else:
                current_stage.stop()
                self.current_stage_index += 1
        
        return "Успешно" if self.current_stage_index == len(self.stages) else "Неуспешно"
    
    def handle_rejection(self):
        if self.current_stage_index == 0:
            print("Проект забракован. Стройка отменяется.")
            self.current_stage_index = len(self.stages) + 1
        else:
            print(f"{self.stages[self.current_stage_index].description} забракован. Возврат к предыдущему этапу.")
            self.current_stage_index -= 1


