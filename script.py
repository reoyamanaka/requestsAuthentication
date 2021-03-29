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
    
    
