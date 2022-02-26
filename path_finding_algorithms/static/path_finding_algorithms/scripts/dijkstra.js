class dijkstra_node {
  constructor(_id, _weight) {
    this.ID = _id;
    this.WEIGHT = _weight;
  }
  
  get weight() {
    return this.WEIGHT;
  }
  
  get id() {
    return this.ID;
  }
}

class dijkstra_algo {
  constructor(aMap) {
    this.data = new mapData(aMap);
    this.list = this.data.list;
    this.bitmap = this.data.bitMap;
    this.inter = this.data.interMap;
    [this.start, this.end] = this.data.SEalgorithm();
    const COMPARE_FUNCTION = function(a, b) {
      return b.weight - a.weight;
    }
    
    this.pq = new priority_queue(COMPARE_FUNCTION);
    this.pq.push(new dijkstra_node(this.start, 0));
    this.path = [];
    this.seen = [];
  }
  
  step() {
    
    let cur = this.pq.pop();
    while(this.seen.includes(cur.id)) {
      cur = this.pq.pop();
      if(cur === undefined) {
        return [this.bitmap, false, [], false];
      }
      
    }
    
    this.seen.push(cur.id);
    if(cur.id == this.end) {
      this.pathFind();
      return [this.bitmap, false, this.path, true];
    } else {
      for(let i = 0; i < this.list[cur.id].adj.length; ++i) {
        if(!this.seen.includes(this.list[cur.id].adj[i])) {
          if(cur.weight + 
             sqrt(this.list[cur.id].weights[i]) >= 
             this.list[this.list[cur.id].adj[i]].dist
          ) continue;
          
          this.list[this.list[cur.id].adj[i]].dist = 
            cur.weight + sqrt(this.list[cur.id].weights[i]);
          
          this.list[this.list[cur.id].adj[i]].parent = 
            cur.id
          
          this.pq.push(new dijkstra_node(
            this.list[cur.id].adj[i], 
            cur.weight + Math.sqrt(this.list[cur.id].weights[i])
          ));
        }
      }
      
      this.fixMap();
      
      if(this.pq.empty()) {
        return [this.bitmap, false, [], false];
      } else {
        return [this.bitmap, true, []]; 
      }
    }
  }
  
  pathFind() {
    let node = this.end;
    let tPath = [];
    while(node != this.start) {
      tPath.push(node);
      node = this.list[node].parent;
    }
    
    tPath.push(this.start);
    
    while (tPath.length!=0) {
      node = tPath.pop();
      
      let xv = 0;
      let yv = 0;  
      
      this.inter.forEach(row => {
        xv = 0;
        row.forEach(cell => {
          if (cell == node) {
            this.path.push({xv: xv, yv: yv});
          }
          xv++;
        });
        yv++;
      });
    }
  }
  
  fixMap() {
    for(let y = 0; y < this.inter.length; ++y) {
      for(let x = 0; x < this.inter[0].length; ++x) {
        
        if(this.inter[y][x] == this.start || this.inter[y][x] == this.end)
          continue;
        
        if(this.seen.includes(this.inter[y][x])) {
          this.bitmap[y][x] = "p";
        }
      }
    }
  }
}