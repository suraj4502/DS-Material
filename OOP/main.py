'''
Project Overview:
The Task Manager will have the following features:

1. Add a new task with a title and description.
2. View all tasks with their details.
3. Mark a task as completed.
4. Remove a task from the list.
'''


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        
        
    def mark_completed(self):
        self.completed = True
        
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self,title,description):
        task = Task(title,description)
        self.tasks.append(task)
        
    def view_task(self):
        print()
        for index, task in enumerate(self.tasks,start=1):
                status = "Completed" if task.completed else "Not completed"
                print(f"{index}. Title: {task.title}, Description: {task.description}, Status: {status}")
            
    def mark_completed(self,task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index -1]
            task.mark_completed()
        else:
            print("Invalid Task index.")
            
    def remove_task(self, task_index):
        if 1<= task_index <= len(self.tasks):
            self.tasks.pop(task_index-1)
        else:
            print("Invalid Task index.")
        
        
        
        
# task_manager = TaskManager()
# task_manager.add_task('first_task','this is my first task')   
# task_manager.view_task()
# task_manager.mark_completed(1)
# task_manager.view_task()
# task_manager.add_task('task2','this is second task')
# task_manager.view_task()
# task_manager.remove_task(2)
# task_manager.view_task()
        
        
def main():
     task_manager = TaskManager()
     
     while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
            print("Task added succssully!..")
            
        elif choice == '2':
            task_manager.view_task()    
            
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            task_manager.mark_completed(task_index)
            
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: "))
            task_manager.remove_task(task_index)
            
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()

        
        