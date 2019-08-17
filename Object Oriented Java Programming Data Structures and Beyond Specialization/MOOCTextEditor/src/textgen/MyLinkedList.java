package textgen;

import java.util.AbstractList;


/** A class that implements a doubly linked list
 * 
 * @author UC San Diego Intermediate Programming MOOC team
 *
 * @param <E> The type of the elements stored in the list
 */
public class MyLinkedList<E> extends AbstractList<E> {
	LLNode<E> head;
	LLNode<E> tail;
	int size;

	/** Create a new empty LinkedList */
	public MyLinkedList() {
		// TODO: Implement this method
		head = new LLNode<E>(null);
		tail = new LLNode<E>(null);
		head.next = this.tail;
		tail.prev = this.head;
		size = 0;
	}

	/**
	 * Appends an element to the end of the list
	 * @param element The element to add
	 */
	public boolean add(E element ) 
	{
		// TODO: Implement this method
		
		if (element == null) {
			
			throw new NullPointerException("At method add(element): element cannot be null");
		}
		
		// create the newNode the element
		LLNode<E> newNode = new LLNode<E>(element);
		
		// update the pointers to the new node created
		newNode.prev = tail.prev;
		newNode.next = tail;
		// update the tail(sentinel node) and the last node (not the sentinel) pointers
		tail.prev = newNode;
		newNode.prev.next = newNode;
		
		// increment the size of the list
		size++;
		
		return true;
	}

	/** Get the element at position index 
	 * @throws IndexOutOfBoundsException if the index is out of bounds. */
	public E get(int index) 
	{
		// TODO: Implement this method.
		if (index < 0 || index > size - 1) {
			
			throw new IndexOutOfBoundsException("At method get(index): index cannot be < 0 or > (size - 1)");
		}
		
		LLNode<E> node = head;
		
		for (int i = 0; i < size; i++) {
			
			if (index == i) {
				
				return node.next.data;
			}
			
			node = node.next;
		}
		
		
		return null;
	}

	/**
	 * Add an element to the list at the specified index
	 * @param The index where the element should be added
	 * @param element The element to add
	 */
	public void add(int index, E element ) 
	{
		// TODO: Implement this method
		if (index < 0 || index > size) {
			
			throw new IndexOutOfBoundsException("At method add(index, element): "
					+ "index cannot be < 0 or > size");
		}else if (element == null) {
			
			throw new NullPointerException("At method add(index, element):"
					+ " element cannot be null");
		}
		
		LLNode<E> node = head.next;
		LLNode<E> newNode = new LLNode<E>(element);
		
		for (int i = 0; i <= size; i++) {
			
			if (index == i) {
				
				newNode.next = node;
				newNode.prev = node.prev;
				node.prev.next = newNode;
				node.prev = newNode;
				size++;
				return;
			}
			
			node = node.next;
		}
	}


	/** Return the size of the list */
	public int size() 
	{
		// TODO: Implement this method
		return this.size;
	}

	/** Remove a node at the specified index and return its data element.
	 * @param index The index of the element to remove
	 * @return The data element removed
	 * @throws IndexOutOfBoundsException If index is outside the bounds of the list
	 * 
	 */
	public E remove(int index) 
	{
		// TODO: Implement this method

		if (index < 0 || index > size - 1) {
			
			throw new IndexOutOfBoundsException("At method remove(index): "
					+ "index cannot be < 0 or > (size - 1)");
		}
		
		LLNode<E> node = head.next;
		E data;
		
		for (int i = 0; i < size; i++) {
			
			if (index == i) {
				
				data = node.data;
				node.prev.next = node.next;
				node.next.prev = node.prev;
				size--;
				return data;
				
			}
			
			node = node.next;
			
		}
		
		return null;
	}

	/**
	 * Set an index position in the list to a new element
	 * @param index The index of the element to change
	 * @param element The new element
	 * @return The element that was replaced
	 * @throws IndexOutOfBoundsException if the index is out of bounds.
	 */
	public E set(int index, E element) 
	{
		// TODO: Implement this method
		
		if (index < 0 || index > size - 1) {
			
			throw new IndexOutOfBoundsException("At method set(index, element): "
					+ "index cannot be < 0 or > (size - 1)");
		}else if (element == null) {
			
			throw new NullPointerException("At method set(index, element):"
					+ " element cannot be null");
		}
		
		LLNode<E> node = head.next;
		E data;
		
		for (int i = 0; i < size; i++) {
			
			if (index == i) {
				
				data = node.data;
				node.data = element;

				return data;
			}
			
			node = node.next;
		}
		
		return null;
	}
	
	public String toString() {
		
		String listRep = "|head| prev: " + head.prev + ", data: " + head.data + ", next: -->\n";
		int index = 0;
		
		for (LLNode<E> node = head.next; node.next != null; node = node.next) {
			
			listRep += "at i = " + index + ": ";
			
			if (node.prev != null) {
				listRep += "<--" + "prev";
			}
			
			listRep += ", data: " + node.data;
			listRep += ", next: " + "-->\n"; 
			
			index++;
		}
		
		listRep += "<--" + "prev" + " ,data: " + tail.data + ", next: " + tail.next + "|tail|";
		
		return listRep;
	}
}

class LLNode<E> 
{
	LLNode<E> prev;
	LLNode<E> next;
	E data;

	// TODO: Add any other methods you think are useful here
	// E.g. you might want to add another constructor
	
	public LLNode() {
		this.prev = null;
		this.next = null;
	}

	public LLNode(E e) 
	{
		this();
		this.data = e;

	}

}
