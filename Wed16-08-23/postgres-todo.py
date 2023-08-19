import os
import psycopg2

database_password = os.environ.get('DATABASE_PASSWORD')
database_user = os.environ.get('DATABASE_USER')
database_name = os.environ.get('DATABASE_NAME')

conn = psycopg2.connect(
        database=database_name,
        user=database_user,
        password=database_password,
        host='localhost',
        port='5432',
    )

cur = conn.cursor()

def create_todo(task: str) -> None:
    """
    function creates a todo task
    """
    cur.execute('INSERT INTO todos (task, completed) VALUES (%s, %s)', (task, False))
    conn.commit()


def get_todos():
    """
    function list all todos from the database
    """
    cur.execute('SELECT * FROM todos')
    return cur.fetchall()


def mark_as_completed(task_id: int) -> None:
    """
    Function marks a task as completed by changing completed value to True
    """
    cur.execute('UPDATE todos SET completed = %s WHERE id = %s', (True, task_id))
    conn.commit()


def delete_task(task_id: int) -> None:
    """
    Function deletes a task from the todos table with a specified id
    """
    cur.execute('DELETE FROM todos WHERE id = %s', (task_id,))
    conn.commit()


def main() -> None:
    """
    main function
    """
    while True:
        print('\nTodo List')
        todos = get_todos()
        for todo in todos:
            print(todo)

        print("\nOptions:")
        print("1. Add Todo")
        print("2. Mark Todo as Completed")
        print("3. Delete Todo")
        print("4. Exit")

        choice = input('Select an option: ')

        if choice == '1':
            task = input('Enter the new task: ')
            create_todo(task)
            print('Task "{}" added'.format(task))
            print('\n')
        elif choice == '2':
            task_name: str = ''
            not_valid, not_exist = True, True
            while not_valid or not_exist:
                task_id = input('Enter id of the completed task: ')
                try:
                    task_id = int(task_id)
                    not_valid = False
                    task_name = next(todo[1] for todo in todos if todo[0] == task_id)
                    not_exist = False
                except:
                    print('No task found')
                    print('Please enter a valid ID')
            mark_as_completed(task_id)
            print(f'"{task_name}" marked as completed')
            print('\n')
        elif choice == '3':
            task_name: str = ''
            not_valid, not_exist = True, True
            while not_valid or not_exist:
                task_id = input('Enter the id of task to delete: ')
                try:
                    task_id = int(task_id)
                    not_valid = False
                    task_name = next(todo[1] for todo in todos if todo[0] == task_id)
                    not_exist = False
                except:
                    print(f'Task with id {task_id} does not exist')
                    print('Please enter a valid ID')
            delete_task(task_id)
            print(f'"{task_name}" task with id {task_id} deleted.')
            print('\n')
        elif choice == '4':
            break
        else:
            print('Please enter a valid option')
            print('\n')

    cur.close()
    conn.close()



if __name__ == '__main__':
    main()
