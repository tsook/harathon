var dis = 150
var radius = 20
var number = 7

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d")


for(var i=0; i<= 2*Math.PI; i += 2*Math.PI/number){
	ctx.beginPath()
	ctx.arc(dis*Math.cos(i) + 250, dis*Math.sin(i) + 250, radius, 0, 2*Math.PI)
	ctx.stroke()
}