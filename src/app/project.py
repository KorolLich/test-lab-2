from datetime import datetime, timedelta, date
from .task import Task
import re

class Project:
    def __init__(self, title: str, description: str, deadline: date) -> None:
        self.title = title
        self.description = description
        
        if not isinstance(deadline, date) or isinstance(deadline, datetime):
            raise ValueError("deadline должен быть производным от класса datetime.date")
    
        # Проверка, что дедлайн как минимум на один день больше сегодняшней даты
        if deadline < (datetime.now() + timedelta(days=1)).date():
            raise ValueError("Дедлайн должен быть как минимум на один день больше сегодняшней даты.")
        
        self.deadline = deadline
        self.tasks = []  # Список задач внутри проекта

    def is_similar_tasks(self, new_task: Task) -> bool:
        cnt_match = 0
        words_new_task = re.findall(r'\b\w+\b', new_task.title)
        for existed_task in self.tasks:
            words_existed_task = re.findall(r'\b\w+\b', existed_task.title)
            for word in words_new_task:
                if word in words_existed_task:
                    cnt_match += 1
            print('Слова: ', words_new_task, words_existed_task)
            print('Кол-во совпадений: ', cnt_match)

            # Если совпаднение больше 70% по какому либо из названий
            if (len(words_existed_task) > 0 and 
                max(cnt_match / len(words_existed_task) * 100, 
                    cnt_match / len(words_new_task) * 100) > 70):
                return True
        
        return False
    
    def add_task(self, task: Task) -> None:
        if task.deadline > self.deadline:
            raise ValueError(f"""Дедлайн для задачи {task.title} больше, 
                             чем дедлайн проекта {self.title} 
                             ({task.deadline} > {self.deadline})""") 
        
        if self.is_similar_tasks(task):
            print("Существует похожая задача, добавления не будет")
            return
        
        self.tasks.append(task)

    def get_info(self) -> str:
        result = f"Список задач в проекте '{self.title}':\n"
        for index, task in enumerate(self.tasks):
            result += f'Номер задачи: {index}\n'
            result += task.get_info() + '\n-------\n'
        return result
