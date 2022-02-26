class priority_queue {
  constructor(_compareFunction) {
    this.heap = [null];
    this.size = 0;
    this.compareFunction = function(_element1, _element2) {
      if(_element2 === null) return false;
      if(_element2 === undefined) return true;
      if(_compareFunction(_element1, _element2) > 0) return true;
      
      return false;
    }
    
    this.parentIndex = function(_index) {
      return Math.floor(_index/2);
    }
    
    this.leftChildIndex = function(_index) {
      return _index*2;
    }
    
    this.rightChildIndex = function(_index) {
      return _index*2 + 1;
    }
    
  }
  
  push(_element) {
    ++this.size; 
    this.heap[this.size] = _element;
    let i = this.size;
    while(this.compareFunction(
      this.heap[i], 
      this.heap[this.parentIndex(i)]
    )) {
      [this.heap[i], this.heap[this.parentIndex(i)]] =
        [this.heap[this.parentIndex(i)], this.heap[i]];
      
      i = this.parentIndex(i);
    }
    
    return this.size;
  }
  
  top() {
    return this.heap[1];
  }
  
  empty() {
    return this.size === 0;
  }
  
  pop() {
    if(this.empty()) return undefined;
    const TOP = this.top();
    [this.heap[1], this.heap[this.size]] =
      [this.heap[this.size], undefined];
    
    --this.size;
    let i = 1;
    while(
      !this.compareFunction(
        this.heap[i], 
        this.heap[this.leftChildIndex(i)]
      ) || !this.compareFunction(
        this.heap[i], 
        this.heap[this.rightChildIndex(i)]
      )
    ) {
      if(
        this.compareFunction(
          this.heap[this.leftChildIndex(i)],
          this.heap[this.rightChildIndex(i)]
        )
      ) {
        [this.heap[i], this.heap[this.leftChildIndex(i)]] =
          [this.heap[this.leftChildIndex(i)], this.heap[i]];
        
        i = this.leftChildIndex(i);
      } else {
        [this.heap[i], this.heap[this.rightChildIndex(i)]] =
          [this.heap[this.rightChildIndex(i)], this.heap[i]];
        
        i = this.rightChildIndex(i);
      }
      
    }
    
    return TOP;
  }
  
}
