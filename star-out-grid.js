function starOutGrid(grid) {
    let idcs = [];
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length; j++){
            if(grid[i][j] == '*'){
                idcs.push(grid[i].indexOf('*'))
                grid[i] = ['*','*','*']
                break;
            }
        }
    }
    for(let grr of grid){
        for(let idx of idcs){
            grr[idx] = '*'
        } 
    }
    console.log(grid)
    return grid;
}


starOutGrid([ ['A', 'B', 'C'], ['D', '*', 'E'], ['F', 'G', 'H'] ])