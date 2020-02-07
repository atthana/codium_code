import helloRedis


def todoList():

    while True:

        instruction = "**Type 1 to add new task Type 2 to view tasks Type 3 to remove any tasks Type Any other key to exit**\n>"
        action = input(instruction)

        if(action == "1"):
            print("Enter your tasks, if you want to finish just enter a blank task.")
            while True:
                tasks = input("Task : ")
                if tasks == "":
                    break
                else:
                    print("come to redis set_name")
                    redis_server.set_name(tasks)

        elif(action == "2"):
            print("These are your tasks: ")
            redis_server.view_items()

        elif(action == "3"):
            print("Do you want to remove any tasks?\nIf yes (press no. of task and press enter), if no just press enter.")

            command = (input("> "))
            if command == "":
                break
            else:
                redis_server.remove_item(int(command)-1)
                print("item " + command + " is removed")
        else:
            print("End.")
            break


redis_server = helloRedis.RedisConnection()
redis_server.connect_server()
todoList()
