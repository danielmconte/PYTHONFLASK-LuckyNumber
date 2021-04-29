function snakeToCamel(phrase) {
    let arr = phrase.split('_');
    let capitalized = [];
    for(let x= 0; x < arr.length; x++){
        if(x==0){
         capitalized.push(arr[x])   
        }else{
        capitalized.push(arr[x].charAt(0).toUpperCase() + arr[x].slice(1))
        }
    }
    let camelCase = capitalized.join("");
    console.log(camelCase)
    return camelCase;
}


snakeToCamel("I_believe_in_miracles");

