# Default Shell sort when step -> step // 2

def shell_sort(array):
    n = len(array)
    # Choosing a step
    gap = len(array)//2
    while gap > 0 :
        for i in range(n):
            m_gap = i
            while m_gap >= gap and array[m_gap] < array[m_gap - gap]:
                array[m_gap] , array[m_gap - gap] = array[m_gap - gap], array[m_gap]
                m_gap -= gap

        # Step reduction
        gap = gap//2
    
    return array

with open("Семинар №4/test_ShellSort.txt") as file:
    for i in file:
        input = list(map(int, i.split()))
        print(input, end='<----->')
        print(shell_sort(input))
          






