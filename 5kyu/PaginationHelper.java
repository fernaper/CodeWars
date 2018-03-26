/**
 *	Solution of the problem 
 *	PaginationHelper
 *	https://www.codewars.com/kata/515bb423de843ea99400000a
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.List;
import java.util.HashMap;

public class PaginationHelper<I> {

	private int size;
	private int pages;
	private int itemsPerPage;
	private HashMap<Integer,List<I>> page;

	/**
	* The constructor takes in an array of items and a integer indicating how many
	* items fit within a single page
	*/
	public PaginationHelper(List<I> collection, int itemsPerPage) {
		this.itemsPerPage = itemsPerPage;
		this.size = collection.size();
		this.pages = (int)Math.ceil((double)this.size/(double)this.itemsPerPage);
		this.page = new HashMap();
		for (int i = 0; i < this.pages; i++)
			this.page.put(i,collection.subList(i*this.itemsPerPage,(int)Math.min((i+1)*this.itemsPerPage,this.size)));
	}

	/**
	* returns the number of items within the entire collection
	*/
	public int itemCount() {
		return this.size;
	}

	/**
	* returns the number of pages
	*/
	public int pageCount() {
		return this.pages;
	}

	/**
	* returns the number of items on the current page. page_index is zero based.
	* this method should return -1 for pageIndex values that are out of range
	*/
	public int pageItemCount(int pageIndex) {
		List<I> currentPage = this.page.get(pageIndex);
		if (currentPage == null)
			return -1;
		return currentPage.size();
	}

	/**
	* determines what page an item is on. Zero based indexes
	* this method should return -1 for itemIndex values that are out of range
	*/
	public int pageIndex(int itemIndex) {
		if (itemIndex >= this.size || itemIndex < 0)
			return -1;
		return itemIndex /this.itemsPerPage;
	}
}