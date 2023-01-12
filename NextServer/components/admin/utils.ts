// let today = new Date(); 
// let hours = today.getHours(); 
// let minutes = today.getMinutes(); 
// let seconds = today.getSeconds(); 
// let milliseconds = today.getMilliseconds();

export const currentTime = function(){
    let today = new Date();
    return `${today.getHours()}시 ${today.getMinutes()}분 ${today.getSeconds()}초`
}