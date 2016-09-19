'''
max sum path to bottom in triangle
'''

import urllib.request

urll = 'https://dl.dropboxusercontent.com/u/28873424/tasks/simple_triangle.txt'
urll_2 = 'https://dl.dropboxusercontent.com/u/28873424/tasks/triangle.txt'
def bild_array(url):
    with urllib.request.urlopen(url) as t:
        array = t.read().decode("utf-8").strip().split('\n')
    for i in range(len(array)):
        array[i]=array[i].split(' ')
    t.close()
    return array

def find_max_pas(pas):
    A = pas
    for i in range((len(A)-2),-1,-1):
        for j in range(0, i+1):
            A[i][j] = int(A[i][j]) + int(max(A[i+1][j],A[i+1][j+1]))
    return A[0][0]
    


if __name__ == '__main__':
    print(find_max_pas(bild_array(urll)))
    print(find_max_pas(bild_array(urll_2)))
        
