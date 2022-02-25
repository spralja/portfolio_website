function loadFile (file) {
  console.log("reading FIle");
  let readMap = file.data;
  let tempMap = [];
  readMap = readMap.split("\n");
  readMap.forEach( (line) => { 
    line = line.trim();
    let charLine = line.split("");
    let intLine = []
    
    for (let i = 0; i < charLine.length; i++) {
      intLine[i] = parseInt(charLine[i]);
      if (isNaN(intLine[i])) {
        intLine[i] = charLine[i]
      }
    }
    
    if (intLine != new Array(0)) {
      
    tempMap.push(intLine)
    }
  
  });
  readMap = tempMap;
  //console.log(readMap);
  
  liveMap = readMap;
  
  setSize(readMap[1].length, readMap.length);
}

function saveFile () {
  let writer = createWriter('map.txt');
  
  liveMap.forEach( (line) => {
    line.forEach( (letter) => {
      writer.write(letter);
    });
    (line != liveMap[liveMap.length - 1]) ? writer.write('\n') : writer.close();
  });
}