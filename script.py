import requests, math

while True:
    print("\nChoose what action to take:")
    print("1) Get")
    print("2) Post")    
    print("3) Test Basic Authentication")
    print("4) Test the timeout duration of 3 seconds.")

    userInput = input()
    if userInput == "1":
        pageNumber = input("Enter page number: ")
        countNumber = input("Enter count number: ")
        payload = {'page':pageNumber, 'count':countNumber}
        r = requests.get("https://httpbin.org/get", params=payload, timeout = 3)
        print("\nBased on your GET request, the url is:\n")
        print(r.url+"\n")
        break
    
    elif userInput == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        payload = {"username": username, "password": password}
        r = requests.post("https://httpbin.org/post", data=payload, timeout = 3)
        r_dict = r.json()
        print("\nBased on your post submission, the posted form values are:\n")
        print(r_dict["form"])
        print()
        break
    
    elif userInput == "3":
        print("\nThanks to httpbin, we can simulate a post submission being made to authenticate a login. The necessary post request parameters are 'testUser' for the username and 'testPassword' for the password. See what happens if you enter invalid credentials!\n")
        username = input("Enter the username (testUser): ")
        password = input("Enter your password (testPassword): ")
        r = requests.get("https://httpbin.org/basic-auth/testUser/testPassword" , auth = (username, password), timeout = 3)
        statusCode = r.status_code
        if statusCode == 401:
            print("\nThe status code was {}. This is an unauthorized response. You entered invalid credentials.\n".format(statusCode))
        elif statusCode == 200:
            print("\nThe status code was {}. This is an OK response. You entered the correct credentials.\n".format(statusCode))
        break
    
    elif userInput == "4":
        print("\nThe timeout threshold is 3 seconds. If you enter less than 3 seconds, the status code should be 200. Otherwise, a timeout exception should be raised.\n")
        loadingTime = math.floor(float(input("Enter loading time: ")))
        
        try:
            r = requests.get(f"https://httpbin.org/delay/{loadingTime}", timeout = 3)
            print("The status code was 200. Everything is OK.\n")
        except:
            print("Connection timeout!\n")
        break
    else:
        print("\nInvalid input.\n")
        


         
