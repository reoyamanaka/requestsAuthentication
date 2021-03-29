import requests

while True:
    print("Choose what action to take:")
    print("1) Get")
    print("2) Post")    

    userInput = input()
    if userInput == "1":
        pageNumber = input("Enter page number: ")
        countNumber = input("Enter count number: ")
        payload = {'page':pageNumber, 'count':countNumber}
        r = requests.get("https://httpbin.org/get", params=payload)
        print("\nBased on your GET request, the url is:\n")
        print(r.url+"\n")
        break
    
    elif userInput == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        payload = {"username": username, "password": password}
        r = requests.post("https://httpbin.org/post", data=payload)
        r_dict = r.json()
        print("\nBased on your post submission, the posted form values are:\n")
        print(r_dict["form"])
        print()
        break 
