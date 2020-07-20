import requests

def main():
    response=requests.get('http://www.google.com')
    print("status Code:",response.status_code)
    print("Header:",response.headers)
    print("Header date:",response.headers['Date'])
    List=list(response.headers)
    print(List)
    # print("Text:",response.text)
    
if __name__ == "__main__":
    main()