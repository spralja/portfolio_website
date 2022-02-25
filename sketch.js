p5.disableFriendlyErrors = true;

let txt;
let x, y, button;
let gameCanvas;
let liveMap;

let dfs, bfs, dijkstra, astar;
let savedMap;
let timer, loopCounter, distTravelled;
let projectData = [{time: [], loop: [], dist: [], name: "DFS\t"}, {time: [], loop: [], dist: [], name: "BFS\t"}, {time: [], loop: [], dist: [], name: "Dijkstra"}, {time: [], loop: [], dist: [], name: "A*\t"}];

class run {
  dfs () {
    clearMap();
    //console.log("DFS TIME",liveMap);
    algorithm_running = true;
    algorithm = 0;
    dfs = new dfs_algo(liveMap);
    timer = millis();
    loopCounter = 0;
    callHolder.html(callHolder.html() + '<br>' + 'DFS');
  }
  bfs () {
    clearMap();
    algorithm_running = true;
    algorithm = 1;
    bfs = new bfs_algo(liveMap);
    timer = millis();
    loopCounter = 0;
    callHolder.html(callHolder.html() + '<br>' + 'BFS');
  }
  dijkstra () {
    clearMap();
    algorithm_running = true;
    algorithm = 2;
    dijkstra = new dijkstra_algo(liveMap);
    timer = millis();
    loopCounter = 0;
    callHolder.html(callHolder.html() + '<br>' + 'Dijkstra');
  }
  astar () {
    clearMap();
    algorithm_running = true;
    algorithm = 3;
    astar = new astar_algo(liveMap);
    timer = millis();
    loopCounter = 0;
    callHolder.html(callHolder.html() + '<br>' + 'A star');
  }
}

let runAlgo = new run();
let runArray = [runAlgo.dfs, runAlgo.bfs, runAlgo.dijkstra, runAlgo.astar];

function clearMap () {
exploring = [];
    
    
    for (let y = 0; y < liveMap.length; y++) {
      let side = liveMap[y];
      for (let x = 0; x < side.length; x++) {
        if(side[x] == "p") liveMap[y][x] = 0;
      }
    }
}



function setup() {
  frameRate(30);
  gameCanvas = createCanvas(500, 350);
  gameCanvas.position(0, 0);
  TextBox();  
  
  document.oncontextmenu = function() {
    return false;
  }
  
  noLoop();
}

function randomMap() {
  let randomness = randomInput.value();
  
  algorithm = -1;
  algorithm_running = false;
  explored = [];
  
  // Make a map if there isn't one otherwise clear it
  if (typeof(liveMap) == 'undefined') setSize()
  else clearMap();
  
  for (let y = 0; y < liveMap.length; y++) {
    let side = liveMap[y];
    for (let x = 0; x < side.length; x++) {
      if (liveMap[y][x] == "S" || liveMap[y][x] == "E") continue;
      liveMap[y][x] = (random(100) < randomness) ? 1 : 0;
    }
  }
}

function randomSE () {
  
  algorithm = -1;
  algorithm_running = false;
  explored = [];
  
  // Make a map if there isn't one otherwise clear it
  if (typeof(liveMap) == 'undefined') setSize()
  else clearMap();
  
  // Remove start / end
  for (let y = 0; y < liveMap.length; y++) {
    let side = liveMap[y];
    for (let x = 0; x < side.length; x++) {
      if (liveMap[y][x] == "S" || liveMap[y][x] == "E") {
        liveMap[y][x] = 0;
      }
    }
  }
  
  // Randomly add new 
  liveMap[floor(random(0, liveMap.length))][floor(random(0, liveMap[0].length))] = "S";
  let x = floor(random(0, liveMap.length));
  let y = floor(random(0, liveMap.length));
  while (liveMap[y][x] == "S") {
    x = floor(random(0, liveMap.length));
    y = floor(random(0, liveMap.length));
  }
  liveMap[y][x] = "E";
}

let timeHeader, timeHolder, loopHeader, loopHolder, callHeader, callHolder, randomInput;

