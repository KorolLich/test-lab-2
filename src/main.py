from datetime import datetime, timedelta
if __name__ == '__main__' or __name__ == 'main':
    from app.task import Task, StatusType
    from app.project import Project
    from app.project_management import ProjectManagement
else:
    from .app.task import Task, StatusType
    from .app.project import Project
    from .app.project_management import ProjectManagement

def create_project(project_management):
    title = input("Введите название проекта: ")
    description = input("Введите описание проекта: ")
    deadline = input("Введите дедлайн проекта в формате ГГГГ-ММ-ДД: ")
    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
    
    try:
        project_management.add_project(Project(title, description, deadline))
    except ValueError as e:
        print(f"Ошибка: {e}")

def add_task_to_project(project_management: ProjectManagement):
    print(project_management.get_info())
    
    project_title = input("Введите название проекта, к которому хотите добавить задачу: ")
    task_title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    deadline = input("Введите дедлайн задачи в формате ГГГГ-ММ-ДД: ")
    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()

    try:
        project_management.add_task_to_project(project_title, Task(task_title, description, deadline))
    except ValueError as e:
        print(f"Ошибка: {e}")

def delete_project(project_management):
    print(project_management.get_info())
    
    project_title = input("Введите название проекта, который хотите удалить: ")

    try:
        project_management.delete_project(project_title)
    except ValueError as e:
        print(f"Ошибка: {e}")

def main():
    project_management = ProjectManagement()

    while True:
        print("\nВыберите команду:")
        print("1. Создать проект")
        print("2. Добавить задачу в проект")
        print("3. Удалить проект")
        print("4. Просмотреть полную информацию о проектах")
        print("5. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            create_project(project_management)
        elif choice == "2":
            add_task_to_project(project_management)
        elif choice == "3":
            add_task_to_project(project_management)
        elif choice == "4":
            print("\n", project_management.get_info())
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
