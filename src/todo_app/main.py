import argparse
from services import TaskService

def main():
    """Main function for the to-do list CLI."""
    task_service = TaskService()
    parser = argparse.ArgumentParser(description="A simple to-do list CLI application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task.")
    add_parser.add_argument("--title", required=True, help="The title of the task.")
    add_parser.add_argument("--description", default="", help="The description of the task.")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks.")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task.")
    update_parser.add_argument("id", type=int, help="The ID of the task to update.")
    update_parser.add_argument("--title", help="The new title of the task.")
    update_parser.add_argument("--description", help="The new description of the task.")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as complete or incomplete.")
    done_parser.add_argument("id", type=int, help="The ID of the task to mark.")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("id", type=int, help="The ID of the task to delete.")

    args = parser.parse_args()

    if args.command == "add":
        new_task = task_service.add_task(args.title, args.description)
        print(f"Added task: '{new_task.title}' with ID: {new_task.id}")
    elif args.command == "list":
        tasks = task_service.get_tasks()
        if not tasks:
            print("No tasks yet.")
        else:
            print(f"{'ID':<4} {'Status':<10} {'Title':<20} {'Description'}")
            print("-" * 60)
            for task in tasks:
                status = "[x]" if task.is_completed else "[ ]"
                print(f"{task.id:<4} {status:<10} {task.title:<20} {task.description}")
    elif args.command == "update":
        updated_task = task_service.update_task(args.id, args.title, args.description)
        if updated_task:
            print(f"Task {updated_task.id} updated.")
        else:
            print(f"Task with ID {args.id} not found.")
    elif args.command == "done":
        task = task_service.toggle_task_completion(args.id)
        if task:
            status = "complete" if task.is_completed else "incomplete"
            print(f"Task {task.id} marked as {status}.")
        else:
            print(f"Task with ID {args.id} not found.")
    elif args.command == "delete":
        if task_service.delete_task(args.id):
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task with ID {args.id} not found.")
    elif args.command is None:
        parser.print_help()
    else:
        print(f"Invalid command: {args.command}")

if __name__ == "__main__":
    main()