function TextBox() {
  let hold = {
    x: gameCanvas.x + gameCanvas.width/2 - 50,
    y: gameCanvas.y + gameCanvas.height
  };
  
  timeHeader = createElement('h3', 'Execution time (ms): ');
  timeHolder = createElement('h3');
  timeHeader.position(gameCanvas.width + 20, gameCanvas.y);
  timeHolder.position(timeHeader.x, timeHeader.y + 20);
  
  timeHolder.style('overflow', 'scroll');
  timeHolder.style('width', 200 + "px");
  timeHolder.style('height', 180 + "px");

  
  loopHeader = createElement('h3', 'Times called: ');
  loopHolder = createElement('h3');
  loopHeader.position(timeHeader.x, timeHeader.y + 200);
  loopHolder.position(loopHeader.x, loopHeader.y + 20);
  
  loopHolder.style('overflow', 'scroll');
  loopHolder.style('width', 200 + "px");
  loopHolder.style('height', 180 + "px");
  
  distHeader = createElement('h3', 'Distance travelled: ');
  distHolder = createElement('h3');
  distHeader.position(loopHeader.x, loopHeader.y + 200);
  distHolder.position(distHeader.x, distHeader.y + 20);
  
  distHolder.style('overflow', 'scroll');
  distHolder.style('width', 200 + "px");
  distHolder.style('height', 180 + "px");
  
  
  callHeader = createElement('h3', 'Algorithm order: ');
  callHolder = createElement('h3');
  callHeader.position(distHeader.x, distHeader.y + 200);
  callHolder.position(callHeader.x, callHeader.y + 20);
  
  callHolder.style('overflow', 'scroll');
  callHolder.style('width', 200 + "px");
  callHolder.style('height', 180 + "px");
  
  
  let slText = createElement('h3', 'Make Map: ');
  slText.position(hold.x, hold.y);
  
  textx = createElement('h3', 'X:');
  texty = createElement('h3', 'Y:');
  textx.position(slText.x + 120, slText.y + 40);
  texty.position(textx.x, textx.y + 20);
  textrand = createElement('h3', 'Random/100:');
  textrand.position(texty.x - 90, texty.y + 20);
  
  let setDim = createElement('h3', 'Set Map Dimentions:');
  setDim.position(textx.x, textx.y - 20);
  
  x = createInput(10);
  x.position(textx.x + 20, textx.y + 18);
  y = createInput(10);
  y.position(texty.x + 20, texty.y + 18);
  randomInput = createInput(30);
  randomInput.position(y.x, y.y + y.height);
  
  
  
  // Create / load map options
  button = createButton('New Map');
  button.position(x.x - x.width - 150, x.y);
  button.mousePressed(setSize);
  
  sbutton = createButton('Save Map');
  sbutton.position(button.x, button.y + button.height);
  sbutton.mousePressed(saveFile);
  
  lbutton = createFileInput(loadFile);
  lbutton.position(sbutton.x + sbutton.width, sbutton.y);
  
  
  let randomText = createElement('h3', 'Automatic Map Editing: ');
  randomText.position(sbutton.x, sbutton.y + 30);
  
  rbutton = createButton('Random Map');
  rbutton.position(randomText.x, randomText.y + 70);
  rbutton.mousePressed(randomMap);
  
  prbutton = createButton('Random Position');
  prbutton.position(rbutton.x, rbutton.y - rbutton.height);
  prbutton.mousePressed(randomSE);
  
  brbutton = createButton('Random Position and Map');
  brbutton.position(rbutton.x, rbutton.y + rbutton.height);
  brbutton.mousePressed(() => {randomMap(); randomSE();});

  cbutton = createButton('Clean Map');
  cbutton.position(rbutton.x + rbutton.width, rbutton.y);
  cbutton.mousePressed(clearMap);
  
  timbutton = createButton('Clean Data');
  timbutton.position(prbutton.x + prbutton.width, prbutton.y);
  timbutton.mousePressed(() => {
    projectData = [{time: [], loop: [], dist: [], name: "DFS\t"}, {time: [], loop: [], dist: [], name: "BFS\t"}, {time: [], loop: [], dist: [], name: "Dijkstra"}, {time: [], loop: [], dist: [], name: "A*\t"}];

    loopHolder.html('');
    timeHolder.html('');
    distHolder.html('');
    callHolder.html('');
  });
  
  lbutton = createButton('Log Data');
  lbutton.position(timbutton.x + timbutton.width, timbutton.y);
  lbutton.mousePressed(() => {
    console.log("0: DFS\t 1:BFS\t 2:Dijkstra\t 3: A*");
    console.log(projectData);
    let ttime, tloop, tdist;
    ttime = tloop = tdist = 0;
    console.log("\nAverages");
    console.log("Name\t  Time\t   Calls\t Distance");
    projectData.forEach(algo => {
      let subtractor_variable = 0;
      
      algo.time.forEach( time => {
        ttime += time;
      })
      ttime /= algo.time.length;
      
      algo.loop.forEach( loop => {
        tloop += loop;
      })
      tloop /= algo.loop.length;
      
      algo.dist.forEach( dist => {
        if (dist != 0) tdist += dist;
        else subtractor_variable++;
      })
      tdist /= (algo.dist.length - subtractor_variable);
      
      console.log(algo.name, ttime.toFixed(2) +'\t ' + tloop.toFixed(1) + '\t\t' + tdist.toFixed(2));
      ttime = tloop = tdist = 0;
    });
  });
  
  
  dfsbutton = createButton('DFS');
  dfsbutton.position(400, 500);
  dfsbutton.mousePressed(runAlgo.dfs);
  
  bfsbutton = createButton('BFS');
  bfsbutton.position(400, 500 + dfsbutton.height);
  bfsbutton.mousePressed(runAlgo.bfs);
  
  asbutton = createButton('A star');
  asbutton.position(400 + dfsbutton.width, 500);
  asbutton.mousePressed(runAlgo.astar);
  
  dibutton = createButton('Dijkstra');
  dibutton.position(400 + bfsbutton.width, 500 + dfsbutton.height);
  dibutton.mousePressed(runAlgo.dijkstra)
  
  
  allbutton = createButton('All Algorithms');
  allbutton.position(gameCanvas.x + (gameCanvas.width/2), dfsbutton.y + (dfsbutton.height*2));
  allbutton.mousePressed(() => {
    iterations = 0;
    repeat = true;
    maxIter = itera.value() * 4;
    randomMap();
    randomSE();
    runAlgo.dfs();
  })
  
  numIt = createElement('h3', 'Iterations:');
  numIt.position(allbutton.x - 70, allbutton.y + 20);
  itera = createInput(4);
  itera.position(numIt.x + 90, numIt.y + 18);
    
  itHeader = createElement('h3');
  itHeader.position(numIt.x - 30, numIt.y);
  
  
  
  
  fill(255, 255, 255);
  textAlign(CENTER);
  //textColor()
  textSize(50);
}

