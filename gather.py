import shodan,os 
from censys.search import CensysHosts

class Init():

    def __init__(self):
        self.shodan_api = None

    def config(self,shodan_api_filename):
        self.set_credentials(shodan_api_filename)
       
    def set_credentials(self, shodan_api_filename):
        if not os.path.exists(shodan_api_filename):
            print('[!!] credentials was not setup!')
            self.shodan_api = input('[!] input shodan_api: ')
            with open(shodan_api_filename, 'wt') as fp:
                fp.write(self.shodan_api)

        if not os.path.exists('~/.config/censys/censys.cfg'):
            os.system('censys config')

        with open(shodan_api_filename, 'rt') as fp:
            self.shodan_api = fp.readline()

    def get_shodan_api(self):
        return self.shodan_api


def query_shodan_with_nip(api_key,  nip):

    print()
    print('[+] resluts of censys query')
    try:
        api = shodan.Shodan(api_key)
        query = f'net:{nip}'
        result = api.search(query)

        for service in result['matches']:
            print(service['ip_str'])

    except Exception as e:
        print(e)

h = CensysHosts()
def query_censys_with_nip(nip):

    print()
    print('[+] resluts of censys query')
    print('[INFO] ip => [ service/port ... coutnry_code]')
    query = h.search(f'ip:{nip}', per_page=5, page=2)
    for page in query:
        for host in page:
            print(host['ip'], end='' )

            print(' => [ ', end = '')
            for service in host['services']:
                print(f'{service["service_name"]}/{service["port"]} ', end='')

            print(host['location']['country_code']+']')


def print_banner():
    print('''
                                                  
           /    /              /  |           /   
 ___  ___ (___ (___  ___  ___ (___| ___  ___ (___ 
|   )|   )|    |   )|___)|   )|   )|   )|___ |    
|__/ |__/||__  |  / |__  |    |  / |__/  __/ |__  
__/                                               

''')

def print_menu():
    print()
    print('Available command')
    print('    sscan: ', 'gather hosts information given sigle ip')
    print('    nscan: ', 'gather hosts information given network ip')
    print()

if __name__ == '__main__':
    print_banner()
    init = Init() 
    init.config('credentials.txt')

    cmd = '' 

    while True:

        print_menu()
        cmd = input('[*] command: ')
        if cmd == 'quit':
            print('bye!')
            break
    
        elif cmd == 'sscan':
            sip = input('[*] input ip address: ')
            pass

        elif cmd == 'nscan':
            nip = input('[*] input network ip address ex) 23.0.0.0/8: ')
            query_shodan_with_nip(init.get_shodan_api(), nip)
            query_censys_with_nip(nip)


