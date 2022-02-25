class node { 
	constructor (val, x, y, adj = [], weights = []) {
		this.val = val;
		this.adj = adj;
		this.weights = weights;
        this.g = 0;
        this.h = 0;
        this.f = 0;
        this.x = x;
        this.y = y;
        this.parent = -1;
        this.dist = 1000000000000;
	}
}

class mapData {
	makeList () {
		let looplist = [-1, 0, 1]
	    let count = 0;

	    let returnList = [];
	    
	    
	    // Loop through entire map
	    for (let y = 0; y < this.bitMap.length; y++) {
			let side = this.bitMap[y];
	      
			for (let x = 0; x < side.length; x++) {
		      	if (side[x] != 1 ) {
		        	// Is a valid position on map
		        	// So we check around it
		        	let adjList = [];
		       		let weightList = [];
		          
		          	// Loop through surrounding positions
		        	looplist.forEach( (dy) => {
		          		looplist.forEach( (dx) => {
		     				if ((dx == 0 && dy == 0) || (x + dx < 0 || x + dx > (side.length - 1)) || (y + dy < 0 || y + dy > (this.bitMap.length - 1))) {
		              			// Index Out of Range
		              		} else {
		              			// Positions on map Adjacent to our Current valid position
		                		if (this.interMap[y + dy][x + dx] != -1) {
		                			// The adjent position is not a wall
		                  			adjList.push(this.interMap[y + dy][x + dx]);
		                  			weightList.push(dy*dy+dx*dx);
		                		} else {
		                			// Adjacent position is a wall
		                		}
		              		}
		            	} );
		            } );

		            // Add this to our adj list
	          		returnList.push(new node(this.interMap[y][x], x, y, adjList, weightList));
	          	}
	       	}
	    }

	    return returnList;
	}


	inter () {
		let nMap = [];
		this.bitMap.forEach( (row) => {nMap.push(row.slice(0))} );

		let count = 0;

			for (let y = 0; y < this.bitMap.length; y++) {
		  	let side = this.bitMap[y]

		  	for (let x = 0; x < side.length; x++) {
		    	if (side[x] != 1) {
		    		nMap[y][x] = count;
		        	count++;
		      	} else {
		      		nMap[y][x] = -1;
		      	}
		    }
		}

		return nMap;
	}

	constructor (Map) {
		this.bitMap = Map;
		this.interMap = this.inter();

		this.list = this.makeList();
	}
  
  SEalgorithm () {
    let count = 0;
    let start, exit;
    
    for (let y = 0; y < this.bitMap.length; y++) {
      let side = this.bitMap[y];
      for (let x = 0; x < side.length; x++) {
        switch (side[x]) {
          case "S":
            start = this.interMap[y][x];
            break;
          case "E":
            exit = this.interMap[y][x];
            break;
          default:
            break;
        }
      }
    }
    
    return [start, exit];
  }

}