function setSize(letx = 0, lety = 0) {
  let intx = (letx == 0) ? parseInt(x.value()) : letx;
  let inty = (lety == 0) ? parseInt(y.value()) : lety;
  
   if (loop == true) {
     noLoop();
  }
  
  if (isNaN(intx) || isNaN(inty)) {
    console.log("Input a Number!!");
  } else {
    dim.x = intx;
    dim.y = inty;
    
    // Turn off algorithm
    algorithm = -1;
    algorithm_running = false;
    
    // Reset path
    exploring = [];
    
    if (letx == 0) {
      liveMap = new Array(inty);
      // make Map array
      for (let i = 0; i < inty; i++) {
        liveMap[i] = new Array(intx);

        for (let j = 0; j < intx; j++) {
          liveMap[i][j] = 0;
        }
      }
      liveMap[inty - 1][intx - 1] = "E"; 
      liveMap[0][0] = "S"; 
    }
    
    //liveMap[1][1] = 1;

    
    loop();
    
    boxWidth = width/dim.x;
    boxHeight = height/dim.y;
  }
} 


let algorithm_running = false;
let algorithm = -1;
let repeat = false;
let iterations = 0;
let maxIter = 0;

function draw() {
  background(255);
  if (algorithm_running) {
    switch (algorithm) {
      // DFS
      case 0:
        [liveMap, algorithm_running, exploring, solved] = dfs.step();
        //console.log(liveMap);
        loopCounter++;
        break;
      // BFS
      case 1:
        [liveMap, algorithm_running, exploring, solved] = bfs.step();
        loopCounter++;
        break;
      // Dijkstra
      case 2:
        [liveMap, algorithm_running, exploring, solved] = dijkstra.step();
        loopCounter++;
        break;
      // A*
      case 3:
        [liveMap, algorithm_running, exploring, solved] = astar.step();
        loopCounter++;
        break;
    }
  } else {
    if (algorithm != -1) {
      //console.log(liveMap)
      if (solved == false) {
        console.log("no SOlution")
        projectData[algorithm].dist.push(0);
      } else {
        projectData[algorithm].dist.push(distTravelled);
      }
      timer = millis() - timer;
      timeHolder.html(timeHolder.html() + '<br>' + timer);
      loopHolder.html(loopHolder.html() + '<br>' + loopCounter);
      distHolder.html(distHolder.html() + '<br>' + distTravelled);
      projectData[algorithm].time.push(timer);
      projectData[algorithm].loop.push(loopCounter);
      itHeader.html('');
      
      
      if (repeat) {
        iterations++;
        repeat = iterations >= maxIter - 1 ? false : true;
        itHeader.html(maxIter-iterations);
        if (iterations%4 == 0) {
          randomMap();
          randomSE();
        }
        clearMap();
        runArray[iterations%4]();
      } else {
        algorithm = -1;
      }
    }
    inputMap();
  }
  //renderMap();
  //console.log(liveMap);
  distTravelled = drawMap();
}