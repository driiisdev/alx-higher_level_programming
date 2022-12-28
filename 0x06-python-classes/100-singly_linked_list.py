#!/usr/bin/python3

"""
This is a module that provides classes Node
object and SinglyLinkedList object
"""


class Node:

    """
    This is a Node object for singly linked lists which has private
    attributes data which must be an integer and next_node which must be
    of object type "Node"
    """

    def __init__(self, data, next_node=None):
        """
        This is the initializer function for class Node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is a Singly linked list object used to build and
    add node to a singly linked list
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        list = ""
        temp = self.__head
        while temp is not None:
            list += "{}".format(temp.data) + "\n"
            temp = temp.next_node
        list = list[:(len(list) - 1)]
        return list

    def sorted_insert(self, value):
        """
        sorted_insert: This method is used to add a new node to the
        singly linked list
        Args:
        self: instance of object
        value: integer data to be in added node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        temp = self.__head
        temp1 = self.__head.next_node
        if value <= temp.data:
                new.next_node = temp
                self.__head = new
                return
        elif temp1 is None:
                temp.next_node = new
                return
        while temp is not None:
            if temp.data <= value <= temp1.data:
                temp.next_node = new
                new.next_node = temp1
                break
            temp = temp1
            if temp1.next_node is not None:
                temp1 = temp1.next_node
            else:
                temp.next_node = new
                break
