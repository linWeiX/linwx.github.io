function squ(n){
    return n*n*n
}
function df(f,x,h=0.001){
    return(f(x+h)-f(x))/h
}
console.log(df(squ,5,0.0000004))
console.log(df((x)=>x*x,5))