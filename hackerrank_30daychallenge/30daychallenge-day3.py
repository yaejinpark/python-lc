if __name__ == '__main__':
    N = int(input().strip())

    if (N % 2 != 0):
        print('Weird')
    
    elif N % 2 == 0 and N in range(2,6):
        print('Weird')
    
    elif N % 2 == 0 and N in range(6,21):
        print('Weird')
        
    else: 
        print('Not Weird')
        
