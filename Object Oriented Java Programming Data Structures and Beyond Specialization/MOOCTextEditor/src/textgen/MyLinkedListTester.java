/**
 * 
 */
package textgen;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Before;
import org.junit.Test;

/**
 * @author UC San Diego MOOC team
 *
 */
public class MyLinkedListTester {

	private static final int LONG_LIST_LENGTH =10; 

	MyLinkedList<String> shortList;
	MyLinkedList<Integer> emptyList;
	MyLinkedList<Integer> longerList;
	MyLinkedList<Integer> list1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		// Feel free to use these lists, or add your own
	    shortList = new MyLinkedList<String>();
		shortList.add("A");
		shortList.add("B");
		emptyList = new MyLinkedList<Integer>();
		longerList = new MyLinkedList<Integer>();
		for (int i = 0; i < LONG_LIST_LENGTH; i++)
		{
			longerList.add(i);
		}
		list1 = new MyLinkedList<Integer>();
		list1.add(65);
		list1.add(21);
		list1.add(42);
		
		
	}

	
	/** Test if the get method is working correctly.
	 */
	/*You should not need to add much to this method.
	 * We provide it as an example of a thorough test. */
	@Test
	public void testGet()
	{
		
		//test empty list, get should throw an exception
		try {
			emptyList.get(0);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
		
		// test short list, first contents, then out of bounds
		assertEquals("Check first", "A", shortList.get(0));
		assertEquals("Check second", "B", shortList.get(1));
		
		try {
			shortList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			shortList.get(2);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		// test longer list contents
		for(int i = 0; i<LONG_LIST_LENGTH; i++ ) {
			assertEquals("Check "+i+ " element", (Integer)i, longerList.get(i));
		}
		
		// test off the end of the longer array
		try {
			longerList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			longerList.get(LONG_LIST_LENGTH);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
		
	}
	
	
	/** Test removing an element from the list.
	 * We've included the example from the concept challenge.
	 * You will want to add more tests.  */
	@Test
	public void testRemove()
	{
		// TODO: Add more tests here
		
		// 1- test removing from an empty list
		try {
			emptyList.get(0);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}

		
		// 2- test removing from the end of the list
		int a = longerList.remove(LONG_LIST_LENGTH - 1);
		assertEquals("Remove: check if removed element from end is correct ", LONG_LIST_LENGTH - 1, a);
		assertEquals("Remove: check element last elemnent is correct ", 
				(Integer)(LONG_LIST_LENGTH - 2), longerList.get(LONG_LIST_LENGTH - 2));
		assertEquals("Remove: check size is correct ", (LONG_LIST_LENGTH - 1), longerList.size());
		
		
		// 3- test removing from the start of the list
		a = list1.remove(0);
		assertEquals("Remove: check if removed element from start is correct ", 65, a);
		assertEquals("Remove: check element 0 is correct ", (Integer)21, list1.get(0));
		assertEquals("Remove: check size is correct ", 2, list1.size());
		
		
		// 4- test removing from the middle of the list
		a = longerList.remove(3);
		assertEquals("Remove: check if removed element from middle is correct ", 3, a);
		assertEquals("Remove: check element before the removed one is correct", 
				(Integer)2, longerList.get(2));
		assertEquals("Remove: check element after the removed one is correct", 
				(Integer)4, longerList.get(3));
		assertEquals("Remove: check size is correct ", (LONG_LIST_LENGTH - 2), longerList.size());
		
	}
	
	/** Test adding an element into the end of the list, specifically
	 *  public boolean add(E element)
	 * */
	@Test
	public void testAddEnd()
	{
        // TODO: implement this test
		// 1- test if adding null element throws an exception
		try {
			emptyList.add(null);
			fail("Check out of bounds");
		}
		catch (NullPointerException e) {
			
		}
		
		// 2- test if a element can be added to an empty list
		emptyList.add(1);
		assertEquals("add at end: check elemented was added to emptylist ", 
				(Integer)1, emptyList.get(0));
		assertEquals("add at end: check pointers for head and tail", 
				emptyList.tail.prev, emptyList.head.next);
		assertEquals("add at end: check pointers for new node", 
				emptyList.tail.prev.prev, emptyList.head);
		
		// 3- test to see if element can be added to list of size 1
		emptyList.add(2);
		assertEquals("Remove: check a is correct ", (Integer)2, emptyList.get(1));
		
		// 4- test to see if element can be added to list of size > 1
		longerList.add(500);
		assertEquals("Remove: check a is correct ", (Integer)500, longerList.get(LONG_LIST_LENGTH));
		
		
	}

	
	/** Test the size of the list */
	@Test
	public void testSize()
	{
		// TODO: implement this test
		
		// 1- test the size of empty list
		assertEquals("test size of empty list", 0, emptyList.size());
		
		// 2- test the size of list of size 1
		assertEquals("test size of empty list", 2, shortList.size());
		
		// 3- test the size of list of size 2
		assertEquals("test size of empty list", LONG_LIST_LENGTH, longerList.size());
		
		// 4- test the size after removing element
		emptyList.add(10);
		emptyList.add(2);
		emptyList.add(3);
		assertEquals("test size of empty list after 3 elements were added",
				3, emptyList.size());
		
		// 5- test the size after adding element
		emptyList.remove(1);
		assertEquals("test size of list after removing an element",
				2, emptyList.size());
	
	}

	
	
	/** Test adding an element into the list at a specified index,
	 * specifically:
	 * public void add(int index, E element)
	 * */
	@Test
	public void testAddAtIndex()
	{
        // TODO: implement this test
		// 1- test if adding null element throws an exception
		try {
			emptyList.add(0, null);
			fail("catching null pointer failed");
		}
		catch (NullPointerException e) {
			
		}
		
		// 2- test if adding element at location > size throw out of bound exception
		try {
			emptyList.add(1, 10);
			fail("catching out of bounds failed");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
		
		//3- test adding to empty list
		emptyList.add(0, 10);
		assertEquals("add at start", (Integer)10, emptyList.get(0));
		assertEquals("check size after add", 1, emptyList.size());
		
		
		//4- test adding to end of list
		longerList.add(LONG_LIST_LENGTH, 30);
		assertEquals("add at end", (Integer)30, longerList.get(LONG_LIST_LENGTH));
		assertEquals("check one index before after add", (Integer)(LONG_LIST_LENGTH - 1),
				longerList.get(LONG_LIST_LENGTH - 1));
		assertEquals("check size after add", LONG_LIST_LENGTH + 1, longerList.size());
		
		//5- test adding to middle of the list
		longerList.add(3, 17);
		assertEquals("add at middle", (Integer)17, longerList.get(3));
		assertEquals("check one index before after add", (Integer) 2, longerList.get(2));
		assertEquals("check one index after after add", (Integer) 3, longerList.get(4));
		assertEquals("check size after add", LONG_LIST_LENGTH + 2, longerList.size());
		
		
		
		
	}
	
	/** Test setting an element in the list */
	@Test
	public void testSet()
	{
	    // TODO: implement this test
		// 1- test if setting null element throws an exception
		try {
			shortList.set(0, null);
			fail("catching null pointer failed");
		}
		catch (NullPointerException e) {
			
		}
		
		// 2- test if setting element at location >= size throw out of bound exception
		try {
			emptyList.set(0, 10);
			fail("catching out of bounds failed");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
	    
		//3- set an element in list of size 1
		emptyList.add(0, 10);
		emptyList.set(0, 50);
		assertEquals("setting element in list of size 1", (Integer)50, emptyList.get(0));
		
		//4- set an element in list of size > 1
		longerList.set(5, 55);
		assertEquals("setting element in list of size > 1", (Integer)55, longerList.get(5));
		
	}
	
	
	// TODO: Optionally add more test methods.
	
}
