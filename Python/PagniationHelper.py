# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

import math 
# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_perpage = items_per_page
        pass
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection )
    
    # returns the number of pages
    def page_count(self):
        # divide the length of the collection by the items per page and round up
        return math.ceil(len(self.collection)/self.items_perpage)
        
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or not self.collection:
            return -1
        
        pages_leftover = (len(self.collection)/self.items_perpage) - page_index
        # subtract pages from page index and then check if it's below 0, above 1, or if there is a fraction of a page left
        if pages_leftover > 1:
            return self.items_perpage
        elif pages_leftover > 0:
            print(self.items_perpage * pages_leftover)
            return round(self.items_perpage * pages_leftover)
        return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index > (len(self.collection) - 1) :
            return -1
        return math.floor((item_index) / self.items_perpage)


empty = PaginationHelper([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 15)
print(empty.page_item_count(1))
