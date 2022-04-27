import shodan,os 


class Init():

    def __init__(self):
        self.shodan_id = None
        self.shodan_secret = None
        self.censys_id = None
        self.censys_secret = None

    def config(self,filename):
        self.set_credentials(filename)
       
    def write_credentials(self, filename):
        with open(filename, 'wt') as fp:
            fp.write(self.shodan_id+'\n')
            fp.write(self.shodan_secret+'\n')
            fp.write(self.censys_id+'\n')
            fp.write(self.censys_secret+'\n')
            
    def set_credentials(self, filename):
        if not os.path.exists(filename):
            print('[!!] credentials was not setup!')
            self.shodan_id = input('[!] input shodan_id: ')
            self.shodan_secret  = input('[!] input shodan_secret: ') 
            self.censys_id = input('[!] input censys_id: ')
            self.censys_secret = input('[!] input censys_secret: ')
            self.write_credentials(filename)

        else:
            with open(filename, 'rt') as fp:
                self.shodan_id = fp.readline()
                self.shodan_secret = fp.readline()
                self.censys_id = fp.readline()
                self.censys_secret = fp.readline()



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
            nip = input('[*] input network ip address: ')
            pass





