from datetime import datetime, timedelta, date
from enum import Enum

class StatusType(Enum):
    NEW_TASK = "Новая задача"
    DEFERRED_TASK = "Отложенная задача"
    IN_PROGRESS = "В работе"
    COMPLETE_TASK = "Завершенная задача"
    EXPIRED_TASK = "Просроченная задача"

    def __str__(self) -> str:
        return self.value

class Task:
    def __init__(self, title: str, description: str, deadline: date) -> None:
        self.title = title
        self.description = description

        if not isinstance(deadline, date) or isinstance(deadline, datetime):
            raise ValueError("deadline должен быть производным от класса datetime.date")
    
        # Проверка, что дедлайн как минимум на один день больше сегодняшней даты
        if deadline < (datetime.now() + timedelta(days=1)).date():
            raise ValueError("Дедлайн должен быть как минимум на один день больше сегодняшней даты.")
        
        self.deadline = deadline

        # Статус "Новая задача"
        self.status = StatusType.NEW_TASK

    def change_status(self, new_status: StatusType) -> bool:
        if new_status == StatusType.NEW_TASK:
            print('Нельзя присвоить задаче статус "Новая"')
            return False
        
        self.status = new_status

        return True
    
    def get_days_before_deadline(self) -> int:
        current_date = datetime.now().date()

        # Если сегодняшняя дата больше дедлайна
        if current_date >= self.deadline:
            return 0  # Задача уже просрочена, 0 дней до дедлайна

        # Разница между дедлайном и текущей датой
        time_difference = self.deadline - current_date

        # Возвращаем количество дней в виде целого числа
        return time_difference.days
        

    def get_info(self):
        return f"Название задачи: {self.title}\nОписание: {self.description}\n" \
               f"Срок выполнения: {self.deadline}\nСтатус: {self.status}\n"

# Пример использования класса
if __name__ == "__main__":

    # Создаем экземпляр задачи
    task1 = Task("Разработка функционала", 
                 "Написать код для нового функционала", 
                 (datetime.now() + timedelta(days=3)).date())

    print("Дней до дедлайна:", task1.get_days_before_deadline())

    # Выводим информацию о задаче до изменения статуса
    print("Информация о задаче до изменения статуса:")
    print(task1.get_info())

    # Изменяем статус задачи
    task1.change_status(StatusType.IN_PROGRESS)

    # Выводим информацию о задаче после изменения статуса
    print("\nИнформация о задаче после изменения статуса:")
    print(task1.get_info())
