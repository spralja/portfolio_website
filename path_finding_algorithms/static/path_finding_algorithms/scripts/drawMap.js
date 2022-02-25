let dim = {x: 0, y: 0}
let boxWidth;
let boxHeight;
let cell = {};
let dragging = false;
let symbol = 1;
let algorithm_stuff;
let heldMap = [];
let exploring = [];


function inputMap () {
  if (mouseX < gameCanvas.width && mouseY < gameCanvas.height){
    cell.x = floor(mouseX/boxWidth);
    cell.y = floor(mouseY/boxHeight);
  } else {
    cell.x = -1;
    cell.y = -1;
  }
  //console.log(algorithm_stuff);
}

function mouseDragged() {
  if ((mouseX > width || mouseX < 0) || (mouseY > height || mouseY < 0)){
    onCanvas = false;
  } else {onCanvas = true}
  
  if (onCanvas) {
    if (dragging) {from.x = cell.x; from.y = cell.y;}
  } else {
    if (dragging) {
      liveMap[from.y][from.x] = symbol;
    }
  }
  //liveMap[cell.y][cell.x] = symbol;
  for (let y = 0; y < liveMap.length; y++) {
    for (let x = 0; x < liveMap[y].length; x++) {
      if (cell.y == y && cell.x == x ) {
        
        liveMap[cell.y][cell.x] = (mouseButton === RIGHT) ? 0 : symbol;
        
      } else {
        if (dragging) liveMap[y][x] = heldMap[y][x];
      }
    }
  }
  
  

}

let from = {};

function mousePressed(e) {
    switch (liveMap[cell.y][cell.x]) {
    case "S":
        liveMap[cell.y][cell.x] = 0;
        from.x = cell.x;
        from.y = cell.y;
        heldMap = liveMap.map(arr => arr.slice());
        dragging = true;
        symbol = "S";
        break;
    case "E":
        liveMap[cell.y][cell.x] = 0;
        from.x = cell.x;
        from.y = cell.y;
        heldMap = liveMap.map(arr => arr.slice());
        dragging = true;
        symbol = "E";
        break;
        
    case 0:
      liveMap[cell.y][cell.x] = 1;
      break;
    case 1:
      liveMap[cell.y][cell.x] = 0;
      break;
    case "p":
      liveMap[cell.y][cell.x] = 1;
      break;
    }
}

let offCanvas = true;

function release () {
    liveMap = heldMap;
    liveMap[from.y][from.x] = symbol;
    dragging = false;
    symbol = 1;
  }


function mouseReleased() {
  if (dragging) release();
}

function drawMap() {
  if(dim.x == 0 ||dim.y == 0) {
   console.log("input dimentions");
    return -1;
  } 
  
  stroke(0);
  
  
  background(255);

  // Draw gridlines  
  /*
  for (let y = 0; y < dim.y + 1; y++) {
    let pos_y = y * (height/dim.y);
    stroke(0);
    line(0, pos_y, width, pos_y);
  }
  
  for (let x = 0; x < dim.x + 1; x++) {
    let pos_x = x * (width/dim.x);
    stroke(0);
    line(pos_x, 0, pos_x, height);
  }*/
  
  let count = 0;
  let bg_color = color(235, 240, 239);
  // Draw objects
  //console.log(liveMap);
  ellipseMode(CENTER);
  let rad = (boxWidth > boxHeight) ? boxWidth/2 : boxHeight/2;
  for (let y = 0; y < liveMap.length; y++) {
    let side = liveMap[y];  
    for (let x = 0; x < side.length; x++) { 
      strokeWeight(1);
      stroke(255);
      switch(side[x]) {
        case 1:
          //fill(20, 117, 196);
          stroke(19, 202, 242)
          strokeWeight(5);
          //rect(x*boxWidth, y*boxHeight, boxWidth, boxHeight);
          line (x*boxWidth + (boxWidth /7), y*boxHeight + (boxHeight /7), x*boxWidth + ((6 *boxWidth) /7), y*boxHeight + 6*(boxHeight /7));
          
          line (x*boxWidth + 6*(boxWidth /7), y*boxHeight + (boxHeight /7), x*boxWidth + (boxWidth /7), y*boxHeight + 6*(boxHeight /7));
          
          break;
        
        case 0: 
          //fill(bg_color);
          //rect(x*boxWidth, y*boxHeight, boxWidth, boxHeight);
          
          fill(0)
          //ellipseMode(CENTER);
          //let rad = (boxWidth > boxHeight) ? boxWidth/2 : boxHeight/2;
          ellipse((x*boxWidth) + (boxWidth/2), (y*boxHeight)+(boxHeight/2), rad/2, rad/2);
          break;
          
        case "E":
          fill(240, 34, 34)
          //ellipse(x*boxWidth, y*boxHeight, rad, rad);
          ellipse((x*boxWidth) + (boxWidth/2), (y*boxHeight)+(boxHeight/2), rad, rad);
          break;
          
        case "S":
          fill(7, 176, 108)
          //ellipse(x*boxWidth, y*boxHeight,rad, rad);
          ellipse((x*boxWidth) + (boxWidth/2), (y*boxHeight)+(boxHeight/2), rad, rad);
          break;
        
        case "p":
          fill(255, 213, 3);//fill(146, 98, 204);
          //ellipse(x*boxWidth, y*boxHeight,rad, rad);
          ellipse((x*boxWidth) + (boxWidth/2), (y*boxHeight)+(boxHeight/2), rad/1.5, rad/1.5);
          break;
      }
    }
  }
  
  let len = 0;
  if (exploring.length != 0) {
    let x1, x2, y1, y2;
    x1 = exploring[0].xv;
    y1 = exploring[0].yv;
    x2 = x1;
    y2 = y1;

      // draw Path
    
    for (let i = 1; i < exploring.length; i++) {
      let cur = exploring[i];
      //console.log(cur);
      // If we are stopping the line and starting elsewhere
      if (cur.xv == x2 && cur.yv == y2) {
        x1 = exploring[i + 1].x;
        y1 = exploring[i + 1].y;
        continue;
      } else { // We are continuing the line
        x2 = cur.xv;
        y2 = cur.yv;

        stroke(0);//stroke(5, 255, 222);
        strokeWeight(5);
        line((x1 * boxWidth ) + boxWidth/2, (y1 * boxHeight) + boxHeight/2, (x2 * boxWidth) + boxWidth/2, (y2 * boxHeight) + boxHeight/2);
        let tempLen = dist(x1, y1, x2, y2);
        len += isNaN(tempLen) ? 0 : tempLen; // int(tempLen * tempLen);

        x1 = x2;
        y1 = y2;


      }
    }
    
  }
  return len;
}