class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class MyLinkedList:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.size = 0
		self.tail = None
		self.head = None


	def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if index >= self.size or index < 0:
			return -1
		else:
			node = self.getIdxNode(index)
			return node.val


	def addAtHead(self, val: int) -> None:
		"""
		Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
		"""
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			#this also covers the case when size == 1, just think
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
		self.size += 1


	def addAtTail(self, val: int) -> None:
		"""
		Append a node of value val to the last element of the linked list.
		"""
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			newNode.prev = self.tail
			self.tail.next = newNode
			self.tail = newNode
		self.size += 1

	def addAtIndex(self, index: int, val: int) -> None:
		"""
		Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
		"""
		if index <= 0:
			#add at head
			self.addAtHead(val)
		elif index == self.size:
			#add at tail
			self.addAtTail(val)
		elif index <= self.size - 1:
			newNode = Node(val)
			idxNode = self.getIdxNode(index)
			#set pointers for newNode
			newNode.prev = idxNode.prev
			newNode.next = idxNode

			#update idxNode.prev
			idxNode.prev.next = newNode

			#idxNode
			idxNode.prev = newNode

			self.size += 1

	def deleteAtIndex(self, index: int) -> None:
		"""
		Delete the index-th node in the linked list, if the index is valid.
		"""
		if index < 0 or index >= self.size:
			return

		if index == 0:
			#delete from head
			self.deleteHead()
		elif index == self.size - 1:
			# delete from tail
			self.deleteTail()
		else:
			idxNode = self.getIdxNode(index)
			idxNode.prev.next = idxNode.next
			idxNode.next.prev = idxNode.prev
			del idxNode

		self.size -= 1

	def getIdxNode(self, idx):
		tmp = self.head
		while idx > 0:
			tmp = tmp.next
			idx -= 1

		return tmp 

	def deleteHead(self):
		oldHead = self.head
		if self.size == 1:
			self.head == None
			self.tail == None
		else:    
			self.head.next.prev = None
			self.head = self.head.next
		del oldHead

	def deleteTail(self):
		oldTail = self.tail
		if self.size == 1:
			self.head == None
			self.tail == None
		else:
			self.tail.prev.next = None
			self.tail = self.tail.prev
		del oldTail