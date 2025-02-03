class LinkedList:
    # Первый элемент в списке
    head = None
    # Длина списка
    length = 0

    
    class Node:
        element = None
        next_node = None
        
        # Функция инициализации для создания узлов
        def __init__(self, element,  next_node = None):
            self.element = element
            self.next_node = next_node
        
    #Функция добавления элемента в конец списка
    def append_back(self, element):
        # Условие, если не существует первого элемента
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return element
        
        # Создаем текущий узел
        node = self.head

        # Пока существует следующий узел 
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self.length += 1
        

        return element
    

    #Функция добавления элемента в начало списка
    def append_front(self, element):
        # Cоздаём новый узел и добавляем в него новое значение element
        new_node = self.Node(element)

        if self.head is None:
            # Eсли ранее список был пуст, значит новый элемент и будет являться головой (head)
            self.head = new_node
            self.length += 1
            return element
        # Eсли список не пуст, то устанавливаем head в качестве параметра next для нового узла
        new_node.next_node = self.head
        # Записываем в head новый узел
        self.head = new_node
        self.length += 1
        return element
    
    # Функция вывода списка в консоль
    def __str__(self):
        node = self.head
        line = '['
        while node.next_node:
            line += str(node.element) + ', '
            node = node.next_node
        line += str(node. element)+ ']'
        return line

    # Функция получения элемента по индексу
    def __getitem__(self, key):
        i = 0
        node = self.head
        while i < key:
            node = node.next_node
            i +=1
        return node.element

    # Функция вставки элемента в середину, key - id элемента, куда вставляем
    def insert(self, key, value):
        i = 0
        # Создаем текущий узел
        node = self.head
        # Создаем также предыдущий 
        prev_node = self.head

        if key == 0:
            old_head = self.head
            self.head = self.Node(value, next_node=old_head)
            return value
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1
        
        prev_node.next_node = self.Node(value, next_node = node)
        return value
    
    # Функция удаления элемента
    def __delitem__(self, key):
        i = 0 
        node = self.head
        prev_node = node
        if key == 0:
            old_head = self.head
            element = self.head.element
            self.head = self.head.next_node
            self.length += 1
            del old_head
            return element
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1
        
        prev_node.next_node = node.next_node
        element = node.element
        self.length += 1
        del node
        return element
    
    # Запись другого значения в уже существующее
    def asign(self, element, key):
        i = 0
        node = self.head
        while i < key:
            node = node.next_node
            i += 1
        node.element = element

    # Функция поиска цикла в списке
    def hasCycle(self):
        node = self.head
        if node == None or node.next_node == None:
            return False
        slow = node
        fast = node.next_node
        while slow != fast:
            # если быстрый указатель null, то список не циклический
            if fast == None or fast.next_node == None:
                return False
        
            slow = slow.next_node
            fast = fast.next_node.next_node

        return True
    
    # Функция разворота  списка
    def reverseLinkedList(self):
        prev_node = None
        node = self.head
        # Проходимся по списку и меняем указатели узлов 
        while node != None:
            next = node.next_node
            node.next_node = prev_node
            prev_node = node
            node = next
        
        self.head = prev_node

    # Функция поиска середины списка
    def middleNode(self):
        slow = fast = self.head
        # Когда быстрый указатель достигнет конца списка, указатель slow будет указывать на середину
        while fast != None and fast.next_node != None:
            slow = slow.next_node
            fast = fast.next_node.next_node
        return slow.element
    


list1 = LinkedList()
# Добавляем элементы вперед
list1.append_front(0)
list1.append_front(-1)
list1.append_front(-2)
list1.append_front(-3)
list1.append_front(-4)
list1.append_front(-5)

list2 = LinkedList()
# Добавляем элементы назад
list2.append_back(1)
list2.append_back(2)
list2.append_back(3)
list2.append_back(4)
list2.append_back(5)

######################
# Дз:
# Функция, соединяющая 2 отсортированных списка 
def mergesortedList(list1, list2):
    result = None
    current = None

    ptr1 = list1.head
    ptr2 = list2.head
    
    while list1 is not None and list2 is not None:
        if ptr1.element < ptr1.element:
            if result is None:
                result = LinkedList.Node(element=ptr1.element)
                current = result
            else:
                current.next_node = LinkedList.Node(element=ptr1.element)
                current = current.next_node
            prt1 = ptr1.next_node
        else:
            if result is None:
                result = LinkedList.Node(element=ptr2.element)
                current = result
            else:
                current.next_node = LinkedList.Node(element=ptr2.element)
                current = current.next_node
            ptr2 = ptr2.next_node
    while list1 is not None:
        if result is None:
            result = LinkedList.Node(element=ptr1.head.element)
            current = result
        else:
            current.next_node = LinkedList.Node(element=ptr2.head.element)
            current = current.next_node
        ptr2 = ptr2.next_node

    while list2 is not None:
        if result is None:
            result = LinkedList.Node(element=ptr2.element)
            current = result
        else:
            current.next_node = LinkedList.Node(element=ptr2.element)
            current = current.next_node
        ptr2 = ptr2.next_node

    return result
            

        
# Создаем список
spisok = LinkedList()

# Добавляем элементы назад
spisok.append_back(1)
spisok.append_back(2)
spisok.append_back(3)
spisok.append_back(4)
spisok.append_back(5)
# Добавляем элементы вперед
spisok.append_front(0)
spisok.append_front(-1)
spisok.append_front(-2)
spisok.append_front(-3)
spisok.append_front(-4)
spisok.append_front(-5)

# Имеет ли список цикл?
#print(spisok.hasCycle())

# Элемент середины списка
#print(spisok.middleNode())
#print(spisok)

#spisok.reverseLinkedList()

#print(spisok)


print(mergesortedList(list1, list2))


print(spisok)
print(list1)
print(list2)
