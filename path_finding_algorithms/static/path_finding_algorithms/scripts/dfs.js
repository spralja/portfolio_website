class dfs_algo {
  constructor (aMap) {
    //console.log(aMap);
    this.stack = [];
    this.explored = [];
    this.seen = [];
    this.data = new mapData(aMap);
    this.list = this.data.list;
    this.inter = this.data.interMap;
    this.bitmap = this.data.bitMap;
    
    this.returnPath = [];
    
    [this.start, this.end] = this.data.SEalgorithm();
    
    this.stack.push(this.start);
  }
  
  
  step () {
    let current = this.stack.pop();
    
    this.explored.push(current);
    
    let adj = this.list[current].adj;
    
    adj.filter( n => !this.seen.includes(n))
      .forEach( n => {
      this.stack.push(n);
      this.seen.push(n);
      this.list[n].parent = current;
    });
    
    this.fixMap();
    
    //console.log(this.bitmap);
    
    if (current == this.end) return [this.bitmap, false, this.returnPath, true]; 
    else return (this.stack.length != 0) ? [this.bitmap, true, this.returnPath] : [this.bitmap, false, this.returnPath, false];
  }
  
  fixMap () {
    this.returnPath = [];
    for (let y = 0; y < this.inter.length; y++) {
      let side=this.inter[y];
      for (let x = 0; x < side.length;x++) {
        
        if (this.inter[y][x] == this.start || this.inter[y][x] == this.end) continue;
        
        if (this.seen.includes(this.inter[y][x])) {
          this.bitmap[y][x] = "p";
        }
      }
    }
    
    let fx, fy;
    let loopCount = 0;
    let distCalc = 0;
    let prev = 0;
    this.explored.forEach(step => {
      this.inter.forEach(layer => {
        if (layer.indexOf(step) != -1) {
          fx = layer.indexOf(step)
          fy = this.inter.indexOf(layer)
          let parent = this.list[this.inter[fy][fx]].parent;
          if (prev != 0) {
          distCalc = dist(fx, fy, 
          prev.xv,
          prev.yv);
        } }
      });
      //console.log(distCalc);
      if (distCalc < 2) {
        this.returnPath.push({xv: fx, yv: fy});
        
      } else {
        this.returnPath.push(prev)
        this.returnPath.push({xv: this.list[this.list[step].parent].x, yv: this.list[this.list[step].parent].y})
        this.returnPath.push({xv: fx, yv: fy});
      }
      prev = {xv: fx, yv: fy};
    });
  }
  
}