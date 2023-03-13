#!/usr/bin/node
// script that prints the first argument passed to it
if(process.argv === undefined){
  console.log("No argument");
}else{
	console.log(process.argv[2]);
}
