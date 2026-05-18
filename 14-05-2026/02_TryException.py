try:
    with open("/workspaces/ITG-EAGLE/14-05-2026/Example.txt", "a") as file:
        file.write("Hello ITG\n")
    
    with open("/workspaces/ITG-EAGLE/14-05-2026/Example.txt", "r") as file:
        content = file.read()
        print(content)
    
    with open("/workspaces/ITG-EAGLE/14-05-2026/Example.txt", "r") as file:
        lines = file.readlines()
        print(lines[5])

except FileNotFoundError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)