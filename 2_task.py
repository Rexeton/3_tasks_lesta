# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.
#
# Оценивается:
#
# Полнота и качество реализации
# Оформление кода
# Наличие сравнения и пояснения по быстродействию
class fifo:
    """Основной класс с проверками"""
    def isint_all_elem(self,all_elem):
        if not isinstance(all_elem,int) or all_elem<0:
            raise Exception(f'Alarm, не бывает цикла с элементами {all_elem}')
        return all_elem
    def isint__start_elem(self,all_elem,_start_elem):
        if not isinstance(_start_elem,int) or _start_elem<0 or _start_elem>all_elem:
            raise Exception(f'начальный элемент{_start_elem} за пределами {all_elem}')
        return _start_elem



class fifo1(fifo):
    """Класс через список
        Плюс
        использование меньше памяти
        можно определить начальный элемент

        Минусы
        ~Без ООП
        более долгий буффер
        """
    def __init__(self,all_elem,_start_elem):
        self._start_elem = self.isint_all_elem(_start_elem)
        self._now_elem = self._start_elem
        self.f=self.isint_all_elem(all_elem)
        self.buffer=[None for _ in range(self.f)]

    def add_elems(self,add_item):
        """Метод для добавления элементов"""
        if isinstance(add_item,list):
            self._now_elem0=self._now_elem
            for el in add_item:
                self.buffer[self._now_elem % self.f] = el
                self._now_elem += 1
        if len(add_item) / self.f>0 or (self._now_elem0>self._now_elem and self._now_elem>self._start_elem):
            self._start_elem=(self._now_elem) % self.f
        self.print_result()

    def del_elems(self,del_item):
        """Метод для удаления элементов"""
        if isinstance(del_item,int):
            self._start_elem0=self._start_elem
            for el in range(del_item):
                self.buffer[self._start_elem % self.f] = None
                self._start_elem += 1
        if del_item // self.f>0 or (self._start_elem0>self._start_elem and self._now_elem<self._start_elem):
            self._now_elem=self._start_elem
        self.print_result()

    def print_result(self):
        print(self.buffer)

class fifo2(fifo):
    """Класс через узлы
        Плюсы
        обращение через объекты
        Меньше кода
        Быстрый

        Минусы
        нельзя поставить начальный элемент
        """
    class node_el:
        def __init__(self, value=None, prev_elem=None,next_elem=None):
            self.value = value
            self.prev_elem = prev_elem
            self.next_elem = next_elem

    def __init__(self,all_elem,_start_elem):
        self._start_elem = self.isint_all_elem(_start_elem)
        self._now_elem = self._start_elem
        self.f=self.isint_all_elem(all_elem)
        self.null_elem=self.node_el()
        self.first_elem=self.node_el(None,self.null_elem,self.null_elem)
        self.count_el=self.first_elem
        self.prev_elem=self.first_elem
        for i in range(self.f-1):
            self.el = self.node_el(None, self.prev_elem, None)
            self.prev_elem.next_elem=self.el
            self.prev_elem=self.el
        self.first_elem.prev_elem=self.el
        self.el.next_elem = self.first_elem
        self.last_elem=self.first_elem
        self.start_elem = self.first_elem


    def add_elems(self,add_item):
        """Метод для добавления элементов"""
        if isinstance(add_item,list):
            for el in add_item:
                self.last_elem.value=el
                self.last_elem=self.last_elem.next_elem
            if self.last_elem.value!=None:
                self.start_elem=self.last_elem
            self.print_result()

    def del_elems(self,del_item):
        """Метод для удаления элементов"""
        if isinstance(del_item,int):
            for el in range(del_item):
                self.start_elem.value=None
                self.start_elem=self.start_elem.next_elem
            self.print_result()
    def print_result(self):
        self.start_el = self.count_el
        self.s = []
        for _ in range(self.f):
            self.s.append(self.start_el.value)
            self.start_el = self.start_el.next_elem
        print(self.s)




fif=fifo2(7,5)
fif.add_elems([2])
fif.add_elems([3,6,8,10,11])
fif.add_elems([12,123,4324,543])
fif.add_elems([555])
fif.del_elems(3)
fif.add_elems([333])
fif.add_elems([3,6,8,10,11])
fif=fifo1(7,5)
fif.add_elems([2])
fif.add_elems([3,6,8,10,11])
fif.add_elems([12,123,4324,543])
fif.add_elems([555])
fif.del_elems(3)
fif.add_elems([333])
fif.add_elems([3,6,8,10,11])
