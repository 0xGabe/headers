import argparse, requests

parser = argparse.ArgumentParser(deion='Check headers and configurations.')
parser.add_argument('--list', action='store', dest='list', required=False, help='Target list.')
parser.add_argument('--url', action='store', dest='url', required=False, help='Target url.')
arguments = parser.parse_args()
targets = []
headers = ['X-Powered-By','Server','Strict-Transport-Security','Content-Security-Policy', 'Access-Control-Allow-Origin']

def doRequest(url):
    return requests.get(url)

def searchHeader(request, header):
    try:
        return request.headers[header]
    except KeyError:
        raise Exception('Not found')

def main(targets):
    for target in targets:
        print("\n[+] Target: " + target)
        for header in headers:
            try:
                headerValue = searchHeader(doRequest(target), header)
                print('[+] ' + header + ': ' + headerValue)
            except:
                print('[-] '+ header +': Not found')


if(arguments.url != None and arguments.list == None):
    targets.append(arguments.url)
    main(targets)

elif(arguments.url != None and arguments.list != None):
    print('You are lost? Look at help bro!!!')
    exit()

else:
    try:
        target_list = open(arguments.list, 'r', errors='ignore')
        for target in target_list.read().splitlines():
            targets.append(target)
        main(targets)

    except FileNotFoundError:
        print('[-] File with url not found.')
        exit()
